#shared value
#共享内存
import multiprocessing as mp
value1=mp.Value('i',0)
value2=mp.Value('d',3.14)
#mp.Array
#用于共享内存的交互，实现进程之间共享数据
#与numpy.array 不同
#只能是一维的
