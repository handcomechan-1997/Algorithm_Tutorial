"""
算法管理器 - 负责管理和组织所有算法实例
"""

import threading
from typing import Dict, List, Optional, Any
from collections import defaultdict

from .algorithm_base import AlgorithmBase, AlgorithmType
from .data_structures import DataStructureBase, DataStructureType
from utils.logger import Logger

class AlgorithmManager:
    """算法管理器
    
    该类负责管理平台中的所有算法和数据结构实例，提供：
    - 算法注册和查找
    - 分类管理
    - 性能比较
    - 批量执行
    
    在学习过程中，可以通过此类来组织和访问各种算法。
    """
    
    def __init__(self):
        """初始化算法管理器"""
        self.logger = Logger()
        
        # 算法存储
        self.algorithms: Dict[str, AlgorithmBase] = {}
        self.algorithms_by_type: Dict[AlgorithmType, List[AlgorithmBase]] = defaultdict(list)
        
        # 数据结构存储
        self.data_structures: Dict[str, DataStructureBase] = {}
        self.data_structures_by_type: Dict[DataStructureType, List[DataStructureBase]] = defaultdict(list)
        
        # 线程安全
        self.lock = threading.RLock()
        
        self.logger.info("算法管理器初始化完成")
    
    def initialize(self):
        """初始化所有算法和数据结构"""
        self.logger.info("正在初始化算法和数据结构...")
        
        # 注册数据结构
        self._register_data_structures()
        
        # 注册算法
        self._register_algorithms()
        
        self.logger.info(f"初始化完成，共注册 {len(self.algorithms)} 个算法，{len(self.data_structures)} 个数据结构")
    
    def register_algorithm(self, algorithm: AlgorithmBase):
        """注册算法
        
        Args:
            algorithm: 要注册的算法实例
        """
        with self.lock:
            self.algorithms[algorithm.name] = algorithm
            self.algorithms_by_type[algorithm.algorithm_type].append(algorithm)
            self.logger.info(f"注册算法: {algorithm.name}")
    
    def register_data_structure(self, data_structure: DataStructureBase):
        """注册数据结构
        
        Args:
            data_structure: 要注册的数据结构实例
        """
        with self.lock:
            self.data_structures[data_structure.name] = data_structure
            self.data_structures_by_type[data_structure.data_type].append(data_structure)
            self.logger.info(f"注册数据结构: {data_structure.name}")
    
    def get_algorithm(self, name: str) -> Optional[AlgorithmBase]:
        """根据名称获取算法
        
        Args:
            name: 算法名称
            
        Returns:
            算法实例，如果未找到返回None
        """
        with self.lock:
            return self.algorithms.get(name)
    
    def get_data_structure(self, name: str) -> Optional[DataStructureBase]:
        """根据名称获取数据结构
        
        Args:
            name: 数据结构名称
            
        Returns:
            数据结构实例，如果未找到返回None
        """
        with self.lock:
            return self.data_structures.get(name)
    
    def get_algorithms_by_type(self, algorithm_type: AlgorithmType) -> List[AlgorithmBase]:
        """根据类型获取算法列表
        
        Args:
            algorithm_type: 算法类型
            
        Returns:
            该类型的所有算法列表
        """
        with self.lock:
            return self.algorithms_by_type[algorithm_type].copy()
    
    def get_data_structures_by_type(self, data_type: DataStructureType) -> List[DataStructureBase]:
        """根据类型获取数据结构列表
        
        Args:
            data_type: 数据结构类型
            
        Returns:
            该类型的所有数据结构列表
        """
        with self.lock:
            return self.data_structures_by_type[data_type].copy()
    
    def get_all_algorithms(self) -> List[AlgorithmBase]:
        """获取所有算法列表"""
        with self.lock:
            return list(self.algorithms.values())
    
    def get_all_data_structures(self) -> List[DataStructureBase]:
        """获取所有数据结构列表"""
        with self.lock:
            return list(self.data_structures.values())
    
    def compare_algorithms(self, algorithm_names: List[str], test_data: Any, **kwargs) -> Dict[str, Any]:
        """比较多个算法的性能
        
        Args:
            algorithm_names: 要比较的算法名称列表
            test_data: 测试数据
            **kwargs: 额外参数
            
        Returns:
            性能比较结果
        """
        results = {}
        
        for name in algorithm_names:
            algorithm = self.get_algorithm(name)
            if algorithm:
                try:
                    performance = algorithm.measure_performance(test_data, **kwargs)
                    results[name] = performance
                    self.logger.info(f"算法 '{name}' 性能测试完成")
                except Exception as e:
                    self.logger.error(f"算法 '{name}' 性能测试失败: {e}")
                    results[name] = {'error': str(e)}
            else:
                self.logger.warning(f"算法 '{name}' 未找到")
                results[name] = {'error': 'Algorithm not found'}
        
        return results
    
    def get_algorithm_categories(self) -> Dict[str, List[str]]:
        """获取算法分类信息
        
        Returns:
            按类型分组的算法名称字典
        """
        with self.lock:
            categories = {}
            for algorithm_type, algorithms in self.algorithms_by_type.items():
                categories[algorithm_type.value] = [alg.name for alg in algorithms]
            return categories
    
    def get_data_structure_categories(self) -> Dict[str, List[str]]:
        """获取数据结构分类信息
        
        Returns:
            按类型分组的数据结构名称字典
        """
        with self.lock:
            categories = {}
            for data_type, data_structures in self.data_structures_by_type.items():
                categories[data_type.value] = [ds.name for ds in data_structures]
            return categories
    
    def _register_data_structures(self):
        """注册所有数据结构"""
        # TODO: 在这里注册所有数据结构
        # 例如：
        # from data_structures.array import Array
        # self.register_data_structure(Array("动态数组"))
        pass
    
    def _register_algorithms(self):
        """注册所有算法"""
        # TODO: 在这里注册所有算法
        # 例如：
        # from sorting.basic_sorting import BubbleSort
        # self.register_algorithm(BubbleSort())
        pass
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取管理器统计信息"""
        with self.lock:
            return {
                'total_algorithms': len(self.algorithms),
                'total_data_structures': len(self.data_structures),
                'algorithm_types': len(self.algorithms_by_type),
                'data_structure_types': len(self.data_structures_by_type),
                'algorithm_categories': self.get_algorithm_categories(),
                'data_structure_categories': self.get_data_structure_categories()
            } 