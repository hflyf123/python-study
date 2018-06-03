#方法的重写
class parent:
    def myMethod(self):
        print("使用父类方法")
    

class child(parent):
    def myMethod(self):
        print("使用子类方法")

c = child()
c.myMethod()
super(child,c).myMethod()
#子类重写父类方法，并调用
#子类使用父类方法