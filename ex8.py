# @Author: Zhang Yongchao <Robin>
# @Date:   2018-04-21T15:10:43+08:00
# @Email:  robinchao2017@gmail.com
# @Project: Learn Python The Hard Way
# @Last modified by:   Robin
# @Last modified time: 2018-04-21T15:14:05+08:00


'''
 **********Exercise 8: Printing, Printing**********
'''

formatter = '%r %r %r %r'

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
'I had this thing.',
'That you could type up right.',
'But it did not sing.',
'So I said goodnight.'
))


'''What You Should See

$ python3 ex8.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' 'But it did not sing.' 'So I said goodnight.'
'''
