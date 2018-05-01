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

about = np.genfromtxt('data.txt',
                      skip_header=1)
my_array2 = np.genfromtxt('data2.txt',
    skip_header=1,
    missing_values = 'nan',
    filling_values=0)
score = my_array2[:,4:9]
score = score.astype(int)
score[score<-5] = 0 
age = my_array2[:,1]-my_array2[:,0]
team = np.arange(1,58)[...,None]


#figure out how to add columns and import these numpy arrays into dj tables
numbers = np.arange(1,58)[...,None]
file = open('data3.txt')
names = file.readlines()
del(names[0])
team_names = np.array(names)[...,None]
age =(Teams().fetch('ended')-Teams().fetch('established'))[...,None]
combined = np.append(numbers, team_names, 1)
combined = np.append(combined, age, 1)
combined.astype(list)


#without creating a table just querrying figure out the correlation coeffiecent
#for the chances of winning versus the age of the franchise
#jk maybe create a table for odds of winning compared to age,




    #my_array2 = np.genfromtxt('data2.txt',
                      #skip_header=1,
                      #missing_values = nan,
                      #filling_values=0)


