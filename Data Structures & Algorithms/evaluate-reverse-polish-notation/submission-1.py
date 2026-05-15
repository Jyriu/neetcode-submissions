class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())

            elif t == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a - b))

            elif t == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif t == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a / b)))
            
            else:
                stack.append(int(t))
            
        return int(stack[0])