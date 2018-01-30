import multiprocessing
import time
#pipe 方法返回（conn1，conn2）管道两端
#pipe 方法参数duplex为True 全双工
#duplex为False conn1 接受，conn2 发送


def proc1(pipe):
    while True:
        for i in range(10000):
            print("send: %s" %(i))
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    while True:
        print("proc2 rev:", pipe.recv())
        time.sleep(1)

def proc3(pipe):
    while True:
        print("PROC3 rev:", pipe.recv())
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    p3 = multiprocessing.Process(target=proc3, args=(pipe[1],))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
