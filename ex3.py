# @Author: Zhang Yongchao <Robin>
# @Date:   2018-04-21T14:09:45+08:00
# @Email:  robinchao2017@gmail.com
# @Project: Learn Python The Hard Way
# @Last modified by:   Robin
# @Last modified time: 2018-04-21T14:18:34+08:00

'''
 **********Exercise 3: Numbers and Math**********

 Basic math symbols

    + 、-、/、*、%、<、>、<=、>=

'''


print('I will now count mu chickens:')

print('Hens', 25 + 30 / 6)
print('Roosters', 100 - 25 * 3 % 4)

print('Now I will count the eggs:')

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print('Is it true that 3 + 2 < 5 - 7?')

print(3 + 2 < 5 - 7)

print('What is 3 + 2?', 3 + 2)
print('What is 5 - 7?', 5 - 7)

print("Oh, that's why it's False.")

print('Is it greater?', 5 > -2)
print('Is it greater or equal?', 5 >= -2)
print('Is it less or equal?', 5 <= -2)





'''What You Should See

$ python ex3.py
I will now count mu chickens:
Hens 30.0
Roosters 97
Now I will count the eggs:
6.75
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
'''
