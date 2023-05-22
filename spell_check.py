from levenshtein import levenshtein

class SpellCheck():
    def __init__(self):
        self.english_dict = {}
        self.user_words = []

    # Reads the txt file and inserts words into hashmap
    def read_file(self):
        file = open("google-10000-english-no-swears.txt", "r")
        lines = file.readlines()

        key = 0
        for line in lines:
            self.english_dict[key] = line.strip("\n")
            key += 1

    # Gets a passage from the user and takes each individual work into a list
    def get_user_input(self):
        passage = input("Enter a passage:\n")
        passage1=passage.lower()
        self.user_words = passage1.split()

    # Checks all words in the passage against the dictionary and returns words that do not exist
    def check_words(self):
        invalid_words = []
        english_dict_values = self.english_dict.values()
        for word in self.user_words:
            if word not in english_dict_values:
                invalid_words.append(word)
        return invalid_words


# Testing functions
if __name__ == "__main__":
    spell_check = SpellCheck()
    spell_check.read_file()
    spell_check.get_user_input()
    words=spell_check.check_words()
    for i in range(len(words)):
        mostSimilarScore=1000
        mostSimilarWord=None
        curWord=words[i]
        for j in range(len(spell_check.english_dict)):
            if abs(len(curWord)-len(spell_check.english_dict[j]))<2:
                similarEnough=False
                if len(curWord)<3:
                    similarEnough=True
                else:
                    similarityScore=0
                    for letter in curWord:
                        if letter in spell_check.english_dict[j]:
                            similarityScore+=1
                    if (len(curWord)-similarityScore)<3:
                            similarEnough=True
                if similarEnough==True:        
                    curComp=levenshtein(curWord, spell_check.english_dict[j])
                    if curComp<mostSimilarScore:
                        mostSimilarScore=curComp
                        mostSimilarWord= spell_check.english_dict[j]
        if mostSimilarWord!=None:
                print(mostSimilarWord, mostSimilarScore)
    print("done")
            
                
        
