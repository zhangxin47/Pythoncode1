n=int(input("輸入工作數：")) #工作數
m=int(input("輸入機台數：")) #機台數
pstr=input("分別輸入工作處理時間：")

p=pstr.split(' ') #分開以空一個去分開
for i in range(n):
	p[i]=int(p[i])
p.sort(reverse=True) #表示由大到小
print(p)

loads=[0]*m #哪個機台有多少loads
assignments=[0]*n #工作分配給哪個Machine

#iteration
for j in range(n):
	#find leastloadmachine
	leastloadmachine=0 #第幾台mahcine最小Load
	leastload=loads[0] #最低的load從machine 0開始
	for i in range(1, m): #從1開始 是因為把machine 0設為最小了
		if loads[i] < leastload:
			leastloadmachine=i #做更新 最小load的機器編號
			leastload=loads[i]  #做更新 最小load的那台機器load
	#分派工作
	loads[leastloadmachine]=loads[leastloadmachine]+ p[j] #將最低的Load 機器加上工作時間
	assignments[j]=leastloadmachine+1
	#確認過程印出每一階段
	print(str(p[j]), ":" , str(loads))
#印出最終結果
print("assignments:" , str(assignments))
print("final load:" , str(loads))