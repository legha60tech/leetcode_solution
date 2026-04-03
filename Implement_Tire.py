class Tire:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True
    def search(self, word):
        node = self._traverse(word)
        return node is not None and "#" in node
    def startsWith(self, prefix):
        return self._traverse(prefix) is not None
    def _traverse(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return None
            node = node[char]
        return node
if __name__ ==  "__main__":
    tire = Tire()
    tire.insert("apple")
    print(tire.search("apple"))
    print(tire.search("app"))
    print(tire.startsWith("app"))
    tire.insert("app")
    print(tire.search("app"))
        
