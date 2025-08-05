"""
数组数据结构实现

数组是最基础的数据结构，提供随机访问和连续存储。
本实现支持动态扩容、插入、删除、搜索等基本操作。
"""

import sys
from typing import Any, List, Optional, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class Array(DataStructureBase):
    """数组数据结构实现
    
    特性：
    - 随机访问 O(1)
    - 动态扩容
    - 支持插入、删除、搜索
    - 内存连续存储
    """
    
    def __init__(self, initial_capacity: int = 10):
        """初始化数组
        
        Args:
            initial_capacity: 初始容量
        """
        super().__init__("Array", DataStructureType.ARRAY)
        self.capacity = initial_capacity
        self.data = [None] * initial_capacity
        self.size = 0
        
    def insert(self, item: Any, position: Optional[int] = None) -> bool:
        """插入元素
        
        Args:
            item: 要插入的元素
            position: 插入位置，None表示插入到末尾
            
        Returns:
            插入是否成功
        """
        try:
            if position is None:
                position = self.size
                
            if position < 0 or position > self.size:
                self.logger.error(f"插入位置 {position} 超出范围")
                return False
                
            # 检查是否需要扩容
            if self.size >= self.capacity:
                self._resize(self.capacity * 2)
                
            # 移动元素为插入腾出空间
            for i in range(self.size, position, -1):
                self.data[i] = self.data[i-1]
                
            self.data[position] = item
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
                    
                # 移动元素覆盖被删除的元素
                for i in range(position, self.size - 1):
                    self.data[i] = self.data[i + 1]
                    
                self.data[self.size - 1] = None
                self.size -= 1
                self.operation_count += 1
                self.modification_count += 1
                
                self.logger.info(f"删除位置 {position} 的元素")
                return True
            else:
                # 按值删除
                for i in range(self.size):
                    if self.data[i] == item:
                        return self.delete(item, position=i)
                        
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
            for i in range(self.size):
                self.access_count += 1
                if self.data[i] == item:
                    self.operation_count += 1
                    self.logger.info(f"找到元素 {item} 在位置 {i}")
                    return i
                    
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
            position = self.search(old_item)
            if position is not None:
                self.data[position] = new_item
                self.operation_count += 1
                self.modification_count += 1
                self.logger.info(f"更新位置 {position} 的元素: {old_item} -> {new_item}")
                return True
            else:
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
        if 0 <= index < self.size:
            self.access_count += 1
            return self.data[index]
        else:
            self.logger.error(f"访问位置 {index} 超出范围")
            return None
    
    def set(self, index: int, value: Any) -> bool:
        """设置指定位置的元素
        
        Args:
            index: 元素位置
            value: 新值
            
        Returns:
            设置是否成功
        """
        if 0 <= index < self.size:
            self.data[index] = value
            self.modification_count += 1
            self.logger.info(f"设置位置 {index} 的值为 {value}")
            return True
        else:
            self.logger.error(f"设置位置 {index} 超出范围")
            return False
    
    def clear(self):
        """清空数组"""
        self.data = [None] * self.capacity
        self.size = 0
        self.operation_count += 1
        self.logger.info("数组已清空")
    
    def _resize(self, new_capacity: int):
        """调整数组容量
        
        Args:
            new_capacity: 新容量
        """
        old_data = self.data
        self.data = [None] * new_capacity
        self.capacity = new_capacity
        
        for i in range(self.size):
            self.data[i] = old_data[i]
            
        self.logger.info(f"数组容量调整为 {new_capacity}")
    
    def __len__(self) -> int:
        """返回数组长度"""
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        """支持索引访问"""
        return self.get(index)
    
    def __setitem__(self, index: int, value: Any):
        """支持索引赋值"""
        self.set(index, value)
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代"""
        for i in range(self.size):
            yield self.data[i]
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Array(size={self.size}, capacity={self.capacity}, data={self.data[:self.size]})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': self.size,
            'capacity': self.capacity,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count,
            'load_factor': self.size / self.capacity if self.capacity > 0 else 0
        } 