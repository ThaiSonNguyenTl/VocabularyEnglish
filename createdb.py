from models.vegetablesFruits import Vegetablesfruits
from playsound import playsound
import mlab
mlab.connect()

# list_vegetables_fruits= [ 
#         { 
#             "image" : "./static/images/img1.jpg",
#             "word" : "garlic",
#             "pronunciation": "",
#             "mean" : "Củ tỏi",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/UK/garlic-British-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img2.jpg",
#             "word" : "cabbage",
#             "pronunciation": "",
#             "mean" : "Cải bắp",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/us_pron/c/cab/cabba/cabbage.mp3",
#         },
#          { 
#             "image" : "./static/images/img3.jpg",
#             "word" : "watercress",
#             "pronunciation": "",
#             "mean" : "Cải xoong",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/US/watercress-American-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img4.jpg",
#             "word" : "tomato",
#             "pronunciation": "",
#             "mean" : "Cà chua",
#             "audio_link": "http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/T/1O0KWY95LVZF1.mp3",
#         },
#          { 
#             "image" : "./static/images/img5.jpg",
#             "word" : "cucumber",
#             "pronunciation": "",
#             "mean" : "Dưa chuột",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/uk_pron/u/ukc/ukcsa/ukcsa__018.mp3",
#         },
#          { 
#             "image" : "./static/images/img6.jpg",
#             "word" : "eggplant",
#             "pronunciation": "",
#             "mean" : "Cà tím",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/us_pron/e/egg/eggpl/eggplant.mp3",
#         },
#          { 
#             "image" : "./static/images/img7.jpg",
#             "word" : "coconut",
#             "pronunciation": "",
#             "mean" : " Dừa",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/UK/coconut-British-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img8.jpg",
#             "word" : "pineapple",
#             "pronunciation": "",
#             "mean" : "Quả dứa",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/uk_pron/u/ukp/ukpil/ukpilot019.mp3",
#         },
#          { 
#             "image" : "./static/images/img9.jpg",
#             "word" : "pear",
#             "pronunciation": "",
#             "mean" : "Quả lê",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/us_pron/p/pai/pair_/pair.mp3",
#         },
#          { 
#             "image" : "./static/images/img10.jpg",
#             "word" : "guava",
#             "pronunciation": "",
#             "mean" : "Quả ổi",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/us_pron/g/gua/guava/guava.mp3",
#         },
#          { 
#             "image" : "./static/images/img11.jpg",
#             "word" : "watermelon",
#             "pronunciation": "",
#             "mean" : "Dưa hấu",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/US/watermelon-American-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img12.jpg",
#             "word" : "lemon",
#             "pronunciation": "",
#             "mean" : "Chanh",
#             "audio_link": "http://s3.amazonaws.com/audio.vocabulary.com/1.0/us/L/10C81KIPQEC9D.mp3",
#         },
#          { 
#             "image" : "./static/images/img13.jpg",
#             "word" : "orange",
#             "pronunciation": "",
#             "mean" : "Cam",
#             "audio_link": "http://img2.tfd.com/pron/mp3/en/US/df/dfslsgdgsjd5drh7.mp3",
#         },
#          { 
#             "image" : "./static/images/img14.jpg",
#             "word" : "(a bunch of)banana",
#             "pronunciation": "",
#             "mean" : "(một nải) chuối",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/US/banana-American-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img15.jpg",
#             "word" : "prune",
#             "pronunciation": "",
#             "mean" : "mận khô",
#             "audio_link": "http://www.onelook.com/pronounce/macmillan/US/prune-American-English-pronunciation.mp3",
#         },
#          { 
#             "image" : "./static/images/img16.jpg",
#             "word" : "mango",
#             "pronunciation": "",
#             "mean" : "Quả xoài",
#             "audio_link": "http://dictionary.cambridge.org/us/media/english/uk_pron/u/ukm/ukmam/ukmammo027.mp3",
#         },
        
#           ]
# for i in list_vegetables_fruits:
#     db = Vegetablesfruits( 
#         image = i["image"],
#         word = i["word"],
#         mean = i["mean"],
#         audio_link = i["audio_link"]
                       
#     )
    # db.save()
