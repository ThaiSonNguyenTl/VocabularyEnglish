# from models.vegetablesFruits import Vegetablesfruits
# from models.user import User
# from playsound import playsound
# import mlab
import random
# mlab.connect()
# def playAudio():
#     total_vegetablesAndFruits = Vegetablesfruits.objects()
#     for audio in total_vegetablesAndFruits:
#         playsound(audio.audio_link)
# playAudio()
# list_wma=[]
# total_vegetablesAndFruits = Vegetablesfruits.objects()
# for i in total_vegetablesAndFruits:
    # word = i.word
    # mean = i.mean
    # audio = i.audio_link
    # image = i.image
    # list_wma.append(word)
    # list_wma.append(mean)
    # list_wma.append(audio)  
    # list_wma.append(image)
# list word
# print(list_wma[0::4])
# list mean
# print(list_wma[1::4])
# list audio 
# print(list_wma[2::4])
# list image
# print(list_wma[3::4])
# randomWord = random.choice(list_wma[0::4])
# print(randomWord)
# print( list_wma)
# x =  User.objects(username = "Bruce Lee").first() 
# print(x)
# for user in User.objects().first() :
#     print(user.username)

answer = input("Play game? ('y' to continue)")
print(" ")
while answer == "y":

    vocabDictionary = {
        "dachi" :"stance",
        "zuke":"punch" ,
        "uke":"block",
        "geri":"kick",
        "ge dan barai" :"downward block",
        "age-uke":"rising block",
        "soto uke":"inward block",
        "uchi-uke":"outward block"
    }
    # turns words into a list 
    keyword_list = list(vocabDictionary.keys()) 
    # shuffle keywords
    random.shuffle(keyword_list)
    correct = 0
    wrong = 0 

    for keyword in keyword_list:
        display = "{}"
        print(display.format(keyword))
        userInputAnswer = input("ANSWER: ")
        print(vocabDictionary[keyword])
        print(" ")
        
        if userInputAnswer == (vocabDictionary[keyword]):
            print("CORRECT")
            correct += 1
        else:
            print("WRONG")
            wrong +=1 
        # line separator
        print('_'*25)
    display = "SCORE: {}  correct and {} wrong"
    print(display.format(correct,wrong))
    answer = input("Play again?('y' to continue)")
print(" ")
print("Thanks for playing")


   

       