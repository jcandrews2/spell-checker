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
        self.user_words = passage.split()

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
    print(spell_check.check_words())
