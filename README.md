# Jimmy & August

Spell checker using the levenshtein algorithm
How to run:
1. run bk_tree.py
2. enter a passage when prompted (preferrably with misspelled words)

Experiment: 
The experiment tests and graphs the comparison count versus the size of the bk tree from the search method.     
The worst case scenario for the search method is whatever word is within one edit distance of the most words in the tree.
For the experiment we choose to search for words similar to 'a'.    
         
bk_tree.py: contains logic for the bk tree and main method.     
bktree.pickles: saved version of the completed bk trees.    
word_bank.txt: word bank of 10,000 popular english words to be checked by levenshtein.     
spell_check.py: checks the input words against the dictionary and returns a list of misspelled words.     
levenshtein.py: contatins the logic to run the levenshtein algorithm on two input words. Returns a similarity score.     
levenshteinWithComps.ipynb: file demonstrating the runtime of the levenshtein algorithm when applied to different lengths of words.    


