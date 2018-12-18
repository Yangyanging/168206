def find_path(start,end,paths):
#此函数作用：在只变化一个字母的之间建立起关系图，且比较出了最近路径的图(同样近的不再构建路径)
	graph={}#只变化一个字母的，之间建立映射关系
	graph[start]=[]
	adict.append(end)
	if start==end:
		return "start=end"
	else:
		visited=[]
		visited.append(start)
		for word in visited:
			#print(word,'**')
			graph[word]=[]#对键初始化一下
			for i in range(len(word)):
				#print(word[i])
				for j in range(ord('a'),ord('z')+1):
					newword=word[:i]+chr(j)+word[i+1:]
					#print(newword)
					if newword in paths and newword not in visited:#已经添加过就不进行添加
						#print(word,newword)
						visited.append(newword)
						graph[word].append(newword)
		print('所有遍历过的节点',visited,'\n')
		print('构建出来的散列表如下')
		for k,v in graph.items():
			print(k,"	",v)
		print('\n')
		return graph

start="hit"#开始状态（可随意更改）
end="cog"#终点状态（可随意更改）
adict=['hot','dot','dog','lot','log']#规定拥有可走的路径（可随意更改）

bbb=find_path(start,end,adict)#形成字典，并且有唯一路径，且为最短路径

jg=[]#沿着路径从后往前找，从而打印路径
adict.append(start)
jg.append(end)
while end!=start:
	for word in adict:
		if end in bbb[word]:
			end=word
			jg.append(end)
jg.reverse()#逆序一下
print('最终转换路径如此列表顺序:',jg)
	