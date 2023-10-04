# pip install googletrans==4.0.0-rc1
from googletrans import Translator
translator = Translator()
language = {                    # We can add any language code if it is not present here
            "ar": "Arabic",
            "bn": "Bangla",
            "zh": "Chinese",
            "en": "English",
            "fr": "French",
            "de": "German",
            "el": "Greek",
            "gu": "Gujarati",
            "he": "Hebrew",
            "hi": "Hindi",
            "ga": "Irish",
            "it": "Italian",
            "ja": "Japanese",
            "ko": "Koren",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "pu": "Punjabi",
            "ru": "Russian",
            "sa": "Sanskrit",
            "es": "Spanish",
            "te": "Telugu",
            "ta": "Tamil",

}

allow=True    # variable to control correct language code input
while allow:    # checking if language code is valid
  user_input=input(f"Please enter the desired language code. To see the language code list enter 'options' \n")

  if user_input=="options":     # showing language options
                   print("Code : Language")
                   for i in language.items():
                      print(f"{i[0]} => {i[1]}")
                   print()

  else:       # validating user input
                   for lan_code in language.keys():
                      if lan_code == user_input:
                          print(f"You have selected : {language[lan_code]}")
                          allow = False
                   if allow:
                      print("It is not a valid language code")

while True:       # starting translation loop
  string_input=input(f"\nWrite the text you want to translate: \nTo exit the program write : 'close'\n")
  if string_input=='close':     # exit program command
    print('Thank you for using the translator \nHave a nice day')
    break

        # translating method from googletrans
  translated = translator.translate(string_input, dest=user_input)

        # printing translation
  print(f'\n{language[user_input]} translation : {translated.text}' )

        # printing pronunciation
  print(f'Pronunciation : {translated.pronunciation}')

  for i in language.items():      # checking if the source language is listed on language dict and printing it
    if translated.src==i[0]:
      print(f'Translated from : {i[1]}')