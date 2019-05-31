numloc=5 #先定義有多少地方要旅行
dis=[[0, 9, 6, 7, 4],[9, 0 , 5, 9, 6],[6, 5, 0, 3, 1],[7, 9, 3, 0, 4],[4, 6, 1, 4, 0]] #二維矩陣 代表各點到各點距離

origin=0   #起點  (後續改成參賽者決定起點)
tour=[origin]  #已旅行過 0
unvisit=[]  #用for去新增扣除0
tourlen=0  #去存取旅行距離

for i in range(numloc):
	unvisit.append(i)
unvisit.remove(origin)


cur = origin  #現在位置


for i in range(numloc-1):
	next = -1     #下一站 要重設
	dismin = 99999 #很大的數 要重設
	
	for j in unvisit:
		if dis[cur][j] < dismin:
			next = j  #更改下一站
			dismin = dis[cur][j] #更改最小值
	tourlen +=dismin #將最小值加到旅途長度內
	tour.append(next) #將下一站加到旅途內
	unvisit.remove(next) #下一站已被刪去未去過的旅途
	cur = next #更新現在地點
	print(tour , tourlen)

#最後一個一定是回到origin
tour.append(origin)  #回到origin
tourlen += dis[cur][origin]

print("旅行人問題路徑:", tour ,"距離為：", tourlen) 


	
