#5. How do you count the number of time names repeated in a list?
	
	#names = ["apple", "mango", "banana", "apple", "apple", "mango"]
	
	#sample output = { "apple": 3,"mango": 2,"banana": 1}

# i did'nt get full output of this program

names = ["apple", "mango", "banana", "apple", "apple", "mango"]
	
_dict = { x:names.count(x) for x in names }
print(_dict)