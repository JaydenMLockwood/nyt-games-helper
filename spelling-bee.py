import json

with open("words_dictionary.json", "r", encoding="utf-8") as file:
    data = json.load(file)

word_list = set(data)

def filter_words(allowed_letters, hero_letter):
    allowed_set = set(allowed_letters) 
    return [word for word in word_list if set(word).issubset(allowed_set) and hero_letter in word and len(word) > 3]

allowed_letters = input("Enter allowed letters: ").strip().lower() 
hero_letter = input("Enter the hero letter: ").strip().lower()  

confirmed_words = filter_words(allowed_letters,hero_letter)

print(confirmed_words)



