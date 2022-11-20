def fib(n):
    nums = [0, 1]
    def loop(i = 2):
        nums.append(nums[i - 1] + nums[i - 2])
        [int, loop][i < n](i + 1)
    loop()
    return nums[:n]

print(fib(18))