from __future__ import print_function

''' 
PrisonerDilemma.py allows hard-coding different strategies
for the Iterative Prisoners Dilemma, the canonical game of game-theory.
Each strategy plays 100 to 200 rounds against each other strategy.
The results of all previous rounds within a 100-200 round stretch are known
to both players. 

play_tournament() executes the tournament and stores output in tournament.txt

Players should each code their strategies in their assigned section of code.

Aggregated results are stored in tournament.txt

Unpublished work (c)2013 Project Lead The Way
CSE Project 1.3.5 Collaborating on a Project
Draft, Do Not Distribute
Version 7/23/15
'''

import random
def play_round(player1, player2, history1, history2, score1, score2):
    '''
    Calls the get_action() function which will get the characters
    'c' or 'b' for collude or betray for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 4-tuple with updated histories and scores
    (history1, history2, score1, score2)
    '''
    
    RELEASE = 0 # (R) when both players collude
    TREAT = 100 # (T) when you betray your partner
    SEVERE_PUNISHMENT = -500 # (S) when your partner betrays you
    PUNISHMENT = -250 # (P) when both players betray each other
    # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma
    
    #Get the two players' actions and remember them.
    action1 = get_action(player1, history1, history2, score1, score2)
    action2 = get_action(player2, history2, history1, score2, score1)
    if type(action1) != str:
        action1=' '
    if type(action2) != str:
        action2=' '
    #Append the actions to the previous histories, to return
    new_history1 = history1 + action1
    new_history2 = history2 + action2
    
    #Change scores based upon player actions
    if action1 not in ('c','b') or action2 not in ('c','b'):
        # Major punishment if player 1 does not return a 'c' or 'b'
        if action1 not in ('c', 'b'):
            new_score1 = score1 - 1000
            # Same goes for player 2
            if action2 not in ('c', 'b'):
                new_score2 = score2 - 1000
            else:
                new_score2 = score2
        else:
            new_score2 = new_score2 - 1000
            new_score1 = score1
        
    else: 
    #Both players' code provided proper actions
        if action1 == 'c':
            if action2 == 'c':
                # both players collude; get reward
                new_score1 = score1 + RELEASE
                new_score2 = score2 + RELEASE
            else:
                # players 1,2 collude, betray; get sucker, tempation
                new_score1 = score1 + SEVERE_PUNISHMENT
                new_score2 = score2 + TREAT
        else:
            if action2 == 'c':
                # players 1,2 betray, collude; get tempation, sucker
                new_score1 = score1 + TREAT
                new_score2 = score2 + SEVERE_PUNISHMENT                       
            else:
                # both players betray; get punishment   
                new_score1 = score1 + PUNISHMENT
                new_score2 = score2 + PUNISHMENT
                    
    #send back the updated histories and scores
    return (new_history1, new_history2, new_score1, new_score2)
   
