class Trie:
    
    class TrieNode(object):
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = self.TrieNode()
                node.children[char] = new_node
                node = new_node
                
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)