num_cases = int(input())

for i in range(num_cases):
    num_customers = int(input())
    customer_times = []
    for j in range(num_customers):
        customer_wood = input().split(" ")[1:]
        results = list(map(float, customer_wood))
        total = 0
        for num in results:
            total = total + num
        customer_times.append(total)

    total_time = 0
    customer_times.sort()
    finished_times = []
    for james in customer_times:
        total_time = total_time + james
        finished_times.append(total_time)

    before_division = 0
    for calculate in finished_times:
        before_division = before_division + calculate

    print(before_division / len(finished_times))
