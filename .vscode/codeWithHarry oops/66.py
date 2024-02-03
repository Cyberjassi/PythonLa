class Emp:
    size = 0
    company = 'Apple'
    
    def __init__(self,name):
        self.name = name
        Emp.size += 1
        
    def show_de(self):
        print(f"You name is {self.name} and company name is {self.company}")
        print(f"Company size is {self.size}")

e = Emp('jay')
e.company = 'gfg'
e.show_de()
e1 = Emp('veer')
e1.show_de()
e2 = Emp('df')
e2.show_de()