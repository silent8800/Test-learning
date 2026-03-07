#定义一个新的数字变量

import random
num = random.randint(1,10)
guess_num = int(input("请输入你要猜测的数字："))
#if语句嵌套进行判断
if guess_num == num:
    print("恭喜，第一次就猜对了")
else:
    if guess_num > num:
        print("不好意思，你猜大了")
    else:
        print("不好意思，你猜小了")
    guess_num = int(input("请再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")
        guess_num = int(input("第三次输入你要猜测的数字："))
        if guess_num == num:
            print("恭喜，第三次就猜中了")
        else:
            print("三次机会都用完了还是没有猜中！！！")


