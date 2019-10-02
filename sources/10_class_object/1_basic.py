class MyFirstClass:
    variable = "variable class"

    def funcname(self):
        print("Accessing function")
        pass
    pass

myobjectz = MyFirstClass()
myobjectq = MyFirstClass()

myobjectz.variable = "update variable"

print(myobjectz.variable)
print(myobjectq.variable)

myobjectq.funcname()
myobjectz.funcname()