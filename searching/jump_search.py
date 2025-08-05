"""
跳跃搜索算法实现

跳跃搜索是一种搜索算法，适用于有序数组。
它通过跳跃固定步长来减少比较次数，然后使用线性搜索在较小的范围内查找。
时间复杂度：O(√n)，空间复杂度：O(1)

学习目标：
1. 理解跳跃搜索的优化思想
2. 掌握步长计算和跳跃策略
3. 学会结合跳跃和线性搜索
4. 理解不同步长对性能的影响
"""

import math
from typing import Any, List, Optional
from core.algorithm_base import AlgorithmBase, AlgorithmType


class JumpSearch(AlgorithmBase):
    """跳跃搜索算法实现
    
    特性：
    - 适用于有序数组
    - 时间复杂度 O(√n)
    - 空间复杂度 O(1)
    - 比线性搜索更高效，比二分搜索简单
    
    学习要点：
    1. 计算最优跳跃步长（通常为 √n）
    2. 通过跳跃快速定位目标范围
    3. 在较小范围内进行线性搜索
    4. 理解步长选择对性能的影响
    """
    
    def __init__(self):
        """初始化跳跃搜索算法"""
        super().__init__("JumpSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行跳跃搜索
        
        TODO: 请实现跳跃搜索算法
        
        实现思路：
        1. 计算跳跃步长：step = √n
        2. 跳跃阶段：从索引0开始，每次跳跃step个位置
           - 检查跳跃位置的值是否小于目标
           - 如果是，继续跳跃；如果否，停止跳跃
        3. 线性搜索阶段：在跳跃范围内进行线性搜索
           - 从上一个跳跃位置开始
           - 逐个检查元素直到找到目标或超出范围
        
        关键点：
        - 跳跃步长通常选择 √n，这是理论最优值
        - 跳跃阶段用于快速缩小搜索范围
        - 线性搜索阶段在较小范围内进行精确查找
        
        提示：
        - 使用 math.sqrt(n) 计算步长
        - 使用 while 循环进行跳跃
        - 使用 for 循环或 while 循环进行线性搜索
        - 记录跳跃和搜索步骤
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现跳跃搜索算法
        pass
    
    def search_with_custom_step(self, data: List[Any], target: Any, step_size: int) -> Optional[int]:
        """使用自定义步长进行跳跃搜索
        
        TODO: 请实现自定义步长的跳跃搜索算法
        
        实现思路：
        1. 使用指定的步长进行跳跃
        2. 跳跃阶段：每次跳跃 step_size 个位置
        3. 线性搜索阶段：在跳跃范围内进行线性搜索
        
        应用场景：
        - 当数据分布不均匀时，可能需要调整步长
        - 当内存访问模式有特殊要求时
        - 当需要平衡跳跃开销和搜索效率时
        
        提示：
        - 与基本跳跃搜索类似，但使用自定义步长
        - 注意处理步长可能不是最优的情况
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            step_size: 自定义跳跃步长
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现自定义步长的跳跃搜索算法
        pass
    
    def find_optimal_step_size(self, data_length: int) -> int:
        """计算最优跳跃步长
        
        TODO: 请实现最优步长计算
        
        理论分析：
        - 跳跃搜索的时间复杂度为 O(√n)
        - 最优步长通常为 √n
        - 但实际最优值可能因数据分布而异
        
        提示：
        - 使用数学公式计算理论最优步长
        - 可以考虑数据分布特征进行调整
        
        Args:
            data_length: 数据长度
            
        Returns:
            最优跳跃步长
        """
        # TODO: 在这里实现最优步长计算
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(√n)',
                'worst_case': 'O(√n)'
            },
            'space_complexity': 'O(1)',
            'description': '跳跃搜索通过跳跃固定步长来减少比较次数，然后在线性范围内搜索'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'JumpSearch',
            'complexity': 'O(√n)',
            'description': '介于线性搜索和二分搜索之间的算法',
            'best_for': '有序数组、中等规模数据',
            'methods': ['search']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行跳跃搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                
        Returns:
            搜索结果（位置或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        return self.search(data, target) 