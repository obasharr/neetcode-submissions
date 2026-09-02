class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                b = stack.pop()
                a = stack.pop()
                result = self.applyOperator(token, a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()

    def applyOperator(self, token: str, a: int, b: int) -> int:
        if token == "+":
            return a + b
        if token == "-":
            return a - b
        if token == "*":
            return a * b
        if token == "/":
            return int(a / b)


        