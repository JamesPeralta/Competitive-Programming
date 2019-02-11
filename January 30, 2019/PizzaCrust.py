import math
i1, i2 = input().split(" ")
radius = int(i1)
crust = int(i2)
innerRadius = radius - crust 

totalarea = math.pi * int(radius) * int(radius)
cheesearea = math.pi * int(innerRadius) * int(innerRadius)
print((cheesearea / totalarea) * 100)

