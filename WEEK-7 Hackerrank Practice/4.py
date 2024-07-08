class TextEditor:

    def __init__(self):
        self.left = []
        self.right = deque([])
        
    def addText(self, text: str) -> None:
        self.left.append(text)
        
    def deleteText(self, k: int) -> int:
        total = 0
        while k:
            if not self.left:
                break
            s = self.left.pop()
            if len(s) > k:
                s = s[:-k]
                self.left.append(s)
                total +=k
                break
            k -= len(s)
            total += len(s)
        return total

    def cursorLeft(self, k: int) -> str:
        total = 0
        while k:
            if not self.left:
                break
            s = self.left.pop()
            if len(s) > k:
                self.left.append(s[:-k])
                self.right.appendleft(s[-k:])
                break
            self.right.appendleft(s)
            k -= len(s)
        return self.get()
        

    def cursorRight(self, k: int) -> str:
        total = 0
        while k:
            if not self.right:
                break
            s = self.right.popleft()
            if len(s) > k:
                self.left.append(s[:k])
                self.right.appendleft(s[k:])
                break
            self.left.append(s)
            k -= len(s)
        return self.get()
    
    def get(self):
        ans = ''
        i = len(self.left) - 1
        while i >= 0 and len(ans) < 10:
            ans = self.left[i] + ans
            i -= 1
        return ans[-10:]