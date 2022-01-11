import random
best_of = input('Input best of \n')
dobby_the_score_keeper = [0,0]
def rps_bot():
    user_input = input('Enter Rock Paper or Scissor \n')
    game = ['Rock','Paper','Scissor']
    bot_plays = game[random.randrange(0, 3)]
    print("Bot Plays : " + bot_plays)
    if user_input == bot_plays:
        print("No points!")
    else:
        if user_input == 'Rock' and bot_plays == 'Paper':
            print("rps bot wins!")
            dobby_the_score_keeper[0]+=1
        elif user_input == 'Paper' and bot_plays == 'Rock':
            print("user wins!")
            dobby_the_score_keeper[1]+=1
        elif user_input == 'Paper' and bot_plays == 'Scissor':
            print("rps bot wins!")
            dobby_the_score_keeper[0]+=1
        elif user_input == 'Scissor' and bot_plays == 'Paper':
            print("user wins!")
            dobby_the_score_keeper[1]+=1
        elif user_input == 'Scissor' and bot_plays == 'Rock':
            print("rps bot wins!")
            dobby_the_score_keeper[0]+=1
        elif user_input == 'Rock' and bot_plays == 'Scissor':
            print("user wins!")
            dobby_the_score_keeper[1]+=1
for _ in range(int(best_of)):
    rps_bot()
if  dobby_the_score_keeper[0] == dobby_the_score_keeper[1]: print("DRAW!") 
else: print("RPS BOT WINS!!!! Score : " + str(dobby_the_score_keeper[0])) if dobby_the_score_keeper[0] > dobby_the_score_keeper[1] else print("USER WINS !!! Score : " + str(dobby_the_score_keeper[1]))                  
