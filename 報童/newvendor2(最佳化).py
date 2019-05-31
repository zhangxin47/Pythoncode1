while 1:
	c=int(input("成本:")) #成本
	r=int(input("售價:")) #售價
	if (r > c and  1<=c<=100):
		break
	else :
		continue
N=int(input("需求函數個數:")) #需求函數個數 x0~x8 固定
# q=int(input("訂貨數量:"))
num_list=[] #空的

for i in range(0,9):
	print("第", i, "個", end="")
	prob=float(input("需求機率:"))
	num_list.append(prob)
	# x0=float(input("i=0機率:") 
	# x1=float(input("i=1機率:") 
	# x2=float(input("i=2機率:") 
	# x3=float(input("i=3機率:") 
	# x4=float(input("i=4機率:") 
	# x5=float(input("i=5機率:") 
	# x6=float(input("i=6機率:") 
	# x7=float(input("i=7機率:") 
	# x8=float(input("i=8機率:")
print(num_list)
j=0	#內圈計數器
k=0 #外圈計數器
#因我們知道N=8，因此不必再多宣告變數
profit=0.0 #利潤
prob=0.0 #機率
maxprofit=-99 #最佳利潤 讓程式去更新
maxq=0 #最佳訂購數量
for k in range (0,N+1):
	profit=0.0  #歸零
	prob=0.0	#歸零
	for j in range( 0 , k+1):

		if (j == k):
			for j in range(0 , k):
				prob=prob+num_list[j] #算機率
			profit=profit+(1-prob) * ((r*k)+(-c*k)) #期望利潤最後一項(X個以上會賣完的機率)
			print()
		else:
			profit= profit+num_list[j] * ((r*j)+(-c*k)) #期望利潤=機率*利潤(買X個會賣完的機率)
	print("購買",k,"個的期望利潤為:",profit)
	if(maxprofit < profit):  #最佳解有更新要更新
		maxprofit=profit
		maxq=k

maxprofit=int(maxprofit)
print("最佳期望數量:", maxq, "\n期望利潤為: ", maxprofit)
