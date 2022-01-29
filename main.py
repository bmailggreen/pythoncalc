'''
class Ize:
    def ize(self):
        print("Fontos")
        pass


print("Helló Világ!!!!")
ize = Ize()
ize.ize()
'''

import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def factorial(user_input):
    factorial_value = 1
    for number in range(user_input):
        if number > 0:
            factorial_value *= number
            print(factorial_value)

main_a = 3
main_b = 4
result_number = add(main_a, main_b)
result_text = str(result_number)

print('3 + 4 = ' + result_text)



number = int(input("give me a number: "))

factorial(number)



sub_result_num = sub(main_a, main_b)
sub_result_text = str(sub_result_num)

print('3 - 4 = ' + sub_result_text)

