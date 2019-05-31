a=int() #花的錢
a=int(input())
if 1<=a<=1000 : 
	print("pass") 
	payback=int(1000-a)
	num500=int(payback//500) #500張數
	num100=int((payback-500*num500)//100) #100張數
	num50=int((payback-500*num500-100*num100)//50) #50張數
	num10=int((payback-500*num500-100*num100-num50*50)//10) #10元張數
	num5=int((payback-500*num500-100*num100-num50*50-10*num10)//5) #5元張數
	num1=int((payback-500*num500-100*num100-num50*50-10*num10-5*num5)//1) #1元張數
	print(num500,num100,num50,num10,num5,num1)
else: print("輸入錯誤，請重新輸入")
