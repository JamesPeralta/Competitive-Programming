arg = input()
nums = list(map(lambda x: int(x), input().split()))
nums = sorted(nums)

left = 0
count = 0
while left < len(nums):
    if nums[left] == -1:
        left += 1
    else:
        value = nums[left] + 1
        right = left + 1
        while right < len(nums):
            if nums[right] == -1 or nums[right] == value - 1:
                right += 1
            elif nums[right] == value:
                value += 1
                nums[right] = -1
                right += 1
            else:
                break

        count += 1
        left += 1

print(count)