graph={}#所有邻居散列表
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2

graph["a"]={}
graph["a"]["fin"]=1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"]={}

infinity=float("inf")#无穷大
#开销表
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

#存储父节点的散列表
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

processed=[]#用于记录处理过的节点

def find_lowest_cost_node(aaaa):#在未处理的节点中找出开销最低的节点
	lowest_cost=float("inf")
	lowest_cost_node=None
	for node in aaaa:
		cost=aaaa[node]
		if cost<lowest_cost and node not in processed:
			lowest_cost=cost#存储当前最低开销
			lowest_cost_node=node#相当于下标标记
	return lowest_cost_node
	
node=find_lowest_cost_node(costs)#找最小节点

while node is not None:
	print("********************************************",node)
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
