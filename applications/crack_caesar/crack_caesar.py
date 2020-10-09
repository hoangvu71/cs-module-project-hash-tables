# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# read the file
with open("ciphertext.txt") as f:
    words = f.read()
# split it to work on it easier
split_words = words.split()
# make a word_visited dict
letter_visited = {}
total_letters_in_file = 0

# special character not letter:
special_letter_to_ignore = "\" â : ; , . - + = / \ | [ ] { } ( ) * ^ & ' € 1 2 3 4 5 6 7 8 9 0 ? ! ” "


# so for every word, we ignore the special chars
for index in range(len(split_words)):
    word = split_words[index]
# for every letter in the word
    for indexL in range(len(word)):
        letter = word[indexL]
        if letter not in special_letter_to_ignore: 
            # keep track of how many letters there are in file
            total_letters_in_file += 1

    # if letter in letter_visted, up the count
            if letter in letter_visited:
                letter_visited[letter] += 1
    # if letter not in letter_visited, count = 1
            elif letter not in letter_visited:
                letter_visited[letter] = 1

print(letter_visited)
# make another dict called word_freq = {}
word_freq = {}
# the key in word_freq is the letter, same as in word visited
for key in letter_visited:
    if key not in word_freq:
        round_value = round(letter_visited[key] / total_letters_in_file * 100, 2)
        word_freq[key] = round_value


read_me = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
word_freq_list = []
decipher = {}
read_me_counter = 0
for i in sorted(word_freq, key=word_freq.get, reverse=True):
    print(i, word_freq[i])
    word_freq_list.append(i)

# however the value in word_freq is in %
# so it will be count / total words, up to 2 decimals

# once we have a dict with the letter and the percentage
# we can sort it ( percentrage sort )

# then we put the key of the word_freq dict
# and the key of the one in readme as a set
# then we can can try and print out the one in the file

    decipher[i] = read_me[read_me_counter]
    read_me_counter += 1

print(word_freq)
print(decipher)
# now that we have the deciper dict
# we can convert everything in the word split and then join them together

# so for every word, we ignore the special chars
for index in range(len(split_words)):
    word = split_words[index]
    new_word = ""
# for every letter in the word
    for indexL in range(len(word)):
        letter = word[indexL]
        if letter not in special_letter_to_ignore: 
            # change the key letter to the value in decipher
            new_word = new_word + f'{decipher[letter]}'
        elif letter in special_letter_to_ignore:
            new_word = new_word + f'{letter}'
    split_words[index] = new_word
    new_word = ""

x = " ".join(split_words)
print(x)