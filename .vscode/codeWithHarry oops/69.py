class E:
    comapny = 'Apple'

    def show(self,name):
        print(f"Your name is {name} and Your company is {self.comapny}")

    @classmethod
    def change(cls,newcompany):
        cls.comapny = newcompany
e = E()
e.show('jay')
e.change('google')
print(e.comapny)