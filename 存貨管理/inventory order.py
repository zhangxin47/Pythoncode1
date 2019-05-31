#continuous order system
Q = int(input("訂貨數:"))
R = int(input("再訂購點:"))
I = int(input("現有存貨:"))


while True:
	sales=int(input("今日銷售數量:"))
	if I-sales >=0 :
		I = I - sales
	else :
		I = 0
	if I < R :
		print("訂購!!")
		I = I + Q
	print("現有存貨:", I)
		