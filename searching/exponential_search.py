"""
指数搜索算法实现

指数搜索是一种搜索算法，适用于在无界或非常大的有序数组中搜索元素。
它首先找到目标元素可能存在的范围，然后在该范围内使用二分搜索。
时间复杂度：O(log n)，空间复杂度：O(1)
"""

from typing import Any, List, Optional
from core.algorithm_base import AlgorithmBase, AlgorithmType


class ExponentialSearch(AlgorithmBase):
    """指数搜索算法实现
    
    特性：
    - 适用于无界搜索
    - 时间复杂度 O(log n)
    - 空间复杂度 O(1)
    - 结合了线性搜索和二分搜索
    """
    
    def __init__(self):
        """初始化指数搜索算法"""
        super().__init__("ExponentialSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行指数搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始指数搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            n = len(data)
            if n == 0:
                self.logger.info("数据列表为空")
                return None
            
            # 如果目标元素是第一个元素
            if data[0] == target:
                self.logger.info(f"找到目标元素 {target} 在位置 0")
                return 0
            
            # 找到目标元素可能存在的范围
            i = 1
            while i < n and data[i] <= target:
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录指数增长步骤
                self.add_step({
                    'type': 'exponential_growth',
                    'index': i,
                    'current_element': data[i],
                    'target': target,
                    'range_size': i
                })
                
                i = i * 2
            
            # 在找到的范围内进行二分搜索
            left = i // 2
            right = min(i, n - 1)
            
            self.logger.info(f"在范围 [{left}, {right}] 内进行二分搜索")
            
            return self._binary_search_range(data, target, left, right)
            
        except Exception as e:
            self.logger.error(f"指数搜索失败: {e}")
            return None
    
    def _binary_search_range(self, data: List[Any], target: Any, left: int, right: int) -> Optional[int]:
        """在指定范围内进行二分搜索
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            left: 左边界
            right: 右边界
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            while left <= right:
                mid = (left + right) // 2
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录二分搜索步骤
                self.add_step({
                    'type': 'binary_search',
                    'left': left,
                    'right': right,
                    'mid': mid,
                    'current_element': data[mid],
                    'target': target
                })
                
                if data[mid] == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 {mid}")
                    self.add_step({
                        'type': 'found',
                        'position': mid,
                        'element': target
                    })
                    return mid
                elif data[mid] < target:
                    left = mid + 1
                    self.add_step({
                        'type': 'move_right',
                        'new_left': left,
                        'new_right': right
                    })
                else:
                    right = mid - 1
                    self.add_step({
                        'type': 'move_left',
                        'new_left': left,
                        'new_right': right
                    })
            
            self.logger.info(f"未找到目标元素 {target}")
            self.add_step({
                'type': 'not_found',
                'target': target
            })
            return None
            
        except Exception as e:
            self.logger.error(f"二分搜索失败: {e}")
            return None
    
    def search_unbounded(self, data_generator, target: Any, max_iterations: int = 1000) -> Optional[int]:
        """无界指数搜索
        
        Args:
            data_generator: 数据生成器函数，接受索引参数
            target: 要搜索的目标元素
            max_iterations: 最大迭代次数
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始无界指数搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            # 检查第一个元素
            try:
                first_element = data_generator(0)
                if first_element == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 0")
                    return 0
            except (IndexError, StopIteration):
                self.logger.info("数据生成器为空")
                return None
            
            # 指数增长阶段
            i = 1
            iteration_count = 0
            
            while iteration_count < max_iterations:
                try:
                    current_element = data_generator(i)
                    self.comparison_count += 1
                    self.operation_count += 1
                    
                    # 记录指数增长步骤
                    self.add_step({
                        'type': 'unbounded_growth',
                        'index': i,
                        'current_element': current_element,
                        'target': target,
                        'range_size': i
                    })
                    
                    if current_element >= target:
                        break
                    
                    i = i * 2
                    iteration_count += 1
                    
                except (IndexError, StopIteration):
                    # 到达数据末尾
                    break
            
            # 在找到的范围内进行二分搜索
            left = i // 2
            right = i
            
            self.logger.info(f"在范围 [{left}, {right}] 内进行二分搜索")
            
            return self._binary_search_unbounded(data_generator, target, left, right)
            
        except Exception as e:
            self.logger.error(f"无界指数搜索失败: {e}")
            return None
    
    def _binary_search_unbounded(self, data_generator, target: Any, left: int, right: int) -> Optional[int]:
        """在无界范围内进行二分搜索
        
        Args:
            data_generator: 数据生成器函数
            target: 要搜索的目标元素
            left: 左边界
            right: 右边界
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            while left <= right:
                mid = (left + right) // 2
                
                try:
                    current_element = data_generator(mid)
                    self.comparison_count += 1
                    self.operation_count += 1
                    
                    # 记录二分搜索步骤
                    self.add_step({
                        'type': 'unbounded_binary_search',
                        'left': left,
                        'right': right,
                        'mid': mid,
                        'current_element': current_element,
                        'target': target
                    })
                    
                    if current_element == target:
                        self.logger.info(f"找到目标元素 {target} 在位置 {mid}")
                        self.add_step({
                            'type': 'found',
                            'position': mid,
                            'element': target
                        })
                        return mid
                    elif current_element < target:
                        left = mid + 1
                        self.add_step({
                            'type': 'move_right',
                            'new_left': left,
                            'new_right': right
                        })
                    else:
                        right = mid - 1
                        self.add_step({
                            'type': 'move_left',
                            'new_left': left,
                            'new_right': right
                        })
                        
                except (IndexError, StopIteration):
                    # 超出数据范围，向左搜索
                    right = mid - 1
                    self.add_step({
                        'type': 'out_of_bounds',
                        'new_left': left,
                        'new_right': right
                    })
            
            self.logger.info(f"未找到目标元素 {target}")
            self.add_step({
                'type': 'not_found',
                'target': target
            })
            return None
            
        except Exception as e:
            self.logger.error(f"无界二分搜索失败: {e}")
            return None
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log n)',
                'worst_case': 'O(log n)'
            },
            'space_complexity': 'O(1)',
            'description': '指数搜索先找到目标范围，然后在该范围内进行二分搜索'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'ExponentialSearch',
            'complexity': 'O(log n)',
            'description': '适用于无界搜索的算法',
            'best_for': '无界数据、流数据',
            'methods': ['search']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行指数搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表或数据生成器
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - data_generator: 数据生成器函数（可选）
                
        Returns:
            搜索结果（位置或None）
        """
        target = kwargs.get('target')
        data_generator = kwargs.get('data_generator')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        if data_generator:
            return self.search_unbounded(data_generator, target)
        elif isinstance(data, list):
            return self.search(data, target)
        else:
            raise ValueError("必须提供数据列表或数据生成器") 