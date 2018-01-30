from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    a=[]
    for i in range(5):
        a.append(p.apply_async(long_time_task, args=(i,)))#非阻塞
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()#先close 再join close后不会有新的进程加入pool
    print('All subprocesses done.')
