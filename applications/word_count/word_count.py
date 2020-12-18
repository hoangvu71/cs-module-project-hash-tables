def word_count(s):
    # Your code here
    # return a dictionary of words and their count
    # case should be ignored and output keys must be lowercase
    # make a list of words that visited
    word_visited = {}
    
    # make those words lower case
    s_lower = s.lower()
    # split the string into list of words
    list_of_words = s_lower.split()
    # if the list of words have the following " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    special_letter_to_ignore = "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &"
    
    for wordIndex in range(len(list_of_words)):
        eachWord = list_of_words[wordIndex]
        for index in range(len(list_of_words[wordIndex])):
            if eachWord[index] in special_letter_to_ignore:
                # delete that special character
                newWord = eachWord.replace(eachWord[index], '')
                list_of_words[wordIndex] = newWord

                
    print(list_of_words)
    # now we have a list of words that are clean and ready to be put into
    # the list of word visited
    # for each word, check if the word is in the word_visited
    for eachWord in list_of_words:
    # if it is not in there, add it in
        if eachWord not in word_visited:
            word_visited[eachWord] = 1
    # if it is in there, up the count
        elif eachWord in word_visited:
            word_visited[eachWord] += 1

    print(word_visited)
    # if the input contains only ignored characters, return an empty dictionary
    for eachWord in list_of_words:
        count = 0
        for eachLetter in eachWord:
            if eachLetter in special_letter_to_ignore:
                count += 1

        # if count == len(eachWord) that means every single letter is a special character
        if count == len(eachWord):
            return {}
    print(word_visited)
    return word_visited

if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))