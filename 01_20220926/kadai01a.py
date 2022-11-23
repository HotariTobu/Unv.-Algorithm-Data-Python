count = 3

nums = []
for i in range(count):
    nums.append(int(input()))

print("max value is", max(*nums))
print("average is", sum(nums) / len(nums))