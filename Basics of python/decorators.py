def func(func1):

    def func3():
        print("Ansh is a good boy")
        func1()
        print("Ansh is also an inncoent boy !!")
    return func3
@func
# if we do not want to use line num 8 then we have to use line 13
def func4():
    print("----------")

# func4 = func(func4)
func4()
