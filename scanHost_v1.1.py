import os,sys,re,threading

'''
V1.1
修复不能输出存活主机列表的问题

'''
def helpip():  
    helpinfo = """ 
============================================================
=                    scanHost_V1.1                         =
=             Written by Joffrey@foxmail.com               =
=                                                          =
=  Usage:                                                  =
=    python scanhost.py 1.2.3.4                            =
=    python scanhost.py 1.2.3.4-200                        = 
=    python scanhost.py 1.2.3.4 5.6.7.8-200 www.baidu.com  =
============================================================
"""  
    print(helpinfo)
    sys.exit(0)

alive=[]
def PingCheck(ip):
	result=os.popen('ping %s'%ip).readlines()
	for i in result:
		if i.upper().find('TTL=')>=0:
			print(ip)
			alive.append(ip)
			break

def GetIP():
	iplist=[]
	#args=sys.argv[1:]
	if len(sys.argv)>=2:
		if sys.argv[1] in ['-h','--help']:helpip()
		for arg in sys.argv[1:]:
			if re.search(r'(-\d+)$',arg):
				start=int(arg.split('.')[3].split('-')[0])
				end=int(arg.split('.')[3].split('-')[1])+1
				for i in range(start,end):
					iplist.append('.'.join(arg.split('.')[:3]+[str(i)]))
			else:iplist.append(arg)
	else:helpip()
	return iplist

def main():	
	iplist=GetIP()
	print('存活主机：')
	for ip in iplist:
		t=threading.Thread(target=PingCheck,args=(ip,))
		t.start()
	while 1:
		if threading.activeCount()==1:
			print(alive)
			break

if __name__ == '__main__':
	main()