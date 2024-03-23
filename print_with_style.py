#author__thea_uy
#date__march_23_2024
#this program will ask the user for their name, dream job, hobby, personality type, and motto
#this program will also display the data inputted by the user

#import modules
import pyfiglet
import colorama
colorama.init(autoreset=True)

#ask the user for their name, dream job, hobby, personality type, and motto
name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")
hobby = input("Enter your hobby: ")
personality_type = input("Enter your personality type: ")
motto = input("Enter your motto: ")

#add a message for the user
message = ("You will reach your dreams, Believe it!")

#define the font style of the variables
name = (pyfiglet.figlet_format(name,font='invita'))
dream_job = (pyfiglet.figlet_format(dream_job,font='invita'))
hobby = (pyfiglet.figlet_format(hobby,font='contessa'))
personality_type = (pyfiglet.figlet_format(personality_type,font='contessa'))
motto = (pyfiglet.figlet_format(motto,font='digital'))
message = (pyfiglet.figlet_format(message,font='digital'))


#define the font color of the variables
name = (colorama.Fore.LIGHTMAGENTA_EX + name)
dream_job = (colorama.Fore.LIGHTCYAN_EX + dream_job)
hobby = (colorama.Fore.LIGHTYELLOW_EX + hobby)
personality_type = (colorama.Fore.LIGHTCYAN_EX + personality_type)
motto = (colorama.Fore.LIGHTMAGENTA_EX + motto)
message = (colorama.Fore.LIGHTBLUE_EX + message)


#display the data
print(name)
print(dream_job)
print(hobby)
print(personality_type)
print(motto)
print(message)

#this is the end of the program!
#thank you for using my program!
#this program had undergone through basic trials
#date finished__march_23_2024_9:02_pm