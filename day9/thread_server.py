from socket import * 
from threading import Thread 
import sys 

#客户端处理函数
def handler(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()

#创建套接子
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#接收客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务端异常:",e)
        continue 
    
    #创建线程
    t = Thread(target=handler,args=(c,))
    t.setDaemon(True)
    t.start()
    

