class conputer:
        def __init__(self,cpu,ram):
            self.cpu=cpu
            self.ram=ram
        def config(self):
            print("my computer RAM is: {} {}".format(self.ram,self.cpu))
com1=conputer('i5',"64GB")
conputer.config(com1)
com1.config()