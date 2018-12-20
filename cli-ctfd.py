#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import re
import sys

def welcome():
    print("     ██████╗██╗     ██╗     ██████╗████████╗███████╗██████╗ ")
    print("    ██╔════╝██║     ██║    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
    print("    ██║     ██║     ██║    ██║        ██║   █████╗  ██║  ██║")
    print("    ██║     ██║     ██║    ██║        ██║   ██╔══╝  ██║  ██║")
    print("    ╚██████╗███████╗██║    ╚██████╗   ██║   ██║     ██████╔╝")
    print("     ╚═════╝╚══════╝╚═╝     ╚═════╝   ╚═╝   ╚═╝     ╚═════╝ ")



def help():
    welcome()
    print("[+] help")
    print("general usage : cli-ctfd --url <link> --scoreboard ")
    print("     --help              show this help ")
    print("     --url               it will use a url to run")
    print("     --scroreboard       show scoreboard")
    print("     --top n             it will show top n player ex : --top 10")
    print("     --about             show about author of this script")

def scoreboard(address):
    welcome()
    #address = "https://ctf-class.ccug.gunadarma.ac.id/scoreboard"
    res     = requests.get(address , timeout = 5)
    content = BeautifulSoup(res.content , "html.parser")
    textContent = []
    raw = ""
    for i in range(0, 1):
        table = content.find_all("tbody")[i].text
        #textContent.append(table)
        raw = table.split("\n\n")

    #print("[+] output : " + str(raw))
    for i in range(len(raw)):
        #print("player : " + raw[i].strip().replace('\n',""))
        if raw[i] == "" :
            continue
        else:
            print("             " + str(i) + " " + re.sub('([0-9])' , "" ,raw[i]).replace("\n", ""))

def top_player(address , num):
    welcome()
    #address = "https://ctf-class.ccug.gunadarma.ac.id/scoreboard"
    res     = requests.get(address , timeout = 5)
    content = BeautifulSoup(res.content , "html.parser")
    textContent = []
    raw = ""
    for i in range(0, 1):
        table = content.find_all("tbody")[i].text
        #textContent.append(table)
        raw = table.split("\n\n")

    #print("[+] output : " + str(raw))
    for i in range(num+1):
        #print("player : " + raw[i].strip().replace('\n',""))
        if raw[i] == "" :
            continue
        else:
            print("             " + str(i) + " " + re.sub('([0-9])' , "" ,raw[i]).replace("\n", ""))


def about():
    welcome()
    print("author       : Arsalan Diponegoro")
    print("blog         : https://blog.tripoloski.ccug.gunadarma.ac.id")
    print("email        : arsalan.dp@gmail.com")

def main():
    row = sys.argv
    if(len(sys.argv) <= 1):
        help()
        exit(0)
    for i in range(len(row)):
        if(str(sys.argv[i]) == "--about"):
            about()
            break
        if(str(sys.argv[i]) == "--url"):
            link  = str(sys.argv[i + 1 ])
            #print("address : " + link)
        if(str(sys.argv[i]) == "--scoreboard"):
            scoreboard(link)
            break
        if(str(sys.argv[i]) == "--top"):
            num = int(sys.argv[i + 1])
            top_player(link , num)
            break
        if(str(sys.argv[i]) == "--help"):
            help()
            break

if __name__ == '__main__':
    main()
