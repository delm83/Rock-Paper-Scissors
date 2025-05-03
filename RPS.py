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
    
    best_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if len(opponent_history) < 3:
        guess = 'P'
    
    if first_two == 'PP':
        guess = abbey_strategy()

    return best_response[guess]
