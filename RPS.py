def player(prev_play, opponent_history=[], best_response = {'P': 'S', 'R': 'P', 'S': 'R'}):

    opponent_history.append(prev_play)
    first_two = "".join(opponent_history[1:3])
    first_three = "".join(opponent_history[1:4])
    last_two = "".join(opponent_history[-2:])

    def abbey_strategy(next_in_sequence={
          # Abbey follows a predictable pattern if I do too
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
          # kris always plays to beat your previous play so your next play should be his previous play.
              'R': 'S',
              'P': 'R',
              'S': 'P',
          }):
            
            return 'R' if len(opponent_history) == 3 else next_in_sequence[prev_play]
    
    def quincy_strategy(next_in_sequence={
          # Quincy always follows the same pattern, unaffected by my choices
              'RR': 'P',
              'RP': 'P',
              'PP': 'S',
              'PS': 'R',
              'SR': 'R',
          }):

            return next_in_sequence[last_two]
    
    def mrugesh_strategy():
               # continually loop through all 3 options to ensure last 10 of my guesses will have 4 of one option and 3 of the other 2 options each round
               # for example [S,R,P,S,R,P,S,R,P,S] (4XS) will be followed by [R,P,S,R,P,S,R,P,S,R] (4XR)
               # this ensures that there is only one option with max frequency each round which will change each round so mrugesh will also change option each round
               if len(opponent_history)%3 == 2:
                    return 'R'
               elif len(opponent_history)%3 == 1:
                    return 'P'
               else:
                    return 'S'
    
    # Deduce opponent based on opponent's first moves
    if len(opponent_history)<3:
         guess = 'P'
    elif first_two == 'PP':
        guess = abbey_strategy()
    elif first_two == 'PR':
        guess = kris_strategy()
    elif first_three == 'RPP':
        guess = quincy_strategy()
    else:
        guess = mrugesh_strategy()
        
    # clear opponent history between each player
    if len(opponent_history) == 1000:
        opponent_history.clear()

    return best_response[guess]
