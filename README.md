# scanHost
python3批量扫描主机，检测其是否存活

## 说明
- 使用os.popen()执行ping命令，多线程提高执行效率
- 使用的库：os,sys,re,threading

## 使用方法
~~~python
python scanhost.py 1.2.3.4
python scanhost.py 1.2.3.4-200 
python scanhost.py 1.2.3.4 5.6.7.8-200 www.baidu.com
~~~

## 更新记录
### V1.1
- 修复不能输出存活主机列表的问题
