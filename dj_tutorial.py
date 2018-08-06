import distutils.core
import datajoint as dj
import numpy as np
best = ['Joel', 'Ben', 'Phineas','Kai','Lincoln', 'Shuri']
deserves_better = ['Caroline', 'Bonnie', 'Mariana' , "Wally", 'Petra']
baller = ['Octavia', 'Sun', 'Wolfgang', 'Magnus', 'Ferb', 'Katherine', 'Spirit']
woorst = ['Elena', 'Diane', 'Pike', 'Trish']
sherlock = ['Sherlock', 'Watson', 'Mary', 'Mycroft', 'Mrs. Hudson', 'Lestrade', 'Sally', 'Anderson', 'Moriarty', 'Euros', 'Molly','The Woman'] 
supernatural = ['Sam', 'Dean', 'Bobby' , 'Castiel', 'Crowley', 'Charlie', 'Jody', 'Kevin']
tvd = ['Elena', 'Jeremy', 'Matt', 'Tyler', "Caroline", 'Stefan', 'Damon', 'Kai', 'Katherine', 'Enzo', 'Bonnie', 'Alaric']
shadowhunters = ['Alec', 'Izzy', 'Clary', 'Jace', 'Valentine', 'Simon', 'Maia', 'Luke', 'Magnus', 'Maryce', 'Rafael']
originals = ['Klaus', 'Elijah', 'Kol', 'Davina', 'Mikael', 'Esther', 'Rebecca', 'Haley', 'Finn', 'Freya', 'Marcel', 'Hope','Vincent', 'Cami']


schema = dj.schema('TaliahMu_pipeline')

@schema
class Characters(dj.Manual):
    definition = """
    # Experimental animals
    name             : varchar(20)                    # First names of character
    ---
    sex="unknown"        : enum('M','F','unknown')      # sex
    age=0                :int                           # age at start of series (or during most of series)
    """


@schema
class About(dj.Manual):
   definition = """
   #16 Personalities
   ->Characters
   ---
   attitude : enum('I','E')       #introverted v extroverted
   perception : enum('S','N')     #sensing v intuition
   processing : enum('T','F')     #thinking v feeling
   implementation : enum('J','P') #judging v percieveing
   """
   
@schema
class Rank(dj.Imported):
    definition = """
    -> Characters
    ---
    ranking:int
    """
    def make(self,key):
        print('key is',key)
    
    
    
