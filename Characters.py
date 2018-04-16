import distutils.core
best = ['Joel', 'Ben', 'Phineas','Kai','Lincoln', 'Shuri']
deserves_better = ['Caroline', 'Bonnie', 'Mariana' , "Wally", 'Petra']
baller = ['Octavia', 'Sun', 'Wolfgang', 'Magnus', 'Ferb', 'Katherine', 'Spirit']
woorst = ['Elena', 'Diane', 'Pike', 'Trish']
sherlock = ['Sherlock', 'Watson', 'Mary', 'Mycroft', 'Mrs. Hudson', 'Lestrade', 'Sally', 'Anderson', 'Moriarty', 'Euros', 'Molly','The Woman'] 
supernatural = ['Sam', 'Dean', 'Bobby' , 'Castiel', 'Crowley', 'Charlie', 'Jody', 'Kevin']
tvd = ['Elena', 'Jeremy', 'Matt', 'Tyler', "Caroline", 'Stefan', 'Damon', 'Kai', 'Katherine', 'Enzo', 'Bonnie', 'Alaric']
shadowhunters = ['Alec', 'Izzy', 'Clary', 'Jace', 'Valentine', 'Simon', 'Maia', 'Luke', 'Magnus', 'Maryce', 'Rafael']
originals = ['Klaus', 'Elijah', 'Kol', 'Davina', 'Mikael', 'Esther', 'Rebecca', 'Haley', 'Finn', 'Freya', 'Marcel', 'Hope','Vincent', 'Cami']
#a list of names that can be edited without changing the original lists
characters = best + deserves_better + baller + woorst + sherlock + supernatural + tvd + shadowhunters + originals
#Needs to be after characters list is defined
#Put in the index you want to start (int) with and it will list the characters
def ordered_list(start):
   for place in range(start,len(characters)):
      print(str(place+1) + '. ' + str(characters[place]))
      place = place +1
#To call on rank of a character, put name in quotes)          
def rank(name):
   rank = characters.index(name) + 1
   print (rank)
#a list of lists
shows = [sherlock[:],supernatural[:],tvd[:],shadowhunters[:],originals[:]]
#a list of lists to edit original lists
#the strings in this list allow user input to find the index of desired list
all_shows = [best, 'best', deserves_better, 'deserves_better', baller, 'baller', woorst, 'woorst',
             sherlock, 'sherlock', supernatural, 'supernatural', tvd, 'tvd', shadowhunters,
             'shadowhunters', originals, 'originals']

#need to add real lists and see how to add strings
#******************************************************************************
#Asks if you want to edit a list and if so it adds however many items you specify
#It will then print the list, copy and paste this new list into the module to save it
#If not it will ask if you want to see the list and it will print it

prompt = str(input("Would you like to edit an existing list? y/n "))
yes_no = bool(distutils.util.strtobool(prompt))
#yes_no needs to be redefined after each prompt
if yes_no == True:
    which_list = input("Which list would you like to edit? ")
    location = all_shows.index(which_list) - 1
    prompt = input("Would you like to see it first? y/n ")
    yes_no = bool(distutils.util.strtobool(prompt))
    if yes_no == True:
      print(all_shows[location])
    how_many = int(input("How many items would you like to add? "))
    for add in range(how_many):   
        new_item = input("add what? ")
        all_shows[location].append(new_item)
    print("Okay, here's your list!" + str(all_shows[location]))       
elif yes_no == False:
    prompt = str(input("Would you like to see the current ranking? y/n "))
    yes_no = bool(distutils.util.strtobool(prompt))
    if yes_no == True:
            print("Okay, here's your list!" + str(characters))
    elif yes_no == False:
            print("Okay!")
