#salesStr=input("輸入Sales:")
salesStr = "14, 23 , 26, 17 ,17 , 12, 24, 19 ,10 , 18, 22, 31 , 19, 16, 22, 28, 20, 27, 20 ,32"
sales = salesStr.split(",")

#把字串改成INT
for i in range(len(sales)):
	sales[i]=int(sales[i])

Q = 30 #訂購數量
I = 20 #期初存貨
invcost = 1000 * 0.073 / 365 #存貨成本
stgcost = 2 #缺貨成本
optimalcost = 9999999 #先選大數值後來會更新
optimalR = 0 #最佳訂購點

for R in range(Q+1):
	totalstgcost=0 #歸零
	totalinvcost=0 #歸零
	totalcost = 0  #歸零
	
	for s in sales: #sales經我們處理過 可依序叫出
		I = I - s
		
		if I < 0 : #存貨不夠
			totalstgcost += -I * stgcost
			I = I + Q
			
		elif I < R:  #存貨量低於訂購點
			I= I + Q
			
		totalinvcost += I * invcost #及時補貨 忽略運輸時間
		
	totalcost = totalinvcost + totalstgcost # sales list跑完計算全部成本
	print("R:" , R ,"totalinvcost:", totalinvcost, "totalstgcost:" , totalstgcost, "totalcost:", totalcost)
	
	if totalcost < optimalcost:
		optimalcost = totalcost
		optimalR = R
print("optimalcost:" , optimalcost , "optimalR:" , optimalR) 
	
		
			
		
			
