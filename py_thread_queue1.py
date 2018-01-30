# queue 内置锁
#因此 可以写生产 消费
# 和 condition 中的queue=[] 不同
# 那里的queue是一个空列表
# 这里是queue.Queue
import queue
import time
import threading
import random
queue = queue.Queue(10)

class Producer(threading.Thread):

    def run(self):
        while True:
            elem = random.randrange(100)
            queue.put(elem)
            print("Producer a elem {}, Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

class Consumer(threading.Thread):

    def run(self):
        while True:
            elem = queue.get()
            queue.task_done()
            print("Consumer a elem {}. Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

def main():

    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()

if __name__=='__main__':
    main()

