#setDaemon()方法
#主线程退出后结束子线程
import threading
import time
import random

class MyThread(threading.Thread):
    def run(self):
        wait_time=random.randrange(1,10)
        print("thread {} will wait {} s".format(self.name,wait_time))
        time.sleep(wait_time)
        print("thread {} finished".format(self.name))

def main():
    print("Start main threading")
    for i in range(5):
        t = MyThread()
        t.setDaemon(True)
        t.start()

    print("End Main threading")

if __name__=='__main__':
    main()
