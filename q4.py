# How to find the top two maximum number in a list?

inp = int(input("Enter limit of a list : "))
lst = []
for x in range(1,inp+1):
    ab = input("Enter "+str(x)+" value : ")
    lst.append(int(ab))
print(lst)
hi = sorted(lst, reverse=True)
print(hi)
print("Top two numbers : ", hi[0],",", hi[1])