"""
算法基类 - 定义所有算法的通用接口
"""

import time
import threading
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum

from utils.logger import Logger

class AlgorithmType(Enum):
    """算法类型枚举"""
    SORTING = "sorting"
    SEARCHING = "searching"
    GRAPH = "graph"
    DYNAMIC_PROGRAMMING = "dynamic_programming"
    GREEDY = "greedy"
    DIVIDE_AND_CONQUER = "divide_and_conquer"

class AlgorithmComplexity(Enum):
    """算法复杂度枚举"""
    O_1 = "O(1)"
    O_LOG_N = "O(log n)"
    O_N = "O(n)"
    O_N_LOG_N = "O(n log n)"
    O_N_SQUARED = "O(n²)"
    O_N_CUBED = "O(n³)"
    O_2_N = "O(2ⁿ)"
    O_N_FACTORIAL = "O(n!)"

class AlgorithmBase(ABC):
    """算法基类
    
    该类定义了所有算法的通用接口，包括：
    - 算法执行方法
    - 性能统计
    - 可视化支持
    - 复杂度分析
    
    在学习过程中，可以继承此类来实现具体的算法。
    """
    
    def __init__(self, name: str, algorithm_type: AlgorithmType):
        """初始化算法基类"""
        self.name = name
        self.algorithm_type = algorithm_type
        self.logger = Logger()
        
        # 性能统计
        self.execution_time = 0.0
        self.memory_usage = 0
        self.comparison_count = 0
        self.swap_count = 0
        
        # 复杂度信息
        self.time_complexity = AlgorithmComplexity.O_N
        self.space_complexity = AlgorithmComplexity.O_1
        self.best_case = AlgorithmComplexity.O_N
        self.worst_case = AlgorithmComplexity.O_N_SQUARED
        self.average_case = AlgorithmComplexity.O_N_SQUARED
        
        # 执行状态
        self.is_running = False
        self.execution_steps = []
        self.current_step = 0
        
        # 线程安全
        self.lock = threading.RLock()
        
        self.logger.info(f"算法 '{name}' 初始化完成")
    
    @abstractmethod
    def execute(self, data: Any, **kwargs) -> Any:
        """执行算法
        
        Args:
            data: 输入数据
            **kwargs: 额外参数
            
        Returns:
            算法执行结果
        """
        pass
    
    def reset_stats(self):
        """重置性能统计"""
        with self.lock:
            self.execution_time = 0.0
            self.memory_usage = 0
            self.comparison_count = 0
            self.swap_count = 0
            self.execution_steps = []
            self.current_step = 0
    
    def measure_performance(self, data: Any, **kwargs) -> Dict[str, Any]:
        """测量算法性能
        
        Args:
            data: 输入数据
            **kwargs: 额外参数
            
        Returns:
            性能统计信息
        """
        with self.lock:
            self.reset_stats()
            self.is_running = True
            
            # 记录开始时间和内存使用
            start_time = time.time()
            start_memory = self._get_memory_usage()
            
            try:
                # 执行算法
                result = self.execute(data, **kwargs)
                
                # 记录结束时间和内存使用
                end_time = time.time()
                end_memory = self._get_memory_usage()
                
                self.execution_time = end_time - start_time
                self.memory_usage = end_memory - start_memory
                
                self.logger.info(f"算法 '{self.name}' 执行完成，耗时: {self.execution_time:.4f}秒")
                
                return {
                    'result': result,
                    'execution_time': self.execution_time,
                    'memory_usage': self.memory_usage,
                    'comparison_count': self.comparison_count,
                    'swap_count': self.swap_count,
                    'steps_count': len(self.execution_steps)
                }
                
            finally:
                self.is_running = False
    
    def add_step(self, step_description: str, data_state: Any = None):
        """添加执行步骤（用于可视化）
        
        Args:
            step_description: 步骤描述
            data_state: 当前数据状态
        """
        with self.lock:
            step = {
                'step': self.current_step,
                'description': step_description,
                'data_state': data_state,
                'comparisons': self.comparison_count,
                'swaps': self.swap_count
            }
            self.execution_steps.append(step)
            self.current_step += 1
    
    def get_complexity_info(self) -> Dict[str, str]:
        """获取算法复杂度信息"""
        return {
            'time_complexity': self.time_complexity.value,
            'space_complexity': self.space_complexity.value,
            'best_case': self.best_case.value,
            'worst_case': self.worst_case.value,
            'average_case': self.average_case.value
        }
    
    def get_execution_steps(self) -> List[Dict[str, Any]]:
        """获取执行步骤（用于可视化）"""
        with self.lock:
            return self.execution_steps.copy()
    
    def _get_memory_usage(self) -> int:
        """获取当前内存使用量（简化实现）"""
        try:
            import psutil
            process = psutil.Process()
            return process.memory_info().rss
        except ImportError:
            return 0
    
    def __str__(self) -> str:
        return f"{self.name} ({self.algorithm_type.value})"
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' type='{self.algorithm_type.value}'>" 