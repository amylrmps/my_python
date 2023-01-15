# # word = "Animal"
# # guess = ""
# # guessCount = 0
# # guessLimit = 5
# # outOfGuesses = False

# # while guess != word and not (outOfGuesses): 
# #     if guessCount < guessLimit:
# #         guess = input("Enter word(6 characters): ")
# #         guessCount += 1
# #     else:
# #         outOfGuesses = True

# # if outOfGuesses:
# #     print("You lose!!!!")
# # else: 
#     # print("You Win!!!!")



# # secretMoneyAmount = "50000"
# # guess = ""
# # guessCount = 0
# # guessLimit = 3
# # outOfGuesses = False

# # guess = input("Enter number(5 digit): ")
# # guessCount = 1
 

# # while guess != secretMoneyAmount and not(outOfGuesses): 
# #     if guessCount < guessLimit:
# #         guess = input("Enter number(5 digit): ")
# #         guessCount += 1
# #     else:
# #         outOfGuesses = True

# # if outOfGuesses:
# #     print("WRONG, WRONG, WRONG, ALL SO WRONG. URG")
# # else:
# #     print("RIGHT, RIGHT, RIGHT, ALL SO RIGHT. WOOO")


 


# # from os import times


# # secret = "abc"
# # attemptLimit = 3
# # attempTimes = 0
# # userInput = ""

# # while secret != userInput and attempTimes < attemptLimit:
# #     userInput = input("enter your pwd: ")
# #     attempTimes +=1


# # if attempTimes >= attemptLimit and secret != userInput:
# #     print("password wrong")
# # else:
# #     print("you passed")



# letter =  "r"
# limit = 5
# attemptTimes = 0
# input1 = ""

# while letter != input1 and attemptTimes < limit:
#     input1 = input("Enter you letter(lowercase): ")
#     attemptTimes += 1
    
# if attemptTimes >= limit and letter != input1:
#     print("INVALID PASS, TRY AGAIN TMRW!")
# else:
#     print("Pass is correct!")

# num_grid = [
#     [12, 21, 3],
#     [64, 15, 61],
#     [17, 18, 59],
#     [0]
# ]

# row_num = 0
# for row in num_grid:
#     row_num +=1
#     for col in row:
#         print(str(row_num) + "-" + str(col))