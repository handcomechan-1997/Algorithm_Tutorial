"""
线性搜索算法实现

线性搜索是最基本的搜索算法，逐个检查每个元素直到找到目标。
时间复杂度：O(n)，空间复杂度：O(1)
"""

from typing import Any, List, Optional, Callable
from core.algorithm_base import AlgorithmBase, AlgorithmType


class LinearSearch(AlgorithmBase):
    """线性搜索算法实现
    
    特性：
    - 适用于任何数据结构
    - 时间复杂度 O(n)
    - 空间复杂度 O(1)
    - 简单易懂
    """
    
    def __init__(self):
        """初始化线性搜索算法"""
        super().__init__("LinearSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行基本线性搜索
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始线性搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            for i, element in enumerate(data):
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'compare',
                    'index': i,
                    'current_element': element,
                    'target': target
                })
                
                if element == target:
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
            self.logger.error(f"线性搜索失败: {e}")
            return None
    
    def search_with_condition(self, data: List[Any], condition: Callable[[Any], bool]) -> Optional[int]:
        """使用自定义条件进行搜索
        
        Args:
            data: 要搜索的数据列表
            condition: 自定义条件函数
            
        Returns:
            满足条件的第一个元素位置，如果未找到返回None
        """
        try:
            self.logger.info("开始条件线性搜索")
            self.operation_count = 0
            self.comparison_count = 0
            
            for i, element in enumerate(data):
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'check_condition',
                    'index': i,
                    'current_element': element
                })
                
                if condition(element):
                    self.logger.info(f"找到满足条件的元素在位置 {i}: {element}")
                    self.add_step({
                        'type': 'condition_met',
                        'position': i,
                        'element': element
                    })
                    return i
            
            self.logger.info("未找到满足条件的元素")
            self.add_step({
                'type': 'condition_not_met'
            })
            return None
            
        except Exception as e:
            self.logger.error(f"条件线性搜索失败: {e}")
            return None
    
    def search_all_occurrences(self, data: List[Any], target: Any) -> List[int]:
        """搜索目标元素的所有出现位置
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素所有出现位置的列表
        """
        try:
            self.logger.info(f"开始搜索所有出现位置，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            occurrences = []
            
            for i, element in enumerate(data):
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'compare',
                    'index': i,
                    'current_element': element,
                    'target': target,
                    'found_count': len(occurrences)
                })
                
                if element == target:
                    occurrences.append(i)
                    self.add_step({
                        'type': 'found_occurrence',
                        'position': i,
                        'total_found': len(occurrences)
                    })
            
            self.logger.info(f"找到 {len(occurrences)} 个目标元素 {target}")
            self.add_step({
                'type': 'search_complete',
                'occurrences': occurrences,
                'count': len(occurrences)
            })
            return occurrences
            
        except Exception as e:
            self.logger.error(f"搜索所有出现位置失败: {e}")
            return []
    
    def search_sentinel(self, data: List[Any], target: Any) -> Optional[int]:
        """哨兵线性搜索（优化版本）
        
        通过添加哨兵元素来减少比较次数
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始哨兵线性搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            # 添加哨兵元素
            original_length = len(data)
            data.append(target)
            
            i = 0
            while data[i] != target:
                i += 1
                self.comparison_count += 1
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'sentinel_compare',
                    'index': i,
                    'current_element': data[i],
                    'target': target
                })
            
            # 移除哨兵元素
            data.pop()
            
            if i < original_length:
                self.logger.info(f"找到目标元素 {target} 在位置 {i}")
                self.add_step({
                    'type': 'found',
                    'position': i,
                    'element': target
                })
                return i
            else:
                self.logger.info(f"未找到目标元素 {target}")
                self.add_step({
                    'type': 'not_found',
                    'target': target
                })
                return None
                
        except Exception as e:
            self.logger.error(f"哨兵线性搜索失败: {e}")
            return None
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(n/2)',
                'worst_case': 'O(n)'
            },
            'space_complexity': 'O(1)',
            'description': '线性搜索逐个检查每个元素，直到找到目标或遍历完所有元素'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'LinearSearch',
            'complexity': 'O(n)',
            'description': '最基本的搜索算法，逐个检查每个元素',
            'best_for': '小数据集、无序数据',
            'methods': ['search', 'search_with_condition', 'search_all_occurrences', 'search_sentinel']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行线性搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - condition: 自定义条件函数（可选）
                - search_type: 搜索类型（'basic', 'condition', 'all', 'sentinel'）
                
        Returns:
            搜索结果（位置、位置列表或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        condition = kwargs.get('condition')
        search_type = kwargs.get('search_type', 'basic')
        
        if search_type == 'condition' and condition:
            return self.search_with_condition(data, condition)
        elif search_type == 'all' and target:
            return self.search_all_occurrences(data, target)
        elif search_type == 'sentinel' and target:
            return self.search_sentinel(data, target)
        elif target:
            return self.search(data, target)
        else:
            raise ValueError("必须提供target参数或condition参数") 