
import time,sys,os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()


def typewriter(message) :
    for char in message :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
def opening_credits():
    print("""

    $$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\                            $$$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\                                              
    $$  __$$\ $$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |                           $$  _____|$$  __$$\ $$$\  $$ |$$  __$$\                                             
    $$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |                           $$ |      $$ /  $$ |$$$$\ $$ |$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ 
    $$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |                           $$$$$\    $$$$$$$$ |$$ $$\$$ |$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  _____|
    $$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |                           $$  __|   $$  __$$ |$$ \$$$$ |$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\  
    $$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |                           $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____| \____$$\ 
    $$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |                           $$ |      $$ |  $$ |$$ | \$$ |\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |
    \__|         \__|       \__|   \__|  \__| \______/ \__|  \__|                           \__|      \__|  \__|\__|  \__| \______/  \_______|\__| \__| \__| \_______|\_______/ 
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               """)
    time.sleep(4)
    cls()

    print("""

                                                             _____                          _       
                                                            |  __ \                        | |      
                                                            | |__) | __ ___  ___  ___ _ __ | |_ ___ 
                                                            |  ___/ '__/ _ \/ __|/ _ \ '_ \| __/ __|
                                                            | |   | | |  __/\__ \  __/ | | | |_\__ \ 
                                                            |_|   |_|  \___||___/\___|_| |_|\__|___/
                                         
                                         
    """)
    time.sleep(4)
    cls()


    print("""

     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |     ______   | || |  _________   | || |   _____      | || |   _____      | || |   ______     | || |  _______     | || |  _________   | || |      __      | || |  ___  ____   | |
    | |   .' ___  |  | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | || |  |_   _ \    | || | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_  ||_  _|  | |
    | |  / .'   \_|  | || |   | |_  \_|  | || |    | |       | || |    | |       | || |    | |_) |   | || |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |_/ /    | |
    | |  | |         | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | || |    |  __'.   | || |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   |  __'.    | |
    | |  \ `.___.'\  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | || |   _| |__) |  | || |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
    | |   `._____.'  | || | |_________|  | || |  |________|  | || |  |________|  | || |  |_______/   | || | |____| |___| | || | |_________|  | || ||____|  |____|| || | |____||____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
    time.sleep(4)

    cls()
    start_game()
def start_game():
    response = input("Are you ready to play? [Y/N] ")
    if response.upper() == "Y" or response.upper() == "YES":
        cls()
        print("Okay lets go!")
        time.sleep(4)
        cls()
        lvl_1_intro()
    elif response.upper() == "N" or response.upper() == "NO":
        cls()
        print("""
        
        ▒█░▄▀ 　 　 ▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 
        ▒█▀▄░ 　 　 ▒█▀▀▄ █▄▄█ █▀▀ █▀▀ █▀▀ 
        ▒█░▒█ 　 　 ▒█▄▄█ ▄▄▄█ ▀▀▀ ▀▀▀ ▀▀▀
        """)
        time.sleep(10)
        cls()
    else:
        print("HUH?")
        time.sleep(3)
        start_game()
def lvl_1_intro():
    typewriter("09:30    DEATH ISLAND MAXIMUM SECURITY PRISON")
    print(" ")
    print(" ")
    time.sleep(6)
    print("'Breakfast alarm rings'")
    time.sleep(3)
    print(" ")
    print("You open your eyes as you do every morning hoping this is just a horrible nightmare that you'll wake up from.")
    time.sleep(3)
    print(" ")
    print("No luck, day 112 it is then in this godforsaken place")
    print(" ")
    time.sleep(3)
    print("You skip breakfast knowing thats it wednesday which is porridge day and with past experience you've seen more appetising things in a toilet bowl")
    time.sleep(3)
    print(" ")
    print("As you brush your teeth you hear the book trolly coming and grab the copy of twilight you've just finished, excited to get the next in the series")
    time.sleep(3)
    print(" ")
    print("The miserable prison librabian just gives you a grunt of acknowlegement, as he hands you a book you see him slide something inside.")
    time.sleep(3)
    print(" ")
    print("You close the door and return to your bunk")
    time.sleep(3)
    print(" ")
    print("you open the book and find a note with a wax seal....")
    time.sleep(5)
    cls()
    print("""
     _______________________________________________   
    |   ╔═╗┌─┐┌─┐┌┬┐┌─┐┬┌┐┌                         |
    |   ║  ├─┤├─┘ │ ├─┤││││                         |
    |   ╚═╝┴ ┴┴   ┴ ┴ ┴┴┘└┘┘                        |
    |   ╔╦╗┌─┐┌┬┐┌─┐┬ ┬  ┬┌─┐  ┌┬┐┬ ┬┌─┐  ┌┬┐┌─┐┬ ┬ |
    |    ║ │ │ ││├─┤└┬┘  │└─┐   │ ├─┤├┤    ││├─┤└┬┘ |
    |    ╩ └─┘─┴┘┴ ┴ ┴   ┴└─┘   ┴ ┴ ┴└─┘  ─┴┘┴ ┴ ┴ ┘|
    |   ┬ ┬┌─┐┬  ┬    ┌┐ ┌─┐  ┬ ┬┌─┐┬┌┬┐┬┌┐┌┌─┐     |
    |   │││├┤ │  │    ├┴┐├┤   │││├─┤│ │ │││││ ┬     |
    |   └┴┘└─┘┴─┘┴─┘  └─┘└─┘  └┴┘┴ ┴┴ ┴ ┴┘└┘└─┘     |
    |   ┌─┐┌┬┐  ┌┬┐┬ ┬┌─┐  ┌─┐┌─┐┌┬┐┌─┐┌─┐  ┌─┐┌┬┐  |
    |   ├─┤ │    │ ├─┤├┤   │ ┬├─┤ │ ├┤ └─┐  ├─┤ │   |
    |   ┴ ┴ ┴    ┴ ┴ ┴└─┘  └─┘┴ ┴ ┴ └─┘└─┘  ┴ ┴ ┴   |
    |   ┌┬┐┬ ┬┌─┐┬┌─                                |
    |    │││ │└─┐├┴┐                                |
    |   ─┴┘└─┘└─┘┴ ┴o                               |
    |   ╔═╗┌─┐┌─┐┌┬┐  ┬  ┬ ┬┌─┐┬┌─                  |
    |   ║ ╦│ ││ │ ││  │  │ ││  ├┴┐                  |
    |   ╚═╝└─┘└─┘─┴┘  ┴─┘└─┘└─┘┴ ┴o                 |
    |_______________________________________________|
    
    """)
    print(" ")
    time.sleep(5)
    cls()
    time.sleep(1)
    cls()
    print("You jump up with excitement! your loyal crew is risking everything to get to Death Island to get you.")
    print(" ")
    time.sleep(2)
    print("The excitement quickly fades as you realise you have to get out of the prison itself to reach the ship.")
    time.sleep(2)
    print(" ")
    print("You start wildly looking around your cell, looking for anything to aid your escape")
    time.sleep(5)
    cls()
    time.sleep(4)
    lvl_1_1() 
def lvl_1_1():
    cls()
    print("You remember theres a bolt conveniently loose on the bed frame , you might be able to chip through the cellwall with it")
    time.sleep(1)
    response = input("do you want to use the bolt? [Y/N]  ")
    if response.upper() == "Y" or response.upper() == "YES":
        time.sleep(2)
        cls()
        print("'bolt breaks'") 
        time.sleep(3)
        cls()
        print("Obviously that would of been too easy!")
        time.sleep(2)
        print(" ")
        print("your never getting through that wall. back to the drawing board!")
        print(" ")
        time.sleep(2)
        lvl_1_2()
    elif response.upper() == "N" or response.upper() == "NO":
        print("smart, the walls are 2 feet thick and you have to escape today or you miss your chance! ")
        print(" ")
        time.sleep(3)
        cls()
        lvl_1_2()
    else:
        print("You had two options, yes or no. obviously thats too difficult for you")
        time.sleep(3)
        cls()
        lvl_1_1()
def lvl_1_2():
    print("Your scan your cell")
    print(" ")
    time.sleep(2)
    print("A guard slams on your door and tells you to stand back, a new cellmate enters.")
    print(" ")
    time.sleep(2)
    print("The guard then leaves. Your cellmate then starts ripping your stuff off the bunk and claiming its as his own.")
    print(" ")
    time.sleep(2)
    cls()
    response = input("Should you show him who the Alpha is here and give him a good hiding? [Y/N]  ")
    if response.upper() == "Y" or response.upper() == "YES":
        print(" ")
        response = input("he falls to the ground, should you keep going and really show him?[Y/N]  ")
        if  response.upper() == "Y" or response.upper() == "YES":
            print(" ")
            print("Your a PSYCHO! you are sent to solitary confinement for 28 days and miss your chance to escape")
            time.sleep(4)
            cls()
            game_over()

        elif response.upper() =="N" or response.upper() == "NO":
            print(" ")
            print("During the scuffle you had a 'EUREKA' moment anda instead of beating him senseless you taunt him and let him heavily injure you")
            time.sleep(3)
            print(" ")
            print("the guards are alerted by the noise and find you injured and unconcious. They take you to the medical ward, where you know you have a better chance of escape")
            time.sleep(3)
            cls()
            lvl_2_1()
            
        else:
            print("You had two options, yes or no. obviously thats too difficult for you")
            time.sleep(4)
            cls()

            lvl_1_2()

    elif response.upper() =="N" or response.upper() == "NO":
        response = input("He then starts to take some of your stuff for his own, are you just going to let him bully you like this? [Y/N]  ")
        if response.upper() == "N" or response.upper() == "NO":    
            print("You go to stop him, you fight and he falls to the ground  ")
            print(" ")
            time.sleep(3)
            response = input("Should you keep going and really show him?[Y/N] ")
            if response.upper() == "Y" or response.upper() == "YES":
                print(" ")
                print("Your a PSYCHO! you are sent to solitary confinement for 28 days and miss your chance to escape")
                time.sleep(4)
                cls()
                game_over()
            elif response.upper() =="N" or response.upper() == "NO":
                print(" ")
                print("During the scuffle you had a 'EUREKA' moment and instead of beating him senseless you taunt him and let him heavily injure you")
                time.sleep(3)
                print(" ")
                print("the guards are alerted by the noise and find you injured and unconcious. They take you to the medical ward, where you know you have a better chance of escape")
                time.sleep(3)
                lvl_2_1()
            else:
                print("huh?")
                time.sleep(2)
                cls()
                print("Restarting level")
                time.sleep(4)
                lvl_1_2()
        



        elif  response.upper() =="YES" or response.upper() == "Y": 
            time.sleep(2)
            cls()
            print("your a coward, you find no means of escape and are subject to your cellmates' bidding for the rest of your life sentence")
            time.sleep(4)
            cls()
            game_over()

        else: 
            print("huh?")
            time.sleep(4)
            cls()
            print("Restarting level")
            time.sleep(4)
            cls()
            lvl_1_2()



    else:
            print("You had two options, yes or no. obviously thats too difficult for you")
            time.sleep(3)
            cls()
            lvl_1_2()
def game_over() :
    print("""

    ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░██╗
    ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗██║
    ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝██║
    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗╚═╝
    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝
    """)
    response = input("Try again? [Y/N]")
    if response.upper() == "Y" or response.upper() == "YES":
        cls()
        lvl_1_intro()
    elif response.upper() == "N" or response.upper() == "NO":
        time.sleep(0.5)
        cls()
        
        typewriter("Thanks for playing!")
        print("""

     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |     ______   | || |  _________   | || |   _____      | || |   _____      | || |   ______     | || |  _______     | || |  _________   | || |      __      | || |  ___  ____   | |
    | |   .' ___  |  | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | || |  |_   _ \    | || | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_  ||_  _|  | |
    | |  / .'   \_|  | || |   | |_  \_|  | || |    | |       | || |    | |       | || |    | |_) |   | || |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |_/ /    | |
    | |  | |         | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | || |    |  __'.   | || |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   |  __'.    | |
    | |  \ `.___.'\  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | || |   _| |__) |  | || |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
    | |   `._____.'  | || | |_________|  | || |  |________|  | || |  |________|  | || |  |_______/   | || | |____| |___| | || | |_________|  | || ||____|  |____|| || | |____||____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
        time.sleep(4)
        cls()
        typewriter(" brought to you by.....")
        print("""

    $$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\                            $$$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\                                              
    $$  __$$\ $$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |                           $$  _____|$$  __$$\ $$$\  $$ |$$  __$$\                                             
    $$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |                           $$ |      $$ /  $$ |$$$$\ $$ |$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ 
    $$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |                           $$$$$\    $$$$$$$$ |$$ $$\$$ |$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  _____|
    $$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |                           $$  __|   $$  __$$ |$$ \$$$$ |$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\  
    $$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |                           $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____| \____$$\ 
    $$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |                           $$ |      $$ |  $$ |$$ | \$$ |\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |
    \__|         \__|       \__|   \__|  \__| \______/ \__|  \__|                           \__|      \__|  \__|\__|  \__| \______/  \_______|\__| \__| \__| \_______|\_______/ 
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               """)
        time.sleep(4)
        cls()
        print("""
        
        ▒█░▄▀ 　 　 ▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 
        ▒█▀▄░ 　 　 ▒█▀▀▄ █▄▄█ █▀▀ █▀▀ █▀▀ 
        ▒█░▒█ 　 　 ▒█▄▄█ ▄▄▄█ ▀▀▀ ▀▀▀ ▀▀▀
        """)
        time.sleep(10)
        cls()
    else:
        print("You had two options, yes or no. obviously thats too difficult for you")
        cls()
        cls()
    typewriter("Thanks for playing!")
    print("""

     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |     ______   | || |  _________   | || |   _____      | || |   _____      | || |   ______     | || |  _______     | || |  _________   | || |      __      | || |  ___  ____   | |
    | |   .' ___  |  | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | || |  |_   _ \    | || | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_  ||_  _|  | |
    | |  / .'   \_|  | || |   | |_  \_|  | || |    | |       | || |    | |       | || |    | |_) |   | || |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |_/ /    | |
    | |  | |         | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | || |    |  __'.   | || |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   |  __'.    | |
    | |  \ `.___.'\  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | || |   _| |__) |  | || |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
    | |   `._____.'  | || | |_________|  | || |  |________|  | || |  |________|  | || |  |_______/   | || | |____| |___| | || | |_________|  | || ||____|  |____|| || | |____||____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
    time.sleep(4)
    cls()
    typewriter(" brought to you by.....")
    print("""

    $$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\                            $$$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\                                              
    $$  __$$\ $$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |                           $$  _____|$$  __$$\ $$$\  $$ |$$  __$$\                                             
    $$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |                           $$ |      $$ /  $$ |$$$$\ $$ |$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ 
    $$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |                           $$$$$\    $$$$$$$$ |$$ $$\$$ |$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  _____|
    $$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |                           $$  __|   $$  __$$ |$$ \$$$$ |$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\  
    $$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |                           $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____| \____$$\ 
    $$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |                           $$ |      $$ |  $$ |$$ | \$$ |\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |
    \__|         \__|       \__|   \__|  \__| \______/ \__|  \__|                           \__|      \__|  \__|\__|  \__| \______/  \_______|\__| \__| \__| \_______|\_______/ 
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               """)
    time.sleep(4)
    cls()
def lvl_2_1():
    cls()
    typewriter( "1430    Medical Ward ")
    print(" ")
    time.sleep(3)
    print(" ")
    print("You slowly start to regain conciousness, hurting all over, a small sacrifice for freedom")
    time.sleep(3)
    print(" ")
    print("As you open your eyes you see a latex gloved hand with a needle uncomfortably close to your face.")
    time.sleep(3)
    print(" ")
    print("The doctor lets the guard know youv've woken up and then continues to finish the stitches on your face.")
    time.sleep(3)
    print(" ")
    print("you scan the room, as planned you are in the medical ward with only one guard and a doctor, you've been here before after a previous clash with a fellow inmate and know that there is an exit nearby.")
    time.sleep(3)
    print(" ")
    print("you just have to find a away to uncuff yourself and find the exit")
    time.sleep(5)
    cls()
    time.sleep(2)
    print("Knowing how early dusk is at this time of year and your short of time, you scan round the room for your chances to escape.")
    response = input("Do you \n\
    A) Try and seduce the doctor and then convince them to aid your escape so you can live happily ever after \n\
              \n\
    B) Grab the doctor while hes close, hold him hostage and negotiate your way out\n\
             \n\
    C) Be patient, a better oppurtinity may arise  ")
    if response.upper() == "A":
        cls()
        time.sleep(3)
        print(" ")
        print(" Unfortunately your seduction skills are terrible, so much so that both the doctor and guard broke down in tears with laughter")
        time.sleep(3) 
        lvl_2_2()
    elif response.upper() == "B":
        cls()
        print(" ")
        time.sleep(3)
        print("Well that was a gigantic fail, the guard slyly hit the alarm which triggers knock out gas and locks the door")
        time.sleep(4)
        cls()
        game_over()
    elif response.upper() == "C":
        cls()
        time.sleep(3)
        print("wise, remember this is your only shot, failure means living the rest of your days in this hellhole!")
        time.sleep(3)
        cls()
        lvl_2_2()
    else:
        cls()
        print("Huh?")
        time.sleep(3)
        lvl_2_1
def lvl_2_2():
    cls()
    print(" After half an hour the doctor finishes up and leaves the room. ")
    print(" ")
    time.sleep(3)
    print(" now its just you and the guard. your brain starts ticking to formulate some kind of plan")
    print(" ")
    time.sleep(3)
    print("All this thinking is thirsty work!")
    print(" ")
    time.sleep(3)
    response = input("Should you ask the guard for a glass of water? [Y/N] ")
    print(" ")
    if response.upper() == "Y" or response.upper == "YES":
        print("He ignores you, you ask again but in a louder and more pathetically desperate voice, he gives in and goes to get it for you")
        time.sleep(3)
        cls()
        lvl_2_3()
    elif response.upper() == "N" or response.upper == "NO":
        print(" ")
        response = input("HMMMM hydration is very important! Ask for a glas of water? [Y/N] ")
        if response.upper() == "Y" or response.upper == "YES":
            print(" ")
            print("He ignores you, you ask again but in a louder and more pathetically desperate voice, he gives in and goes to get it for you")
            time.sleep(3)
            cls()
            lvl_2_3()

        elif response.upper() == "N" or response.upper == "NO":
            print("Your stubborn! you missed your oppurtunity to escape")
            time.sleep(3)
            cls()
            game_over()
        else:
            print(" ")
            print("huh? it was a simple yes or no, your a fool and must restart the level ")
            time.sleep(3)
            cls()
            lvl_2_2()
    else:
        print(" ")
        print("huh? it was a simple yes or no, your a fool and must restart the level ")
        time.sleep(3)
        cls()
        lvl_2_2()
def lvl_2_3():
    cls()
    print("The guard returns with your water, he comes to the side of the bed and places it down.")
    print(" ")
    time.sleep(2)
    response = input("Do you \n\
        A) Take this chance and grab the guard \n\
        or \n\
        B) Just enjoy the lovely thirst-quenching water? \n\
         ")
    if response.upper() == "A":
        cls()
        print("success! you get him in a chokehold and he passes out.")
        time.sleep(2)
        print(" ")
        time.sleep(2)
        print("you grab his keys and uncuff your arm and then proceed to steal his uniform.")
        time.sleep(3)
        cls()
        lvl_2_4()
    elif response.upper() == "B":
        cls()
        time.sleep(2)
        print("You fool! I hope that water was worth it, you've missed your chance to escape")
        time.sleep(3)
        cls()
        game_over()
    else:
        print(" ")
        print("huh? it was a simple A or B, your a fool and must restart the level ")
        time.sleep(3)
        cls()
        lvl_2_3()
def lvl_2_4():
    print("Now disguised as a guard, you head to the door and take peek in to the corridor")
    print(" ")
    time.sleep(3)
    cls()
    response = input("  You look right and see a sign for you exit but see a couple of guards stood chatting, \n\
     \n\
    you look left and its clear but no idea where it goes. \n\
    \n\
    Do you go Left or Right? ")
    if response.upper() == "L" or response.upper() == "LEFT":
        time.sleep(3)
        cls()
        print("It's a dead end, you have to turn back")
        time.sleep(3)
        cls()
        print("you pull your stolen guard cap down to cover your face and confidently start walking towards the guards")
        time.sleep(5)
        cls()
        print("Success! the guards were too deep in conversation to take a good look at you, you flash your key card at the exit doors and step outside.")
        time.sleep(4)
        cls()
        lvl_3_1()
    elif response.upper() =="R" or response.upper() =="RIGHT":
        cls()
        time.sleep(3)
        print("you pull your stolen guard cap down to cover your face and confidently start walking towards the guards")
        time.sleep(5)
        cls()
        print("Success! the guards were too deep in conversation to take a good look at you, you flash your key card at the exit doors and step outside.")
        time.sleep(4)
        cls()
        lvl_3_1()
    else:
        print(" ")
        print("huh? it was a simple Left or Right, your a fool and must restart the level ")
        time.sleep(3)
        cls()
        lvl_2_4()
def lvl_3_1():
    print("You're outside, you see the front gate, but it's heavily guarded and there's a security checkpoint.")
    time.sleep(1)
    response = input("You've got two options,  \n\
         A: Try and blend in with the guards \n\
         B: Look for another way out ")
    if response.upper() == "A":
        time.sleep(3)
        print("You try and blend in but as you get to the gate, the doctor that tended to you was also leaving, he recognises you and raises the alarm!")
        time.sleep(3)
        print("you've been caught, enjoy your life sentence")
        time.sleep(3)
        cls()
        game_over()
    elif response.upper() == "B":
        time.sleep(3)
        cls()

        lvl_3_2()
    else:
        print(" ")
        print("huh? it was a simple A or B, your a fool and must restart the level ")
        time.sleep(3)
        cls()
        lvl_3_1()
def lvl_3_2():
    cls()
    print("You hide behind a bush and hear the prison alarams going off, they have found the unconcious officer and know your escaping. you can see snipers in the towers and you hear the dogs being let loose.")
    time.sleep(5)
    response = input("What are you going to do? \n\
    A: Run for the fence \n\
    B: Stay put and think of a better plan  ")
    if response.upper() == "A":
        time.sleep(3)
        print ("You've been caught by the dogs")
        time.sleep(3)
        cls()
        game_over()
    elif response.upper() == "B":
        time.sleep(3)
        "smart its one thing tryin to outrun snipers, but dogs aswell, you'd most definitely toast!"
        time.sleep(3)
        cls()
        lvl_3_3()
    else:
        print(" ")
        print("huh? it was a simple A or B, your a fool and must restart the level ")
        time.sleep(3)
        cls()
        lvl_3_2()

def lvl_3_3():
    print("The dogs are getting closer. the ground is filthy and smells suspiciously like faeces.")
    time.sleep(3)
    print(" ")
    response = input("Do you cover yourself in mud?[Y/N]  ")
    if response.upper() == "Y" or response.upper() == "YES":
        print ("Smart move! the mud hides your scent from the dogs")
        time.sleep(4)
        cls()
        end_game()
        
    elif response.upper() == "N" or response.upper() == "NO":
        time.sleep(3)
        print(" ")
        print ("The dogs Sniff you and catch you!")
        time.sleep(2)
        print(" ")
        print("who knew a good mud bath could of saved your life?")
        time.sleep(4)
        cls()
        game_over()
    else:
        print("Huh?")
        time.sleep(4)
        cls()
        lvl_3_3()
def end_game():
    print("As the dogs run past, you scan the fence for weakness's and looking for sniper blindspots")
    time.sleep(3)
    print(" ")
    print("Failing to find any feasible route, you hear a great explosion coming from the gates")
    time.sleep(3)
    print(" ")
    print("In the smoke and debris where the gate once stood you see your ship!") 
    time.sleep(3)
    print(" ")
    print("noticing all the guards are distracted or injured you make a run for it, its now or never.")
    time.sleep(6)
    cls()
    typewriter("You made it aboard your ship welcomed by your crew. But there is no time for celebration, you must now plan to clear your name and take your revenge!")
    time.sleep(5)
    cls()
    typewriter("TO BE CONTINUED ..............................  ")
    cls()
    typewriter("Thanks for playing!")
    print("""

     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |     ______   | || |  _________   | || |   _____      | || |   _____      | || |   ______     | || |  _______     | || |  _________   | || |      __      | || |  ___  ____   | |
    | |   .' ___  |  | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | || |  |_   _ \    | || | |_   __ \    | || | |_   ___  |  | || |     /  \     | || | |_  ||_  _|  | |
    | |  / .'   \_|  | || |   | |_  \_|  | || |    | |       | || |    | |       | || |    | |_) |   | || |   | |__) |   | || |   | |_  \_|  | || |    / /\ \    | || |   | |_/ /    | |
    | |  | |         | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | || |    |  __'.   | || |   |  __ /    | || |   |  _|  _   | || |   / ____ \   | || |   |  __'.    | |
    | |  \ `.___.'\  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | || |   _| |__) |  | || |  _| |  \ \_  | || |  _| |___/ |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
    | |   `._____.'  | || | |_________|  | || |  |________|  | || |  |________|  | || |  |_______/   | || | |____| |___| | || | |_________|  | || ||____|  |____|| || | |____||____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """)
    time.sleep(4)
    cls()
    typewriter(" brought to you by.....")
    print("""

    $$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\                            $$$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\                                              
    $$  __$$\ $$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |                           $$  _____|$$  __$$\ $$$\  $$ |$$  __$$\                                             
    $$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |                           $$ |      $$ /  $$ |$$$$\ $$ |$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$$\ 
    $$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |                           $$$$$\    $$$$$$$$ |$$ $$\$$ |$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  _____|
    $$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |                           $$  __|   $$  __$$ |$$ \$$$$ |$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\$$$$$$\  
    $$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |                           $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____| \____$$\ 
    $$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |                           $$ |      $$ |  $$ |$$ | \$$ |\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |
    \__|         \__|       \__|   \__|  \__| \______/ \__|  \__|                           \__|      \__|  \__|\__|  \__| \______/  \_______|\__| \__| \__| \_______|\_______/ 
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                                                                                               """)
    time.sleep(4)
    cls()

game_over()


