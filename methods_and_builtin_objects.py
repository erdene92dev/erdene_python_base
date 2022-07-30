# # append method
# my_list=[1,2,3,4,5]
# # # append method, add item to object
# my_list.append(4)
# print(my_list)


# # pop method
word_list=['apple','banana','fudgecake','watermelon','orange']
print('word_list before pop:',word_list)
word_list.pop(2)
print('word_list after pop',word_list)

word_list=['apple','banana','fudgecake','watermelon','orange','fudgecake']
print('\nword_list =',word_list,'\ntotal items in word list:',len(word_list))
# # # count method
# # # Value equired. Any type (string, number, list, tuple, etc.). The value to search for.
# # print(word_list.count('fudgecake'))

# # extend
# # extend method takes an iterable such as list, tuple, string etc
# # and adds all the elements of an iterable (list, tuple, string etc.) to the end of a list.
# # The extend() method modifies the original list. It doesn't return any value.
my_tuple = ('queen', 'linkin park')
word_list.extend(my_tuple)
print('after extend:',word_list, '\ntotal items after extend:', len(word_list))

# append works the same way
word_list.append(('queen2','linkinpark'))
print('after append:',word_list, '\ntotal items after extend:', len(word_list))

# insert works like extend/append, what makes it unique is that it allows you
# to insert the new objects at a particular inde

word_list.insert(1,('new york','california'))
print('after insert=',word_list,'\ntotal items after extend:', len(word_list))



