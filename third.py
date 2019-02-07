num = int(input("Enter any number:"))
x = num%2
if x == 0:
	print(num,"is an even number")
elif x == 1:
	print(num,"is an odd number")
else:
	print("Error,Invalid input")
