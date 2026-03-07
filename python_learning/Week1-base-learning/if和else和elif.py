#通过键盘输入数字来进行猜想，使用了if和elif结合进行比较
num = 10
if int(input("请输入第一次猜想的数字:")) >= num:
    print("恭喜第一次就猜对了！！！")
elif int(input("不对，再猜一次：")) >= num:
    print("猜对了")
elif int(input("不对，猜最后一次：")) >= num:
    print("恭喜终于在最后猜对了")
else:
    print("sorry,全部猜错了，我想的是：10")


