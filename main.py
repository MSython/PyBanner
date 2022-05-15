#M.Sython
#PyBanner

#pip install termcolor2
#pip install pyfiglet


#import modules:
from termcolor2 import * #for coloring text
from pyfiglet import * #for create banner


#input text:
text = input("Type your text: ")

#input color:
color = input("Type your text color: ")

#check color:
colors = ["blue","red","green","yellow","white"] #list of colors of
if color not in colors:
    print(colored("Your color is wrong !", color="red"))
    print(colored("colors: ",color="yellow"))
    print(colors)
    color = "white"

#create banner:
text = figlet_format(text) #text to banner
text = colored(text,color) #coloring banner

#print banner:
print(text)
