from number import Number

class IPv4:
    def __init__(self, number):
        try:
            self.cidr = int(number.split("/")[1])
            lst_number = number.split("/")[0].split(".")
            self.number = 0
            for oktet in lst_number:
                self.number *= 256
                self.number += int(oktet) 
        except :
            self.number = -1    
            self.cidr = -1

    def __str__(self):
        pass

    def get_str(self, diff = 0):
        answer = ""
        counter = self.number + diff
        for i in range(4):
            answer = str(counter%256) + "." + answer
            counter //= 256
        return f"{answer[:-1]}/{self.cidr}"
        
    def get_mask(self):
        numbers = ["0", "128", "192", "224", "240", "248", "252", "254", "255"]
        answer = ""
        counter = self.cidr
        for i in range(4):
            if counter >= 8:
                answer = answer + "." + "255"
            elif counter == 0:
                answer = answer + "." + "0"
            else:
                answer = answer + "." + numbers[counter]
            if counter >=8:
                counter -= 8
            else:    
                counter = 0
        return answer[1:]
    