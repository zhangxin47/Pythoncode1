a = int()
"""
while not (1 <= a <= 999) : #不直觀哦! 不建議
	a=int(input())
	print("輸入值不落在1~999區間")
print(a)
"""
#比較直觀 可讀性高
while 1:
	a = int( input())
	if (1 <= a <= 999):
		break
	else:
		print("輸入值不落在1~999區間")
		continue


payback=int(1000-a)
num500=int(payback//500) #500張數
num100=int((payback-500*num500)//100) #100張數
num50=int((payback-500*num500-100*num100)//50) #50張數
num10=int((payback-500*num500-100*num100-num50*50)//10) #10元張數
num5=int((payback-500*num500-100*num100-num50*50-10*num10)//5) #5元張數
num1=int((payback-500*num500-100*num100-num50*50-10*num10-5*num5)//1) #1元張數

#輸出答案
result=""
if (num500 > 0):
	result+="500, "+str(num500)+"; "
if (num100 > 0):
	result+="100, "+str(num100)+"; "
if (num50 > 0):
	result+="50, "+str(num50)+"; "
if (num10 > 0):
	result+="10, "+str(num10)+"; "
if (num5 > 0):
	result+="5, "+str(num5)+"; "
if (num1 > 0):
	result+="1, "+str(num1)+"; "
print(result[:-2]) #最後兩碼不顯示