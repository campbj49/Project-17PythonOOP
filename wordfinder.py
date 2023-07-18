"""Word Finder: finds random words from a dictionary."""

from random import random
class WordFinder:
    def __init__(self, path):
        raw_file = open(path)
        num_words = 0
        self.word_list = []
        for line in raw_file:
            num_words+=1
            self.word_list += [line.strip()]
        raw_file.close()
        print (f"{num_words} words read")
        
    def random(self):
        return self.word_list[int(random() * len(self.word_list))]
        
        
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        current_category = "#header"
        self.categories = {current_category:[]}
        
        num_cat = 0
        for word in self.word_list:
            if(str(word)[0] =="#"):
                current_category = word
                self.categories[current_category] = []
                num_cat += 1
            else: self.categories[current_category] += [word]
        
        print (f"{num_cat} categories read")    
        
    def random_within_category(self, category):
        self.word_list = self.categories[category]
        return self.random()
demoFinder = SpecialWordFinder("words.txt")
print(demoFinder.random())
print(demoFinder.random())

print(demoFinder.random_within_category("#thirdThird"))
print(demoFinder.random_within_category("#thirdThird"))
print(demoFinder.random_within_category("#thirdThird"))
