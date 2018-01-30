#fork()
#调用一次返回2次
#父进程复制一份为子进程后，分别返回
#子进程一直返回0
#父进程返回子进程的id
#子进程getppid（）可以拿父进程的ID
# not in windows
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
