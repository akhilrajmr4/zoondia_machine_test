# 2. In a list 1-100 numbers are stored, one number is missing how do you find it? Write a method
# which accepts a list and return the missing number.
# (eg) if list is [1,2,3,5,6] then return missing number is 4

# i did'nt get this answer
lst = [1, 2, 3, 6, 7]
print(lst)
for x in lst:
    for j in (2, x+1):
        print(x, j)
        ak = j-x
        print(ak)