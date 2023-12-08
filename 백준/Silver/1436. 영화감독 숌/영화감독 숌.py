N = int(input())
nums = []
for i in range(666, 1000 * N):
    if '666' in str(i):
        nums.append(i)
    if len(nums) == N:
        break
print(nums[len(nums)-1])