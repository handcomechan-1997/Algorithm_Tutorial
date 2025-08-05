"""
链表数据结构实现

链表是一种线性数据结构，由节点组成，每个节点包含数据和指向下一个节点的指针。
本实现包括单向链表和双向链表的基本操作。
"""

from typing import Any, Optional, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class Node:
    """链表节点类"""
    
    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        """初始化节点
        
        Args:
            data: 节点数据
            next_node: 下一个节点
        """
        self.data = data
        self.next = next_node
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList(DataStructureBase):
    """单向链表实现
    
    特性：
    - 动态大小
    - 插入删除 O(1) (在头部)
    - 搜索 O(n)
    - 内存不连续
    """
    
    def __init__(self):
        """初始化链表"""
        super().__init__("LinkedList", DataStructureType.LINKED_LIST)
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, item: Any, position: Optional[int] = None) -> bool:
        """插入元素
        
        Args:
            item: 要插入的元素
            position: 插入位置，None表示插入到头部
            
        Returns:
            插入是否成功
        """
        try:
            if position is None:
                position = 0
                
            if position < 0 or position > self.size:
                self.logger.error(f"插入位置 {position} 超出范围")
                return False
            
            new_node = Node(item)
            
            if position == 0:
                # 插入到头部
                new_node.next = self.head
                self.head = new_node
                if self.tail is None:
                    self.tail = new_node
            else:
                # 插入到指定位置
                current = self.head
                for _ in range(position - 1):
                    current = current.next
                
                new_node.next = current.next
                current.next = new_node
                
                if new_node.next is None:
                    self.tail = new_node
            
            self.size += 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"在位置 {position} 插入元素 {item}")
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
            position = kwargs.get('position', None)
            
            if position is not None:
                # 按位置删除
                if position < 0 or position >= self.size:
                    self.logger.error(f"删除位置 {position} 超出范围")
                    return False
                
                if position == 0:
                    # 删除头部
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                else:
                    # 删除指定位置
                    current = self.head
                    for _ in range(position - 1):
                        current = current.next
                    
                    current.next = current.next.next
                    if current.next is None:
                        self.tail = current
                
                self.size -= 1
                self.operation_count += 1
                self.modification_count += 1
                
                self.logger.info(f"删除位置 {position} 的元素")
                return True
            else:
                # 按值删除
                if self.head is None:
                    return False
                
                if self.head.data == item:
                    # 删除头部
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                    self.size -= 1
                    self.operation_count += 1
                    self.modification_count += 1
                    self.logger.info(f"删除头部元素 {item}")
                    return True
                
                current = self.head
                while current.next is not None:
                    if current.next.data == item:
                        current.next = current.next.next
                        if current.next is None:
                            self.tail = current
                        self.size -= 1
                        self.operation_count += 1
                        self.modification_count += 1
                        self.logger.info(f"删除元素 {item}")
                        return True
                    current = current.next
                
                self.logger.warning(f"未找到要删除的元素 {item}")
                return False
                
        except Exception as e:
            self.logger.error(f"删除元素失败: {e}")
            return False
    
    def search(self, item: Any) -> Optional[int]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            元素的位置，如果未找到返回None
        """
        try:
            current = self.head
            position = 0
            
            while current is not None:
                self.access_count += 1
                if current.data == item:
                    self.operation_count += 1
                    self.logger.info(f"找到元素 {item} 在位置 {position}")
                    return position
                current = current.next
                position += 1
            
            self.logger.info(f"未找到元素 {item}")
            return None
            
        except Exception as e:
            self.logger.error(f"搜索元素失败: {e}")
            return None
    
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素
        
        Args:
            old_item: 旧元素
            new_item: 新元素
            
        Returns:
            更新是否成功
        """
        try:
            current = self.head
            
            while current is not None:
                if current.data == old_item:
                    current.data = new_item
                    self.operation_count += 1
                    self.modification_count += 1
                    self.logger.info(f"更新元素: {old_item} -> {new_item}")
                    return True
                current = current.next
            
            self.logger.warning(f"未找到要更新的元素 {old_item}")
            return False
            
        except Exception as e:
            self.logger.error(f"更新元素失败: {e}")
            return False
    
    def get(self, index: int) -> Optional[Any]:
        """获取指定位置的元素
        
        Args:
            index: 元素位置
            
        Returns:
            元素值，如果位置无效返回None
        """
        if index < 0 or index >= self.size:
            self.logger.error(f"访问位置 {index} 超出范围")
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        self.access_count += 1
        return current.data
    
    def set(self, index: int, value: Any) -> bool:
        """设置指定位置的元素
        
        Args:
            index: 元素位置
            value: 新值
            
        Returns:
            设置是否成功
        """
        if index < 0 or index >= self.size:
            self.logger.error(f"设置位置 {index} 超出范围")
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.data = value
        self.modification_count += 1
        self.logger.info(f"设置位置 {index} 的值为 {value}")
        return True
    
    def clear(self):
        """清空链表"""
        self.head = None
        self.tail = None
        self.size = 0
        self.operation_count += 1
        self.logger.info("链表已清空")
    
    def reverse(self):
        """反转链表"""
        if self.size <= 1:
            return
        
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        self.operation_count += 1
        self.modification_count += 1
        self.logger.info("链表已反转")
    
    def __len__(self) -> int:
        """返回链表长度"""
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        """支持索引访问"""
        return self.get(index)
    
    def __setitem__(self, index: int, value: Any):
        """支持索引赋值"""
        self.set(index, value)
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代"""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """字符串表示"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return f"LinkedList(size={self.size}, data=[{', '.join(elements)}])"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': self.size,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count,
            'has_head': self.head is not None,
            'has_tail': self.tail is not None
        } 