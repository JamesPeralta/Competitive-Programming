first = input()
second = input()

orangeJ, appleJ, pineappleJ = first.split(" ")
orangeC, appleC, pineappleC = second.split(" ")

orangeJNum = float(orangeJ)
appleJNum = float(appleJ)
pineappleJNum = float(pineappleJ)
orangeCNum = float(orangeC)
appleCNum = float(appleC)
pineappleCNum = float(pineappleC)

orangeRatio = orangeJNum /  orangeCNum
appleRatio = appleJNum / appleCNum
pineappleRatio = pineappleJNum / pineappleCNum
myList = [orangeRatio, appleRatio, pineappleRatio]
smallest = min(myList)
final1 = orangeJNum - (smallest * orangeCNum)
final2 = appleJNum - (smallest * appleCNum)
final3 = pineappleJNum - (smallest * pineappleCNum)
print("%f %f %f" %(final1, final2, final3))
