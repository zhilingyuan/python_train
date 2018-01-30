class Human(object):  
    Can_Talk = True  
    Can_Walk = True  
    Age = 0  
    Name = ["Li", "Lei"]  
   
   
a = Human()  
b = Human()  
   
a.Age += 1  
print(a.Age)  
print(b.Age)  
   
a.Name[0] = "Wang"  
print(a.Name) 
print(b.Name)

print(a.__class__.__dict__)
print(a.__dict__)
print(b.__class__.__dict__)
print(b.__dict__)
# 为了避免 出现重复的class 中内容
# 应该添加class 内不__init__ 方法
