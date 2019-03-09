num_days = int(input())

outstanding_share = 0
price_bought = 0
cash_flow = 100

known_days = []
for i in range(num_days):
    known_days.append(input())
results = list(map(int, known_days))


index = 0
for i in results:
    day_rate = i

    if day_rate < results[index+ 1]:
        # Buy
        # Need to add case when shares is less than 100,000
        outstanding_share = day_rate // cash_flow
        cash_flow -= day_rate * outstanding_share
        price_bought = day_rate
    else:
        if day_rate <= results[index+  1] or index == len(results) - 1:
            cash_flow += outstanding_share * day_rate
            outstanding_share = 0
            price_bought = 0


print(cash_flow)
