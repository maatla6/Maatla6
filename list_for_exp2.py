# Read the number from the user
num = int(input("Enter a number to display its multiplication table: "))

# Display the multiplication table using a for loop
print("Multiplication table of",num,":")
for i in range(1, 11):
    result = num * i
    print(num,"*" ,i," =" , result)

