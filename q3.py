# How do you find the second highest number in an integer list? 

inp = int(input("Enter limit of a list : "))
lst = []
for x in range(1,inp+1):
    ab = input("Enter "+str(x)+" value : ")
    lst.append(int(ab))
se = sorted(lst, reverse=True)
print(se)
print("second largest number is : ", se[1])