# 接口测试框架（基于json格式、http协议，dubbo协议请求,python3,不兼容python2.x版本） 
##  java实现版本：https://github.com/liwanlei/java_jiekou
## 注：现在基于Excel文件管理测试用例基本实现,)

# 2018-9-14版本修改
### 1.失败用例重试功能，失败用例可以重试，重试次数可配置
### 2.去掉重复的功能
### 3.基础url可以在config配置，只需要写api

# 2018-3-13版本修改
### 原来的测试报告更加详细的展示错误类型，对部分代码进行了优化，断言结果返回更加详细，更快的定位测试问题

## (目前在部分window上会出现FileNotFoundError [Errno 2] No such file or directory，这个bug是路径过长,解决方案为吧log日志放在当前目录，或者修改动态生成的文件的名字，给了第一种方式，测试日志放在当前目录）
## qq交流群：194704520  一群   683894834 二群
### 使用的库 requests，绝大部分是基于Python原有的库进行的，这样简单方便，
# 友情推荐本人其他开源代码：
#      1.python接口测试平台版本!https://github.com/liwanlei/FXTest
#      2.python app自动化测试平台版本：https://github.com/liwanlei/UFATestPlan
#      3.python+flask 做后台，实现微信小程序：https://github.com/liwanlei/webchat_app
### 使用脚本参数分离等思想，尽可能降低代码的耦合度。
# 2017-11-1版本修改
## 引入ddt数据驱动和BSTestRunner，并且测试过程使用python的unittest库，运行可以使用run_new来运行测试，新的运行更加简单，对预期结果进行了自定义，
## 并且对预期结果的自定义格式进行转换，升级后的接口测试框架提供了两套的运行模式，一套是封装后基于自定义的断言格式的接口测试的框架，比较简单粗糙，但是
## 定义的报告更加具有代表性，一套是封装好完全基于python库的接口测试。使用起来简单，可以供大家选择，新增加测试用例格式为ddt_case.py的格式。
# 运行后的测试报告如下
![Alt text](https://github.com/liwanlei/jiekou-python3/blob/master/img/%E6%96%B0%E7%89%88%E6%9C%AC%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.png)
# log日志
![Alt text](https://github.com/liwanlei/jiekou-python3/blob/master/img/xinbanbenlog.png)
#  新增后可以提供两个入口让供你选择，
## 一：自定义断言方式，自定义测试报告，提供Excel，html格式报告，均为自定义。
##  二：引用unittest，ddt和BSTestRunner等，让测试用例更加简单明了，代码更加简洁。通俗易懂，且使用更多成熟的框架。
# ---------------旧版本内容---------
# 首先我们来看下我们的目录
##
![Alt text](https://github.com/liwanlei/jiekou-python3/blob/master/img/xiangmujiegoutu.png)
##
### 1.Case文件夹用来存放我们的测试用例相关的，
### 2.test_case用来存储我们的测试数据，Excel管理测试用例，yaml文件管理测试用例，后续要把yaml管理测试用例的也封装出来。
### 3.Interface对测试接口相关的封装，包括requests库，发送测试报告的email的封装，从Excel取测试数据的封装
### 4.Public 展示测试报告相关的脚本，这里可以自己封装，也可以使用现成的，我这里是基于我自己封装的，最后生成的测试报告更加易懂，出错可以尽快排查相关原因
### 5.report 存放测试报告，
### 6.run_excel_re.py/run_html.py 主运行文件。运行后可以生成相应的测试报告
##
## 产生的html测试报告如下
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/cebaogaotu.png)
##
### 增加了Excel管理测试报告的功能，目前在继续优化功能，增加了config目录，一些配置文件的目录，
##
## 产生的Excel测试报告如下
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/excel.png)
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/excel2.png)
### 现在的测试结构更加完整，最新的一次提交增加了log日志的展示，使功能更加完善，log日志在控制台展示如下，对目录进行优化
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/log.png)
