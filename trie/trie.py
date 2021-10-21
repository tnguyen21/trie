""" trie/trie.py

File which holds the Trie class and associated
algorithms.
"""
from .trienode import TrieNode
from utils.string_utils import string_preprocess


class Trie:
    def __init__(
        self,
        root: TrieNode = TrieNode(""),
        entry_list: [str] = [],
    ):
        self.root = root
        self.entry_list = entry_list  # think about removing this
        self.max_current_search_level = 0

    def dump(self):
        """
        Print trie into a formatted string
        """
        self.root.dump()

    def add_entry(self, word):
        """
        Insert a word into the trie

        Args:
            word: the word to be inserted
        """
        # add to entry list, check for duplicates
        if word in entry_list:
            self.entry_list.append(word)

        # return last node added (pointer to last node)
        # TODO we want to connect this last node to entry list
        end_node = self.root.add_entry(word)

    def dfs(self, node, prefix):
        """
        Depth-first traversal of the trie

        Args:
            node: the node to start with
            prefix: the current prefix, for tracing a
                    word while traversing the trie
        """
        if node.is_end_of_word:
            self.output.append((prefix + node.char, node.node_level))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """
        Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def similarity_search(self, prefix: str, max_edit_distance: int) -> [str]:
        """
        Given a prefix, conduct a similarity search on the trie using the
        notion of an "edit distance" and keeping track of how edit distance
        changes as we traverse the trie.

        Args:
            prefix: the prefix to search for

        Returns:
            A list of words in the trie that are within the edit distance
            of the prefix
        """
        # init lists of active nodes
        # only valid for edit distance = 2, we want to dynamically generate these lists depending on max_edit_distance
        # suggestion: use a dictionary and dynamically populate it given max_edit_distance
        # nodes in this dictionary are considerd "active"
        # these nodes have to access to dicionry to know whether they are active or not
        # prefer to store tree pointer in each node
        # structure needs to be property in tree that is accessible in each node
        _level_zero_nodes = [self.root]
        _level_one_nodes = [self.root.children]
        _level_two_nodes = [
            self.root.children[child].children for child in self.root.children
        ]
        # think of nodes having responsibility to add/remove themselves to active nodes
        # edit distance is only valid when it's in active nodes -- otherwise we need to do something to make sure it has an accurate value when it gets added/removed from active nodes

        print(_level_zero_nodes)
        print(_level_one_nodes)
        print(_level_two_nodes)
