# write your code here
class Hcalc:
    memory = 0.0
    msg_0 = 'Enter an equation'
    msg_1 = 'Do you even know what numbers are? Stay focused!'
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = 'Yeah... division by zero. Smart move...'
    msg_4 = 'Do you want to store the result? (y / n):'
    msg_5 = 'Do you want to continue calculations? (y / n):'
    msg_6 = ' ... lazy'
    msg_7 = ' ... very lazy'
    msg_8 = ' ... very, very lazy'
    msg_9 = 'You are'
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
    operations = {"+": lambda x, y: x + y,
                  "-": lambda x, y: x - y,
                  "*": lambda x, y: x * y,
                  "/": lambda x, y: x / y
                  }

    def __init__(self, x, operator, y):
        self.x = x
        self.operator = operator
        self.y = y

    def check(self):
        if self.x == 'M':
            self.x = self.memory
        if self.y == 'M':
            self.y = self.memory
        try:
            float(self.x)
            float(self.y)
            return False
        except ValueError:
            print(Hcalc.msg_1)
            return True
        finally:
            if self.operator not in Hcalc.operations:
                print(Hcalc.msg_2)
                return True

    @staticmethod
    def is_one_digit(temp):
        #  print(temp)
        return True if -10 < temp < 10 and temp.is_integer() else False

    def message(self):
        msg = ''
        if (Hcalc.is_one_digit(self.x) and Hcalc.is_one_digit(self.y)) is True:
            #  print(Hcalc.is_one_digit(self.x), Hcalc.is_one_digit(self.y))
            msg = Hcalc.msg_6
        if (self.x == 1 or self.y == 1) and self.operator == '*':
            msg = msg + Hcalc.msg_7
        if (self.x == 0 or self.y == 0) and self.operator in ("+", "-", "*"):
            msg = msg + Hcalc.msg_8
        if Hcalc.msg_9 + msg == 'You are':
            pass
        else:
            print(Hcalc.msg_9 + msg)

    def tease(self):
        if Hcalc.is_one_digit(Hcalc.operations[self.operator](self.x, self.y)) is True:
            if input(Hcalc.msg_10) == 'y':
                if input(Hcalc.msg_11) == 'y':
                    if input(Hcalc.msg_12) == 'y':
                        Hcalc.memory = Hcalc.operations[self.operator](self.x, self.y)
                        #  print(Hcalc.memory, 'store1')
                        cont = input(Hcalc.msg_5)
                        if cont == 'y':
                            return True
                        #  return True
                    else:
                        cont = input(Hcalc.msg_5)
                        if cont == 'y':
                            return True
                        else:
                            return False
                else:
                    cont = input(Hcalc.msg_5)
                    if cont == 'y':
                        return True
                    else:
                        return False
            else:
                cont = input(Hcalc.msg_5)
                if cont == 'y':
                    return True
                else:
                    return False
        else:
            Hcalc.memory = Hcalc.operations[self.operator](self.x, self.y)
            #  print(Hcalc.memory, 'store2')
            cont = input(Hcalc.msg_5)
            if cont == 'y':
                return True
            else:
                return False

    def store_continue(self):
        store = input(Hcalc.msg_4)
        if store == 'y':
            if Hcalc.tease(self) is True:
                return True
        #      Hcalc.memory = Hcalc.operations[self.operator](self.x, self.y)
        #      cont = input(Hcalc.msg_5)
        #      if cont == 'y':
        #          return True
        #      else:
        #          return False
        if store == 'n':
            cont = input(Hcalc.msg_5)
            if cont == 'y':
                return True
            else:
                return False

    def control_func(self):
        if Hcalc.check(self) is True:
            return True

        self.x = float(self.x)
        self.y = float(self.y)
        Hcalc.message(self)

        if self.operator in ["+", "-", "*", "/"]:
            if self.operator == "/" and self.y == 0:
                print(Hcalc.msg_3)
                return True
            else:
                print(Hcalc.operations[self.operator](self.x, self.y))

        if Hcalc.store_continue(self) is True:
            return True


z = True
while z is True:
    x_, operator_, y_ = input('Enter an equation').split()
    calc = Hcalc(x=x_, operator=operator_, y=y_)
    z = calc.control_func()
