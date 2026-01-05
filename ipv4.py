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
    
    def get_nid(self):
        lst_ip = self.get_str().split("/")[0].split(".")
        lst_mask = self.get_mask().split(".")
        lst_nid = []
        for i in range(4):
            lst_nid.append(int(lst_ip[i]) & int(lst_mask[i]))
        return f"{lst_nid[0]}.{lst_nid[1]}.{lst_nid[2]}.{lst_nid[3]}"
        
    def get_bc(self):
        lst_ip = self.get_str().split("/")[0].split(".")
        lst_mask = self.get_mask().split(".")
        lst_bc = []
        for i in range(4):
            lst_bc.append(256+(int(lst_ip[i]) | ~int(lst_mask[i])))
        return f"{lst_bc[0]}.{lst_bc[1]}.{lst_bc[2]}.{lst_bc[3]}"
