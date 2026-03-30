class Node:
    def __init__(self) -> None:
        self.nodes = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
                
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Node()
            curr = curr.nodes[c]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        if curr.end == True:
            return True
        
        return False
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True
        