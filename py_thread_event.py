#thread communicate with event
#共享内存也是一种方法
import time
import threading

class MyThread(threading.Thread):
    def __init__(self, event):
        super(MyThread, self).__init__()
        self.event = event

    def run(self):
        print("thread {} is ready\n ".format(self.name))
        self.event.wait()#阻塞线程
        print("thread {} run\n".format(self.name))

signal = threading.Event()

def main():
    start = time.time()
    for i in range(3):
        t = MyThread(signal)
        t.start()
    time.sleep(3)
    print("after {}s".format(time.time() - start))
    signal.set()
    #在 threading.Thread.event调用set（）方法后开始进行
if __name__=='__main__':
    main()
