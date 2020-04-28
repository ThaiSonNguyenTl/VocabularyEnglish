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

    animalDictionary = {
        "ngựa vằn":"Zebra",
        "Hươu cao cổ":"Giraffe",
        "Tê giác ":"Rhinoceros",
        "Con voi ":"Elephant",
        "Sư tử":"Lion",
        "Con hổ":"Tiger",
        "Con báo":"Leopard",
        "Hà mã":"Hippopotamus",
        "Linh dương đầu bò":"Gnu",
        "Linh dương":"Antelope",
        "Lạc đà":"Camel",
        "Đại bàng":"Eagle",
        "Cú mèo":"Owl",
        "Chim ưng":"Falcon",
        "Đà điểu":"Ostrich",
        "Chim gõ kiến":"Woodpecker",
    }
    # turns words into a list 
    keyword_list = list(animalDictionary.keys()) 
    # shuffle keywords
    random.shuffle(keyword_list)
    correct = 0
    wrong = 0 

    for keyword in keyword_list:
        display = "{}"
        word = display.format(keyword)
        print(word)
        userInputAnswer = input("ANSWER: ")
        print(animalDictionary[word])
        print(" ")
        
        if userInputAnswer.lower() == (animalDictionary[word]).lower():
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


   

       