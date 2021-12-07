import random

if __name__ == '__main__':
    a = random.randint(0, 99)   # 若取0则会报错，改进代码自行研究
    b = random.randint(0, 99)   # 若取0则会报错，改进代码自行研究
    print(id(a))
    print(type(a))
    print(a+b, a-b, a*b, a/b, a**b)



