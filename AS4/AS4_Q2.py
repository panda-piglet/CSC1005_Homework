def dfs_traversal(tree: list, order: str) -> list:
    """
    对以列表表示的二叉树执行深度优先搜索 (DFS) 遍历。

    Args:
        tree (list): 表示二叉树的列表，其中 None 表示空节点。
        order (str): 遍历顺序，必须是 "preorder", "inorder", 或 "postorder"。

    Returns:
        list: 按指定顺序访问的节点值列表。
    """

    # 将 order 转换为小写，以确保匹配
    order = order.lower()

    if order not in ["preorder", "inorder", "postorder"]:
        raise ValueError("Traversal order must be 'preorder', 'inorder', or 'postorder'.")

    visited_nodes = []

    def traverse(index):
        """
        递归地遍历树，使用索引来追踪当前节点。

        Args:
            index (int): 当前节点的列表索引。
        """
        # 1. 检查越界或空节点
        if index >= len(tree) or tree[index] is None:
            return

        node_value = tree[index]

        # 计算子节点索引
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # --- 2. 核心 DFS 逻辑 ---

        if order == "preorder":
            # 访问根 -> 左 -> 右
            visited_nodes.append(node_value)
            traverse(left_index)
            traverse(right_index)

        elif order == "inorder":
            # 访问 左 -> 根 -> 右
            traverse(left_index)
            visited_nodes.append(node_value)
            traverse(right_index)

        elif order == "postorder":
            # 访问 左 -> 右 -> 根
            traverse(left_index)
            traverse(right_index)
            visited_nodes.append(node_value)

    # 从根节点 (索引 0) 开始遍历
    traverse(0)

    return visited_nodes


# --- 3. 测试函数 ---

# 示例树: [1, 2, 3, 4, 5, None, 6]
# 结构:
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
def main():
    example_tree = [1, 2, 3, 4, 5, None, 6]

    print("--- DFS 遍历结果 ---")

    # Preorder (根 -> 左 -> 右): 1, 2, 4, 5, 3, 6
    preorder_output = dfs_traversal(example_tree, "preorder")
    print(f"Preorder:  {preorder_output}")

    # Inorder (左 -> 根 -> 右): 4, 2, 5, 1, 3, 6
    inorder_output = dfs_traversal(example_tree, "inorder")
    print(f"Inorder:   {inorder_output}")

    # Postorder (左 -> 右 -> 根): 4, 5, 2, 6, 3, 1
    postorder_output = dfs_traversal(example_tree, "postorder")
    print(f"Postorder: {postorder_output}")
