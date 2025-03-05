import random
print("""
 _   _ _       _                 _                           
| | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __ 
| |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
|  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |   
|_| |_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|   
         |___/                                               
""")


print("Welcome to the Higher Lower game! This program is a simple comparison game between options.\nIn this case, countries!")

options = [
    ["China", 1412],
    ["India", 1408],
    ["USA", 331],
    ["Indonesia", 276],
    ["Pakistan", 231],
    ["Brazil", 214],
    ["Nigeria", 223],
    ["Bangladesh", 171],
    ["Russia", 143],
    ["Mexico", 128],
    ["Japan", 125],
    ["Ethiopia", 120],
    ["Philippines", 113],
    ["Egypt", 110],
    ["Vietnam", 99],
    ["Turkey", 86],
    ["Germany", 84],
    ["Iran", 86],
    ["United Kingdom", 67],
    ["France", 65],
    ["Italy", 59],
    ["South Africa", 60],
    ["South Korea", 52],
    ["Canada", 39],
    ["Australia", 26]
]

option_type = "inhabitants"

def higher_lower(option_list, type):
    random.shuffle(option_list)
    player_score = 0
    playing = True
    while playing:
        for i, option in enumerate(option_list[:-1]):
            print(f"\nA) {option[0].capitalize()} has {option[1]} {type}\n")
            print(f"Does B) {option_list[i + 1][0].capitalize()} have more?")
            guess = input("\ntype 'higher' or 'lower'\n")
            answer = ''
            if option[1] > option_list[i + 1][1]:
                answer='lower'
            elif option[1] < option_list[i+1][1]:
                answer='higher'
            if guess == answer:
               player_score+=1
               print(f"\nThat's right!\nYour new score is {player_score}.\nKeep going!\n\n")
            else:
               print(f"\nOh no!\n That's wrong...\nYour score was {player_score}.\nGood luck next time!\n\n")
               playing=False
               break

higher_lower(options, option_type)