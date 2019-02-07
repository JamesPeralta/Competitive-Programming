steps = int(input())
while steps != 0:
    binary = bin(steps)
    binaryString = binary[2:]
    print(binaryString)
    steps = int(input())
