"""
A TestRunner for use with the Python unit testing framework. It generates a HTML report to show the result at a glance.
The simplest way to use this is to invoke its main method. E.g.

    import unittest
    import BSTestRunner

    ... define your tests ...

    if __name__ == '__main__':
        BSTestRunner.main()


For more customization options, instantiates a BSTestRunner object.
BSTestRunner is a counterpart to unittest's TextTestRunner. E.g.

    # output to a file
    fp = file('my_report.html', 'wb')
    runner = BSTestRunner.BSTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by BSTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(my_test_suite)


------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
Copyright (c) 2016, Eason Han
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__author__ = "Wai Yip Tung && Eason Han"
__version__ = "0.8.4"

"""
Change History

Version 0.8.3
* Modify html style using bootstrap3.

Version 0.8.3
* Prevent crash on class or module-level exceptions (Darren Wurf).

Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).

Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.

Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat <script> block as CDATA.

Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).
"""

# TODO: color stderr
# TODO: simplify javascript using ,ore than 1 class in the class attribute?

import datetime
import unittest
from xml.sax import saxutils
import os
import sys, copy
from io import StringIO as StringIO


# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before BSTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=BSTestRunner.stdout_redirector)
#   >>>

def to_unicode(s):
    return s
    # try:
    #     return unicode(s)
    # except UnicodeDecodeError:
    #     # s is non ascii byte string
    #     return s.decode('unicode_escape')


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        lines = map(to_unicode, lines)
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: '通过',
        1: '失败',
        2: '错误',
    }

    DEFAULT_TITLE = '测试报告'
    DEFAULT_DESCRIPTION = ''

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" ">
    <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
    %(stylesheet)s

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="http://cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
      <![endif]-->
  </head>
<body>
<div class="container">
    %(heading)s
    %(report)s
    %(ending)s
</div>
 %(scripts)s
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">

/* -- css div popup ------------------------------------------------------------------------ */
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #99CCFF;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 10pt;
    width: 1200px;
}

/* -- report ------------------------------------------------------------------------ */

#show_detail_line .label {
    font-size: 85%;
    cursor: pointer;
}

#show_detail_line {
    margin: 2em auto 1em auto;
}

#total_row  { font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }

</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
     <div >
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div> </div >
"""
    HEADING_TMPL_New = """
 <div class='heading'>
     <div style='width: 50%%;float:left;margin-top:inherit'>
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div> 

<div id='container2' style='width:50%%;float:left;margin-top:20px;height:200px;'>
    </div>
</div >
<div id='containerchart' style='height: 300px;margin-top: 20%%;'></div>
    """
    HEADING_OLD = """<div class='heading'>
    <h1>%(title)s</h1>
    %(parameters)s
    <p class='description'>%(description)s</p>
    </div>
    """
    HEADING_ATTRIBUTE_TMPL = """<p><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
<p id='show_detail_line'>
<span class="label label-primary" onclick="showCase(0)">公用</span>
<span class="label label-danger" onclick="showCase(1)">失败</span>
<span class="label label-default" onclick="showCase(2)">所有</span>
</p>
<table id='result_table' class="table">
    <thead>
        <tr id='header_row'>
            <th>测试组/测试用例</td>
            <th>数量</td>
            <th>通过</td>
            <th>失败</td>
            <th>错误</td>
            <th>查看</td>
        </tr>
    </thead>
    <tbody>
        %(test_list)s
    </tbody>
    <tfoot>
        <tr id='total_row'>
            <td>总计</td>
            <td>%(count)s</td>
            <td class="text text-success">%(Pass)s</td>
            <td class="text text-danger">%(fail)s</td>
            <td class="text text-warning">%(error)s</td>
            <td>&nbsp;</td>
        </tr>
    </tfoot>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a class="btn btn-xs btn-primary"href="javascript:showClassDetail('%(cid)s',%(count)s)">详情</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link btn btn-xs btn-default" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""
    SCRPICTold = """
      <script language='javascript' type='text/javascript'>
      output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName('tr');
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}
function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>

</body>
</html>
    """

    SCRPICTDATA = r"""
    <script language='javascript' type='text/javascript'>
