"""
插值搜索算法实现

插值搜索是二分搜索的改进版本，适用于均匀分布的有序数据。
它通过线性插值来估计目标元素的位置，从而减少搜索次数。
时间复杂度：O(log log n) 平均情况，O(n) 最坏情况
"""

from typing import Any, List, Optional
from core.algorithm_base import AlgorithmBase, AlgorithmType


class InterpolationSearch(AlgorithmBase):
    """插值搜索算法实现
    
    特性：
    - 适用于均匀分布的有序数据
    - 平均时间复杂度 O(log log n)
    - 最坏情况时间复杂度 O(n)
    - 空间复杂度 O(1)
    """
    
    def __init__(self):
        """初始化插值搜索算法"""
        super().__init__("InterpolationSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行插值搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始插值搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            n = len(data)
            if n == 0:
                self.logger.info("数据列表为空")
                return None
            
            left, right = 0, n - 1
            
            # 检查边界条件
            if target < data[left] or target > data[right]:
                self.logger.info(f"目标元素 {target} 超出范围 [{data[left]}, {data[right]}]")
                return None
            
            while left <= right and data[left] <= target <= data[right]:
                # 避免除零错误
                if data[right] == data[left]:
                    if data[left] == target:
                        self.logger.info(f"找到目标元素 {target} 在位置 {left}")
                        return left
                    else:
                        break
                
                # 计算插值位置
                pos = left + int(((target - data[left]) * (right - left)) / (data[right] - data[left]))
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'interpolate',
                    'left': left,
                    'right': right,
                    'pos': pos,
                    'data_left': data[left],
                    'data_right': data[right],
                    'target': target
                })
                
                self.comparison_count += 1
                if data[pos] == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 {pos}")
                    self.add_step({
                        'type': 'found',
                        'position': pos,
                        'element': target
                    })
                    return pos
                
                self.comparison_count += 1
                if data[pos] < target:
                    left = pos + 1
                    self.add_step({
                        'type': 'move_right',
                        'new_left': left,
                        'new_right': right
                    })
                else:
                    right = pos - 1
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
            self.logger.error(f"插值搜索失败: {e}")
            return None
    
    def search_with_bounds_check(self, data: List[Any], target: Any) -> Optional[int]:
        """带边界检查的插值搜索
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        try:
            self.logger.info(f"开始带边界检查的插值搜索，目标元素: {target}")
            self.operation_count = 0
            self.comparison_count = 0
            
            n = len(data)
            if n == 0:
                self.logger.info("数据列表为空")
                return None
            
            left, right = 0, n - 1
            
            while left <= right:
                # 边界检查
                if target < data[left] or target > data[right]:
                    self.logger.info(f"目标元素 {target} 超出当前范围 [{data[left]}, {data[right]}]")
                    break
                
                # 避免除零错误
                if data[right] == data[left]:
                    if data[left] == target:
                        self.logger.info(f"找到目标元素 {target} 在位置 {left}")
                        return left
                    else:
                        break
                
                # 计算插值位置
                pos = left + int(((target - data[left]) * (right - left)) / (data[right] - data[left]))
                
                # 确保位置在有效范围内
                pos = max(left, min(right, pos))
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'interpolate_with_bounds',
                    'left': left,
                    'right': right,
                    'pos': pos,
                    'data_left': data[left],
                    'data_right': data[right],
                    'target': target
                })
                
                self.comparison_count += 1
                if data[pos] == target:
                    self.logger.info(f"找到目标元素 {target} 在位置 {pos}")
                    self.add_step({
                        'type': 'found',
                        'position': pos,
                        'element': target
                    })
                    return pos
                
                self.comparison_count += 1
                if data[pos] < target:
                    left = pos + 1
                    self.add_step({
                        'type': 'move_right',
                        'new_left': left,
                        'new_right': right
                    })
                else:
                    right = pos - 1
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
            self.logger.error(f"带边界检查的插值搜索失败: {e}")
            return None
    
    def is_uniformly_distributed(self, data: List[Any], tolerance: float = 0.1) -> bool:
        """检查数据是否均匀分布
        
        Args:
            data: 要检查的数据列表
            tolerance: 容差，用于判断是否均匀分布
            
        Returns:
            如果数据均匀分布返回True，否则返回False
        """
        if len(data) < 3:
            return True
        
        try:
            # 计算相邻元素的差值
            differences = []
            for i in range(1, len(data)):
                diff = abs(data[i] - data[i-1])
                differences.append(diff)
            
            if not differences:
                return True
            
            # 计算平均差值
            avg_diff = sum(differences) / len(differences)
            
            # 检查差值是否接近平均值
            for diff in differences:
                if abs(diff - avg_diff) / avg_diff > tolerance:
                    return False
            
            return True
            
        except Exception:
            return False
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log log n)',
                'worst_case': 'O(n)'
            },
            'space_complexity': 'O(1)',
            'description': '插值搜索通过线性插值估计目标位置，适用于均匀分布的数据'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'InterpolationSearch',
            'complexity': 'O(log log n)',
            'description': '适用于均匀分布数据的改进二分搜索',
            'best_for': '均匀分布的有序数据',
            'methods': ['search']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行插值搜索算法（实现抽象基类方法）
        
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