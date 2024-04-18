class newNode:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		self.hd = 0

def topview(root):

	if(root == None):
		return
	q = []
	m = dict()
	hd = 0
	root.hd = hd

	q.append(root)

	while(len(q)):
		root = q[0]
		hd = root.hd
		if hd not in m:
			m[hd] = root.data
		if(root.left):
			root.left.hd = hd - 1
			q.append(root.left)

		if(root.right):
			root.right.hd = hd + 1
			q.append(root.right)

		q.pop(0)
	for i in sorted(m):
		print(m[i], end=" ")


# Driver Code
if __name__ == '__main__':

	root = newNode('A')
	root.left = newNode('B')
	root.right = newNode('C')
	root.left.left = newNode('D')
	root.left.right = newNode('E')
	root.right.left = newNode('F')
	root.right.right = newNode('G')
	print("The top view of the tree is: ")
	topview(root)

