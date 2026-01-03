import random

class Number():
    def __init__(self, number=-1, zsystem = "d"):
        if zsystem == "d":
            # decimal
            if number == -1:
                self.number = self.set_rnd()
            else:
                self.number = number
        elif zsystem == "b":
            # binär
            self.set_bin(number)
        elif zsystem == "h":
            # hexadezimal
            self.set_hex(number)

    def set_bin(self, nstring):
        zahl = 0
        for ziffer in nstring:
            if ziffer in "1Ii":
                zahl *= 2
                zahl += 1
            elif ziffer == "0":
                zahl *= 2
        self.number = zahl

    def set_rnd(self, max_number=-1):
        if max_number == -1:
            max_number = 255
        return random.randint(0, max_number)
    
    def get_dec(self):
        return self.number
    
    def get_bin(self, len_answer=8, sign="1"):
        answer = ""
        loc_number = self.number
        while loc_number > 0:
            x = loc_number % 2
            if x == 0:
                answer = "0" + answer
            else:
                answer = sign + answer
            loc_number //= 2
        if len(answer) < len_answer:
            # Links mut Nullen auffüllen
            answer = "0"*(len_answer-len(answer))+answer 
        return answer
    
    def get_hex(self):
        letters = "0123456789ABCDEF"
        answer = letters[self.number//16]
        answer += str(letters[self.number%16])
        return answer

    def get_number(self):
        return self.number
    
    def __str__(self):
        return str(self.number)
    

    
         