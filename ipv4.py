from number import Number

class IPv4:
    def __init__(self, number):
        try:
            test = number.split("/")
            print(test)
            self.cidr = int(number.split("/")[1])
            lst_number = number.split("/")[0].split(".")
            self.number = 0
            print(lst_number)
            for oktet in lst_number:
                self.number *= 256
                self.number += int(oktet) 
        except :
            self.number = -1    
            self.cidr = -1
        finally:
            pass