#3.4
for i in range(1,3):
    for x in range (1,8):
        print("@",end=" ")
    print()
# 3.9
num = int(input("Please enter a 7 to 10 digit number: "))
m = len(str(num))-1

while m >= 0:
    print(num // (10 ** m))
    num %= (10 ** m)
    m -= 1
# 3.11
galused = None
total = 0
while galused != -1:
    galused = int(input("Enter the gallons used (-1 to end): "))
    if galused != -1:
        miles = int(input("Enter the miles driven: "))
        mpg = miles / galused
        print(f'The miles/gallon for this tank was {mpg}')
        total += mpg
    else:
        break
print(f'The overall average miles/gallon was {total}')

# 3.12
while True:
    num = input("Please enter a 5 digit integer: ")
    if len(num) == 5:
        num = int(num)
        if num // 10000 == num % 10 and (num // 10) % 10 == (num // 1000) % 10:
            print("Palindrome!")
        else:
            print("Not a Palidrome!")
            break
    else:
        break
    break

# 3.14
m = 0
denom = 1
pi = 0
while m <= 3000:
    if m % 2 == 0:
        pi += 4/denom
    else:
        pi -= 4/denom
    denom += 2
    m += 1
    print("At iteration",m,"Pi is equal to",pi)
# first iteration where 3.14 occurs twice in a row is iteration 627 and 628
# first iterations where 3.141 occurs twice in a row is iteration 2454 and 2455



