#2.3
grade = eval(input("What is your current class grade?: "))
if grade >= 90:
    print(f'Congratulations! Your grade of {grade} earns you an A in this course.')

#2.4
print(27.5 + 2)
print(27.5 - 2)
print(27.5  / 2)
print(27.5 // 2)
print(27.5 * 2)
print(27.5 ** 2)

#2.5
π = 3.14159
r = 2
diameter = 2 * r
circumference = 2 * π * r
area = π * (r ** 2)
print("Diameter:",diameter,"\nCircumference:",circumference,"\nArea:",area)

#2.6
num = input("Please enter an integer: ")
num = eval(num)
if num % 2 == 0:
        print("The number you entered was even.")
else:
        print("The number you entered was odd.")

#2.7
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else: 
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

#2.8
print("number \tsquare \tcube")
print("0\t",0**2,"\t",0**3)
print("1\t",1**2,"\t",1**3)
print("2\t",2**2,"\t",2**3)
print("3\t",3**2,"\t",3**3)
print("4\t",4**2,"\t",4**3)
print("5\t",5**2,"\t",5**3)