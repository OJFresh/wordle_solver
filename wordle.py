f = open('5 letter list.txt','r')
wordle_list = []
wordle_dictionary = {}
for line in f:
    line = line.replace('\n', '')
    wordle_list.append(line)
f.close()

best = {'e':56.88, 'a':43.31,
        'r':38.64, 'i':38.45,
        'o':36.51, 't':35.43,
        'n':33.92, 's':29.23,
        'l':27.98, 'c':23.13,
        'u':18.51, 'd':17.25,
        'p':16.14, 'm':15.36,
        'h':15.31, 'g':12.59,
        'b':10.56, 'f':9.24,
        'y':9.06, 'w':6.57,
        'k':5.61, 'v':5.13,
        'x':1.48, 'z':1.39,
        'j':1.00, 'q':1.00,}

def freq_score(word):
  score = 0
  for i in range(5):
    score += best[word[i]]
  return score

def freq_score_highest():
  top_score = 0
  top_word = ""
  for i in wordle_list:
    if freq_score(i)>top_score:
      top_score = freq_score(i)
      top_word = i
  print("The top word is " +  top_word + " with a score of " + str(top_score))


def lowest_remaining():
  temp = wordle_list
  for a in wordle_list:
    return 0



def average_gyb_score(guess):
  sum = 0
  for i in range(len(wordle_list)):
    output = 0
    for x in range(5):
      if guess[x] == wordle_list[i][x]:
          output += 3
      elif (guess[x] != wordle_list[i][x]) and (guess[x] in wordle_list[i]) :
          output += 1
    if output == 15:
      print(wordle_list[i])
      sum += output

    return sum/len(wordle_list)

def highest_score():
  top_score = 0
  top_word = ""
  for x in wordle_list:
    if average_gyb_score(x) > top_score:
      top_score = average_gyb_score(x)
      top_word = x
  print("The top word is " +  top_word + " with a score of " + str(top_score) + " and a sum of " + str(top_score*len(wordle_list)))

def remove_high():
  top_score = 0
  top_word = ""
  for x in wordle_list:
    if average_gyb_score(x) < top_score:
      top_score = average_gyb_score(x)
      top_word = x
  wordle_list.remove(top_word)
  print("The top word: " +  top_word + " is being removed")

def yellow_checker(word):
  return 0

def solve(guess,actual):
    output = ['','','','','']
    for x in range(5):
        if guess[x] == actual[x]:
            output[x] = 'g'
        elif (guess[x] != actual[x]) and (guess[x] in actual):
            output[x] = 'y'
        else:
            output[x] = 'b'
    return output






print("\nThis is a solver for the game wordle! \n")
x=1
##y is Yellow, g is green, b is black
while(x==1):
    print("There are " + str(len(wordle_list)) + " words remaining \n")
    guess = input("Input a 5 letter word : ")
    if(len(guess) == 6):
      wordle_list.remove(guess[0:4])
    else:
      solve_state = input("\nInput a 5 letter solve state : ")
      for i in range(5):
          if solve_state == 'ggggg':
              x=0
          if (solve_state[i] == "g"):
              for j in list(wordle_list):
                  if(j[i] != guess[i]):
                      wordle_list.remove(j)
          elif (solve_state[i] == "y"):
              for j in list(wordle_list):
                  if(j[i] == guess[i]):
                      wordle_list.remove(j)
                  if(guess[i] not in j):
                      wordle_list.remove(j)
          elif (solve_state[i] == "b"):
              for j in list(wordle_list):
                  dup = guess[i]
                  temp = 0
                  for t in range(5):
                      if (dup == guess[t]) and (solve_state[t] != "b"):
                          temp = 1
                  if temp == 1:
                      if(j[i] == guess[i]):
                          wordle_list.remove(j)
                  elif temp == 0:
                      if(guess[i] in j):
                          wordle_list.remove(j)
print("The word is : " + guess)