nums = input().split(" ")

matrix = []
for i in range(int(nums[0])):
    for k in range(int(nums[1])):
        if i % 2 == 0 and k % 2 == 0:
            matrix.append(".")
        elif i % 2 == 0 and k % 2 != 0:
            matrix.append("*")
        elif i % 2 != 0 and k % 2 == 0:
            matrix.append("*")
        elif i % 2 != 0 and k % 2 != 0:
            matrix.append(".")

num = [k for k in range(1, (int(nums[0])*int(nums[1])) + 1) if k % int(nums[1]) == 0]
print(*matrix[:int(nums[1])])
for u in range(len(num) - 1):
    print(*matrix[num[u]:num[u + 1]])