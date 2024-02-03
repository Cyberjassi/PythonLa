class E:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"You are name is {self.name}")
class D:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"You are dance is {self.dance}")
class Ed(D,E):
    def __init__(self,name,dance):
       D.__init__(self,dance)
       E.__init__(self,name)
    # def show(self):
    #     print(f"You are name is {self.dance} and your dance is {self.dance}")

m = Ed('jay','kathak')
m.show()


