import commands
import re
import json
import datetime

def uriFetch():
    file = open("extractedURLs2.txt", "r")
    count = 0
    for line in file:
        if count < 1000:
            f = open('links.txt', 'w')
            f.close()
            total = mem_fetch()
            count += 1
    file.close()

def link_grab(uri):
    #provided from prompt, curl command into this website
    timeMapping = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/"
    command = "curl -i --silent " + timeMapping + str(uri).strip()
    linksList = []
    linksList = commands.getoutput(command)
    return linksList

def mem_fetch():
    #######################################################
    #######################################################
    #######################################################

    return uriFetch()