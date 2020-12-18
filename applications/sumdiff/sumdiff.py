"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# so ex: 
# f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
# f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
# f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
# f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
# f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
# f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
# f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18

# what we can do is to check everypossible combination of addition ( f + f )
# make add_sub_dict
add_sub_dict = {}

# iterate through the q twice
for num1 in q:
    for num2 in q:
        # if the combination not in dict, = the value
        if (f(num1) + f(num2)) not in add_sub_dict:
            add_sub_dict[f(num1) + f(num2)] = [f'f({num1}) + f({num2})']
        elif (f(num1) + f(num2)) in add_sub_dict:
            add_sub_dict[f(num1) + f(num2)].append(f'f({num1}) + f({num2})')
for num1 in q:
    for num2 in q:
        if (f(num1) - f(num2)) not in add_sub_dict:
            add_sub_dict[f(num1) - f(num2)] = [f'f({num1}) - f({num2})']
        elif (f(num1) - f(num2)) in add_sub_dict:
            add_sub_dict[f(num1) - f(num2)].append(f'f({num1}) - f({num2})')

# now lets filter out the ones with muliple values ( those are the ones with the same num formula from above)

filter_dict = {}
for value in add_sub_dict:
    if len(add_sub_dict[value]) > 1:
        filter_dict[value] = add_sub_dict[value]

for value in filter_dict:
    print(value, " : ", filter_dict[value])

# for every value in filter dict we wanna check if they contains both the add and sub combination
# if they do, we will add them into a filter_dict2
filter_dict2 = {}
print("##########")
for value in filter_dict:
    print(value, filter_dict[value])
# now that we have the combination we need to check if the list contains both the add comb and the sub comb
# lets make a function for that called
# check_comb()
def check_comb(array):
    # run though each array and run through each string
    add = False
    sub = False
    for string in array:
        for letter in string:
            if letter == "+":
                add = True
            if letter == "-":
                sub = True
    if add and sub:
        return True
    else:
        return False

# once we have the function, we can check every value in the filter dict
# if it is True (check_comb()), then we put it into another dict called the filter_dict2
for value in filter_dict:
    if check_comb(filter_dict[value]):
        filter_dict2[value] = filter_dict[value]

print("filterdict2")
for value in filter_dict2:
    print(value, filter_dict2[value])



# once we have the final dict(filter dict2), we can
# use a list, and iterate over the key, then iterate over the value to add every single value into the list
def print_formula(array):
    for num1 in array:
        for num2 in array:
            if num1 != num2 and is_add(num1) and is_sub(num2):
                print(num1, " = ", num2)

def is_add(string):
    for letter in string:
        if letter == "+":
            return True
    return False

def is_sub(string):
    for letter in string:
        if letter == "-":
            return True
    return False

for value in filter_dict2:
    print_formula(filter_dict2[value])

# then we can iterate over the list, like
# for num1 in list
    # for num2 in list
# though make sure that num1 and num2 is not the same, cuz that s not what we want
# also make sure that num1 is a add comb and num2 is a sub comb
# we can create two different functions for that called is_add(string) is_sub(string)



 