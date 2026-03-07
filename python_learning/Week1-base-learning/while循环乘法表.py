#while循环===9*9乘法表
#外层循环
i = 1
while i <= 9:
#内层循环
    j = 1
    while j <= i:
        #内层循环，print不要换行，添加制表符\t
        print(f"{j}*{i} = {j * i}\t",end='')
        j += 1
    i +=1
    print() #输出一个空换行

