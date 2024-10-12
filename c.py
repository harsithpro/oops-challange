class a:
    def __init__(self,a):
        self.a=a
    def __it__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
ob1=a(1234567890)
ob2=a(12345678901234567890)
print(ob1.a,ob2.a)
