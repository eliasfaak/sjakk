mylines = []
with  open("chessgames_unedited.pgn", "rt") as myfile:
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline)
games_wanted = 5000
games_made = 0
line = 0
while games_made < games_wanted:
    f = open("/Users/eliasfakvam/Desktop/AI/gitrepo/gamefiles/%agame.pgn" % games_made, "w")
    blank_counter = 0
    while blank_counter < 2:
        if mylines[line] == "\n":
            blank_counter+=1
            line+=1

        else:
            if len(mylines[line]) < 100:
                line+=1
                pass
            else:
                f.write(mylines[line])
                line+=1
    f.close()
    games_made +=1
