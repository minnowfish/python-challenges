import random


playlist = [["Little Talks","Of Monsters and Men"],["Dirty Paws","Of Monsters and Men"],["Mountain Sound","Of Monsters and Men"],["King And Lionheart","Of Monsters and Men"],["Crystals","Of Monsters and Men"],["Wolves Without Teeth","Of Monsters and Men"],["Human","Of Monsters and Men"],["Alligator","Of Monsters and Men"],["Sugar in a Bowl","Of Monsters and Men"],["Visitor","Of Monsters and Men"],["Everything Black","Unlike Pluto"],["JOLT","Unlike Pluto"],["Worst In Me","Unlike Pluto"],["Fade All My Life","Unlike Pluto"],["As They Bloom","Unlike Pluto"],["No Scrubs","Unlike Pluto"],["Guts","Unlike Pluto"],["Goner","Unlike Pluto"],["8 Legged Dreams","Unlike Pluto"],["We're Screwed","Unlike Pluto"],["Heather","Conan Gray"],["Memories","Conan Gray"],["Astronomy","Conan Gray"],["Maniac","Conan Gray"],["Wish You Were Sober","Conan Gray"],["Family Line","Conan Gray"],["People Watching","Conan Gray"],["Winner","Conan Gray"],["Disaster","Conan Gray"],["Crush Culture","Conan Gray"],["This Is Home","Cavetown"],["Devil Town","Cavetown"],["Juliet","Cavetown"],["Boys Will Be Bugs","Cavetown"],["Lemon Boy","Cavetown"],["Fool","Cavetown"],["Sweet Tooth","Cavetown"],["Talk To Me","Cavetown"],["Smoke Signals","Cavetown"],["Green","Cavetown"],["Line Without A Hook","Ricky Montgomery"],["Mr. Loverman","Ricky Montgomery"],["This December","Ricky Montgomery"],["My Heart Is Buried In Venice","Ricky Montgomery"],["Cabo","Ricky Montgomery"],["Talk To You","Ricky Montgomery"],["Sorry For Me","Ricky Montgomery"],["Erase","Ricky Montgomery"],["Don't Say That","Ricky Montgomery"],["Snow","Ricky Montgomery"]]

shuffled = []
artistTracker =[]

for x in range(20):
    i = random.randint(0,len(playlist)-1)
    while playlist[i][1] in artistTracker or playlist[i] in shuffled:
        i = random.randint(0, len(playlist)-1)
    shuffled.append(playlist[i])
    artistTracker.append(playlist[i][1])

    if len(artistTracker) > 2:
        artistTracker.pop(0)

for i in range(len(shuffled)):
    print(f"{i+1}. {shuffled[i][0]} by {shuffled[i][1]}")