def play_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds) 
    of the iterative prisoners' dilemma between two strategies.
    identified in the parameters as integers.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600) 
    but with much longer strings 
    '''
    number_of_rounds = random.randint(100,200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        moves1, moves2, score1, score2 = \
            play_round(player1, player2, moves1, moves2, score1, score2)
    return (moves1, moves2, score1, score2)

def get_action(player, history, opponent_history, score, opponent_score, getting_team_name=False):
    '''Gets the strategy for the player, given their own history and that of
    their opponent, as well as the current scores within this pairing.
    The parameters history and opponenet history are strings with one letter
    per round that has been played so far: either an 'c' for collude or a 'b' for 
    betray. The function should return one character, 'c' or 'b'. 
    The history strings have the first round between these two players 
    as the first character and the most recent round as the last character.'''
      
    ######
    ######
    #
<<<<<<< HEAD
    # This example player always colludes
    if player == 0:
        if getting_team_name:
            return 'loyal'
        else:
            return 'c'

    
=======
    # This nonexample player nearly always colludes... right?
    if player == 0:
        global KNTHScoreLIST
        if not 'KNTHMoveLIST' in globals():
            global KNTHMoveLIST
            KNTHMoveLIST = ''
            KNTHScoreLIST = [0]
            KNTHBScores = [0]
            KNTHCScores = [0]
        if getting_team_name:
            return 'KNTH!!'
               
        else:
            if len(history) == 0: #if it's the first round, collude since I'm hoepful
                KNTHMoveLIST += 'c'
                return 'c'
            else:
              KNTHScoreLIST += [score-sum(KNTHScoreLIST)]
              KNTHBScores = [KNTHScoreLIST[i] if KNTHMoveLIST[i] == 'b' else 0 for i in range(len(history))]
              KNTHCScores = [KNTHScoreLIST[i] for i in range(len(history)) if KNTHMoveLIST[i] == 'c']
              KNTHBAverage = sum(KNTHBScores)/len(KNTHBScores)
              KNTHCAverage = sum(KNTHCScores)/len(KNTHCScores)
              if len(history) ==  1:# if it's the second round, betray... I've got a bad feeling about this...
                KNTHMoveLIST += 'b'
                return 'b'
              elif KNTHCAverage > KNTHBAverage:
                KNTHMoveLIST += 'c'
                return 'c'
              elif opponent_score < -300: #otherwise if the opponent is doing pretty badly collude, we should work together
                  KNTHMoveLIST += 'c'
                  return 'c'
              elif opponent_score < score:#same reasoning
                  #print('My opponent is losin\'!!')
                  KNTHMoveLIST += 'c'
                  return 'c'
              else: #if nothing else is true, then betray, at least the other person will feel worse
                  #print('My opponent is winning!!')
                  KNTHMoveLIST += 'b'
                  return 'b'


>>>>>>> origin/master
        
            
                
                    
                            
    ######
    ######
    #
    #This example player always betrays.      
    elif player == 1:
        if getting_team_name:
<<<<<<< HEAD
            return 'backstabber'
        else:
            return 'b'
=======
            return 'Marco and Max'
        else:
	   if len(history) > 2:
		if opponent_history[-1] == 'c' and opponent_history[-2] == 'c' and opponent_history[-3] == 'c':
		  return 'c'
		else:
		  return 'b'
	   else:
	       return 'b'
>>>>>>> origin/master








    ######
    ######
<<<<<<< HEAD
    #   
=======
>>>>>>> origin/master
    #This example player is silent at first and then 
    #only betrays if they were a sucker last round.
    elif player == 2:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
=======
            return 'Ping and Caden'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
<<<<<<< HEAD
                return 'c' #otherwise collude


    
    
    
    
    # EACH STUDENT TEAM CAN CHANGE ONE OF THESE elif SEGMENTS OF CODE.






=======
             	return 'c' #otherwise collude
>>>>>>> origin/master




    ######
    ######
    #
    elif player == 3:
        if getting_team_name:
<<<<<<< HEAD
            return 'backstabber'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
=======
            return 'Ping and Caden'
        else:
            if len(opponent_history)<5: # Collude for first 5 rounds
                return 'c'
            else:
                return opponent_history[-1] # Do whatever opponet did last round
>>>>>>> origin/master











    ######
    ######
    #
    elif player == 4:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful with permanent second impression'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            size = len(history)
            if(size%3==0): #the number of rounds played is a multiple of 3
                return 'c'
            else:
                return 'b'
=======
            return 'Marco and Max'
        else:
	   if len(history) > 2:
		if opponent_history[-1] == 'c' and opponent_history[-2] == 'c' and opponent_history[-3] == 'c':
		  return 'c'
		else:
		  return 'b'
	   else:
	       return 'b'
>>>>>>> origin/master
    
    
    








    ######
    ######        
    #
<<<<<<< HEAD
    elif player == 5:
        if getting_team_name:
            return 'backstabber'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
    
    
    
=======

    elif player == 5:
        if getting_team_name:
            return 'Liam?'
        else:
            if len(opponent_history)==0:
                return 'c'
            else:
                recent_round_opponent = opponent_history[-1]
                recent_round_me = history[-1]
                for round in range(len(history)-1):
                    prior_round_opponent = opponent_history[round]
                    prior_round_me = history[round]
                    #if one matches
                    if (prior_round_me == recent_round_me) and \
                            (prior_round_opponent == recent_round_opponent):
                        return opponent_history[round]
                if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # betray is they were severely punished last time
                else:
                    return 'c' #otherwise collude 
  
>>>>>>> origin/master
    





    ######
    ######        
    #
    elif player == 6:
        if getting_team_name:
<<<<<<< HEAD
            return 'backstabber'
=======
            return 'Dat1AZNBanana'
>>>>>>> origin/master
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
<<<<<<< HEAD
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
=======
                return 'b'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'b' #otherwise collude
>>>>>>> origin/master
    










    ######
    ######       
    #
    elif player == 7:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
=======
            return 'AhnafC'
>>>>>>> origin/master
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were sucker last time
            else:
                return 'c' #otherwise collude











    ######
    ######        
    #
    elif player == 8:
        if getting_team_name:
            #if there was a previous round just like 
<<<<<<< HEAD
            return 'loyal vengeful with permanent second impression'
=======
            return 'Mitchell'
>>>>>>> origin/master
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy      
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            else:
                # if there was a previous round just like the last one,
                # do whatever they did in the round that followed it
                recent_round_opponent = opponent_history[-1]
                recent_round_me = history[-1]
                            
                #go through rounds before that one
                for round in range(len(history)-1):
                    prior_round_opponent = opponent_history[round]
                    prior_round_me = history[round]
                    #if one matches
                    if (prior_round_me == recent_round_me) and \
                            (prior_round_opponent == recent_round_opponent):
                        return opponent_history[round]
                # no match found
                if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # betray is they were severely punished last time
                else:
                    return 'c' #otherwise collude












    ######
    ######
    #
    elif player == 9:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
=======
            return 'Juichi and Willow'
        else:
            if len(opponent_history)==0:
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b'
            else:
                return 'c'

>>>>>>> origin/master










    ######
    ######
    #
    elif player == 10:
        if getting_team_name:
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude









    ######
    ######
    #
    elif player == 11:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
=======
            return 'CJ'
        else:
            return 'b'
>>>>>>> origin/master










    ######
    ######
    #
    elif player == 12:
        if getting_team_name:
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
    
    


    ######
    ######
    #
    elif player == 13:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
=======
            return 'Bryson'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
    
    







    ######
    ######
    #
    elif player == 14:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful occasionally greedy'
=======
            return 'DK! Dillon Kong!'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                if random.random()<0.1: #10% of the other rounds
                    return 'b'         #betray
                else:
                    return 'c'         #otherwise collude
    
    
    
    



    ######
    ######
    #
    elif player == 15:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
=======
            return 'Juichi'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
    
    







    ######
    ######
    #
    elif player == 16:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
=======
            return 'nick hills bad bot'
        else:
            if len(opponent_history)==0: #opener
                if random.random() <= 0.5:
                    return 'c'
                else:
                    return 'b'
            
            else:
                prev_betrays = 0;
                for i in range(1,len(opponent_history)): #count previous betrayals
                    if opponent_history[i] == 'b':
                        prev_betrays = prev_betrays + 1
                
                betray_chance = prev_betrays / len(opponent_history) #calculate chance of the next choice being a betrayal
                
                if opponent_history[-1] == 'b': #if last opponent choice was betray, add 75% to betray chance
                    betray_chance = betray_chance + 0.75
                
                if random.random() <= betray_chance: #if float lands in betray chance range, betray
                    return 'b'
                else: #collude by default
                    return 'c'
>>>>>>> origin/master
    
    







    ######
    ######
    #
    elif player == 17:
        if getting_team_name:
<<<<<<< HEAD
            return 'loyal vengeful'
=======
            return 'Ryo Takei'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
    
    







    ######
    ######
    #
    elif player == 18:
        if getting_team_name:
            return 'loyal vengeful'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude

elif player == 21:
    if getting_team_name:
        return 'Rafa'
        else:
            return 'b'









    ######
    ######
    #
<<<<<<< HEAD
    elif player == 19:
        if getting_team_name:
            return 'loyal vengeful'
=======
 elif player == 19:
        if getting_team_name:
            return 'Ben'
>>>>>>> origin/master
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
<<<<<<< HEAD
            else:
                return 'c' #otherwise collude
=======
            elif history[-1]=='b' and opponent_history[-1]=='b':
                return 'c' # collude if they were punished last time
            elif history[-1]=='b' and opponent_history[-1]=='c':
                return 'c' # collude if they were set free
            else:
                return 'c' #otherwise collude

>>>>>>> origin/master
            
    elif player == 20:
        if getting_team_name:
            return 'loyal vengeful'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude

<<<<<<< HEAD
=======

>>>>>>> origin/master
    
    







def play_tournament(num_players):
    #create a list of zeros, one per player
    scores = []
    for i in range(num_players):
        scores += [0]
    
    
    ''' Get the team name from each team algorithm'''
    #create a list of the right length
    team_names = range(num_players)
    for player in range(num_players):
        team_names[player] = get_action(player,'','',0,0,getting_team_name=True)
             
    # each element will become a column for each player
    # range is just to get list of correct size
    result_table=range(num_players)     
    moves_table=range(num_players) 
    
    
    for player1 in range(num_players):  
        # create the column for each player
        # range just to get list of correct size
        result_table[player1]=range(num_players) 
        result_table[player1][player1]=0 # initialize unused diagonal to 0
        moves_table[player1]=range(num_players)
        # play a game between with every other player of lower number
        for player2 in range(player1):
            moves1, moves2, score1, score2 = \
                play_iterative_rounds(player1, player2)
            
            rounds = len(moves1)
            score1_per_round = score1/rounds 
            score2_per_round = score2/rounds
            
            result_table[player1][player2]=score1_per_round
            result_table[player2][player1]=score2_per_round
            
            moves_table[player1][player2] = moves1
            moves_table[player2][player1] = moves2
            
            #accumulate the results for the two players
            scores[player1] += score1*1.0/len(moves1)#ends up same as column sum
            scores[player2] += score2*1.0/len(moves2)#ends up same as column sum
     
    '''report round-level results in a data file'''
    use_datafile=True
    if use_datafile:
        # use the same directory as the python script
        import os.path              
        directory = os.path.dirname(os.path.abspath(__file__))  
        
        #name the file tournament.txt
        filename = os.path.join(directory, 'tournament.txt')
        #create the file for the round-by-round results
        results = open(filename,'w')
        for player1 in range(num_players):
            for player2 in range(player1):
                # store the results in the file
                #title by team numbers
                results.write('team ' + str(player1) + 
                              ' vs. ' + 'team ' + str(player2) +'\n')
                #title by player-on-player average score
                results.write(str(result_table[player1][player2]) + 
                              ' vs. ' + str(result_table[player2][player1])+'\n')
                #title by team names
                results.write(team_names[player1] + 
                             ' vs. ' + team_names[player2] + '\n')
                #show the moves, aligned vertically
                results.write(moves_table[player1][player2] +'\n')
                results.write(moves_table[player2][player1] +'\n')
                #blank line between each pair's results
                results.write('\n')
            
        #at the bottom repeat the output that was sent to the screen
        #print a title for the table
        results.write('\n\n\n\tEach column shows score earned per round against each other player.\n\n\n')
        #print header line
        results.write('\t') #skip 1st column
        for player1 in range(num_players):
            results.write('P'+str(player1)+'\t') # label each additional column
        results.write('\n')
        
        #print each player's scores
        for player2 in range(num_players):
            results.write('P'+str(player2)+'\t') #label the player's row
            for player1 in range(num_players):
                #print score against each other player
                results.write(str(result_table[player1][player2])+'\t') 
            results.write('\n')
        results.write('Total:\t')
        for player1 in range(num_players):
            results.write(str(int(scores[player1]))+'\t')
        results.write('\n\n\n Average per round, with team strategy names:\n\n')       
    
        #print team ids, total scores, and names
        for player in range(num_players):
            results.write('player ' + str(player) + ': ' + \
                    str(int(scores[player])/num_players) + ' points: '+\
                    team_names[player]+'\n')
                    
                    
        #append the file showing algorithms
        results.write('\n\n' + '-'*79 + '\n' + \
                    'Here is the code that produced this data:\n\n')
        this_code_file = open(__file__, 'r')
        for line in this_code_file:
            results.write(line)
                
    '''report the results on screen'''        
    #print a title for the table
    print('\n\n\tEach column shows score earned per round against each other player.\n\n')
    
    #print header line
    print('\t', end='') #skip 1st column
    for player1 in range(num_players):
        print('P',player1, end='\t') # label each additional column
    print()
    
    #print each player's scores
    for player2 in range(num_players):
        print('P',player2, end='\t') #label the player's row
        for player1 in range(num_players):
            #print score against each other player
            print(result_table[player1][player2], end='\t') 
        print()
    #print row of total scores
    print('Total:\t',end='')
    for player1 in range(num_players):
        print(str(int(scores[player1])),end='\t')

    print('\n\n\n Average per round, with team strategy names:\n\n')
    #print team ids, total scores, and names
    for player in range(num_players):
        print('player ' + str(player) , ': ' , 
               str(int(scores[player])/num_players) , ' points: ',
               team_names[player])
    
