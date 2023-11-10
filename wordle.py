wordle_list = []
with open('5 letter list.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        wordle_list.append(line)


def remove_words(solve_state):
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


#y is Yellow, g is green, b is black
while True:
    print(wordle_list)
    print("There are " + str(len(wordle_list)) + " words remaining \n")
    guess = input("Input a 5 letter word : ")
    input_state = input("\nInput a 5 letter solve state : ")
    if input_state == 'ggggg':
        break
    remove_words(input_state)
print("The word is : " + guess)
