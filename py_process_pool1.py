from multiprocessing import Pool

def f(x):
    return x*x

def g(name):
    print('hello',name)

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
    with Pool(5) as p:
        res=[p.apply_async(f,(i,)) for i in range(10)]#iterator#非阻塞，apply 阻塞
        print([resi.get() for resi in res])
