l = input('城市数、选择数和距离:')
m = l.split()
for i in range(len(m)):
    m[i]=int(m[i])
n = m[0]
p = m[1]
d = m[2]
ls = list()
for j in range(n):
    ls1 = input('城市坐标和人口:')
    ls2 = ls1.split()
    for k in range(3):
        ls2[k] = int(ls2[k])
    ls.append(ls2)
m1 = list(range(n)) #初始化城市列表序号
m3 = 0
while p > 0:
    mi = 0 #设置初始覆盖人口
    for i in m1:
        l1 = []
        m2 = ls[i][2]
        for j in m1:
            if i == j:
                continue
            elif ((ls[i][0] - ls[j][0])**2 + (ls[i][1]-ls[j][1])**2)**0.5 <= d:
                m2 += ls[j][2]
                l1.append(j)
        if mi < m2:
            mi = m2
            n1 = i
            l1.append(i) #不要忘记删除城市P自身
            l2 = l1
            print(l1)
    
    print(mi,n1+1)
    m1 = list(set(m1)^set(l2)) #删除每轮找到的城市，更新剩下城市列表
    p -= 1
    m3 +=mi
    print(m1)
print(m3)