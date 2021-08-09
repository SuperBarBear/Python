from ClassTest import *

x = ["Winter", "Spring", "Fall"]

print(type(x))

for e in x:
    print(e)

# this is a testidfdh test sample111
for w in x:
    print(w)


data = [x for x in range(1, 4) if x > 0]

print(data)

# this is a testing for branch
# dfgsdjkfdsjkfsdkj
# this dfdfdsff
# fdfd
mike = Person('Mike', 5)  # 帶進去的參數Mike與5分辨對應__init__裡的name與age
john = Person('John', 10)

# 呼叫實體的方法
mike.say_hi()  # output: Hi, my name is Mike, I am 5 years old
john.say_hi()
