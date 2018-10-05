print("Hello world")

number1 = 2
number2 = 40

print(number1, number2)

sum = number1 + number2

print(sum)


#if 'condition':
# 'your code'

if number1 < number2:
    print("hi, welcome to Python!")
elif number1 > number2:
    print("your number is greater!")
else:
    print("The condition is false")


temp = 90
if temp > 80:
    print("We will go swiming")
elif temp < 50:
    print("We will wear a jacket")
else:
    print("We will stay at home")

#while 'condition'
#    'your code'

number = 0
while number < 10:
    print("Hi") #prints all numbers '(number, end= ' ')' in one line in Python 3
    number += 1

a = [1,2,4,5,6,7,8,9,10]
number = 0
while number <= 10:
    print(number),
    number += 1

# for 'num' in 'list':
#   'your code'
print

number = {1,2,3,4,5,6,7,8,9,10}
for number in range(10):
    print(number),

#Print all numbers between 10 and 20, inclusively

print

numbers = [10,11,12,13,14,15,16,17,18,19,20,21]
for numbers in range(10, 21):
    print(numbers),

print
a = 12
for a in range(12, 22):
    print (a)

print

arr = [10, 20, 30, 40]
arr[1] = 30
print(arr)
