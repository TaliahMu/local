import datajoint as dj
schema = dj.schema
@schema
class Shows (dj.Lookup):
    definition = """
    #show and category
    show : varchar(100) #show name
    ---
    category : enum('comedy','supernatural','drama') #category
    """
@schema
class Characters (dj.Manual):
    definition = """
    ->Shows
    name : varchar(100) #character first name
    ---
    hair : enum('black','brown','blonde','red','crazy','multi')
    relationship : enum('single','married','dating','complicated')
    partner='unknown' : varchar(100)
    """
@schema
class Rank (dj.Lookup):
    definition = """
    ->Characters
    ---
    rank : int
    """
