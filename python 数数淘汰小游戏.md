n = int(input("请输入"))
m = int(input("数到几淘汰"))
t = m-1
man = [i for i in range (1,n+1)]
def move(man, sep):
    
    for i in range(sep):
        item = man.pop(0)
        man.append(item)
while len(man) > 2:
    move(man, t)
    man.pop(0)
    
man    
