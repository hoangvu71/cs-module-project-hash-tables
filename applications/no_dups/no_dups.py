def no_dups(s):
    # Your code here
    # split string into list of words
    new_s = s.split()
    # have a word visited
    word_visited = {}

    # have an empty list
    empty_list = []

    # for each word in the list
    for index in range(len(new_s)):
    # check if word already in the word visited
    # if it is, remove that word
    
    # if it is not, add it to the word visited
        if new_s[index] not in word_visited:
            word_visited[new_s[index]] = True
            empty_list.append(new_s[index])

    # edge case where it is an empty string
    if len(s) == 0:
        return s
    
    # join all the words together
    space = " "
    empty_list = space.join(empty_list)
    return empty_list
    print(empty_list)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))