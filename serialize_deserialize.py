class Codec:
    def serialize(self, root):
        q, res = deque([root]), []
        while q:
            node =q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        if vals[0] == "null":
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
data = input("Enter tree (comma separated, use null): ")
codec = Codec()
root = codec.deserialize(data)
output = codec.serialize(root)
print("Serialized again:", output)

   
