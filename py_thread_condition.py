import time
import threading
import random
#Condition 对象 acquire 条件变量锁
#不足 wait 并notify 其他线程 重新判断条件
queue=[]
con=threading.Condition()
class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue)>2:
                    con.wait()
                else:
                    elem=random.randrange(100)
                    queue.append(elem)
                    print('producer a elem {},Now size is {}'.format(elem,queue))
                    time.sleep(random.randrange(3))
                    con.notify()
                con.release()
class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue)<=0:
                    con.wait()
                else:
                    elem=queue.pop()
                    print("consumer a elem {}.Now size is {}".format(elem,len(queue)))
                    time.sleep(random.randrange(2))
                con.release()
def main():
    for i in range(3):
        Producer().start()
    for i in range(2):
        Consumer().start() #个数不确定 但是 sleep time 不对的话卡死

if __name__=='__main__':
    main()
