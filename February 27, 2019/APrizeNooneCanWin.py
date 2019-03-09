arg1 = input()
arg2, arg3 = arg1.split(" ")

total_items = int(arg2)
max_amount = int(arg3)
item_prices = input().split(" ")
results = list(map(int, item_prices))
results.sort()

if total_items < 2:
    print(total_items)
else:
    number_of_items = 0
    last_price = 0
    for i in results:
        if last_price + int(i) <= max_amount:
            last_price = int(i)
            number_of_items = number_of_items + 1

    if number_of_items == 0:
        print(1)
    else:
        print(number_of_items)
