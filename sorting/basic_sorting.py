"""
基础排序算法 - 实现冒泡排序、选择排序、插入排序
"""

import copy
from typing import List, Any

from core.algorithm_base import AlgorithmBase, AlgorithmType, AlgorithmComplexity

class BubbleSort(AlgorithmBase):
    """冒泡排序算法
    
    冒泡排序是一种简单的排序算法，它重复地遍历要排序的数列，
    一次比较两个元素，如果它们的顺序错误就把它们交换过来。
    
    时间复杂度：
    - 最好情况：O(n) - 已经排序
    - 最坏情况：O(n²) - 逆序排列
    - 平均情况：O(n²)
    
    空间复杂度：O(1)
    """
    
    def __init__(self):
        """初始化冒泡排序算法"""
        super().__init__("冒泡排序", AlgorithmType.SORTING)
        
        # 设置复杂度信息
        self.time_complexity = AlgorithmComplexity.O_N_SQUARED
        self.space_complexity = AlgorithmComplexity.O_1
        self.best_case = AlgorithmComplexity.O_N
        self.worst_case = AlgorithmComplexity.O_N_SQUARED
        self.average_case = AlgorithmComplexity.O_N_SQUARED
    
    def execute(self, data: List[Any], **kwargs) -> List[Any]:
        """执行冒泡排序
        
        Args:
            data: 要排序的列表
            **kwargs: 额外参数
            
        Returns:
            排序后的列表
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        # 创建副本避免修改原数据
        arr = copy.deepcopy(data)
        n = len(arr)
        
        self.add_step("开始冒泡排序", arr.copy())
        
        # 外层循环控制排序轮数
        for i in range(n):
            swapped = False
            
            # 内层循环进行相邻元素比较和交换
            for j in range(0, n - i - 1):
                self.comparison_count += 1
                
                # 如果前一个元素大于后一个元素，则交换
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swap_count += 1
                    swapped = True
                    
                    self.add_step(f"交换元素 arr[{j}]={arr[j+1]} 和 arr[{j+1}]={arr[j]}", arr.copy())
            
            # 如果没有发生交换，说明已经排序完成
            if not swapped:
                self.add_step("数组已排序完成，提前结束", arr.copy())
                break
            
            self.add_step(f"第 {i+1} 轮排序完成", arr.copy())
        
        self.add_step("冒泡排序完成", arr.copy())
        return arr

class SelectionSort(AlgorithmBase):
    """选择排序算法
    
    选择排序是一种简单直观的排序算法。它的工作原理是：
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    
    时间复杂度：
    - 最好情况：O(n²)
    - 最坏情况：O(n²)
    - 平均情况：O(n²)
    
    空间复杂度：O(1)
    """
    
    def __init__(self):
        """初始化选择排序算法"""
        super().__init__("选择排序", AlgorithmType.SORTING)
        
        # 设置复杂度信息
        self.time_complexity = AlgorithmComplexity.O_N_SQUARED
        self.space_complexity = AlgorithmComplexity.O_1
        self.best_case = AlgorithmComplexity.O_N_SQUARED
        self.worst_case = AlgorithmComplexity.O_N_SQUARED
        self.average_case = AlgorithmComplexity.O_N_SQUARED
    
    def execute(self, data: List[Any], **kwargs) -> List[Any]:
        """执行选择排序
        
        Args:
            data: 要排序的列表
            **kwargs: 额外参数
            
        Returns:
            排序后的列表
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        # 创建副本避免修改原数据
        arr = copy.deepcopy(data)
        n = len(arr)
        
        self.add_step("开始选择排序", arr.copy())
        
        # 外层循环，每次选择最小的元素放到前面
        for i in range(n):
            min_idx = i
            
            # 内层循环，找到未排序部分的最小元素
            for j in range(i + 1, n):
                self.comparison_count += 1
                
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # 如果找到了更小的元素，则交换
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                self.swap_count += 1
                
                self.add_step(f"将最小元素 arr[{min_idx}]={arr[i]} 放到位置 {i}", arr.copy())
            else:
                self.add_step(f"位置 {i} 的元素已经是未排序部分的最小值", arr.copy())
        
        self.add_step("选择排序完成", arr.copy())
        return arr

class InsertionSort(AlgorithmBase):
    """插入排序算法
    
    插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
    对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    
    时间复杂度：
    - 最好情况：O(n) - 已经排序
    - 最坏情况：O(n²) - 逆序排列
    - 平均情况：O(n²)
    
    空间复杂度：O(1)
    """
    
    def __init__(self):
        """初始化插入排序算法"""
        super().__init__("插入排序", AlgorithmType.SORTING)
        
        # 设置复杂度信息
        self.time_complexity = AlgorithmComplexity.O_N_SQUARED
        self.space_complexity = AlgorithmComplexity.O_1
        self.best_case = AlgorithmComplexity.O_N
        self.worst_case = AlgorithmComplexity.O_N_SQUARED
        self.average_case = AlgorithmComplexity.O_N_SQUARED
    
    def execute(self, data: List[Any], **kwargs) -> List[Any]:
        """执行插入排序
        
        Args:
            data: 要排序的列表
            **kwargs: 额外参数
            
        Returns:
            排序后的列表
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        # 创建副本避免修改原数据
        arr = copy.deepcopy(data)
        n = len(arr)
        
        self.add_step("开始插入排序", arr.copy())
        
        # 从第二个元素开始，逐个插入到已排序序列中
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            self.add_step(f"准备插入元素 arr[{i}]={key}", arr.copy())
            
            # 将比key大的元素都向后移动一位
            while j >= 0:
                self.comparison_count += 1
                
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    self.swap_count += 1
                    j -= 1
                    
                    self.add_step(f"将 arr[{j+1}] 向后移动", arr.copy())
                else:
                    break
            
            # 将key插入到正确位置
            arr[j + 1] = key
            self.add_step(f"将 {key} 插入到位置 {j+1}", arr.copy())
        
        self.add_step("插入排序完成", arr.copy())
        return arr 