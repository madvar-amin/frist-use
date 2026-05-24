#imports and global vareiables
import random
USER_Choice = ['rock', 'paper', 'seasor']
#get user input
def get_user_input():
    user_in = input('pick![\'rock\', \'paper\', \'seasor\']')
    while user_in not in USER_Choice:
        user_in = input('pick![\'rock\', \'paper\', \'seasor\']')
    return user_in
#get pc input
def get_pc_input():
    return random.choice(USER_Choice)


#compare and determine which one is the winner
def who_is_winner(get_user_input, get_pc_input):
    if get_pc_input == get_user_input:
        print('DRAW')
    elif get_user_input == 'rock' and get_pc_input =='paper':
        print( 'pc won!')
    elif get_user_input =='rock' and get_pc_input =='seasor':
        print( 'you won')
    elif get_user_input =='paper' and get_pc_input =='rock':
        print( 'you won')
    elif get_user_input == 'paper' and get_pc_input=='seasor':
        print( 'pc won')
    elif get_user_input =='seasor' and get_pc_input== 'rock':
        print( 'pc won')
    else:
        print( 'you won')

#create main function as runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    who_is_winner(user_input,pc_input )
    print('end of program')

#make the loop for game
answer = 'y'
while answer =='y':
    main()
    answer = input('do you want to continue? (y/n):')