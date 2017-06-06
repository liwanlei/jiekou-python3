# 接口测试框架（基于json格式、http请求）
## 注：现在基于Excel文件管理测试用例基本实现，yaml文件管理测试用例现在功能还在处理中）
### 使用的库 requests，绝大部分是基于Python原有的库进行的，这样简单方便，
### 使用脚本参数分离等思想，尽可能降低代码的耦合度。
# 首先我们来看下我们的目录
##
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/xiangmujiegoutu.png)
##
### 1.Case文件夹用来存放我们的测试用例相关的，
### 2.Data用来存储我们的测试数据，Excel管理测试用例，yaml文件管理测试用例，后续要把yaml管理测试用例的也封装出来。
### 3.Interface对测试接口相关的封装，包括requests库，发送测试报告的email的封装，从Excel取测试数据的封装
### 4.Public 展示测试报告相关的脚本，这里可以自己封装，也可以使用现成的，我这里是基于我自己封装的，最后生成的测试报告更加易懂，出错可以尽快排查相关原因
### 5.report 存放测试报告，
### 6.main.py 主运行文件。
##

# 产生的测试报告如下
![Alt text](https://github.com/liwanlei/jiekou/blob/master/img/cebaogaotu.png)
##
##  后续还会有相应的优化版本，现在主要功能做出来了。



