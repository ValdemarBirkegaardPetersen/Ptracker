import os


# Paths
#tourn_path = "C:/Users/Vla/Desktop/MTT"
#history_path = "C:/Users/Vla/Desktop/Cash Game"
tourn_path = "C:/Users/Deida/AppData/Local/PokerStars.DK/TournSummary/Valdemar1743"
history_path = "C:/Users/Deida/AppData/Local/PokerStars.DK/HandHistory/Valdemar1743"

tourn_files = []
history_files = []

# Generates file names for all files in tournament summary folder
for root, dirs, files in os.walk(tourn_path, topdown=False):
   for name in files:
      tourn_files.append(os.path.join(root, name))
      
# Generates fill names for all files in hand history folder
for root, dirs, files in os.walk(history_path, topdown=False):
    for name in files:
        history_files.append(os.path.join(root, name))

# Getting raw content and then using strip to remove extra space        
with open(tourn_files[14]) as raw_file:
    raw_content = raw_file.readlines()
    content = [x.strip() for x in raw_content]

# Here we start searching the tourn summary files for information, one by one filling the information we need by searching in strings
stringContainer = []
tv = 0

# line is each line in .txt and words is each word in each line
for line in content:
    words = line.split()
    stringContainer.append(line)
    
    # Constrainer. We dont need to check all lines.
    tv += 1
    if tv > 11:
        break
 
# Get tournament id   
tourn_id_0 = ""
tourn_id_0 = stringContainer[0][stringContainer[0].find("#")+1:stringContainer[0].find(",")]


# Get tournament type
tourn_type_0 = ""
tourn_type_0 = stringContainer[0][stringContainer[0].find(",")+2:]

# Get tournament date
tourn_date_0 = ""
store_date = 0
stringCotainer_str = str(stringContainer)
store_date = stringCotainer_str.find("started")
tourn_date_0 = stringCotainer_str[store_date+8:store_date+31]

# Get tournament description
tourn_description_0 = ""
store_desc = stringCotainer_str.find("Satellite")
tourn_description_0 = stringCotainer_str[store_desc:store_desc+9]
if tourn_description_0 != "Satellite":
    tourn_description_0 = "MTT"

# Get tournament buy-in
tourn_buyin_0 = ""
store_buyin = stringCotainer_str.find("Buy-In") # Searcing for start of sentence
letstry = stringCotainer_str[store_buyin:store_buyin+50].find("'") # Finding next ' from after "Buy-In"
tourn_buyin_0 = stringCotainer_str[store_buyin:store_buyin+letstry] # Making new string from the two character positions just found 







# Get net won. Might have to check hand histories for this

# Match tournament id in both folders tournsummary and handhistory
for i in history_files: 
    if tourn_id_0 in i:
        identical_tourn = i

# Open the identical tournament as a raw file and parse the document into variables that is stripped off useless characters
with open(identical_tourn) as raw_file:
    raw_hand_content = raw_file.readlines()
    hand_content = [x.strip() for x in raw_hand_content]

# In the txt handhistory .txt we can find the player/users name by searching for "Dealt To", and in this case: "Dealt To Valdemar1743" This way the alias can be used as a varaible later on
aliasContainer = hand_content[:50]
for i in aliasContainer:
    if "Dealt to" in i:
        tourn_alias = i
        tourn_alias = tourn_alias[9:tourn_alias.find("[")-1]
        break

"""There is several ways the txt logs store how much you won. If you havent won it will say "Valdemar1743 finished the tournament in blabla place"
If you win, it can say "Valdemar1743 wins the tournament and receives $0.50 - congratulations!"
If you win money but is not 1st place you get something like "Valdemar1743 finished the tournament in 5th place and received $1.58."""


last_section = hand_content[-40:-1] # Take the last section of file

start_netwon = 0 # For handparsing
end_netwon = 0 # For handparsing
tourn_won = "$0.00"
won_something = ""
# Check if something was won
for i in last_section:
    if tourn_alias in i and "receives" in i:
        won_something = i
        start_netwon = won_something.find("$")
        end_netwon = 0
        numeric_counter = start_netwon
        for y in won_something[start_netwon:start_netwon+10]:
            if y != " ":
                numeric_counter += 1
            else:
                end_netwon = numeric_counter
                tourn_won = won_something[start_netwon:end_netwon]
                break
    elif tourn_alias in i and "received" in i:
        tourn_won = i[i.find("$"):-1]
        break






# Get prizepools
for i in stringContainer:
    if "Total Prize Pool" in i:
        tourn_prizepool_0 = i

tourn_prizepool_0 = tourn_prizepool_0[18:]

# Get players
for i in stringContainer:
    if "players" in i:
        tourn_player_count_0 = i


holder = ""
# Get placement, just last line in document
placement_section = content[-15:-1]
for i in placement_section:
    if "You finished in" in i:
        holder = i

place_word_start = holder.find("place")
tourn_placement_0 = holder[16:place_word_start+5]


print(tourn_id_0)
print(tourn_date_0)
print(tourn_description_0)
print(tourn_type_0)
print(tourn_buyin_0)

print(tourn_prizepool_0)
print(tourn_player_count_0)
print(tourn_placement_0)
print(tourn_won)


# Other variables
print(tourn_alias)
print(tourn_won)

