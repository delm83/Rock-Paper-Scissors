# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], guess = ''):

    opponent_history.append(prev_play)
    first_two = "".join(opponent_history[1:3])
    first_three = "".join(opponent_history[1:4])
    last_two = "".join(opponent_history[-2:])

    def abbey_strategy(next_in_sequence={
              'RR': 'S',
              'RP': 'S',
              'RS': 'S',
              'PR': 'P',
              'PP': 'R',
              'PS': 'R',
              'SR': 'R',
              'SP': 'P',
              'SS': 'P',
          }):

            return next_in_sequence[last_two]
    
    def kris_strategy(next_in_sequence={
              'R': 'S',
              'P': 'R',
              'S': 'P',
          }):
            
            return 'R' if len(opponent_history) == 3 else next_in_sequence[prev_play]
    
    def quincy_strategy(next_in_sequence={
              'RR': 'P',
              'RP': 'P',
              'PP': 'S',
              'PS': 'R',
              'SR': 'R',
          }):

            return next_in_sequence[last_two]
    
    best_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if first_two == 'PP':
        guess = abbey_strategy()
    elif first_two == 'PR':
        guess = kris_strategy()
    elif first_three == 'RPP':
        guess = quincy_strategy()
    else:
        guess = 'P'
        
    # empty opponent history between each player
    if len(opponent_history) == 1000:
        opponent_history.clear()

    return best_response[guess]
