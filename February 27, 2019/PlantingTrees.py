arg1 = input()
trees_cases = input().split(" ")
results = list(map(int, trees_cases))
results.sort(reverse=True)

days_passed = 1
longest_possible = 0
for i in results:
    if i + days_passed > longest_possible:
        longest_possible = i + days_passed
    days_passed = days_passed + 1

print(longest_possible + 1)