print("Enter details for Team 1:")
team1_name = input("Team Name: ")
team1_members = int(input("Number of members (Allowed: 2 to 4): "))
team1_r1 = int(input("Round 1 Score: "))
team1_r2 = int(input("Round 2 Score: "))


print("\nEnter details for Team 2:")
team2_name = input("Team Name: ")
team2_members = int(input("Number of members (Allowed: 2 to 4): "))
team2_r1 = int(input("Round 1 Score: "))
team2_r2 = int(input("Round 2 Score: "))
print("\nCalculating results...\n")
valid_sizes = True

if team1_members < 2 or team1_members > 4:
    print(f"Error: {team1_name} has an invalid size! Must be between 2 and 4 members.")
    valid_sizes = False

if team2_members < 2 or team2_members > 4:
    print(f"Error: {team2_name} has an invalid size! Must be between 2 and 4 members.")
    valid_sizes = False


if valid_sizes:
    
    team1_total = team1_r1 + team1_r2
    team2_total = team2_r1 + team2_r2

   
    print(f"{team1_name} Total Score: {team1_total}")
    print(f"{team2_name} Total Score: {team2_total}")

    if team1_total > team2_total:
        print(f"1st Place: {team1_name}")
        print(f"2nd Place: {team2_name}")
        
    elif team2_total > team1_total:
        print(f"1st Place: {team2_name}")
        print(f"2nd Place: {team1_name}")
        
    else:
        print("Tie detected! Applying tie-breaker rule (Highest Round 2 score wins)...")
        
      
        if team1_r2 > team2_r2:
            print(f"1st Place: {team1_name} (Won via Round 2 tie-breaker)")
            print(f"2nd Place: {team2_name}")
        elif team2_r2 > team1_r2:
            print(f"1st Place: {team2_name} (Won via Round 2 tie-breaker)")
            print(f"2nd Place: {team1_name}")
        else:
            print("Complete Tie! Both teams share the same rank.")
else:
    print("Ranking canceled due to invalid team size(s). Please restart.")
