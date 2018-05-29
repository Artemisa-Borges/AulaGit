
'''
Simple function that takes a list square its elements
and returns another list
'''
def square(list_num):
    results = []
    for i in list_num:
        results.append(i*i)

    return results

list_num = range(1,10)
sqr_list = square(list_num)
print(sqr_list)

'''
Modifying the code above to produce a Generator
'''

def square(list_num):

    for i in list_num:
        yield i*i



list_num = range(1,10)
sqr_list = square(list_num)
print(sqr_list)         # prints the generator object reference
print(next(sqr_list))   # because generators produce an iterator you can call next on the object
print(next(sqr_list))

# Since sqr_list is an iterable you can use a for loop on them
for i in sqr_list:
    print(i)


# Create Generators from list comprehension
#############################################

sqr_list = [ x * x for x in range(1,11)]


# To convert a list comprehension to a generator just replace the [] by ()
sqr_list = ( x * x for x in range(1,11))


print(sqr_list)
for i in sqr_list:
    print(i)







