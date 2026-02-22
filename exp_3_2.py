'''2. Find whether the given number is Armstrong number. '''
num = int(input("Enter a number: "))
original = num
total = 0
power = len(str(num))

while num > 0:
    digit = num % 10
    total += digit ** power
    num //= 10

if total == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
