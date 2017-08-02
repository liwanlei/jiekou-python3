# 接口测试框架（基于json格式、http请求,python3,不兼容python2.x版本） 
## 注：现在基于Excel文件管理测试用例基本实现,)
## (目前在部分window上会出现FileNotFoundError [Errno 2] No such file or directory，这个bug是路径过长,解决方案为吧log日志放在当前目录，或者修改动态生成的文件的名字，给了第一种方式，测试日志放在当前目录）
### 使用的库 requests，绝大部分是基于Python原有的库进行的，这样简单方便，
### 使用脚本参数分离等思想，尽可能降低代码的耦合度。
# 首先我们来看下我们的目录
##
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/xiangmujiegoutu%20.png)
##
### 1.Case文件夹用来存放我们的测试用例相关的，
### 2.Data用来存储我们的测试数据，Excel管理测试用例，yaml文件管理测试用例，后续要把yaml管理测试用例的也封装出来。
### 3.Interface对测试接口相关的封装，包括requests库，发送测试报告的email的封装，从Excel取测试数据的封装
### 4.Public 展示测试报告相关的脚本，这里可以自己封装，也可以使用现成的，我这里是基于我自己封装的，最后生成的测试报告更加易懂，出错可以尽快排查相关原因
### 5.report 存放测试报告，
### 6.main.py 主运行文件。
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



