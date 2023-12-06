"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def __init__(self):
        self.top = -1
        self.stack = []
        self.brackets = {"(" : ")", "[": "]", "{": "}"}

    def isEmpty(self):
        return True if self.top == -1 else False
    
    def pop(self):
        if self.isEmpty():
            return -1
        self.top -= 1
        return self.stack.pop()

    def push(self, value):
        self.top += 1
        self.stack.append(value)

    def isValid(self, s: str) -> bool:       
        for char in s:
            
            if char in self.brackets.keys():
                self.push(char)
                isValid = False
            else:
                if not self.isEmpty() and char == self.brackets.get(self.pop()):
                    continue
                else:
                    return False
        return self.isEmpty()
