var1 = input()
came, people = var1.split(" ")
leftovers = int(people) - int(came)
pieces = "pieces"
if(leftovers == 1 or leftovers == -1):
    pieces = "piece"

if(leftovers < 0):
    leftovers = leftovers * -1
    print('Dr. Chaz needs ' + str(leftovers) +' more '+pieces+' of chicken!')
else:
    print('Dr. Chaz will have '+ str(leftovers) +' '+ pieces + ' of chicken left over!')

