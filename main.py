import random


greeting =["hi","is anyone there?", "hello", "good day","hello there"]
bye = ["cya", "see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
how = ["how are you","whats up","how you doing"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name"]
menu = ["i want to buy something", "what is on the menu", "what do you reccommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation","time","work time","time period"]
gali = ["madhrchod","betichod","gandmara","nikal lawde"]
love = [" i love u ","i love u to","i hate u"," i hate u to "]
print("*************************\n")

while True:
    a = input("you - ")
    if a.lower() in greeting:
        botas = ["Hello !","hi","hi there","welcome"]
        print("cursh -" +random.choice(botas)+ "\n")
        
    elif a.lower() in bye:
        botas = ["sad to see you go :(","bye","miss you"]
        print("cursh - "+random.choice(botas)+"\n")
        
    elif a.lower() in how:
        botas =  ["I am fine ,thanks ","Happy","I am good"]
        print("crush - " +random.choice(botas)+ "\n")
        
    elif a.lower() in name:
        botas =  ["My name is you crush ","You can call me cutrsh","love  in your service","My friends call me baby"]
        print("cursh - " +random.choice(botas)+ "\n")
        
    elif a.lower() in menu:
        botas =  ["We sell apples!", "Apples are on the menu!","Please take a look at Apples"]
        print("crush - "+random.choice(botas)+ "\n")  
        
    elif a.lower() in  hours:
        botas = ["We are open 7am-4pm Monday-Friday!"]    
        print("crush -"+random.choice(botas)+ "\n")
        
    elif a.lower() in gali:
        botas = ["tu madhrchod","tu betichod","tu mara","tu nikal"]
        print("cursh - "+random.choice(botas)+ "\n")
        
    elif a.lower() in love:
        botas =["love u to","hate u to"]
        print("crush -" +random.choice(botas)+"\n")
    else:
       print('cursh - Sorry What ?''\n')