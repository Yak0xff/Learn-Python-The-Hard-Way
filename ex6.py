# @Author: Zhang Yongchao <Robin>
# @Date:   2018-04-21T15:02:17+08:00
# @Email:  robinchao2017@gmail.com
# @Project: Learn Python The Hard Way
# @Last modified by:   Robin
# @Last modified time: 2018-04-21T15:07:28+08:00


'''
 **********Exercise 6: Strings and Text**********
'''


x = 'There are %d types of people.' % 10
binary = 'Binary'
do_not = "don't"
y = 'Those who know %s and those who %s.' % (binary, do_not)

print(x)
print(y)

print('I said: %r.' % x)
print("I alse said: '%s'" % y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = 'This is the left side of ...'
e = 'a string with a right side.'

print(w + e)


'''What You Should See

$ python3 ex6.py
There are 10 types of people.
Those who know Binary and those who don't.
I said: 'There are 10 types of people.'.
I alse said: 'Those who know Binary and those who don't.'
Isn't that joke so funny?! False
This is the left side of ...a string with a right side.
'''
