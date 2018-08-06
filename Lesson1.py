
best = ['Joel', 'Ben', 'Phineas','Kai','Lincoln', 'Shuri']
deserves_better = ['Caroline', 'Bonnie', 'Mariana' , "Wally", 'Petra']
baller = ['Octavia', 'Sun', 'Wolfgang', 'Magnus', 'Ferb', 'Katherine', 'Spirit']
woorst = ['Elena', 'Diane', 'Pike', 'Trish']
sherlock = ['Sherlock', 'Watson', 'Mary', 'Mycroft', 'Mrs. Hudson', 'Lestrade', 'Sally', 'Anderson', 'Moriarty', 'Euros', 'Molly','The Woman'] 
supernatural = ['Sam', 'Dean', 'Bobby' , 'Castiel', 'Crowley', 'Charlie', 'Jody', 'Kevin']
tvd = ['Elena', 'Jeremy', 'Matt', 'Tyler', "Caroline", 'Stefan', 'Damon', 'Kai', 'Katherine', 'Enzo', 'Bonnie', 'Alaric']
shadowhunters = ['Alec', 'Izzy', 'Clary', 'Jace', 'Valentine', 'Simon', 'Maia', 'Luke', 'Magnus', 'Maryce', 'Rafael']
originals = ['Klaus', 'Elijah', 'Kol', 'Davina', 'Mikael', 'Esther', 'Rebecca', 'Haley', 'Finn', 'Freya', 'Marcel', 'Hope','Vincent', 'Cami']

#a list of lists
shows = [sherlock[:],supernatural[:],tvd[:],shadowhunters[:],originals[:]]

#a list of lists to edit original lists
#the strings in this list allow user input to find the index of desired list
all_shows = [best, 'best', deserves_better, 'deserves_better', baller, 'baller', woorst, 'woorst',
             sherlock, 'sherlock', supernatural, 'supernatural', tvd, 'tvd', shadowhunters,
             'shadowhunters', originals, 'originals']
#need to add real lists and see how to add strings

#first prompt asks the user if they want make a new list
#if yes input list name
#if no move to second promt asking if they want to add to a current list
#if yes input list name
#then input character name that should be appended
#if exit loop??

prompt1 = str(input("Would you like to create a new list? y/n "))
if prompt1 == 'y':
   prompt1 = True
elif prompt1 == 'n':
   prompt1 = False
prompt2 = str(input("Would you like to edit a current list? y/n "))
if prompt2 == 'y':
   prompt2 = True
elif prompt2 == 'n':
   prompt2 = False

def new_list:
   if prompt1 = True:
   elif new_list = False:
def edit_list(add):
   if prompt2 == True:
      edit_list = str(input("Which list? "))
      add = int(input("add what? "))
      edit_list.append(add)

while prompt2 == True:
    prompt2 = edit_list(add)

#THIS ADDS TO THE LIST BUT EVEN IF KEEP ADDING RETURNS FALSE IT CONTINUES
list1 = [2,4,6,8]

def new_item(what):
        new_item = int(input("add what? "))
        list1.append(new_item)
        keep_going = bool(input("Keep adding? True/False "))
        return keep_going

add =bool(input("add? True/False "))
while add == True:
    add = new_item(add)




best_ranked = [[best[:]],
               [1,6,3,5,2,4]]
#print (best_ranked)

characters = best + deserves_better + baller + woorst + sherlock + supernatural + tvd + shadowhunters + originals
#need to find a way to see what characters are in more than one list (on the characters list twice) and which lists they're on

faves = best + deserves_better + baller

#print(characters)

#build something that functions like a table/2dnumpyarray so that the items in one list correspond to items in another
#associate the ranks for each character and then print the characters in order of their ranks

#rank=0
#print[best[rank]]

#a loop that will delete the trashy characters from the character list
#while any string that exists in the woorst list also exists in the characters list delete that string
#else print the characters list: should return the list of characters without any of the worst list included

#if x exist in woorst and in characters
#    characters.remove(x)
#    else print(characters)

#same loop but if the characters' rank is below a certain number add it to the laame list
#then remove any characters in the laame list from the characters list
#user input needs to be the index range in the characters list and the list the characters should move to
#if it's not possible to input the index, incoorporte a for loop that requires an input so from a certain point for a certain number of times

def buh_bye(felicia):
   while felicia exists in characters[user input index]:
       return home = input ("To what list? ")
   if "home" exist:
       move characters[user input index] to 'home'
   else:
       create list "user input list name"
       move characters[user input index] to 'home'


#once list is in order based on rank
def rank(name):
    rank = characters.index(str(name)) + 1
    print (rank)

#I want to print all of their names like indexing a single one prints a string
#I think I'll have to make a loop that will go through the list and print each
#element individually
    #works well but place is set to zero within the function so will always print whole list, try making place a user input
def whole_list(place):
    place=0
    while place < len(characters):
        print(characters[place])
        place = place +1





#This version you have to input an integer for which list and it will append
#to that list: ex: if  you input 2 it will append to list 2 (l_2)
l_1 = [2,4,6,8]
l_2 = [1,3,5,7]
l_3 = [5,10,15,20]
lofl = [l_1,l_2,'odd_numbers',l_3]

#Asks if you want to edit a list and if so it adds however many items you specify
#It will then print the list, copy and paste this new list into the module to save it
#If not it will ask if you want to see the list and it will print it
#would have to repeat if which_list == 'list3': list3.append(new_item) for every list

prompt2 = str(input("Would you like to edit an existing list? y/n "))
if prompt2 == 'y':
   prompt2 = True
elif prompt2 == 'n':
   prompt2 = False
   
if prompt2 == True:
        which_list = int(input("Which list would you like to edit? ")) - 1
        new_item = int(input("add what? "))
        lofl[which_list].append(new_item)
        
elif prompt2 == False:
        print("Okay!")

