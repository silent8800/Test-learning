

name = '\"哈喽\"'
print(type(name))

str_tab = '哈哈哈毒啊回电话'+'333'
tab2 = '"22"' + """777"""
print(str_tab)


kb = "很好"
int_money = 999
avg_num = 9.888888
message = ("你说的：%s吗, 总共花了：%d吧,还有平均:%f " %(kb, int_money, avg_num))

print(message)


#重新开始
num = 0.6455
print("数字11宽度限制,结果是：%4.2f " %(num))

num1 = 11.226
print("数字无宽度限制，小数精度2,结果是：%.3f " % (num1))

#带f的字符格式化

name = "嘤嘤嘤"
stu_year = 2020
cost_price = 88.22
print(f"我的名字：{name},然后我是：{stu_year}出生的,花费了{cost_price}")

#字符串格式化-表达式格式化
name = "马上好公司"
stock_price = 16.66
stock_code = 1222
stock_price_daily_growth_factor = 2.2
growth_days = 8
print(f"公司是{name},股票代码是：{stock_price},当前股价是：{stock_price}")
print("每日增长系数是：%f,经过了%d的增长,股价达到了：" % (stock_price, stock_code,growth_days))



