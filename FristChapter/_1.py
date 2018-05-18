import math
'''输出球的直径， 圆周长， 表面积， 体积'''
def func(r : float) -> float:
    print("直径是：", 2*r)
    print("圆周长是：", 2*math.pi*r)
    print("圆表面积是:", 4*math.pi*r*r)
    print("圆体积是：", 4*math.pi*r**3/3)

func(1)
