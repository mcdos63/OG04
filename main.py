def func(*args):
    res="Салют"
    for i,v in enumerate(args):
        if i==len(args)-1:
            res+=f" и {v}!"
        else:
            res+=f", {v}"
    return res

print(func("Коля","Вася","Петя"))