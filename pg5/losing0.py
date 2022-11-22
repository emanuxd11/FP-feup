def remove_leading(ip):
    nums = ip.split('.')
    nums[0] = str(int(nums[0]))
    nums[1] = str(int(nums[1]))
    nums[2] = str(int(nums[2]))
    nums[3] = str(int(nums[3]))
    return '.'.join(nums)

print(remove_leading('255.024.01.01'))