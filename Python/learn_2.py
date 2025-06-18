x = 5
x, y = y = 1, x
print(x, y) # 1 (1, 5)


# ----------------------------------------------------------------------
def peak_element(nums):
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return nums[i]
    return max(nums)

lst1 = [1, 3, 20, 4, 1, 0]
print(peak_element(lst1))

# Given a npn-empty array of digits representing a integer, increment this integer by one and return the updated arrary of digit 
# nums = [1, 2, 3] -> 123 + 1 = 124
# nums = [9] -> 9 + 1 = 10

def list_Intger_Increment(nums):
    if isinstance(nums, list):
        newNums = ''; fl = 0; st = 0
        for i in nums:
            if type(i) is int: newNums += str(i)
            elif type(i) is float: fl += 1; newNums += str(i)
            elif type(i) is str: st += 1
        
        if st != 0: print(f'There are {st} Other type, value present inside a list. we can only accept int or float.')
        if fl == 0: finalNums = int(newNums) + 1
        else: finalNums = float(newNums) + 1

    return finalNums

lst1 = [1, 2, 3, 1.3, 9, 'st', 10, '0']
print(list_Intger_Increment(lst1))

# -------------------------------------------------------------------------------------
nums = [1, 10, 2, 20, 3, 30]
nums.sort(key=lambda x: x % 10)
print(nums)

# -------------------------------------------------------------------------------------
a = 'learn'
b = 'about'
c = 'string'
d = 'variable'
e = 'in'
f = 'python'

res = c[3] + ' ' + a[0] + b[2] + d[0] + d[len(d) - 1] + ' ' + b[-2]
print(res)

# --------------------------------------------------------------------------------------
