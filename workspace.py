import datajoint as dj
import numpy as np
schema = dj.schema('TaliahMu_NHL')

@schema
class Teams(dj.Manual):
	definition = """
        #Team names and how long they've been active
        Team:int #NHL team name
        ---
        Established:int  #year established
        Ended:int   #year ended or current year active
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
class Chances(dj.Computed):
        definition = """
        #odds of winning
        ->Scores
        ---
        total : int # total games played = wins + losses + ties + ot_losses
        winning : float # wins / total
        """
        def make (self, key):
                wins = (Scores() & key).fetch1('wins')
                losses =(Scores() & key).fetch1('losses')
                ties =(Scores() & key).fetch1('ties')
                ot_losses = (Scores() & key).fetch1('ot_losses')
                total = wins + losses + ties + ot_losses
                
                key['total'] = wins + losses + ties + ot_losses
                key['winning'] = wins / total
                self.insert1(key)
                print('Computed percent chance of winning for franchise {team}'.format(**key))

    #my_array2 = np.genfromtxt('data2.txt',
                      #skip_header=1,
                      #missing_values = nan,
                      #filling_values=0)


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


@schema
class Performance(dj.Manual):
        definition = """
        #create another computed table that looks at the odds the franchise will make playoffs, division, conference, championship, and stanley cup
        ->Teams 
        ---
        layoffs:int #years team made the playoffs
        Division      :int #years team finished first (or tied for first) in the division
        Conference    :int #years team won the playoff conference championship
        Championship  :int #years team won the league championship
        Cup           :int #years team won the stanley cup
        """
