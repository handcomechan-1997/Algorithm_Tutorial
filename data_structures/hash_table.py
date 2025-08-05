"""
哈希表数据结构实现

哈希表是一种通过哈希函数将键映射到值的数据结构。
本实现支持动态扩容、冲突处理、键值对操作等。
"""

from typing import Any, Optional, List, Tuple, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class HashTable(DataStructureBase):
    """哈希表实现
    
    特性：
    - 键值对存储
    - 平均 O(1) 的查找、插入、删除
    - 动态扩容
    - 链地址法处理冲突
    """
    
    def __init__(self, initial_capacity: int = 16, load_factor: float = 0.75):
        """初始化哈希表
        
        Args:
            initial_capacity: 初始容量
            load_factor: 负载因子
        """
        super().__init__("HashTable", DataStructureType.HASH_TABLE)
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(initial_capacity)]
    
    def put(self, key: Any, value: Any) -> bool:
        """插入键值对
        
        Args:
            key: 键
            value: 值
            
        Returns:
            插入是否成功
        """
        try:
            # 检查是否需要扩容
            if self.size >= self.capacity * self.load_factor:
                self._resize(self.capacity * 2)
            
            hash_code = self._hash(key)
            bucket = self.buckets[hash_code]
            
            # 检查是否已存在相同的键
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    self.operation_count += 1
                    self.modification_count += 1
                    self.logger.info(f"更新键值对: {key} -> {value}")
                    return True
            
            # 插入新的键值对
            bucket.append((key, value))
            self.size += 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"插入键值对: {key} -> {value}")
            return True
            
        except Exception as e:
            self.logger.error(f"插入键值对失败: {e}")
            return False
    
    def get(self, key: Any) -> Optional[Any]:
        """获取值
        
        Args:
            key: 键
            
        Returns:
            对应的值，如果未找到返回None
        """
        try:
            hash_code = self._hash(key)
            bucket = self.buckets[hash_code]
            
            for k, v in bucket:
                self.access_count += 1
                if k == key:
                    self.operation_count += 1
                    self.logger.info(f"找到键值对: {key} -> {v}")
                    return v
            
            self.logger.info(f"未找到键 {key}")
            return None
            
        except Exception as e:
            self.logger.error(f"获取值失败: {e}")
            return None
    
    def remove(self, key: Any) -> bool:
        """删除键值对
        
        Args:
            key: 要删除的键
            
        Returns:
            删除是否成功
        """
        try:
            hash_code = self._hash(key)
            bucket = self.buckets[hash_code]
            
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket.pop(i)
                    self.size -= 1
                    self.operation_count += 1
                    self.modification_count += 1
                    self.logger.info(f"删除键值对: {key}")
                    return True
            
            self.logger.warning(f"未找到要删除的键 {key}")
            return False
            
        except Exception as e:
            self.logger.error(f"删除键值对失败: {e}")
            return False
    
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素（键值对）
        
        Args:
            item: 键
            **kwargs: 额外参数，包含value
            
        Returns:
            插入是否成功
        """
        value = kwargs.get('value', None)
        return self.put(item, value)
    
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素（键值对）
        
        Args:
            item: 键
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        return self.remove(item)
    
    def search(self, item: Any) -> Optional[Any]:
        """搜索元素（获取值）
        
        Args:
            item: 键
            
        Returns:
            对应的值，如果未找到返回None
        """
        return self.get(item)
    
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素（更新键）
        
        Args:
            old_item: 旧键
            new_item: 新键
            
        Returns:
            更新是否成功
        """
        try:
            # 获取旧键对应的值
            value = self.get(old_item)
            if value is None:
                self.logger.warning(f"未找到要更新的键 {old_item}")
                return False
            
            # 删除旧键值对
            self.remove(old_item)
            
            # 插入新键值对
            return self.put(new_item, value)
            
        except Exception as e:
            self.logger.error(f"更新键失败: {e}")
            return False
    
    def clear(self):
        """清空哈希表"""
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.operation_count += 1
        self.logger.info("哈希表已清空")
    
    def _hash(self, key: Any) -> int:
        """计算哈希值
        
        Args:
            key: 键
            
        Returns:
            哈希值
        """
        return hash(key) % self.capacity
    
    def _resize(self, new_capacity: int):
        """调整哈希表容量
        
        Args:
            new_capacity: 新容量
        """
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(new_capacity)]
        self.size = 0
        
        # 重新插入所有键值对
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
        
        self.logger.info(f"哈希表容量调整为 {new_capacity}")
    
    def __len__(self) -> int:
        """返回哈希表的大小"""
        return self.size
    
    def __str__(self) -> str:
        """字符串表示"""
        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{key}:{value}")
        return f"HashTable(size={self.size}, items=[{', '.join(items)}])"
    
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
            'load_factor': self.size / self.capacity if self.capacity > 0 else 0,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        }