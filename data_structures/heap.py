"""
堆数据结构实现

堆是一种特殊的完全二叉树，满足堆性质。
本实现包括最小堆和最大堆，支持插入、删除、堆化等操作。
"""

from typing import Any, Optional, List, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class MinHeap(DataStructureBase):
    """最小堆实现
    
    特性：
    - 完全二叉树结构
    - 父节点值小于等于子节点值
    - 根节点是最小值
    - 插入和删除都是 O(log n)
    """
    
    def __init__(self):
        """初始化最小堆"""
        super().__init__("MinHeap", DataStructureType.HEAP)
        self.data = []
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
            self.data.append(item)
            self.size += 1
            self._heapify_up(self.size - 1)
            
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
            # 找到要删除的元素位置
            index = -1
            for i, val in enumerate(self.data):
                if val == item:
                    index = i
                    break
            
            if index == -1:
                self.logger.warning(f"未找到要删除的元素 {item}")
                return False
            
            # 将最后一个元素移到删除位置
            self.data[index] = self.data[-1]
            self.data.pop()
            self.size -= 1
            
            # 如果还有元素，进行堆化
            if self.size > 0:
                self._heapify_down(index)
            
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"删除元素 {item}")
            return True
            
        except Exception as e:
            self.logger.error(f"删除元素失败: {e}")
            return False
    
    def extract_min(self) -> Optional[Any]:
        """提取最小值
        
        Returns:
            最小值，如果堆为空返回None
        """
        if self.is_empty:
            self.logger.warning("堆为空，无法提取最小值")
            return None
        
        min_value = self.data[0]
        self.delete(min_value)
        return min_value
    
    def peek_min(self) -> Optional[Any]:
        """查看最小值
        
        Returns:
            最小值，如果堆为空返回None
        """
        if self.is_empty:
            self.logger.warning("堆为空，无法查看最小值")
            return None
        
        self.access_count += 1
        return self.data[0]
    
    def search(self, item: Any) -> Optional[int]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            元素的位置，如果未找到返回None
        """
        try:
            for i, val in enumerate(self.data):
                self.access_count += 1
                if val == item:
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
            index = self.search(old_item)
            if index is not None:
                self.data[index] = new_item
                
                # 根据新值的大小决定向上或向下堆化
                if new_item < old_item:
                    self._heapify_up(index)
                else:
                    self._heapify_down(index)
                
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
        """清空堆"""
        self.data.clear()
        self.size = 0
        self.operation_count += 1
        self.logger.info("最小堆已清空")
    
    def _heapify_up(self, index: int):
        """向上堆化
        
        Args:
            index: 要堆化的位置
        """
        parent = (index - 1) // 2
        while index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2
    
    def _heapify_down(self, index: int):
        """向下堆化
        
        Args:
            index: 要堆化的位置
        """
        while True:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if left_child < self.size and self.data[left_child] < self.data[smallest]:
                smallest = left_child
            
            if right_child < self.size and self.data[right_child] < self.data[smallest]:
                smallest = right_child
            
            if smallest == index:
                break
            
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest
    
    def build_heap(self, items: List[Any]):
        """从列表构建堆
        
        Args:
            items: 要构建堆的元素列表
        """
        self.data = items.copy()
        self.size = len(items)
        
        # 从最后一个非叶子节点开始向下堆化
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify_down(i)
        
        self.operation_count += 1
        self.modification_count += 1
        self.logger.info(f"从列表构建堆，共 {self.size} 个元素")
    
    @property
    def is_empty(self) -> bool:
        """检查堆是否为空"""
        return self.size == 0
    
    def __len__(self) -> int:
        """返回堆的大小"""
        return self.size
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代"""
        for item in self.data:
            yield item
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"MinHeap(size={self.size}, data={self.data})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': self.size,
            'is_empty': self.is_empty,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        }


class MaxHeap(DataStructureBase):
    """最大堆实现
    
    特性：
    - 完全二叉树结构
    - 父节点值大于等于子节点值
    - 根节点是最大值
    - 插入和删除都是 O(log n)
    """
    
    def __init__(self):
        """初始化最大堆"""
        super().__init__("MaxHeap", DataStructureType.HEAP)
        self.data = []
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
            self.data.append(item)
            self.size += 1
            self._heapify_up(self.size - 1)
            
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
            # 找到要删除的元素位置
            index = -1
            for i, val in enumerate(self.data):
                if val == item:
                    index = i
                    break
            
            if index == -1:
                self.logger.warning(f"未找到要删除的元素 {item}")
                return False
            
            # 将最后一个元素移到删除位置
            self.data[index] = self.data[-1]
            self.data.pop()
            self.size -= 1
            
            # 如果还有元素，进行堆化
            if self.size > 0:
                self._heapify_down(index)
            
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"删除元素 {item}")
            return True
            
        except Exception as e:
            self.logger.error(f"删除元素失败: {e}")
            return False
    
    def extract_max(self) -> Optional[Any]:
        """提取最大值
        
        Returns:
            最大值，如果堆为空返回None
        """
        if self.is_empty:
            self.logger.warning("堆为空，无法提取最大值")
            return None
        
        max_value = self.data[0]
        self.delete(max_value)
        return max_value
    
    def peek_max(self) -> Optional[Any]:
        """查看最大值
        
        Returns:
            最大值，如果堆为空返回None
        """
        if self.is_empty:
            self.logger.warning("堆为空，无法查看最大值")
            return None
        
        self.access_count += 1
        return self.data[0]
    
    def search(self, item: Any) -> Optional[int]:
        """搜索元素
        
        Args:
            item: 要搜索的元素
            
        Returns:
            元素的位置，如果未找到返回None
        """
        try:
            for i, val in enumerate(self.data):
                self.access_count += 1
                if val == item:
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
            index = self.search(old_item)
            if index is not None:
                self.data[index] = new_item
                
                # 根据新值的大小决定向上或向下堆化
                if new_item > old_item:
                    self._heapify_up(index)
                else:
                    self._heapify_down(index)
                
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
        """清空堆"""
        self.data.clear()
        self.size = 0
        self.operation_count += 1
        self.logger.info("最大堆已清空")
    
    def _heapify_up(self, index: int):
        """向上堆化
        
        Args:
            index: 要堆化的位置
        """
        parent = (index - 1) // 2
        while index > 0 and self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2
    
    def _heapify_down(self, index: int):
        """向下堆化
        
        Args:
            index: 要堆化的位置
        """
        while True:
            largest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            
            if left_child < self.size and self.data[left_child] > self.data[largest]:
                largest = left_child
            
            if right_child < self.size and self.data[right_child] > self.data[largest]:
                largest = right_child
            
            if largest == index:
                break
            
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            index = largest
    
    def build_heap(self, items: List[Any]):
        """从列表构建堆
        
        Args:
            items: 要构建堆的元素列表
        """
        self.data = items.copy()
        self.size = len(items)
        
        # 从最后一个非叶子节点开始向下堆化
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify_down(i)
        
        self.operation_count += 1
        self.modification_count += 1
        self.logger.info(f"从列表构建堆，共 {self.size} 个元素")
    
    @property
    def is_empty(self) -> bool:
        """检查堆是否为空"""
        return self.size == 0
    
    def __len__(self) -> int:
        """返回堆的大小"""
        return self.size
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代"""
        for item in self.data:
            yield item
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"MaxHeap(size={self.size}, data={self.data})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'size': self.size,
            'is_empty': self.is_empty,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        } 