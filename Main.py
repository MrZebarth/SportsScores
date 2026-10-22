# Create an Intramural score tracker

# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against
print ("Welcome to the Intramural Score Tracker!")
# You will ask how many teams are playing.
print("How many teams are playing?")
numTeams=int(input())
while (numTeams<2):
    print("You need at least 2 teams for a competition! Try again")
    numTeams=int(input())

print(f"Got it. {numTeams} teams. Now let's set those up.")
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
teams=[]
for i in range(numTeams):
    team=[]
    print(f"What's the team name for team #{i+1}?")
    team.append(input())
    team.extend(0 for i in range(6))
    print(team)
    teams.append(team)
print(teams)

# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit
choice=0
while choice!=4:
    print("\nPick one of the following options:")
    print("1. Add a score")
    print("2. See Team Stats")
    print("3. See Overall Standings")
    print("4. Quit")
    print("Your choice: ")
    choice=int(input())

    if choice==1:
#   1) Enter team 1, team 2, goals for team 1, goals for team 2
        # List teams, pick one
        counter = 1
        for i in teams:
            print(f"{counter}: {i[0]}")
            counter+=1
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie
        teamChoice=0
        while teamChoice>numTeams or teamChoice<1:
            print("Please enter your choice for the first team:")
            teamChoice=int(input())
            if teamChoice<1 or teamChoice>numTeams:
                print("That is an invalid choice. Please try again.")

        teamChoice2=0
        counter=1
        for i in teams:
            print(f"{counter}: {i[0]}")
            counter+=1
        while teamChoice2>numTeams or teamChoice2<=0 or teamChoice2==teamChoice:
            print("Enter your choice for the second team:")
            teamChoice2=int(input())
            if teamChoice2>numTeams or teamChoice2<=0 or teamChoice2==teamChoice:
                print("That is not a valid choice. Please try again.")
        teamChoice-=1
        teamChoice2-=1
        # Get the scores
        print(f"Enter the score for {teams[teamChoice][0]}")
        score1=int(input())
        print(f"Enter the score for {teams[teamChoice2][0]}")
        score2=int(input())
        # Update Team 1
        # Games Played
        teams[teamChoice][1]+=1
        # Goals for
        teams[teamChoice][5]+=score1
        # Goals against
        teams[teamChoice][6]+=score2

        # Update Team 2
        # Games Played
        teams[teamChoice2][1]+=1
        # Goals for
        teams[teamChoice2][5]+=score2
        # Goals against
        teams[teamChoice2][6]+=score1

        #Win/Loss/Tie
        if score1>score2:
            teams[teamChoice][2]+=1
            teams[teamChoice2][3]+=1
            print(f"\n{teams[teamChoice][0]} beat {teams[teamChoice2][0]} by a score of {score1} - {score2}. Entered\n")
        elif score2>score1:
            teams[teamChoice][3]+=1
            teams[teamChoice2][2]+=1
            print(f"\n{teams[teamChoice2][0]} beat {teams[teamChoice][0]} by a score of {score2} - {score1}. Entered\n")
        else:
            teams[teamChoice][4]+=1
            teams[teamChoice2][4]+=1
            print(f"\n{teams[teamChoice][0]} tied {teams[teamChoice][1]} with a score of {score1} - {score2}. Entered\n")


    elif choice==2:
#   2) Print a list of team names.
        for i in range(len(teams)):
            print(f"{i+1}: {teams[i][0]}")
        print("Which team would you like to see?")
        teamChoice=int(input())
        while teamChoice<1 or teamChoice>len(teams):
            print("That is an invalid choice. Please try again.")
            teamChoice=int(input())
#       Once the user selects, Print out their stats
        current=teams[teamChoice-1]
        print(f"\nTeam: {current[0]}")
        print(f"Games Played: {current[1]}")
        print(f"Wins: {current[2]}\tLosses: {current[3]}\tTies: {current[4]}")
        print(f"Goals For: {current[5]}")
        print(f"Goals Against: {current[6]}\n")

    elif choice==3:
#   3) Print out the teams in order from most team points to least
        # Make a new output list
        standings=[]
        # Loop through the teams
        for i in teams:
            # Create an entry with [name, pts, goals for, goals against]
            entry=[i[0],i[2]*2+i[4],i[5],i[6]]
            placed=False
            for j in range(len(standings)):
                if not placed and entry[1]>standings[j][1]:
                    standings.insert(j,entry)
                    placed=True
                elif not placed and entry[1]==standings[j][1]:
                    if entry[2]>standings[j][2]:
                        standings.insert(j,entry)
                        placed=True
                    elif entry[2]==standings[j][2] and entry[3]<standings[j][3]:
                        standings.insert(j,entry)
                        placed=True
                    else:
                        standings.insert(j+1,entry)
                        placed=True
            if not placed:
                standings.append(entry)

        # Print out the results
        for i in range(len(standings)):
            print(f"{i+1}: {standings[i][0]}: {standings[i][1]} pts, {standings[i][2]} GF, {standings[i][3]} GA")

#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.
        pass

    elif choice==4:
#   4) Say goodbye and break out of the loop
        print("\nThank you for using the Sports Scores App!")
        exit(0)

    else:
        pass




