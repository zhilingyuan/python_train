a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
zipped=zip(a,b)
print(list(zipped))
#对应元素打包成tuple 再组成列表
#* 相反的过程
print(*zipped)
print(zip(*zipped))
d= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
e=zip(*d)
f=map(list,zip(*e))
f=list(f)
print(f)
