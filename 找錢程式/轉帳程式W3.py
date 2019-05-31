x1 = x2 = y = -1 #宣告變數
while 1:
	x1 = int(input()) #第一個帳戶$
	x2 = int(input()) #第二個帳戶$
	y  = int(input()) #轉帳$
	if (( 0 <= x1 <= 100000 ) and ( 0 <= x2 <= 100000 ) and ( 0 <= y <= 100000 )):
		break
	else:
		print("您輸入的帳戶與金額不在0與100000區間")
		continue
#轉帳$低於帳戶
if (y<=x1):  
	x2=x2+y
	x1=x1-y
else: #先給$，再把x1帳戶清空
	x2=x2+x1
	x1=0
print (x1, x2)