class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        self.top = 0
        self.front = 0

    def pushCharacter(self, c):
        self.stack.append(c)

    def enqueueCharacter(self, c):
        self.queue.append(c)

    def popCharacter(self):
        if self.top > -1:
            self.top = len(self.stack) - 1
            c = self.stack[self.top]
            del self.stack[self.top]
            return c

    def dequeueCharacter(self):
        c = self.queue[self.front]
        del self.queue[self.front]
        return c


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
