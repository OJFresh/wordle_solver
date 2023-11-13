wordle_list = []
with open('5 letter list.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        wordle_list.append(line)


def letter_freq(digit):
    mylist = [0]*26
    for word in wordle_list:
        character = ord(word[digit]) - 97
        mylist[character] += 1
    new_list = []
    for char in mylist:
        new_list.append(100*char/len(wordle_list))
    return new_list


def remove_words(solve_state, guess):
    for i in range(5):
        if solve_state[i] == "g":
            for j in list(wordle_list):
                if j[i] != guess[i]:
                    wordle_list.remove(j)
        elif solve_state[i] == "y":
            for j in list(wordle_list):
                if j[i] == guess[i]:
                    wordle_list.remove(j)
                if guess[i] not in j:
                    wordle_list.remove(j)
        elif solve_state[i] == "b":
            for j in list(wordle_list):
                dup = guess[i]
                temp = 0
                for t in range(5):
                    if (dup == guess[t]) and (solve_state[t] != "b"):
                        temp = 1
                if temp == 1:
                    if j[i] == guess[i]:
                        wordle_list.remove(j)
                elif temp == 0:
                    if guess[i] in j:
                        wordle_list.remove(j)


def word_score(word, concat_letter_freq):
    final_score = 0
    for character in range(5):
        letter_num = ord(word[character]) - 97
        letter_score = concat_letter_freq[character][letter_num]
        final_score += letter_score
    return final_score


def best_word(recs):
    prev_recs = []
    for num in range(1, recs+1):
        highest_score = 0
        output_word = ''
        for word, score in wordle_dict.items():
            if score > highest_score and word not in prev_recs:
                highest_score = score
                output_word = word
        print("the", int, "best word is: " + output_word)
        prev_recs.append(output_word)


# y is Yellow, g is green, b is black
while True:
    letter_freq_list = [letter_freq(x) for x in range(5)]
    print(letter_freq_list)
    wordle_dict = {word: word_score(word, letter_freq_list) for word in wordle_list}
    print("There are " + str(len(wordle_list)) + " words remaining \n")
    best_word(3)
    input_word = input("Input a 5 letter word : ")
    input_state = input("\nInput a 5 letter solve state : ")
    if input_state == 'ggggg':
        break
    remove_words(input_state, input_word)
print("The word is : " + input_word)
