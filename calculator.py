class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b > 0:
            for i in range(b):
                result = self.add(result, a)
            return result
        if b < 0:
            b = abs(b)
            for i in range(b):
                result = self.add(result, a)
            return -result

    def divide(self, a, b):
        result = 0
        if b == 0 :
            return "หารไม่ได้"
        elif a > 0 and b < 0:
            b = abs(b)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        elif a < 0 and b > 0:
            a = abs(a)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        elif a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        elif b == 0 :
            return "หารไม่ได้"
        elif a >= b:
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        
    
    def modulo(self, a, b):
        if b == 0:
            return "modไม่ได้"
        if a < 0:
            a = abs(a)
            if b > 0:
                while a >= b:
                    a = a-b
            elif b < 0:
                b = abs(b)
                while a >= b:
                    a = a-b
        if a > 0 :
            if b > 0:
                while a >= b:
                    a = a-b
            elif b < 0:
                b = abs(b)
                while a >= b:
                    a = a-b
        
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    #print("Example: addition: ", calc.add(1, 2))
    #print("Example: subtraction: ", calc.subtract(4, 2))
    #print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(3, 0))
    #print("Example: modulo: ", calc.modulo(-5, 5))