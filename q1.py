# 1. Write a method which will remove any given character from a String?
_str = input("Enter a string : ")
print(_str) 
_str1 = input("Enter which character you want to remove : ")
print("The removing charecter", _str1)

ou = _str.replace(_str1,'')
print("The output is : ",ou)