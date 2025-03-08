class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 根据给定规则构建二叉树
def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value <= root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

# 打印树形结构
def print_tree(root, level=0, prefix="根节点: "):
    if root is not None:
        print(" " * (level * 4) + prefix + root.value.upper()+f" -{level}层")
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "左--- ")
            print_tree(root.right, level + 1, "右--- ")

# 主程序
def main():
    # 输入字符串
    input_str = input("请输入一个字符串：")
    
    # 获取第一个字母作为根节点
    root = TreeNode(input_str[0])
    
    # 从第二个字母开始，依次插入树中
    for char in input_str[1:]:
        root = insert_bst(root, char)
    
    # 输出树形结构
    print("\n生成的二叉树为：")
    print_tree(root)
    print("\n程序执行完毕！【感谢GPT之神】")

if __name__ == "__main__":
    while True:
        main()
    