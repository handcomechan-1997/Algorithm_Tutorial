"""
树数据结构实现

树是一种层次化的数据结构，由节点和边组成。
本实现包括二叉树的基本操作：插入、删除、搜索、遍历等。
"""

from typing import Any, Optional, List, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class TreeNode:
    """树节点类"""
    
    def __init__(self, data: Any):
        """初始化树节点
        
        Args:
            data: 节点数据
        """
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return f"TreeNode({self.data})"


class BinaryTree(DataStructureBase):
    """二叉树实现
    
    特性：
    - 层次化结构
    - 每个节点最多有两个子节点
    - 支持多种遍历方式
    - 动态大小
    """
    
    def __init__(self):
        """初始化二叉树"""
        super().__init__("BinaryTree", DataStructureType.TREE)
        self.root = None
        self.size = 0
    
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素
        
        Args:
            item: 要插入的元素
            **kwargs: 额外参数
            
        Returns:
            插入是否成功
        """
        try:
            new_node = TreeNode(item)
            
            if self.root is None:
                self.root = new_node
            else:
                # 使用层序遍历找到第一个空位置
                queue = [self.root]
                while queue:
                    current = queue.pop(0)
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    elif current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        queue.append(current.left)
                        queue.append(current.right)
            
            self.size += 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"插入元素 {item}")
            return True
            
        except Exception as e:
            self.logger.error(f"插入元素失败: {e}")
            return False
    
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素
        
        Args:
            item: 要删除的元素
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        try:
            node = self._find_node(item)
            if node is None:
                self.logger.warning(f"未找到要删除的元素 {item}")
                return False
            
            # 如果是叶子节点，直接删除
            if node.left is None and node.right is None:
                if node.parent is None:
                    self.root = None
                elif node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            
            # 如果只有一个子节点
            elif node.left is None:
                if node.parent is None:
                    self.root = node.right
                elif node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                if node.right:
                    node.right.parent = node.parent
            
            elif node.right is None:
                if node.parent is None:
                    self.root = node.left
                elif node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                if node.left:
                    node.left.parent = node.parent
            
            # 如果有两个子节点，找到右子树的最小值替换
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                self.delete(successor.data)
                return True
            
            self.size -= 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"删除元素 {item}")
            return True
            
        except Exception as e:
            self.logger.error(f"删除元素失败: {e}")
            return False
    
    def search(self, item: Any) -> Optional[TreeNode]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            包含该元素的节点，如果未找到返回None
        """
        return self._find_node(item)
    
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素
        
        Args:
            old_item: 旧元素
            new_item: 新元素
            
        Returns:
            更新是否成功
        """
        try:
            node = self._find_node(old_item)
            if node is not None:
                node.data = new_item
                self.operation_count += 1
                self.modification_count += 1
                self.logger.info(f"更新元素: {old_item} -> {new_item}")
                return True
            else:
                self.logger.warning(f"未找到要更新的元素 {old_item}")
                return False
                
        except Exception as e:
            self.logger.error(f"更新元素失败: {e}")
            return False
    
    def clear(self):
        """清空树"""
        self.root = None
        self.size = 0
        self.operation_count += 1
        self.logger.info("二叉树已清空")
    
    def _find_node(self, item: Any) -> Optional[TreeNode]:
        """查找包含指定元素的节点
        
        Args:
            item: 要查找的元素
            
        Returns:
            包含该元素的节点，如果未找到返回None
        """
        if self.root is None:
            return None
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            self.access_count += 1
            
            if current.data == item:
                self.operation_count += 1
                return current
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return None
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """找到以指定节点为根的子树中的最小值节点
        
        Args:
            node: 根节点
            
        Returns:
            最小值节点
        """
        while node.left is not None:
            node = node.left
        return node
    
    def preorder_traversal(self) -> List[Any]:
        """前序遍历
        
        Returns:
            前序遍历结果
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def inorder_traversal(self) -> List[Any]:
        """中序遍历
        
        Returns:
            中序遍历结果
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def postorder_traversal(self) -> List[Any]:
        """后序遍历
        
        Returns:
            后序遍历结果
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def levelorder_traversal(self) -> List[Any]:
        """层序遍历
        
        Returns:
            层序遍历结果
        """
        result = []
        if self.root is None:
            return result
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        """前序遍历递归实现"""
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        """中序遍历递归实现"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Any]):
        """后序遍历递归实现"""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def get_height(self) -> int:
        """获取树的高度
        
        Returns:
            树的高度
        """
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node: Optional[TreeNode]) -> int:
        """递归计算树的高度"""
        if node is None:
            return -1
        return max(self._get_height_recursive(node.left), 
                  self._get_height_recursive(node.right)) + 1
    
    def __len__(self) -> int:
        """返回树的大小"""
        return self.size
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代（中序遍历）"""
        for item in self.inorder_traversal():
            yield item
    
    def __str__(self) -> str:
        """字符串表示"""
        if self.root is None:
            return "BinaryTree(empty)"
        
        elements = self.levelorder_traversal()
        return f"BinaryTree(size={self.size}, height={self.get_height()}, data={elements})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': self.size,
            'height': self.get_height(),
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count,
            'has_root': self.root is not None
        } 