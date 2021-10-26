import os

tv = 0

# Paths
tourn_path = "C:/Users/Vla/Desktop/MTT"
history_path = "C:/Users/Vla/Desktop/Cash Game"

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
with open(tourn_files[0]) as raw_file:
    raw_content = raw_file.readlines()
    content = [x.strip() for x in raw_content]
    
    
nn = []

tourn_id_0 = ""
tourn_type_0 = ""

# line is each line in .txt and words is each word in each line
for line in content:
    words = line.split()
    nn.append(line)
    
    # Constrainer. We dont need to check all lines.
    tv += 1
    if tv > 15:
        break
    
tourn_id_0 = nn[0][nn[0].find("#"):nn[0].find(",")]
tourn_type_0 = nn[0][nn[0].find(",")+2:]

print(tourn_id_0)
print(tourn_type_0)


#print(raw_content)    
#print(content)