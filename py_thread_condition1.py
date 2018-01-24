import  queue  
import time  
import threading  
import  random  
  
  
q=queue.Queue(5)  
  
#生产者  
def pr():  
    name=threading.current_thread().getName()  
    print(name+"线程启动......")  
    for i in range(100):  
        t=random.randint(2,9)  
        print(name,"睡眠时间: ",t)  
        time.sleep(t);  
        d="A"+str(i)  
        print(name+"正在存第",i+1,"个数据: ",d)  
        #q.put("A"+str(i),False,2000)  
        q.put(d)  
    print("生产完毕!")  
  
  
#消费者  
def co():  
    name=threading.current_thread().getName()  
    time.sleep(1)  
    print(name+"线程启动......")  
  
    while True:  
        print(name+"检测到队列数量: ",q.qsize())  
        t=random.randint(2,9)  
        print(name,"睡眠时间: ",t)  
        data=q.get();  
        print(name+"消费一个数据: ",data)  
  
  
  
  
p1=threading.Thread(target=pr,name="生产者1")
p2=threading.Thread(target=pr,name="生产者2")
#c1=threading.Thread(target=co,name="消费者1")  
c2=threading.Thread(target=co,name="消费者2")  
  
p1.start()
p2.start()
#c1.start()  
c2.start()  
