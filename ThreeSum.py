def threeSum(nums):
    p = 0
    for i in nums:
        if i != 0:
            p += 1
            break
    if p==0:
        return [[0,0,0]]

    def twoSum(num, x):
        d = {}
        twonum = []
        a = []
        for i, n in enumerate(num):
            pair = x - n
            if pair in d:
                if [pair,n] != a:
                    twonum.append([pair,n])
                    a = [pair,n]
            else:
                #store index of n into dict d since searching in dict is 0(1)
                d[n] = i
        if twonum != []:
            return twonum
        else:
            return False

    nums.sort()
    result = []
    for i in range(len(nums)):
        if i == 0:
            pair = twoSum(nums[i+1:], 0 - nums[i])
            if pair != False:
                for x in pair:
                    sol = [nums[i],x[0],x[1]]
                    result.append(sol)

        elif nums[i] != nums[i-1]:
            pair = twoSum(nums[i+1:], 0 - nums[i])
            if pair != False:
                for x in pair:
                    sol = [nums[i],x[0],x[1]]
                    result.append(sol)
    return result

threeSum([-2,0,0,2,2])

twoSum([-1,0,1,2], 1)

    j=0
    for i in nums:
        pair = twoSum(nums[j+1:], 0 - i)
        j += 1
        if pair != False:
            for x in pair:
                sol = [i,x[0],x[1]]
                result.append(sol)


a = [0,2,-2]
b = [2,-2,0]
set(a) == set(b)



d = {'2':'5'}


c = [1,1,2,4]
c.remove(1)
c

c = [[2, 0, -2], [-2, 0, 2]]
c[0] in c[1]

set(c[0]
d = {}
for i,n in enumerate(c):
    if set(n) in d:
        d[set(n)] += 1
    else:
        d[set(n)] = 1
