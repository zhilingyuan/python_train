import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
#Queue.Queue是进程内非阻塞队列，
#multiprocess.Queue是跨进程通信队列。多进程前者是各自私有，后者是各子进程共有。
#这个是多进程并发的Queue队列，用于解决多进程间的通信问题。
#普通Queue实现不了。例如来跑多进程对一批IP列表进行运算，
#运算后的结果都存到Queue队列里面，这个就必须使用
