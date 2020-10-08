# Your code here

def histogram(file):
    # open and save to variable
    with open(file) as f:
        words = f.read()

    # make strings lower case
    # split strings to list
    lower_words = words.lower()

    split_words = lower_words.split()

    # clean up
    # if word contains special characters
    # delete that special character

    special_characters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    for index in range(len(split_words)):
        word = split_words[index]
        for indexWord in range(len(word)):
            letter = word[indexWord]
            if letter in special_characters:
                new_word = word.replace(letter, ' ')
                split_words[index] = new_word
                word = split_words[index]

    # strip all space from the replace ' ' from previous line
    for index in range(len(split_words)):
        word = split_words[index]
        split_words[index] = word.strip()

    # now every word is clean
    # make a word_visited dict
    # if word in word_visited, add a "#"
    # if not, = "#"
    word_visited = {}
    for index in range(len(split_words)):
        word = split_words[index]
        if word in word_visited:
            word_visited[word] = word_visited[word] + '#'
        elif word not in word_visited:
            word_visited[word] = '#'


    # once we have the dict finished, we need to output it as
    # the ones that have the most # gets printed first
    # if they have the same amounts of #, print it alphabetically
    # i think this one we can do a dict
    # ex: 11: "the and of"
    # 11 is amount of # and the and of is the key of word_visited
    # split the value, and sort. 

    hastag_dict = {}
    # for every word in the word_visited
    for index in range(len(split_words)):
        word = split_words[index]
    # see how many # it is in a particular index
        number_of_hastags = len(word_visited[word])
    # check to see if the number of # is already in dict
        if number_of_hastags in hastag_dict:
        # if it is in dict, add the key (meaning the word) to the string in there
            if word not in hastag_dict[number_of_hastags]:
                hastag_dict[number_of_hastags].append(word)

        # if it is not in a dict, make it = to the word
        elif number_of_hastags not in hastag_dict:
            hastag_dict[number_of_hastags] = [word]
    
    
    # so now we can print the ones with the most hastags first, lets work on
    # sorting it alphabetically

    # for every key in the dict, sort its value
    for everyKey in hastag_dict:
        hastag_dict[everyKey].sort()


    

    # alright, so we now have a dict that is sorted by numbers and if numbers are the same,
    # then sort it alphabetically

    # so now what we need to do is print the number 
    # so for every value in the hastag_dict
    # ex: you and do what
    # print( that value + the value of key ( which we will convert to a string of #)
    for i in sorted (hastag_dict.keys(), reverse=True) :
        for index in range(len(hastag_dict[i])):    
            everyValue = hastag_dict[i][index]
        # everyKey is a number, let's convert it to a number of hastags
            hastag_convert = ""
            for index in range(i):
                hastag_convert += '#'
        # so now we have the word ( which is the everyValue)  and the
        # hastag ( which is hastag_convert)
        # let's print
            # found out we need to print "organizibly", is that a word?
            # anyway, we can do a len(word) and len(space), in which, space will be
            # the total length of space - len(word)
            # let's put total space = like 20 characters
            total_space = 20
            # a space
            a_space = " "
            space_left = total_space - len(everyValue)
            for numberSpace in range(space_left):
                a_space += " "
            print(everyValue, a_space, hastag_convert)

            # reset hastag convert
            hastag_convert = ""

            # DONE!
            # NICE!
histogram("robin.txt")