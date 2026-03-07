#字符串格式化-表达式格式化
name = "马上好公司"
stock_price = 16.66
stock_code = "00003"
stock_price_daily_growth_factor = 2.2
growth_days = 8
finally_stock_prince = stock_price * growth_days **stock_price_daily_growth_factor
print(f"公司:{name},股票代码是：{stock_price},当前股价是：{stock_price}")
print("每日增长系数是：%f,经过了%d的增长,股票的最终价格是%.2f "%(stock_price_daily_growth_factor,growth_days,finally_stock_prince))

#input(语句函数)
print("你在干什么啊？")
ab = input
print("没干什么啊,我在：%s" %(ab))
