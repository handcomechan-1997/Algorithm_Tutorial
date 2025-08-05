"""
二分搜索算法实现

二分搜索是一种高效的搜索算法，要求数据必须是有序的。
时间复杂度：O(log n)，空间复杂度：O(1)
"""

from typing import Any, List, Optional, Tuple
from core.algorithm_base import AlgorithmBase, AlgorithmType


class BinarySearch(AlgorithmBase):
    """二分搜索算法实现
    
    特性：
    - 要求数据必须有序
    - 时间复杂度 O(log n)
    - 空间复杂度 O(1)
    - 非常高效
    """
    
    def __init__(self):
        """初始化二分搜索算法"""
        super().__init__("BinarySearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行二分搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始二分搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            left, right = 0, len(data) - 1
            
            while left <= right:
                mid = (left + right) // 2
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'compare',
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
    
    def search_first_occurrence(self, data: List[Any], target: Any) -> Optional[int]:
        """搜索目标元素的第一次出现位置
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素第一次出现的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始二分搜索第一次出现位置，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            left, right = 0, len(data) - 1
            result = None
            
            while left <= right:
                mid = (left + right) // 2
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'compare',
                    'left': left,
                    'right': right,
                    'mid': mid,
                    'current_element': data[mid],
                    'target': target
                })
                
                if data[mid] == target:
                    result = mid
                    right = mid - 1  # 继续向左搜索
                    self.add_step({
                        'type': 'found_continue_left',
                        'position': mid,
                        'new_left': left,
                        'new_right': right
                    })
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
            
            if result is not None:
                self.logger.info(f"找到目标元素 {target} 第一次出现在位置 {result}")
            else:
                self.logger.info(f"未找到目标元素 {target}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"二分搜索第一次出现位置失败: {e}")
            return None
    
    def search_last_occurrence(self, data: List[Any], target: Any) -> Optional[int]:
        """搜索目标元素的最后一次出现位置
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素最后一次出现的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始二分搜索最后一次出现位置，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            left, right = 0, len(data) - 1
            result = None
            
            while left <= right:
                mid = (left + right) // 2
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'compare',
                    'left': left,
                    'right': right,
                    'mid': mid,
                    'current_element': data[mid],
                    'target': target
                })
                
                if data[mid] == target:
                    result = mid
                    left = mid + 1  # 继续向右搜索
                    self.add_step({
                        'type': 'found_continue_right',
                        'position': mid,
                        'new_left': left,
                        'new_right': right
                    })
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
            
            if result is not None:
                self.logger.info(f"找到目标元素 {target} 最后一次出现在位置 {result}")
            else:
                self.logger.info(f"未找到目标元素 {target}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"二分搜索最后一次出现位置失败: {e}")
            return None
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息
        
        Returns:
            复杂度信息字典
        """
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log n)',
                'worst_case': 'O(log n)'
            },
            'space_complexity': 'O(1)',
            'description': '二分搜索通过不断缩小搜索范围来快速定位目标元素'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'BinarySearch',
            'complexity': 'O(log n)',
            'description': '高效的有序数组搜索算法',
            'best_for': '有序数组、大数据集',
            'methods': ['search', 'search_first_occurrence', 'search_last_occurrence']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行二分搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - search_type: 搜索类型（'basic', 'first', 'last'）
                
        Returns:
            搜索结果（位置或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        search_type = kwargs.get('search_type', 'basic')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        if search_type == 'first':
            return self.search_first_occurrence(data, target)
        elif search_type == 'last':
            return self.search_last_occurrence(data, target)
        else:
            return self.search(data, target) 