import os
import sys
import time
import webbrowser

def game_welcome():
    os.system("cls")

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    def print_center(text=""):
        print(text.center(terminal_width))

    time.sleep(2)

    border = "=" * 75

    print_center(border)
    print_center("Welcome to the Game!")
    print_center("Rule: Answer 'yes' or 'no' to my hot takes. Choose wisely! ")
    print_center(border)

    time.sleep(1)
    input("Press ENTER to start the game...".center(terminal_width))

    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"

    point = 0

    # Question 1
    while True:
        os.system("cls")
        print(f"{point} points".rjust(terminal_width))
        print_center("1. Is F1 (Formula One) 🏎️ the best race or the worst?")
        print_center("Type 'best', 'worst', or 'i' for info")
        answer = input("\nYour answer: ").strip().lower()

        if answer == 'i':
            print_center(BLUE +  "Opening Wikipedia..." + RESET)
            time.sleep(1)
            webbrowser.open("https://www.google.com/search?q=F1&sca_esv=074237d04407bddc&sxsrf=APpeQnsXYvzH9IqOkQSv3jpEYftOPnsYCw%3A1791907140037&ei=RFXOauTQAZ-W4-EPwP2p-AI&biw=1766&bih=948&uact=5&oq=F1&gs_lp=Egxnd3Mtd2l6LXNlcnAiAkYxMgQQIxgnMgQQIxgnMgoQIxjwBRjJAhgnMg0QLhiABBiKBRhDGLEDMgoQABiABBiKBRhDMgYQABgHGB4yBhAAGAcYHjINEAAYgAQYigUYQxixAzIGEAAYBxgeMgYQABgHGB4yHBAuGIAEGIoFGEMYsQMYlwUY3AQY3gQY4ATYAQJI-wRQpwFYpwFwAXgBkAEAmAGkAqABpAKqAQMyLTG4AQPIAQD4AQGYAgKgArwCwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAhcQLhjcBhi4BhjaBhjYAhjIAxiwA9gBAZgDAIgGAZAGDLoGBAgBGBm6BgYIAhABGBSSBwUxLjMtMaAHkwmyBwMzLTG4B64CwgcDMy0yyAcSgAgB&sclient=gws-wiz-serp#:~:text=Formula%20One%20is%20the%20highest%20class%20of%20worldwide%20racing%20for%20open%2Dwheel%2C%20single%2Dseater%20formula%20racing%20cars%20run%20by%20the%20Formula%20One%20Group%20and%20sanctioned%20by%20the%20F%C3%A9d%C3%A9ration%20Internationale%20de%20l%27Automobile.")

        elif answer == "best":
            point += 1
            print_center(GREEN + "Correct! F1 is indeed the best race!🔥🔥 (+1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        elif answer == "worst":
            point -= 0
            print_center(RED + "Nigga you r gay!😑 (-1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        else:
            print_center("Invalid input type 'best', 'worst' or 'i' for info")

    # Question 2
    while True:
        os.system("cls")
        print(f"{point} points".rjust(terminal_width))
        print_center("2. Does pizza 🍕 taste better with pineapple 🍍?")
        answer = input("\nYour answer (yes/no): ").strip().lower()

        if answer == "yes":
            point -=1
            print_center(RED + "Nah bruh you kidding me? Pineapple on pizza is a crime against humanity!😧 (-1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        elif answer == "no":
            point += 1
            print_center(GREEN + "Correct! Humanity is still alive!🥲😇 (+1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        else:
            print_center("Invalid input. Please type 'yes' or 'no'.")

    # Question 3
    while True:
        os.system("cls")
        print(f"{point} points".rjust(terminal_width))
        print_center("3. Is Messi the GOAT 🐐?")
        answer = input("\nYour answer (yes/no): ").strip().lower()

        if answer == "yes":
            point += 1
            print_center(GREEN + "Dayum bro speaking Fax🗣️🔥 (+1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break 
        elif answer == "no":
            point -= 0
            print_center(RED + "Nah bro you're wrong!🙄 (-1 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        elif answer == "ronaldo":
            point += 0.5
            print_center(GREEN + "True both Messi and Ronaldo are legends🐐 (+0.5 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        elif answer == "cristiano ronaldo":
            point += 0.5
            print_center(GREEN + "True both Messi and Ronaldo are legends🐐 (+0.5 point)" + RESET)
            input("\nPress ENTER to continue...".center(terminal_width))
            break
        else:
            print_center("Invalid input. Please type 'yes' or 'no'.")

    # print_center(f"Game Over! You scored {point} points.".center(terminal_width))

    #TODO: Add more questions and scoring logic as needed.

    os.system("cls")

    print_center(border)
    print_center(f"{CYAN}FINAL AGREEMENT SCORE: {point}{RESET}")

    if point >= 2:
        print_center(GREEN + "Result: You are my best friend! We agree on almost everything." + RESET)
    elif point == 1:
        print_center(YELLOW + "Result: We are neutral. A good mix of harmony and debate." + RESET)
    else:
        print_center(RED + "Result: You are my rival! We have completely opposite opinions." + RESET)
    print_center(border)