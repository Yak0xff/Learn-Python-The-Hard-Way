# @Author: Zhang Yongchao <Robin>
# @Date:   2018-04-21T14:56:07+08:00
# @Email:  robinchao2017@gmail.com
# @Project: Learn Python The Hard Way
# @Last modified by:   Robin
# @Last modified time: 2018-04-21T15:02:10+08:00



'''
 **********Exercise 5: More Variables and Printing**********
'''


my_name = 'Robin Chao'
my_age = 33 # not a lie
my_height = 74 # inches
my_weight = 130 #lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print('Actually that is not too heavy.')
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print('His teeth are usually %s depending on the coffee.' % my_teeth)

# this line is tricky, try to get it exactly right
print('If I add %d, %d, and %d I get %d.' % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))


'''What You Should See

$ python3 ex5.py
Let's talk about Robin Chao.
He's 74 inches tall.
He's 130 pounds heavy.
Actually that is not too heavy.
He's got Black eyes and Black hair.
His teeth are usually White depending on the coffee.
If I add 33, 74, and 130 I get 237.
'''
