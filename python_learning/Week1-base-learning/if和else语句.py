#假设年龄大于30岁，18岁就成年
age = 30
if age >= 18:
    print("我已经成年了")
    print("我已经")

#练习案例
print("欢迎来到游乐园，儿童免费，成人需要收费.")
age = input("请输入您的年龄：")
if int(age) >= 18:
    print(f"您以成年，游玩需要补票：10元")
else:
    print("您未成年,可以免费游玩！")
    print("祝您玩得愉快！！")

#if else结合案例分析
print("欢迎来到黑马动物园")
stature = float(input("请输入您的身高(cm):"))
if stature >= 120:
    print(f"您的身高超过120cm,游玩需要买票10元")
else:
    print("您的身高未达到120，可以免费游玩！")
print("祝您玩的开心！！！！")