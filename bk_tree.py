import pickle
import networkx as nx

from spell_check import SpellCheck
from levenshtein import levenshtein


class Node():
    def __init__(self, value):
        self.value = value
        self.children = {}


class BKTree():
    def __init__(self):
        self.root = None
        self.gr = nx.Graph()

    # Inserts word into correct location in tree
    def insert(self, current_node, to_insert):
        # If the root is none, make a root
        if current_node is None:
            self.root = Node(to_insert)
            return self.root

        distance = levenshtein(current_node.value, to_insert)

        if distance == 0:
            return current_node

        # If a child node had the same distance, then go to that node and insert as a child
        # Else insert into current_node's children
        if distance in current_node.children:
            self.insert(current_node.children[distance], to_insert)
        else:
            new_node = Node(to_insert)
            current_node.children[distance] = new_node
            self.gr.add_edge(current_node, new_node)
            
        return current_node

    # Gets a list of nodes close to current_node within the search distance
    def search(self, current_node, search_word, max_distance):
        to_return = []
        distance = levenshtein(current_node.value, search_word)

        if distance <= max_distance:
            to_return.append(current_node.value)

        low_bound = distance - max_distance
        high_bound = distance + max_distance
        for key in current_node.children.keys():
            if key >= low_bound and key <= high_bound:
                to_return.extend(self.search(
                    current_node.children[key], search_word, max_distance))

        return to_return

    # Prints all the values of the children of given node
    def print_children(self, current_node):
        children = current_node.children.values()
        for child in children:
            print(child.value)


if __name__ == "__main__":
    # Testing
    spell_check = SpellCheck()
    spell_check.read_file()
    tree = BKTree()

    '''
    progress_bar = 0
    print("Loading BK tree...")
    for dict_word in spell_check.english_dict.values():
        if len(dict_word) < 8:
            tree.insert(tree.root, dict_word)
            print(progress_bar, "out of 9558")
            progress_bar += 1
        else:
            print(progress_bar, "out of 9558")
            progress_bar += 1
       
    pickle.dump(tree.gr, open('bktree.pickle', 'wb'))
    '''

    tree.gr = pickle.load(open('bktree.pickle', 'rb'))
    loaded_tree = list(tree.gr.nodes)
  
    spell_check.get_user_input()
    words = spell_check.check_words()
    for word in words:
        print("Misspelled word:\n", word)
        print("Similar words:\n", tree.search(loaded_tree[0], word, 1))
            
