import os


# Paths
#tourn_path = "C:/Users/Vla/Desktop/MTT"
#history_path = "C:/Users/Vla/Desktop/Cash Game"
tourn_path = "C:/Users/Deida/AppData/Local/PokerStars.DK/TournSummary/Valdemar1743"
history_path = "C:/Users/Deida/AppData/Local/PokerStars.DK/HandHistory/Valdemar1743"

# Generates file names for all files in tournament summary folder
def get_tourn_filenames(tourn_path):
    tourn_files = []
    for root, dirs, files in os.walk(tourn_path, topdown=False):
       for name in files:
          tourn_files.append(os.path.join(root, name))
    return tourn_files
      
# Generates fill names for all files in hand history folder
def get_hist_filenames(history_path):
    history_files = []
    for root, dirs, files in os.walk(history_path, topdown=False):
        for name in files:
            history_files.append(os.path.join(root, name))
    return history_files

# Getting raw content and then using strip to remove extra space
def get_content(dataList,dataLength):    
    content_arr = []
    for x in range(dataLength):    
        with open(dataList[x]) as raw_file:
            raw_content = raw_file.readlines()
            content = [x.strip() for x in raw_content]
            content_arr.append(content)

    return content_arr



# line is each line in .txt and words is each word in each line
# Here we start searching the tourn summary files for information, one by one filling the information we need by searching in strings
def get_first_bit(input_content):
    stringContainer = []
    tv = 0
    for line in input_content:
        words = line.split()
        stringContainer.append(line)
        
        # Constrainer. We dont need to check all lines.
        tv += 1
        if tv > 11:
            break
    return stringContainer
 

# Get tournament id 
def get_tourn_id(input_content):  
    tourn_id_0 = ""
    tourn_id_0 = input_content[0][input_content[0].find("#")+1:input_content[0].find(",")]
    return tourn_id_0


# Get tournament type
def get_tourn_type(input_content):
    tourn_type_0 = ""
    tourn_type_0 = input_content[0][input_content[0].find(",")+2:]
    return tourn_type_0

# Get tournament date
def get_tourn_date(input_content):
    tourn_date_0 = ""
    store_date = 0
    stringCotainer_str = str(input_content)
    store_date = stringCotainer_str.find("started")
    tourn_date_0 = stringCotainer_str[store_date+8:store_date+31]
    return tourn_date_0

# Get tournament buy-in
def get_tourn_buyin(input_content):
    stringCotainer_str = str(input_content)
    tourn_buyin_0 = ""
    store_buyin = stringCotainer_str.find("Buy-In") # Searcing for start of sentence
    letstry = stringCotainer_str[store_buyin:store_buyin+50].find("'") # Finding next ' from after "Buy-In"
    tourn_buyin_0 = stringCotainer_str[store_buyin:store_buyin+letstry] # Making new string from the two character positions just found
    return tourn_buyin_0

# Get net won. Might have to check hand histories for this

# Match tournament id in both folders tournsummary and handhistory
def match_id(tourn_id, hist_filenames):
    identical_tourn = ""
    for i in hist_filenames: 
        if tourn_id in i:
            identical_tourn = i
    return identical_tourn

# Open the identical tournament as a raw file and parse the document into variables that is stripped off useless characters
def get_handhistory_content(identical_tourn):
    with open(identical_tourn) as raw_file:
        raw_hand_content = raw_file.readlines()
        hand_content = [x.strip() for x in raw_hand_content]
    return hand_content

def get_alias(hand_history_content):
    the_alias = hand_history_content[:50]
    for i in the_alias:
        if "Dealt to" in i:
            le_tourn_alias = i
            le_tourn_alias = le_tourn_alias[9:le_tourn_alias.find("[")-1]
            break
    return le_tourn_alias

# In the txt handhistory .txt we can find the player/users name by searching for "Dealt To", and in this case: "Dealt To Valdemar1743" This way the alias can be used as a varaible later on
def how_much_won(hand_history_content):
    tourn_alias = get_alias(hand_history_content)

    """There is several ways the txt logs store how much you won. If you havent won it will say "Valdemar1743 finished the tournament in blabla place"
    If you win, it can say "Valdemar1743 wins the tournament and receives $0.50 - congratulations!"
    If you win money but is not 1st place you get something like "Valdemar1743 finished the tournament in 5th place and received $1.58."""

    last_section = hand_history_content[-40:-1] # Take the last section of file

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
    return tourn_won

# Get prizepools
def get_prizepool(input_str):
    for i in input_str:
        if "Total Prize Pool" in i:
            tourn_prizepool_0 = i

    tourn_prizepool_0 = tourn_prizepool_0[18:]
    return tourn_prizepool_0



# Get players
def get_players(input_str):
    for i in input_str:
        if "players" in i:
            tourn_player_count_0 = i
            whenTheNumbersEnd = tourn_player_count_0.find(" ")
            tourn_player_count_0_int = int(tourn_player_count_0[0:whenTheNumbersEnd])
    return tourn_player_count_0_int



# Checking if its a knockout tournament
def checkForKnockout(hand_content_last_section):
    for i in hand_content_last_section:
        if "bounty" in i:
            return True

# Get tournament description
def get_tourn_description(input_str, tourn_player_count, hand_hist_content):
    tourn_description_0 = ""

    if tourn_player_count <= 9:
        tourn_description_0 = "Sit & Go"
    if tourn_player_count > 9:
        tourn_description_0 = "MTT"
    for i in input_str:
        if "Satellite" in i and tourn_player_count <= 9:
            tourn_description_0 = "Sit & Go Satellite"
            break
        if "Satellite" in i and tourn_player_count > 9:
            tourn_description_0 = "Satelitte MTT"
            break
        if checkForKnockout(hand_hist_content) == True and tourn_player_count > 9:
            tourn_description_0 = "Knockout MTT"
            break

    return tourn_description_0



# Get placement, just last line in document
def get_placement(content_input,tourn_alias):
    holder = ""
    placement_section = content_input[-15:-1]
    for i in placement_section:
        if "You finished in" in i:
            holder = i
            break

    place_word_start = holder.find("place")
    tourn_placement_0 = holder[16:place_word_start+5]

    # Sometimes it does not say "finished in ??nd place", so if container is empty we check tournamnet .txt for tourn_alias in doing some parsing to get placement.
    semicolon_where = 0
    if holder == "":
        for i in content_input[8:]:
            if tourn_alias in i:
                semicolon_where = i.find(":")
                tourn_placement_0 = i[0:semicolon_where] + " place"
                break

    return tourn_placement_0


