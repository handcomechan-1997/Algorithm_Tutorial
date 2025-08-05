"""
数据结构基类 - 定义基本数据结构的通用接口
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Iterator
from enum import Enum

from utils.logger import Logger

class DataStructureType(Enum):
    """数据结构类型枚举"""
    ARRAY = "array"
    LINKED_LIST = "linked_list"
    STACK = "stack"
    QUEUE = "queue"
    TREE = "tree"
    GRAPH = "graph"
    HEAP = "heap"
    HASH_TABLE = "hash_table"

class DataStructureBase(ABC):
    """数据结构基类
    
    该类定义了所有数据结构的通用接口，包括：
    - 基本操作（增删改查）
    - 遍历方法
    - 大小和状态查询
    - 可视化支持
    
    在学习过程中，可以继承此类来实现具体的数据结构。
    """
    
    def __init__(self, name: str, data_type: DataStructureType):
        """初始化数据结构基类"""
        self.name = name
        self.data_type = data_type
        self.logger = Logger()
        
        # 操作统计
        self.operation_count = 0
        self.access_count = 0
        self.modification_count = 0
        
        # 状态信息
        self.size = 0
        self.is_empty = True
        
        self.logger.info(f"数据结构 '{name}' 初始化完成")
    
    @abstractmethod
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素
        
        Args:
            item: 要插入的元素
            **kwargs: 额外参数（如位置等）
            
        Returns:
            插入是否成功
        """
        pass
    
    @abstractmethod
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素
        
        Args:
            item: 要删除的元素
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        pass
    
    @abstractmethod
    def search(self, item: Any) -> Optional[Any]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            找到的元素，如果未找到返回None
        """
        pass
    
    @abstractmethod
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素
        
        Args:
            old_item: 旧元素
            new_item: 新元素
            
        Returns:
            更新是否成功
        """
        pass
    
    def clear(self):
        """清空数据结构"""
        self.size = 0
        self.is_empty = True
        self.operation_count = 0
        self.access_count = 0
        self.modification_count = 0
        self.logger.info(f"数据结构 '{self.name}' 已清空")
    
    def get_size(self) -> int:
        """获取数据结构大小"""
        return self.size
    
    def is_structure_empty(self) -> bool:
        """检查数据结构是否为空"""
        return self.is_empty
    
    def get_statistics(self) -> dict:
        """获取操作统计信息"""
        return {
            'size': self.size,
            'is_empty': self.is_empty,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        }
    
    def reset_statistics(self):
        """重置统计信息"""
        self.operation_count = 0
        self.access_count = 0
        self.modification_count = 0
    
    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        """迭代器接口"""
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """长度接口"""
        pass
    
    @abstractmethod
    def __contains__(self, item: Any) -> bool:
        """包含关系接口"""
        pass
    
    def __str__(self) -> str:
        return f"{self.name} ({self.data_type.value}) - Size: {self.size}"
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' type='{self.data_type.value}' size={self.size}>" 