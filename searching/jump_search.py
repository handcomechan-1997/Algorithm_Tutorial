"""
跳跃搜索算法实现

跳跃搜索是一种搜索算法，适用于有序数组。
它通过跳跃固定步长来减少比较次数，然后使用线性搜索在较小的范围内查找。
时间复杂度：O(√n)，空间复杂度：O(1)
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
    """
    
    def __init__(self):
        """初始化跳跃搜索算法"""
        super().__init__("JumpSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行跳跃搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始跳跃搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            n = len(data)
            if n == 0:
                self.logger.info("数据列表为空")
                return None
            
            # 计算跳跃步长
            step = int(math.sqrt(n))
            self.logger.info(f"跳跃步长: {step}")
            
            # 跳跃阶段
            prev = 0
            while prev < n and data[min(step, n) - 1] < target:
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录跳跃步骤
                self.add_step({
                    'type': 'jump',
                    'from_index': prev,
                    'to_index': min(step, n) - 1,
                    'current_element': data[min(step, n) - 1],
                    'target': target,
                    'step': step
                })
                
                prev = step
                step += int(math.sqrt(n))
                
                # 如果超出数组范围
                if prev >= n:
                    break
            
            # 线性搜索阶段
            while prev < min(step, n):
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录线性搜索步骤
                self.add_step({
                    'type': 'linear_search',
                    'index': prev,
                    'current_element': data[prev],
                    'target': target
                })
                
                if data[prev] == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 {prev}")
                    self.add_step({
                        'type': 'found',
                        'position': prev,
                        'element': target
                    })
                    return prev
                prev += 1
            
            self.logger.info(f"未找到目标元素 {target}")
            self.add_step({
                'type': 'not_found',
                'target': target
            })
            return None
            
        except Exception as e:
            self.logger.error(f"跳跃搜索失败: {e}")
            return None
    
    def search_with_custom_step(self, data: List[Any], target: Any, step_size: int) -> Optional[int]:
        """使用自定义步长进行跳跃搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            step_size: 自定义跳跃步长
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始自定义步长跳跃搜索，目标元素: {target}，步长: {step_size}")
            self.operation_count = 0
            self.comparison_count = 0
            
            n = len(data)
            if n == 0:
                self.logger.info("数据列表为空")
                return None
            
            # 跳跃阶段
            prev = 0
            while prev < n and data[min(prev + step_size, n) - 1] < target:
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录跳跃步骤
                self.add_step({
                    'type': 'custom_jump',
                    'from_index': prev,
                    'to_index': min(prev + step_size, n) - 1,
                    'current_element': data[min(prev + step_size, n) - 1],
                    'target': target,
                    'step_size': step_size
                })
                
                prev += step_size
                
                # 如果超出数组范围
                if prev >= n:
                    break
            
            # 线性搜索阶段
            end_index = min(prev, n)
            for i in range(prev - step_size, end_index):
                if i < 0:
                    continue
                    
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录线性搜索步骤
                self.add_step({
                    'type': 'custom_linear_search',
                    'index': i,
                    'current_element': data[i],
                    'target': target
                })
                
                if data[i] == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 {i}")
                    self.add_step({
                        'type': 'found',
                        'position': i,
                        'element': target
                    })
                    return i
            
            self.logger.info(f"未找到目标元素 {target}")
            self.add_step({
                'type': 'not_found',
                'target': target
            })
            return None
            
        except Exception as e:
            self.logger.error(f"自定义步长跳跃搜索失败: {e}")
            return None
    
    def find_optimal_step_size(self, data_length: int) -> int:
        """计算最优跳跃步长
        
        Args:
            data_length: 数据长度
            
        Returns:
            最优跳跃步长
        """
        return int(math.sqrt(data_length))
    
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