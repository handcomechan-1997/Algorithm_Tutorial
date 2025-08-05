"""
图搜索算法实现

包含深度优先搜索(DFS)和广度优先搜索(BFS)算法。
这些算法用于遍历图结构，寻找路径或连通分量。
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
    """
    
    def __init__(self):
        """初始化深度优先搜索算法"""
        super().__init__("DepthFirstSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any = None) -> List[Any]:
        """执行深度优先搜索
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点（可选）
            
        Returns:
            访问顶点的顺序列表
        """
        try:
            self.logger.info(f"开始深度优先搜索，起始顶点: {start_vertex}")
            self.operation_count = 0
            self.comparison_count = 0
            
            visited = set()
            result = []
            
            def dfs_recursive(vertex: Any):
                if vertex in visited:
                    return
                
                visited.add(vertex)
                result.append(vertex)
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'visit',
                    'vertex': vertex,
                    'visited_count': len(visited),
                    'path': result.copy()
                })
                
                # 如果找到目标顶点，可以提前结束
                if target_vertex is not None and vertex == target_vertex:
                    self.add_step({
                        'type': 'target_found',
                        'vertex': vertex,
                        'path': result.copy()
                    })
                    return
                
                # 递归访问邻居
                neighbors = graph.get_neighbors(vertex)
                for neighbor, weight in neighbors:
                    self.comparison_count += 1
                    if neighbor not in visited:
                        self.add_step({
                            'type': 'explore',
                            'from_vertex': vertex,
                            'to_vertex': neighbor,
                            'weight': weight
                        })
                        dfs_recursive(neighbor)
            
            dfs_recursive(start_vertex)
            
            self.logger.info(f"深度优先搜索完成，访问了 {len(result)} 个顶点")
            return result
            
        except Exception as e:
            self.logger.error(f"深度优先搜索失败: {e}")
            return []
    
    def find_path(self, graph: Graph, start_vertex: Any, target_vertex: Any) -> Optional[List[Any]]:
        """查找从起始顶点到目标顶点的路径
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            
        Returns:
            路径列表，如果不存在路径返回None
        """
        try:
            self.logger.info(f"开始查找路径: {start_vertex} -> {target_vertex}")
            self.operation_count = 0
            self.comparison_count = 0
            
            visited = set()
            path = []
            parent = {}
            
            def dfs_path(vertex: Any):
                if vertex in visited:
                    return False
                
                visited.add(vertex)
                path.append(vertex)
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'visit',
                    'vertex': vertex,
                    'current_path': path.copy()
                })
                
                if vertex == target_vertex:
                    self.add_step({
                        'type': 'path_found',
                        'path': path.copy()
                    })
                    return True
                
                neighbors = graph.get_neighbors(vertex)
                for neighbor, weight in neighbors:
                    self.comparison_count += 1
                    if neighbor not in visited:
                        parent[neighbor] = vertex
                        self.add_step({
                            'type': 'explore',
                            'from_vertex': vertex,
                            'to_vertex': neighbor,
                            'weight': weight
                        })
                        if dfs_path(neighbor):
                            return True
                
                path.pop()
                return False
            
            if dfs_path(start_vertex):
                self.logger.info(f"找到路径: {' -> '.join(map(str, path))}")
                return path
            else:
                self.logger.info(f"未找到从 {start_vertex} 到 {target_vertex} 的路径")
                return None
                
        except Exception as e:
            self.logger.error(f"查找路径失败: {e}")
            return None
    
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
    """
    
    def __init__(self):
        """初始化广度优先搜索算法"""
        super().__init__("BreadthFirstSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any = None) -> List[Any]:
        """执行广度优先搜索
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点（可选）
            
        Returns:
            访问顶点的顺序列表
        """
        try:
            self.logger.info(f"开始广度优先搜索，起始顶点: {start_vertex}")
            self.operation_count = 0
            self.comparison_count = 0
            
            visited = set()
            result = []
            queue = [start_vertex]
            visited.add(start_vertex)
            
            while queue:
                vertex = queue.pop(0)
                result.append(vertex)
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'visit',
                    'vertex': vertex,
                    'queue_size': len(queue),
                    'visited_count': len(visited),
                    'path': result.copy()
                })
                
                # 如果找到目标顶点，可以提前结束
                if target_vertex is not None and vertex == target_vertex:
                    self.add_step({
                        'type': 'target_found',
                        'vertex': vertex,
                        'path': result.copy()
                    })
                    break
                
                # 访问邻居
                neighbors = graph.get_neighbors(vertex)
                for neighbor, weight in neighbors:
                    self.comparison_count += 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        self.add_step({
                            'type': 'explore',
                            'from_vertex': vertex,
                            'to_vertex': neighbor,
                            'weight': weight,
                            'queue_size': len(queue)
                        })
            
            self.logger.info(f"广度优先搜索完成，访问了 {len(result)} 个顶点")
            return result
            
        except Exception as e:
            self.logger.error(f"广度优先搜索失败: {e}")
            return []
    
    def find_shortest_path(self, graph: Graph, start_vertex: Any, target_vertex: Any) -> Optional[List[Any]]:
        """查找从起始顶点到目标顶点的最短路径
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            
        Returns:
            最短路径列表，如果不存在路径返回None
        """
        try:
            self.logger.info(f"开始查找最短路径: {start_vertex} -> {target_vertex}")
            self.operation_count = 0
            self.comparison_count = 0
            
            visited = set()
            parent = {}
            queue = [(start_vertex, 0)]  # (vertex, distance)
            visited.add(start_vertex)
            
            while queue:
                vertex, distance = queue.pop(0)
                self.operation_count += 1
                
                # 记录搜索步骤
                self.add_step({
                    'type': 'visit',
                    'vertex': vertex,
                    'distance': distance,
                    'queue_size': len(queue)
                })
                
                if vertex == target_vertex:
                    # 重建路径
                    path = []
                    current = vertex
                    while current is not None:
                        path.append(current)
                        current = parent.get(current)
                    path.reverse()
                    
                    self.add_step({
                        'type': 'shortest_path_found',
                        'path': path,
                        'distance': distance
                    })
                    
                    self.logger.info(f"找到最短路径: {' -> '.join(map(str, path))}，距离: {distance}")
                    return path
                
                neighbors = graph.get_neighbors(vertex)
                for neighbor, weight in neighbors:
                    self.comparison_count += 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = vertex
                        queue.append((neighbor, distance + weight))
                        
                        self.add_step({
                            'type': 'explore',
                            'from_vertex': vertex,
                            'to_vertex': neighbor,
                            'weight': weight,
                            'new_distance': distance + weight
                        })
            
            self.logger.info(f"未找到从 {start_vertex} 到 {target_vertex} 的路径")
            return None
            
        except Exception as e:
            self.logger.error(f"查找最短路径失败: {e}")
            return None
    
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