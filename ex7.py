# @Author: Zhang Yongchao <Robin>
# @Date:   2018-04-21T15:07:54+08:00
# @Email:  robinchao2017@gmail.com
# @Project: Learn Python The Hard Way
# @Last modified by:   Robin
# @Last modified time: 2018-04-21T15:10:28+08:00


'''
 **********Exercise 7: More Printing**********
'''


print('Mary had a little lamb.')
print('Its fleece was white as %s.' % 'snow')
print('And everywhere that Mary went.')
print("." * 10)  # what'd that do?



end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)




'''What You Should See

$ python3 ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese
Burger
'''
