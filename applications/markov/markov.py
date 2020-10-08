import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# after reading the file, let's put the text into an array
text = words
# put that array into a list of words by string.split
list_of_words = text.split()

# make a word_followed_by dict
word_followed_by = {}

# for everyword in the list of words,
for index in range(len(list_of_words)):
    word = list_of_words[index]
# if word in word_followed_by, then add in the word after it
    # edge case where it is the last word:
    if index < len(list_of_words) - 1:
        if word in word_followed_by:
            word_followed_by[word] += (" " + list_of_words[index + 1])
    # if word not in word_followed_by, then add that word and the word after it
        elif word not in word_followed_by:
            word_followed_by[word] = list_of_words[index + 1]
# once we have a dataset to work with



# TODO: construct 5 random sentences
# Your code here

# Choose a random "start word" (with capitalization)
# let's choose "That's" as start word
start_word = "You"
# if that word is in the word_followed_by
list_words = []
list_words.append(start_word)
stop_word_sign = '.?!'
def talk(word):
# and if there are multiple, choose a random word in there and
    if word in word_followed_by:
        new_word = word_followed_by[word].split()

        # check if word is a stop word
        for letter in word:
            if letter in stop_word_sign:
                return list_words

        if len(new_word) > 1:
            next_word = random.choice(new_word)
            list_words.append(next_word)
        
        else:
            next_word = word_followed_by[word]
            list_words.append(next_word)
        
        return talk(next_word)

five_sentences = ["You", "The", "What", "Now", "Do"]
for sentence in five_sentences:
    start_word = sentence
    # reset list words
    list_words = []
    list_words.append(start_word)
    talk(start_word)
    final_string = " ".join(list_words)
    print(final_string)
# add it to the string
# continue to do this (recursive should work nicely)
# if the word that we choose has a '.?!' then that means it is a "stop word"
