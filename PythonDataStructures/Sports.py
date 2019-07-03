Cricket=[ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football=[ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton=[ "PKM", "ALN", "NV", "KM","RMV"]
all_Players_list=list()
all_Players_list.extend(Cricket)
all_Players_list.extend(Football)
all_Players_list.extend(Badminton)


def displayNames(data):
    for name in data:
        print(name ,end=" ")
    print()    
        
print("All Players List")
displayNames(all_Players_list)

unique_Players_Set=set()

for name in all_Players_list:
    unique_Players_Set.add(name)

print("Unique Players")
displayNames(unique_Players_Set)

all_games_players_list=list() 

for name in unique_Players_Set:
    if name in (Cricket and Football and Badminton):
        all_games_players_list.append(name)

print("Player  who play all 3 games")
displayNames(all_games_players_list)


        