var dom = document.getElementById('containerchart');
var myChart = echarts.init(dom);
var domone = document.getElementById('container2');
var myChartone = echarts.init(domone);
var optionsone;
optionsone = {
    title: {
        text: '历史记录'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['成功', '失败','错误']
    },
    grid: {
        left: '3%%',
        right: '4%%',
        bottom: '3%%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: %(reslutname)s
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '成功',
            type: 'line',
            stack: '总量',
            data: %(success)s
        },
        {
            name: '失败',
            type: 'line',
            stack: '总量',
            data: %(fail)s
        },
        {
            name: '错误',
            type: 'line',
            stack: '总量',
            data: %(error)s
        }

    ]
};
if (optionsone && typeof optionsone === 'object') {
    myChartone.setOption(optionsone);
}
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName('tr');
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>
</body>
</html>
    """


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class MyResult(TestResult):
    def __init__(self, verbosity=1, trynum=1):
        # 默认次数是0
        TestResult.__init__(self)
        self.outputBuffer = StringIO()
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.trynnum = trynum
        self.result = []
        self.trys = 0  #
        self.istry = False

    def startTest(self, test):
        TestResult.startTest(self, test)
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr

    def complete_output(self):
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # 判断是否要重试
        if self.istry is True:
            # 如果执行的次数小于重试的次数 就重试
            if self.trys < self.trynnum:
                # 删除最后一个结果
                reslut = self.result.pop(-1)
                # 判断结果，如果是错误就把错误的个数减掉
                # 如果是失败，就把失败的次数减掉
                if reslut[0] == 1:
                    self.failure_count -= 1
                else:
                    self.error_count -= 1
                sys.stderr.write('{}:用例正在重试中。。。'.format(test.id()) + '\n')
                # 深copy用例
                test = copy.copy(test)
                # 重试次数增加+1
                self.trys += 1
                # 测试
                test(self)
            else:
                self.istry = False
                self.trys = 0
        self.complete_output()

    def addSuccess(self, test):
        # 成功就不要重试
        self.istry = False
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        # 重试+1，错误次数+1
        self.istry = True
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.istry = True
        TestResult.startTestRun(self)
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

    def stop(self) -> None:
        pass


class _TestResult(MyResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1, trynum=1):
        TestResult.__init__(self)
        super().__init__(verbosity, trynum)


class BSTestRunner(Template_mixin):
    """
    """

    def __init__(self, stream=sys.stdout,
                 verbosity=1,
                 title=None,
                 description=None,
                 trynum=1,
                 is_show=False,
                 filepath=""):
        self.stream = stream
        self.verbosity = verbosity
        self.trynum = trynum
        self.is_show = is_show
        self.filepath = filepath
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity, trynum=self.trynum)
        try:
            test(result)
        except TypeError:
            pass
        self.stopTime = datetime.datetime.now()
        if self.is_show:
            name = os.path.join(self.filepath, self.stopTime.strftime('%Y_%m_%d_%H_%M_%S') + '.txt')
            with open(name, 'w+') as f:
                f.write(
                    result.success_count.__str__() + "_" + result.error_count.__str__() + "_" + result.failure_count.__str__())
                f.close()
        self.generateReport(test, result)
        print('\n测试耗时: %s' % (self.stopTime - self.startTime))
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        if result.success_count: status.append(
            '<span class="text text-success">通过 <strong>%s</strong></span>' % result.success_count)
        if result.failure_count: status.append(
            '<span class="text text-danger">失败 <strong>%s</strong></span>' % result.failure_count)
        if result.error_count:   status.append(
            '<span class="text text-warning">错误 <strong>%s</strong></span>' % result.error_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        return [
            ('开始时间', startTime),
            ('持续时间', duration),
            ('状态', status),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'BSTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        if self.is_show:
            scrpit = self.___generate_scrpitone()
        else:
            scrpit = self._generate_scrpit()
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            scripts=scrpit,
            heading=heading,
            report=report,
            ending=ending
        )
        self.stream.write(output.encode("utf-8"))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        ISSHOWPERDATA = True
        if ISSHOWPERDATA:
            a_lines = []
            for name, value in report_attrs:
                line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),  ####更改
                    # value = saxutils.escape(value),

                    value=value,
                )
                a_lines.append(line)
            if self.is_show:
                heading = self.HEADING_TMPL_New % dict(
                    title=saxutils.escape(self.title), parameters=''.join(a_lines),
                    description=saxutils.escape(self.description), )
            else:
                heading = self.HEADING_TMPL % dict(
                    title=saxutils.escape(self.title),
                    parameters=''.join(a_lines),
                    description=saxutils.escape(self.description),
                )
            return heading
        else:
            a_lines = []
            for name, value in report_attrs:
                line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),  ####更改
                    # value = saxutils.escape(value),

                    value=value,
                )
                a_lines.append(line)
            heading = self.HEADING_OLD % dict(
                title=saxutils.escape(self.title),
                parameters=''.join(a_lines),
                description=saxutils.escape(self.description),
            )
            return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'text text-warning' or nf > 0 and 'text text-danger' or 'text text-success',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            # Class = (n == 0 and 'hiddenRow' or 'text text-success'),
            # style = n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            style=n == 2 and 'text text-warning' or (n == 1 and 'text text-danger' or 'text text-success'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL

    def ___generate_scrpitone(self):
        namerun, faillist, success, error = self._readresult()
        return self.SCRPICTDATA % dict(reslutname=namerun,
                                       success=success,
                                       fail=faillist,
                                       error=error)

    def _readresult(self):
        namerun = []
        faillist = []
        success = []
        error = []
        for root, dirs, files in os.walk(self.filepath):
            for file in files:
                if file.endswith(".txt"):
                    namerun.append(file.split(".")[0].split("/")[-1])
                    with open(os.path.join(root, file), 'r') as f:
                        reslut = f.readline().split('\n')[0].split("_")
                        success.append(reslut[0])
                        error.append(reslut[1])
                        faillist.append(reslut[2])
        return namerun, faillist, success, error

    def _generate_scrpit(self):
        return self.SCRPICTold


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick BSTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate BSTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = BSTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################
