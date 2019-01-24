numOfPeriods = int(input())
qaly = 0
for i in range(0, numOfPeriods):
    a, b = str(input()).split(" ")
    a_float = float(a)
    b_float = float(b)
    qaly += a_float * b_float

print(qaly)
