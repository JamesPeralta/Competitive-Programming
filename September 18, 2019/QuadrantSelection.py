x = int(input())
y = int(input())

# quadrant 1
if x > 0 and y > 0:
    print(1)
# quadrant 2
elif x < 0 and y > 0:
    print(2)
# quadrant 3
elif x < 0 and y < 0:
    print(3)
# quadrant 4
else:
    print(4)
