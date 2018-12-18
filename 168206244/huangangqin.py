graph={}#所有邻居散列表
graph["yuepu"]={}
graph["yuepu"]["heijiao"]=5
graph["yuepu"]["haibao"]=0

graph["heijiao"]={}
graph["heijiao"]["jita"]=15
graph["heijiao"]["jiazigu"]=20


graph["haibao"]={}
graph["haibao"]["jita"]=30
graph["haibao"]["jiazigu"]=35

graph["jita"]={}
graph["jita"]["gangqin"]=20

graph["jiazigu"]={}
graph["jiazigu"]["gangqin"]=10

graph["gangqin"]={}

infinity=float("inf")#无穷大
#开销表
costs={}
costs["heijiao"]=5
costs["haibao"]=0
costs["jita"]=infinity
costs["jiazigu"]=infinity
costs["gangqin"]=infinity

#存储父节点的散列表
parents={}
parents["heijiao"]="yuepu"
parents["haibao"]="yuepu"
parents["jita"]=None
parents["jiazigu"]=None
parents["gangqin"]=None

processed=[]#用于记录处理过的节点

def find_lowest_cost_node(costs):#在未处理的节点中找出开销最低的节点
	lowest_cost=float("inf")
	lowest_cost_node=None
	for node in costs:
		cost=costs[node]
		if cost<lowest_cost and node not in processed:
			lowest_cost=cost#存储当前最低开销
			lowest_cost_node=node#相当于下标标记
	return lowest_cost_node
	
node=find_lowest_cost_node(costs)#找最小节点

print("*************换钢琴过程如下******************\n\n")
while node is not None:
	print("*********************************当前开销最低的节点:",node)
	cost=costs[node]
	neighbors=graph[node]
	for n in neighbors.keys():
		new_cost=cost+neighbors[n]
		if costs[n]>new_cost:
			costs[n]=new_cost
			parents[n]=node
			#print(parents[n],costs[n])
	processed.append(node)
	node=find_lowest_cost_node(costs)
	
	print("原图散列表")
	for k,v in graph.items():
		print(k,"	",v)
	print("\n")
	
	print("开销列表")
	for k,v in costs.items():
		print(k,"	",v)
	print("\n")
	
	print("父节点列表")
	for k,v in parents.items():
		print(k,"	",v)
	print("\n")