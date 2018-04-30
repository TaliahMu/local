import datajoint as dj
import numpy as np
schema = dj.schema('TaliahMu_NHL')

@schema
class Teams(dj.Manual):
	definition = """
        #Team names and how long they've been active
        Team:varchar(100) #NHL team name
        ---
        Established:int  #year established
        Ended:int   #year ended or current year active
        """

@schema
class Scores(dj.Manual):
    definition = """
    # team wins, losses, ties, overtime loss, points
    random : int #test number just to check the table but this should be inhereted from Teams and the primary key should be team name
    ---
    wins : int
    losses : int
    ties : int
    ot_losses : int
    points : int
    """
    
