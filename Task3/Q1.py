import numpy as np
a=int(input("First Number: "))
b=int(input("Last Number: "))
nums=np.arange(a,b+1)
new_nums=np.zeros(len(nums)+(len(nums)-1)*(5))
new_nums[::6]=nums
print(new_nums)
