# *agrs = args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple.
# **kwargs = **kwargs it passes the data as a dictonary

def fun(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


normal = "Hey normal"
aa = ["ansh","pratik","prakhar"]
bb={"ansh":"monitor","pratik":"cpu","prakhar":"mouse"}
fun(normal,*aa,**bb)
