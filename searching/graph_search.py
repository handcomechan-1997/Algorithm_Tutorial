"""
图搜索算法实现

包含深度优先搜索(DFS)和广度优先搜索(BFS)算法。
这些算法用于遍历图结构，寻找路径或连通分量。

学习目标：
1. 理解图搜索的基本概念
2. 掌握深度优先搜索的实现
3. 掌握广度优先搜索的实现
4. 学会处理路径查找问题
"""

from typing import Any, List, Optional, Set, Dict, Tuple
from core.algorithm_base import AlgorithmBase, AlgorithmType
from data_structures.graph import Graph


class DepthFirstSearch(AlgorithmBase):
    """深度优先搜索算法实现
    
    特性：
    - 使用栈或递归实现
    - 优先探索深层节点
    - 时间复杂度 O(V + E)
    - 空间复杂度 O(V)
    
    学习要点：
    1. 理解深度优先的搜索策略
    2. 掌握递归或栈的实现方式
    3. 学会记录访问状态和路径
    4. 理解回溯的概念
    """
    
    def __init__(self):
        """初始化深度优先搜索算法"""
        super().__init__("DepthFirstSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any = None) -> List[Any]:
        """执行深度优先搜索
        
        TODO: 请实现深度优先搜索算法
        
        实现思路：
        1. 初始化访问集合和结果列表
        2. 定义递归函数 dfs_recursive(vertex)：
           - 如果顶点已访问，直接返回
           - 将顶点标记为已访问，加入结果列表
           - 如果找到目标顶点，可以提前结束
           - 递归访问所有未访问的邻居
        3. 从起始顶点开始递归搜索
        
        关键点：
        - 使用 visited 集合记录已访问的顶点
        - 使用递归或栈实现深度优先
        - 记录搜索步骤和访问顺序
        
        提示：
        - 使用 set() 创建访问集合
        - 使用递归函数实现深度优先
        - 使用 graph.get_neighbors(vertex) 获取邻居
        - 记录搜索步骤和访问状态
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点（可选）
            
        Returns:
            访问顶点的顺序列表
        """
        # TODO: 在这里实现深度优先搜索算法
        pass
    
    def find_path(self, graph: Graph, start_vertex: Any, target_vertex: Any) -> Optional[List[Any]]:
        """查找从起始顶点到目标顶点的路径
        
        TODO: 请实现路径查找算法
        
        实现思路：
        1. 使用深度优先搜索查找路径
        2. 记录路径信息（可以使用字典或列表）
        3. 当找到目标顶点时，重建路径
        4. 如果没找到路径，返回 None
        
        关键点：
        - 需要记录路径信息以便重建
        - 可以使用回溯或路径记录
        - 处理路径不存在的情况
        
        提示：
        - 使用字典记录父节点关系
        - 使用列表记录当前路径
        - 当找到目标时重建完整路径
        - 记录搜索步骤和路径信息
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            
        Returns:
            路径列表，如果不存在路径返回None
        """
        # TODO: 在这里实现路径查找算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(V + E)',
                'worst_case': 'O(V + E)'
            },
            'space_complexity': 'O(V)',
            'description': '深度优先搜索使用递归或栈，优先探索深层节点'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'DepthFirstSearch',
            'complexity': 'O(V + E)',
            'description': '深度优先图遍历算法',
            'best_for': '图遍历、拓扑排序',
            'methods': ['search', 'find_path']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行深度优先搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的图对象
            **kwargs: 额外参数，包括：
                - start_vertex: 起始顶点
                - target_vertex: 目标顶点（可选）
                - search_type: 搜索类型（'traversal', 'path'）
                
        Returns:
            搜索结果（访问顺序列表或路径）
        """
        if not hasattr(data, 'get_neighbors'):
            raise ValueError("输入数据必须是图对象")
        
        start_vertex = kwargs.get('start_vertex')
        target_vertex = kwargs.get('target_vertex')
        search_type = kwargs.get('search_type', 'traversal')
        
        if not start_vertex:
            raise ValueError("必须提供start_vertex参数")
        
        if search_type == 'path' and target_vertex:
            return self.find_path(data, start_vertex, target_vertex)
        else:
            return self.search(data, start_vertex, target_vertex)


class BreadthFirstSearch(AlgorithmBase):
    """广度优先搜索算法实现
    
    特性：
    - 使用队列实现
    - 优先探索近邻节点
    - 时间复杂度 O(V + E)
    - 空间复杂度 O(V)
    
    学习要点：
    1. 理解广度优先的搜索策略
    2. 掌握队列的实现方式
    3. 学会记录访问状态和层次
    4. 理解最短路径的概念
    """
    
    def __init__(self):
        """初始化广度优先搜索算法"""
        super().__init__("BreadthFirstSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any = None) -> List[Any]:
        """执行广度优先搜索
        
        TODO: 请实现广度优先搜索算法
        
        实现思路：
        1. 初始化访问集合、结果列表和队列
        2. 将起始顶点加入队列和访问集合
        3. 当队列不为空时：
           - 从队列取出一个顶点
           - 将顶点加入结果列表
           - 如果找到目标顶点，可以提前结束
           - 将所有未访问的邻居加入队列
        4. 返回访问顺序列表
        
        关键点：
        - 使用队列实现广度优先
        - 使用 visited 集合记录已访问的顶点
        - 记录搜索步骤和访问顺序
        
        提示：
        - 使用列表作为队列（append 入队，pop(0) 出队）
        - 使用 set() 创建访问集合
        - 使用 graph.get_neighbors(vertex) 获取邻居
        - 记录搜索步骤和队列状态
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点（可选）
            
        Returns:
            访问顶点的顺序列表
        """
        # TODO: 在这里实现广度优先搜索算法
        pass
    
    def find_shortest_path(self, graph: Graph, start_vertex: Any, target_vertex: Any) -> Optional[List[Any]]:
        """查找从起始顶点到目标顶点的最短路径
        
        TODO: 请实现最短路径查找算法
        
        实现思路：
        1. 使用广度优先搜索查找最短路径
        2. 记录父节点关系以便重建路径
        3. 当找到目标顶点时，重建路径
        4. 如果没找到路径，返回 None
        
        关键点：
        - 广度优先搜索保证找到的是最短路径
        - 需要记录父节点关系
        - 处理路径不存在的情况
        
        提示：
        - 使用字典记录父节点关系
        - 使用队列存储 (vertex, distance) 元组
        - 当找到目标时重建完整路径
        - 记录搜索步骤和距离信息
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            
        Returns:
            最短路径列表，如果不存在路径返回None
        """
        # TODO: 在这里实现最短路径查找算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(V + E)',
                'worst_case': 'O(V + E)'
            },
            'space_complexity': 'O(V)',
            'description': '广度优先搜索使用队列，优先探索近邻节点'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'BreadthFirstSearch',
            'complexity': 'O(V + E)',
            'description': '广度优先图遍历算法',
            'best_for': '最短路径、层次遍历',
            'methods': ['search', 'find_shortest_path']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行广度优先搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的图对象
            **kwargs: 额外参数，包括：
                - start_vertex: 起始顶点
                - target_vertex: 目标顶点（可选）
                - search_type: 搜索类型（'traversal', 'shortest_path'）
                
        Returns:
            搜索结果（访问顺序列表或最短路径）
        """
        if not hasattr(data, 'get_neighbors'):
            raise ValueError("输入数据必须是图对象")
        
        start_vertex = kwargs.get('start_vertex')
        target_vertex = kwargs.get('target_vertex')
        search_type = kwargs.get('search_type', 'traversal')
        
        if not start_vertex:
            raise ValueError("必须提供start_vertex参数")
        
        if search_type == 'shortest_path' and target_vertex:
            return self.find_shortest_path(data, start_vertex, target_vertex)
        else:
            return self.search(data, start_vertex, target_vertex) 