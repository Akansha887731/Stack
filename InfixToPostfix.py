"""
Infix expression: The expression of the form “a operator b” (a + b) i.e., when an operator is in-between every pair of operands.
Postfix expression: The expression of the form “a b operator” (ab+) i.e., When every pair of operands is followed by an operator.
"""

class Conversion:
    def __init__(self, capacity):
        self.top =-1
        self.capacity = capacity

        self.stack = []
        self.postfix = []
        
        self.precedence_map = {"+" : 1, "-": 1, "*": 2, "/":2, "^": 3}

    def push(self, element):
        if len(self.stack) >= self.capacity:
            print("Stack overflow.")
            return -1
        self.top += 1
        self.stack.append(element)

    def isEmpty(self):
        return True if self.top == -1 else False

    def pop(self):
        if self.isEmpty():
            print("Stack underflow.")
            return "$"
        self.top -= 1
        return self.stack.pop()

    def islessprecedence(self, value):
        try :
            if self.precedence_map.get(value) <= self.precedence_map.get(self.stack[self.top]):
                return True
            else:
                False
        except Exception as e:
            print(e)
            return False

    def infixToPostfix(self, expression):
        for value in expression:
            if value.isalpha():
                self.postfix.append(value)
            elif value == "(":
                self.push(value)
            elif value == ")":
                while not self.isEmpty() and self.stack[self.top] != "(":
                    self.postfix.append(self.pop())
                    
                if  not self.isEmpty() and self.stack[self.top] != "(":
                    print("No Opening paranthesis encountered.")
                    return -1
                self.pop()
            else:
                while not self.isEmpty() and self.islessprecedence(value):
                    self.postfix.append(self.pop())
                self.push(value)
            print(f"value = {value}, postfix = {self.postfix}, stack = {self.stack}, top = {self.top}")
        while not self.isEmpty():
            self.postfix.append(self.pop())
            
        self.traverse()

    def traverse(self):
        for i in self.postfix:
            print(i, end="")

expression = "a+b*(c^d-e)^(f+g*h)-i"
object = Conversion(100)
object.infixToPostfix(expression)


"""
Output :-
value = a, postfix = ['a'], stack = [], top = -1
value = +, postfix = ['a'], stack = ['+'], top = 0
value = b, postfix = ['a', 'b'], stack = ['+'], top = 0
value = *, postfix = ['a', 'b'], stack = ['+', '*'], top = 1
value = (, postfix = ['a', 'b'], stack = ['+', '*', '('], top = 2
value = c, postfix = ['a', 'b', 'c'], stack = ['+', '*', '('], top = 2
'<=' not supported between instances of 'int' and 'NoneType'
value = ^, postfix = ['a', 'b', 'c'], stack = ['+', '*', '(', '^'], top = 3
value = d, postfix = ['a', 'b', 'c', 'd'], stack = ['+', '*', '(', '^'], top = 3
'<=' not supported between instances of 'int' and 'NoneType'
value = -, postfix = ['a', 'b', 'c', 'd', '^'], stack = ['+', '*', '(', '-'], top = 3
value = e, postfix = ['a', 'b', 'c', 'd', '^', 'e'], stack = ['+', '*', '(', '-'], top = 3
value = ), postfix = ['a', 'b', 'c', 'd', '^', 'e', '-'], stack = ['+', '*'], top = 1
value = ^, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-'], stack = ['+', '*', '^'], top = 2
value = (, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-'], stack = ['+', '*', '^', '('], top = 3
value = f, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f'], stack = ['+', '*', '^', '('], top = 3
'<=' not supported between instances of 'int' and 'NoneType'
value = +, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f'], stack = ['+', '*', '^', '(', '+'], top = 4
value = g, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g'], stack = ['+', '*', '^', '(', '+'], top = 4
value = *, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g'], stack = ['+', '*', '^', '(', '+', '*'], top = 5
value = h, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h'], stack = ['+', '*', '^', '(', '+', '*'], top = 5
value = ), postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+'], stack = ['+', '*', '^'], top = 2
value = -, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+', '^', '*', '+'], stack = ['-'], top = 0
value = i, postfix = ['a', 'b', 'c', 'd', '^', 'e', '-', 'f', 'g', 'h', '*', '+', '^', '*', '+', 'i'], stack = ['-'], top = 0

Final postfix notation = abcd^e-fgh*+^*+i-
"""
