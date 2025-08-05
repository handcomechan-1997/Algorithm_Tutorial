"""
启发式搜索算法实现

包含A*搜索算法，这是一种结合了Dijkstra算法和启发式函数的搜索算法。
适用于寻找最优路径的问题。
"""

import heapq
from typing import Any, List, Optional, Set, Dict, Tuple, Callable
from core.algorithm_base import AlgorithmBase, AlgorithmType
from data_structures.graph import Graph


class AStarSearch(AlgorithmBase):
    """A*搜索算法实现
    
    特性：
    - 结合了Dijkstra算法和启发式函数
    - 使用优先队列（最小堆）
    - 时间复杂度取决于启发式函数的质量
    - 空间复杂度 O(V)
    """
    
    def __init__(self):
        """初始化A*搜索算法"""
        super().__init__("AStarSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any, 
               heuristic_func: Callable[[Any, Any], float] = None) -> Optional[List[Any]]:
        """执行A*搜索
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            heuristic_func: 启发式函数，用于估计从顶点到目标的距离
            
        Returns:
            最优路径列表，如果不存在路径返回None
        """
        try:
            self.logger.info(f"开始A*搜索: {start_vertex} -> {target_vertex}")
            self.operation_count = 0
            self.comparison_count = 0
            
            # 如果没有提供启发式函数，使用默认的（总是返回0）
            if heuristic_func is None:
                heuristic_func = lambda x, y: 0
            
            # 初始化数据结构
            open_set = []  # 优先队列，存储待访问的顶点
            closed_set = set()  # 已访问的顶点
            came_from = {}  # 记录路径
            g_score = {start_vertex: 0}  # 从起点到当前顶点的实际距离
            f_score = {start_vertex: heuristic_func(start_vertex, target_vertex)}  # f = g + h
            
            # 将起始顶点加入开放集
            heapq.heappush(open_set, (f_score[start_vertex], start_vertex))
            
            while open_set:
                current_f, current_vertex = heapq.heappop(open_set)
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'visit',
                    'vertex': current_vertex,
                    'f_score': current_f,
                    'g_score': g_score.get(current_vertex, float('inf')),
                    'open_set_size': len(open_set),
                    'closed_set_size': len(closed_set)
                })
                
                # 如果到达目标顶点
                if current_vertex == target_vertex:
                    path = self._reconstruct_path(came_from, current_vertex)
                    self.add_step({
                        'type': 'path_found',
                        'path': path,
                        'total_cost': g_score[current_vertex]
                    })
                    self.logger.info(f"A*搜索完成，找到路径: {' -> '.join(map(str, path))}")
                    return path
                
                closed_set.add(current_vertex)
                
                # 检查所有邻居
                neighbors = graph.get_neighbors(current_vertex)
                for neighbor, weight in neighbors:
                    self.comparison_count += 1
                    
                    # 如果邻居已经在关闭集中，跳过
                    if neighbor in closed_set:
                        continue
                    
                    # 计算从起点经过当前顶点到邻居的距离
                    tentative_g_score = g_score[current_vertex] + weight
                    
                    # 如果邻居不在开放集中，或者找到了更好的路径
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current_vertex
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + heuristic_func(neighbor, target_vertex)
                        
                        # 将邻居加入开放集
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        
                        self.add_step({
                            'type': 'explore',
                            'from_vertex': current_vertex,
                            'to_vertex': neighbor,
                            'weight': weight,
                            'g_score': tentative_g_score,
                            'f_score': f_score[neighbor]
                        })
            
            # 如果没有找到路径
            self.logger.info(f"未找到从 {start_vertex} 到 {target_vertex} 的路径")
            self.add_step({
                'type': 'no_path_found',
                'start': start_vertex,
                'target': target_vertex
            })
            return None
            
        except Exception as e:
            self.logger.error(f"A*搜索失败: {e}")
            return None
    
    def _reconstruct_path(self, came_from: Dict[Any, Any], current: Any) -> List[Any]:
        """重建路径
        
        Args:
            came_from: 路径记录字典
            current: 当前顶点
            
        Returns:
            路径列表
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
    
    def search_with_multiple_goals(self, graph: Graph, start_vertex: Any, 
                                 target_vertices: List[Any],
                                 heuristic_func: Callable[[Any, Any], float] = None) -> Dict[Any, List[Any]]:
        """搜索到多个目标的最短路径
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertices: 目标顶点列表
            heuristic_func: 启发式函数
            
        Returns:
            到每个目标的路径字典
        """
        try:
            self.logger.info(f"开始A*搜索到多个目标: {start_vertex} -> {target_vertices}")
            results = {}
            
            for target in target_vertices:
                path = self.search(graph, start_vertex, target, heuristic_func)
                results[target] = path
            
            return results
            
        except Exception as e:
            self.logger.error(f"多目标A*搜索失败: {e}")
            return {}
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(E log V)',
                'worst_case': 'O(V log V)'
            },
            'space_complexity': 'O(V)',
            'description': 'A*搜索的时间复杂度取决于启发式函数的质量'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'AStarSearch',
            'complexity': 'O(E log V)',
            'description': '启发式搜索算法，结合Dijkstra和启发式函数',
            'best_for': '路径规划、游戏AI',
            'methods': ['search', 'find_path']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行A*搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的图对象
            **kwargs: 额外参数，包括：
                - start_vertex: 起始顶点
                - target_vertex: 目标顶点
                - heuristic: 启发式函数
                - search_type: 搜索类型（'traversal', 'path'）
                
        Returns:
            搜索结果（访问顺序列表或路径）
        """
        if not hasattr(data, 'get_neighbors'):
            raise ValueError("输入数据必须是图对象")
        
        start_vertex = kwargs.get('start_vertex')
        target_vertex = kwargs.get('target_vertex')
        heuristic = kwargs.get('heuristic')
        search_type = kwargs.get('search_type', 'traversal')
        
        if not start_vertex or not target_vertex:
            raise ValueError("必须提供start_vertex和target_vertex参数")
        
        if not heuristic:
            raise ValueError("必须提供heuristic参数")
        
        # A*搜索总是返回路径，所以search_type参数在这里不起作用
        return self.search(data, start_vertex, target_vertex, heuristic)
    
    def create_manhattan_heuristic(self) -> Callable[[Any, Any], float]:
        """创建曼哈顿距离启发式函数
        
        Returns:
            曼哈顿距离启发式函数
        """
        def manhattan_distance(pos1: Any, pos2: Any) -> float:
            """计算曼哈顿距离
            
            Args:
                pos1: 位置1
                pos2: 位置2
                
            Returns:
                曼哈顿距离
            """
            if isinstance(pos1, (list, tuple)) and isinstance(pos2, (list, tuple)):
                return sum(abs(a - b) for a, b in zip(pos1, pos2))
            else:
                return abs(pos1 - pos2) if isinstance(pos1, (int, float)) else 0
        
        return manhattan_distance
    
    def create_euclidean_heuristic(self) -> Callable[[Any, Any], float]:
        """创建欧几里得距离启发式函数
        
        Returns:
            欧几里得距离启发式函数
        """
        import math
        
        def euclidean_distance(pos1: Any, pos2: Any) -> float:
            """计算欧几里得距离
            
            Args:
                pos1: 位置1
                pos2: 位置2
                
            Returns:
                欧几里得距离
            """
            if isinstance(pos1, (list, tuple)) and isinstance(pos2, (list, tuple)):
                return math.sqrt(sum((a - b) ** 2 for a, b in zip(pos1, pos2)))
            else:
                return abs(pos1 - pos2) if isinstance(pos1, (int, float)) else 0
        
        return euclidean_distance 