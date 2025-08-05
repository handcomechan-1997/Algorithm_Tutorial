"""
栈数据结构实现

栈是一种后进先出(LIFO)的数据结构，类似于现实生活中的盘子堆叠。
本实现基于链表，提供压栈、弹栈、查看栈顶等基本操作。
"""

from typing import Any, Optional
from core.data_structures import DataStructureBase, DataStructureType
from .linked_list import LinkedList


class Stack(DataStructureBase):
    """栈数据结构实现
    
    特性：
    - 后进先出 (LIFO)
    - 压栈 O(1)
    - 弹栈 O(1)
    - 查看栈顶 O(1)
    """
    
    def __init__(self):
        """初始化栈"""
        super().__init__("Stack", DataStructureType.STACK)
        self.data = LinkedList()
    
    def push(self, item: Any) -> bool:
        """压栈操作
        
        Args:
            item: 要压入栈的元素
            
        Returns:
            压栈是否成功
        """
        return self.insert(item)
    
    def pop(self) -> Optional[Any]:
        """弹栈操作
        
        Returns:
            栈顶元素，如果栈为空返回None
        """
        if self.is_empty:
            self.logger.warning("栈为空，无法弹栈")
            return None
        
        top_item = self.data.get(0)
        self.data.delete(top_item, position=0)
        self.operation_count += 1
        self.modification_count += 1
        self.logger.info(f"弹栈元素: {top_item}")
        return top_item
    
    def peek(self) -> Optional[Any]:
        """查看栈顶元素
        
        Returns:
            栈顶元素，如果栈为空返回None
        """
        if self.is_empty:
            self.logger.warning("栈为空，无法查看栈顶")
            return None
        
        top_item = self.data.get(0)
        self.access_count += 1
        self.logger.info(f"查看栈顶元素: {top_item}")
        return top_item
    
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素（压栈）
        
        Args:
            item: 要插入的元素
            **kwargs: 额外参数（栈中忽略位置参数）
            
        Returns:
            插入是否成功
        """
        success = self.data.insert(item, position=0)
        if success:
            self.operation_count += 1
            self.modification_count += 1
            self.logger.info(f"压栈元素: {item}")
        return success
    
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素（弹栈）
        
        Args:
            item: 要删除的元素
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        if self.is_empty:
            return False
        
        # 栈只能删除栈顶元素
        top_item = self.data.get(0)
        if top_item == item:
            return self.pop() is not None
        else:
            self.logger.warning(f"栈只能删除栈顶元素，无法删除 {item}")
            return False
    
    def search(self, item: Any) -> Optional[int]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            元素在栈中的位置（从栈顶开始计数），如果未找到返回None
        """
        return self.data.search(item)
    
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素
        
        Args:
            old_item: 旧元素
            new_item: 新元素
            
        Returns:
            更新是否成功
        """
        return self.data.update(old_item, new_item)
    
    def clear(self):
        """清空栈"""
        self.data.clear()
        self.operation_count += 1
        self.logger.info("栈已清空")
    
    @property
    def is_empty(self) -> bool:
        """检查栈是否为空"""
        return len(self.data) == 0
    
    def __len__(self) -> int:
        """返回栈的大小"""
        return len(self.data)
    
    def __str__(self) -> str:
        """字符串表示"""
        elements = list(self.data)
        return f"Stack(size={len(self)}, data=[{', '.join(map(str, elements))}])"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': len(self),
            'is_empty': self.is_empty,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        } 