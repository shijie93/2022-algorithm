class Node:
    def __init__(self, val=None, childrent=None):
        self.val = val
        self.isEnd = False
        if not childrent:
            self.childrent = []

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            for child in cur.childrent:
                if child.val == i:
                    cur = child
                    break
            else:
                newNode = Node(i)
                cur.childrent.append(newNode)
                cur = newNode
        else:
            cur.isEnd = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            for child in cur.childrent:
                if child.val == i:
                    cur = child
                    break
            else:
                return False
        if cur.isEnd:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            for child in cur.childrent:
                if child.val == i:
                    cur = child
                    break
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)