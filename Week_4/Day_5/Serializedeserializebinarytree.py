# 
class Codec:
    def serialize(self, root):
        ans = []

        def dfs(node):
            if not node:
                ans.append("N")
                return

            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(ans)


    def deserialize(self, data):
        values = data.split(",")

        def dfs():
            val = values.pop(0)

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs() 