#再寫一次code
n=int(input("Job數:"))  #job數
m=int(input("機台數:"))	#machine數
pstr=input("輸入各工作的loading:") #string

p=pstr.split(" ")
for i in range(n):
	p[i]= int(p[i])  #轉換型態
p.sort(reverse=True)

load=[0]*m #各機台loading
assignment=[0]*n #第幾個工作指派給哪個machine

for j in range(n):
	leastloadmachine=0 #先指派第0台machine為最低loading
	leastload=load[0] #第0台Machine的loading
	
	for i in range (1 , m):
		if load[i] < leastload:
			leastloadmachine=i
			leastload=load[i]
	
	load[leastloadmachine]=load[leastloadmachine] + p[j]
	assignment[j]=leastloadmachine+1
	print(str(p[j]) , ":" , str(load))

print( "assignment:", str(assignment))
print( "machine loading:", str(load))
			
