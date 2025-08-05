"""
队列数据结构实现

队列是一种先进先出(FIFO)的数据结构，类似于现实生活中的排队。
本实现基于链表，提供入队、出队、查看队首等基本操作。
"""

from typing import Any, Optional
from core.data_structures import DataStructureBase, DataStructureType
from .linked_list import LinkedList


class Queue(DataStructureBase):
    """队列数据结构实现
    
    特性：
    - 先进先出 (FIFO)
    - 入队 O(1)
    - 出队 O(1)
    - 查看队首 O(1)
    """
    
    def __init__(self):
        """初始化队列"""
        super().__init__("Queue", DataStructureType.QUEUE)
        self.data = LinkedList()
    
    def enqueue(self, item: Any) -> bool:
        """入队操作
        
        Args:
            item: 要入队的元素
            
        Returns:
            入队是否成功
        """
        return self.insert(item)
    
    def dequeue(self) -> Optional[Any]:
        """出队操作
        
        Returns:
            队首元素，如果队列为空返回None
        """
        if self.is_empty:
            self.logger.warning("队列为空，无法出队")
            return None
        
        front_item = self.data.get(0)
        self.data.delete(front_item, position=0)
        self.operation_count += 1
        self.modification_count += 1
        self.logger.info(f"出队元素: {front_item}")
        return front_item
    
    def front(self) -> Optional[Any]:
        """查看队首元素
        
        Returns:
            队首元素，如果队列为空返回None
        """
        if self.is_empty:
            self.logger.warning("队列为空，无法查看队首")
            return None
        
        front_item = self.data.get(0)
        self.access_count += 1
        self.logger.info(f"查看队首元素: {front_item}")
        return front_item
    
    def back(self) -> Optional[Any]:
        """查看队尾元素
        
        Returns:
            队尾元素，如果队列为空返回None
        """
        if self.is_empty:
            self.logger.warning("队列为空，无法查看队尾")
            return None
        
        back_item = self.data.get(len(self.data) - 1)
        self.access_count += 1
        self.logger.info(f"查看队尾元素: {back_item}")
        return back_item
    
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素（入队）
        
        Args:
            item: 要插入的元素
            **kwargs: 额外参数（队列中忽略位置参数）
            
        Returns:
            插入是否成功
        """
        success = self.data.insert(item, position=len(self.data))
        if success:
            self.operation_count += 1
            self.modification_count += 1
            self.logger.info(f"入队元素: {item}")
        return success
    
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素（出队）
        
        Args:
            item: 要删除的元素
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        if self.is_empty:
            return False
        
        # 队列只能删除队首元素
        front_item = self.data.get(0)
        if front_item == item:
            return self.dequeue() is not None
        else:
            self.logger.warning(f"队列只能删除队首元素，无法删除 {item}")
            return False
    
    def search(self, item: Any) -> Optional[int]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            元素在队列中的位置（从队首开始计数），如果未找到返回None
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
        """清空队列"""
        self.data.clear()
        self.operation_count += 1
        self.logger.info("队列已清空")
    
    @property
    def is_empty(self) -> bool:
        """检查队列是否为空"""
        return len(self.data) == 0
    
    def __len__(self) -> int:
        """返回队列的大小"""
        return len(self.data)
    
    def __str__(self) -> str:
        """字符串表示"""
        elements = list(self.data)
        return f"Queue(size={len(self)}, data=[{', '.join(map(str, elements))}])"
    
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