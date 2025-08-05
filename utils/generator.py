"""
数据生成器 - 提供各种测试数据生成功能
"""

import random
from typing import List, Any, Callable

class DataGenerator:
    """数据生成器
    
    该类提供各种测试数据的生成功能，包括：
    - 随机数据生成
    - 有序数据生成
    - 逆序数据生成
    - 特殊数据生成
    """
    
    def __init__(self, seed: int = None):
        """初始化数据生成器
        
        Args:
            seed: 随机数种子
        """
        if seed is not None:
            random.seed(seed)
    
    def generate_random_array(self, size: int, min_val: int = 1, max_val: int = 100) -> List[int]:
        """生成随机整数数组
        
        Args:
            size: 数组大小
            min_val: 最小值
            max_val: 最大值
            
        Returns:
            随机整数数组
        """
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    def generate_sorted_array(self, size: int, min_val: int = 1, max_val: int = 100) -> List[int]:
        """生成有序数组
        
        Args:
            size: 数组大小
            min_val: 最小值
            max_val: 最大值
            
        Returns:
            有序数组
        """
        arr = self.generate_random_array(size, min_val, max_val)
        return sorted(arr)
    
    def generate_reverse_sorted_array(self, size: int, min_val: int = 1, max_val: int = 100) -> List[int]:
        """生成逆序数组
        
        Args:
            size: 数组大小
            min_val: 最小值
            max_val: 最大值
            
        Returns:
            逆序数组
        """
        arr = self.generate_sorted_array(size, min_val, max_val)
        return list(reversed(arr))
    
    def generate_nearly_sorted_array(self, size: int, swap_ratio: float = 0.1) -> List[int]:
        """生成近似有序数组
        
        Args:
            size: 数组大小
            swap_ratio: 交换比例
            
        Returns:
            近似有序数组
        """
        arr = self.generate_sorted_array(size)
        num_swaps = int(size * swap_ratio)
        
        for _ in range(num_swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        
        return arr
    
    def generate_duplicate_array(self, size: int, unique_ratio: float = 0.3) -> List[int]:
        """生成包含重复元素的数组
        
        Args:
            size: 数组大小
            unique_ratio: 唯一元素比例
            
        Returns:
            包含重复元素的数组
        """
        unique_size = int(size * unique_ratio)
        unique_elements = self.generate_random_array(unique_size, 1, unique_size)
        
        arr = []
        for _ in range(size):
            arr.append(random.choice(unique_elements))
        
        return arr
    
    def generate_special_arrays(self, size: int) -> List[List[int]]:
        """生成特殊数组集合
        
        Args:
            size: 数组大小
            
        Returns:
            特殊数组集合
        """
        arrays = {
            'random': self.generate_random_array(size),
            'sorted': self.generate_sorted_array(size),
            'reverse_sorted': self.generate_reverse_sorted_array(size),
            'nearly_sorted': self.generate_nearly_sorted_array(size),
            'duplicate': self.generate_duplicate_array(size),
            'all_same': [1] * size,
            'alternating': [i % 2 for i in range(size)]
        }
        
        return arrays
    
    def generate_test_sets(self, sizes: List[int]) -> List[List[int]]:
        """生成不同大小的测试数据集
        
        Args:
            sizes: 数据大小列表
            
        Returns:
            测试数据集列表
        """
        test_sets = []
        for size in sizes:
            test_sets.append(self.generate_random_array(size))
        
        return test_sets
    
    def generate_graph_data(self, num_nodes: int, edge_probability: float = 0.3) -> List[List[int]]:
        """生成图数据（邻接矩阵）
        
        Args:
            num_nodes: 节点数量
            edge_probability: 边存在概率
            
        Returns:
            邻接矩阵
        """
        graph = [[0] * num_nodes for _ in range(num_nodes)]
        
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() < edge_probability:
                    weight = random.randint(1, 100)
                    graph[i][j] = weight
                    graph[j][i] = weight  # 无向图
        
        return graph
    
    def generate_string_data(self, size: int, min_length: int = 3, max_length: int = 10) -> List[str]:
        """生成字符串数据
        
        Args:
            size: 字符串数量
            min_length: 最小长度
            max_length: 最大长度
            
        Returns:
            字符串列表
        """
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        strings = []
        
        for _ in range(size):
            length = random.randint(min_length, max_length)
            string = ''.join(random.choice(chars) for _ in range(length))
            strings.append(string)
        
        return strings 