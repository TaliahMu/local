import datajoint as dj
import numpy as np
schema = dj.schema('TaliahMu_NHL')

@schema
class Teams(dj.Manual):
	definition = """
        #Team names and how long they've been active
        Team:int #NHL team name
        ---
        established:int  #year established
        ended:int   #year ended or current year active
        """

#Data in 'data.txt' file
#
@schema
class Info(dj.Lookup):
        definition = """
        #Team name and age
        ->Teams #team number
        ---
        name : varchar(100) #team name as a string need to remove the slash n
        age : int #how long the team has been playing
        """
@schema
class Scores(dj.Manual):
    definition = """
    # team wins, losses, ties, overtime loss, points
    ->Teams #test number just to check the table but this should be inhereted from Teams and the primary key should be team name
    ---
    total : int #number of games played-should be wins + losses + ties + ot_losses
    wins : int
    losses : int
    ties : int
    ot_losses : int
    points : int
    """
@schema
class Performance(dj.Manual):
    definition = """
    # team wins, losses, ties, overtime loss, points
    ->Teams #test number just to check the table but this should be inhereted from Teams and the primary key should be team name
    ---
    playoffs : int #years the team made the playoffs
    division : int #years the team finished first (or tied for first) in the division
    conference : int #years the team won the playoff conference championship
    championship : int #years the team won the league championship
    cup : int #years the team won the stanley cup
    """
    
@schema
class Chances(dj.Computed):
        definition = """
        #odds of winning
        ->Scores
        ->Performance
        ---
        total : int # total games played = wins + losses + ties + ot_losses
        winning : float # percent chance of winning
        yrs_plyf : float #percent of years been established that made it to the playoffs
        div : float
        conf : float
        champ : float
        st_cup : float
        """
        def make (self, key):
                wins = (Scores() & key).fetch1('wins')
                losses =(Scores() & key).fetch1('losses')
                ties =(Scores() & key).fetch1('ties')
                ot_losses = (Scores() & key).fetch1('ot_losses')
                total = wins + losses + ties + ot_losses
                age =(Teams()&key).fetch1('ended')-(Teams() & key).fetch1('established')
                
                key['total'] = wins + losses + ties + ot_losses
                key['winning'] = (wins / total) * 100
                key['yrs_plyf'] = ((Performance() & key).fetch1('playoffs') / age) * 100
                key['div'] = ((Performance() & key).fetch1('division') / age) * 100
                key['conf'] = ((Performance() & key).fetch1('conference') / age) * 100
                key['champ'] = ((Performance() & key).fetch1('championship') / age) * 100
                key['st_cup'] = ((Performance() & key).fetch1('cup') / age) * 100
                self.insert1(key)
                print('Computed percent chance of winning for franchise {team}'.format(**key))

#added replica of Teams() called Test() by:
#        about = np.genfromtxt('data.txt',skip_header=1)
#        about=about.astype(int)
#        Test.insert(about)
@schema
class Test(dj.Manual):
	definition = """
        #Team names and how long they've been active
        team:int #NHL team name
        ---
        established:int  #year established
        ended:int   #year ended or current year active
        """

numbers = np.arange(1,58)[...,None]
file = open('data3.txt')
names = file.readlines()
del(names[0])
with open("data3.txt") as file:
    names = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        names.append(line.rstrip().split(","))
flat_list = [item for sublist in names for item in sublist]
team_names = np.array(flat_list)[...,None]
age =(Test().fetch('ended')-Test().fetch('established'))[...,None]
combined = np.append(numbers, team_names, 1)
combined = np.append(combined, age, 1)








#        about = np.genfromtxt('data.txt',
#                              skip_header=1)
#        my_array2 = np.genfromtxt('data2.txt',
#            skip_header=1,
#            missing_values = 'nan',
#            filling_values=0)
#        score = my_array2[:,4:9]
#        score = score.astype(int)
#        score[score<-5] = 0 
#        age = my_array2[:,1]-my_array2[:,0]
#        team = np.arange(1,58)[...,None]


#figure out how to add columns and import these numpy arrays into dj tables
#the [...,None] changes list to list of lists
#        numbers = np.arange(1,58)[...,None]
#        file = open('data3.txt')
#        names = file.readlines()
#        del(names[0])
#        team_names = np.array(names)[...,None]
#        age =(Teams().fetch('ended')-Teams().fetch('established'))[...,None]
#        combined = np.append(numbers, team_names, 1)
#        combined = np.append(combined, age, 1)
#idk why it'd be asytpe list
#combined.astype(list)


#without creating a table just querrying figure out the correlation coeffiecent
#for the chances of winning versus the age of the franchise
#jk maybe create a table for odds of winning compared to age,






    #my_array2 = np.genfromtxt('data2.txt',
                      #skip_header=1,
                      #missing_values = nan,
                      #filling_values=0)


