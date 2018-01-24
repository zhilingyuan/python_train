import time
import threading
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)

def main():
    print("Start main threading")
    # 创建三个线程
    threads = [MyThread() for i in range(3)]
    # 启动三个线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()#等待直到线程结束
        #join 挡住 无法执行join 后的语句
    print("End Main threading")


if __name__ == '__main__':
    main()

