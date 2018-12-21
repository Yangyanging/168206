print("题目：\nA：我没有偷钻石。\nB：D就是罪犯。\nC：B是盗窃这块钻石的罪犯。\nD：B有意诬陷我。",
"\n假定只有一个人说的是真话，编程序判断谁偷走了钻石。",
"\n\n思路：一个一个假设是小偷，判断是否有且只有一个人说真话。\n")
flag=0
for thief in range(ord('A'),ord('D')+1):#从A到D一个一个假设是小偷
	print("假设",chr(thief),
	"偷了钻石，那么：")
	if thief!=ord('A'):
		print("A说了真话")
	else:
		print("A说了假话")
	if thief==ord('D'):
		print("B说了真话")
	else:
		print("B说了假话")
	if thief==ord('B'):
		print("C说了真话")
	else:
		print("C说了假话")
	if thief!=ord('D'):
		print("D说了真话")
	else:
		print("D说了假话")
	zhenhua=(thief!=ord('A'))+(thief==ord('D'))+(thief==ord('B'))+(thief!=ord('D'))#zhenhua的值表示说真话人数
	print("这时共有",zhenhua,"个人说了真话")
	if zhenhua==1:#只有一个人说真话
		print("符合题意，假设成立，说明是",chr(thief),"偷走了钻石\n\n")
		flag=1
	else:
		print("不符题意，假设失败,说明",chr(thief),"没有偷钻石\n\n")
if(flag==0):
	print("没有找到小偷")