####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'team6' # Only 10 chars displayed
strategy_name = 'whatStrategy'
strategy_description = 'IDEK what we did, man...'
    
def move(my_history, their_history, my_score, their_score):
    '''So we gonna have a big overall conditional?? maybe. if (our points? (poss??)
    are above a certain range, like >-2000, be less agressive, by using more 'c'. 
    If <= -2000, then go more aggressive, like more 'b' used instead of 'c'. There
    would be conditionals inside this broad one as well tho... idk. So to have a 
    'less' agressive strats would be like... 
    '''
    if my_score>-2000:
        if my_history[-1]== 'c' and their history[-1]=='c':
            
    elif my_score<=-2000:
        
    else: 
        