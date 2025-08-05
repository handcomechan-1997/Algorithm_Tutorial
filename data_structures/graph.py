"""
图数据结构实现

图是由顶点和边组成的非线性数据结构。
本实现支持有向图和无向图，提供顶点和边的增删改查操作。
"""

from typing import Any, Optional, List, Set, Dict, Tuple, Iterator
from core.data_structures import DataStructureBase, DataStructureType


class Graph(DataStructureBase):
    """图数据结构实现
    
    特性：
    - 支持有向图和无向图
    - 邻接表表示
    - 动态添加/删除顶点和边
    - 支持权重边
    """
    
    def __init__(self, directed: bool = False):
        """初始化图
        
        Args:
            directed: 是否为有向图
        """
        super().__init__("Graph", DataStructureType.GRAPH)
        self.directed = directed
        self.vertices = {}  # 顶点字典 {vertex_id: vertex_data}
        self.edges = {}     # 边字典 {vertex_id: {neighbor_id: weight}}
        self.size = 0       # 顶点数量
        self.edge_count = 0 # 边数量
    
    def add_vertex(self, vertex_id: Any, data: Any = None) -> bool:
        """添加顶点
        
        Args:
            vertex_id: 顶点标识
            data: 顶点数据
            
        Returns:
            添加是否成功
        """
        try:
            if vertex_id in self.vertices:
                self.logger.warning(f"顶点 {vertex_id} 已存在")
                return False
            
            self.vertices[vertex_id] = data
            self.edges[vertex_id] = {}
            self.size += 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"添加顶点 {vertex_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"添加顶点失败: {e}")
            return False
    
    def remove_vertex(self, vertex_id: Any) -> bool:
        """删除顶点
        
        Args:
            vertex_id: 顶点标识
            
        Returns:
            删除是否成功
        """
        try:
            if vertex_id not in self.vertices:
                self.logger.warning(f"顶点 {vertex_id} 不存在")
                return False
            
            # 删除所有相关的边
            if self.directed:
                # 有向图：删除出边和入边
                for neighbor in self.edges[vertex_id]:
                    self.edge_count -= 1
                
                for v in self.edges:
                    if vertex_id in self.edges[v]:
                        self.edges[v].pop(vertex_id)
                        self.edge_count -= 1
            else:
                # 无向图：删除所有相关边
                for neighbor in self.edges[vertex_id]:
                    self.edges[neighbor].pop(vertex_id)
                    self.edge_count -= 1
            
            # 删除顶点
            self.vertices.pop(vertex_id)
            self.edges.pop(vertex_id)
            self.size -= 1
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"删除顶点 {vertex_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"删除顶点失败: {e}")
            return False
    
    def add_edge(self, from_vertex: Any, to_vertex: Any, weight: float = 1.0) -> bool:
        """添加边
        
        Args:
            from_vertex: 起始顶点
            to_vertex: 目标顶点
            weight: 边权重
            
        Returns:
            添加是否成功
        """
        try:
            if from_vertex not in self.vertices or to_vertex not in self.vertices:
                self.logger.error(f"顶点 {from_vertex} 或 {to_vertex} 不存在")
                return False
            
            if to_vertex in self.edges[from_vertex]:
                self.logger.warning(f"边 {from_vertex} -> {to_vertex} 已存在")
                return False
            
            # 添加边
            self.edges[from_vertex][to_vertex] = weight
            self.edge_count += 1
            
            # 如果是无向图，添加反向边
            if not self.directed and from_vertex != to_vertex:
                self.edges[to_vertex][from_vertex] = weight
                self.edge_count += 1
            
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"添加边 {from_vertex} -> {to_vertex} (权重: {weight})")
            return True
            
        except Exception as e:
            self.logger.error(f"添加边失败: {e}")
            return False
    
    def remove_edge(self, from_vertex: Any, to_vertex: Any) -> bool:
        """删除边
        
        Args:
            from_vertex: 起始顶点
            to_vertex: 目标顶点
            
        Returns:
            删除是否成功
        """
        try:
            if from_vertex not in self.vertices or to_vertex not in self.vertices:
                self.logger.error(f"顶点 {from_vertex} 或 {to_vertex} 不存在")
                return False
            
            if to_vertex not in self.edges[from_vertex]:
                self.logger.warning(f"边 {from_vertex} -> {to_vertex} 不存在")
                return False
            
            # 删除边
            self.edges[from_vertex].pop(to_vertex)
            self.edge_count -= 1
            
            # 如果是无向图，删除反向边
            if not self.directed and from_vertex != to_vertex:
                self.edges[to_vertex].pop(from_vertex)
                self.edge_count -= 1
            
            self.operation_count += 1
            self.modification_count += 1
            
            self.logger.info(f"删除边 {from_vertex} -> {to_vertex}")
            return True
            
        except Exception as e:
            self.logger.error(f"删除边失败: {e}")
            return False
    
    def insert(self, item: Any, **kwargs) -> bool:
        """插入元素（添加顶点）
        
        Args:
            item: 顶点标识
            **kwargs: 额外参数
            
        Returns:
            插入是否成功
        """
        data = kwargs.get('data', None)
        return self.add_vertex(item, data)
    
    def delete(self, item: Any, **kwargs) -> bool:
        """删除元素（删除顶点）
        
        Args:
            item: 顶点标识
            **kwargs: 额外参数
            
        Returns:
            删除是否成功
        """
        return self.remove_vertex(item)
    
    def search(self, item: Any) -> Optional[Any]:
        """搜索元素（查找顶点）
        
        Args:
            item: 顶点标识
            
        Returns:
            顶点数据，如果未找到返回None
        """
        self.access_count += 1
        if item in self.vertices:
            self.operation_count += 1
            self.logger.info(f"找到顶点 {item}")
            return self.vertices[item]
        else:
            self.logger.info(f"未找到顶点 {item}")
            return None
    
    def update(self, old_item: Any, new_item: Any) -> bool:
        """更新元素（更新顶点数据）
        
        Args:
            old_item: 顶点标识
            new_item: 新的顶点数据
            
        Returns:
            更新是否成功
        """
        try:
            if old_item in self.vertices:
                self.vertices[old_item] = new_item
                self.operation_count += 1
                self.modification_count += 1
                self.logger.info(f"更新顶点 {old_item} 的数据")
                return True
            else:
                self.logger.warning(f"未找到要更新的顶点 {old_item}")
                return False
                
        except Exception as e:
            self.logger.error(f"更新顶点失败: {e}")
            return False
    
    def get_neighbors(self, vertex_id: Any) -> List[Tuple[Any, float]]:
        """获取顶点的邻居
        
        Args:
            vertex_id: 顶点标识
            
        Returns:
            邻居列表 [(neighbor_id, weight), ...]
        """
        if vertex_id not in self.vertices:
            return []
        
        neighbors = []
        for neighbor_id, weight in self.edges[vertex_id].items():
            neighbors.append((neighbor_id, weight))
        
        self.access_count += 1
        return neighbors
    
    def get_degree(self, vertex_id: Any) -> int:
        """获取顶点的度数
        
        Args:
            vertex_id: 顶点标识
            
        Returns:
            顶点度数
        """
        if vertex_id not in self.vertices:
            return 0
        
        degree = len(self.edges[vertex_id])
        
        # 如果是无向图，需要检查入度
        if not self.directed:
            for v in self.edges:
                if vertex_id in self.edges[v]:
                    degree += 1
        
        return degree
    
    def has_edge(self, from_vertex: Any, to_vertex: Any) -> bool:
        """检查是否存在边
        
        Args:
            from_vertex: 起始顶点
            to_vertex: 目标顶点
            
        Returns:
            是否存在边
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False
        
        return to_vertex in self.edges[from_vertex]
    
    def get_edge_weight(self, from_vertex: Any, to_vertex: Any) -> Optional[float]:
        """获取边权重
        
        Args:
            from_vertex: 起始顶点
            to_vertex: 目标顶点
            
        Returns:
            边权重，如果边不存在返回None
        """
        if self.has_edge(from_vertex, to_vertex):
            return self.edges[from_vertex][to_vertex]
        return None
    
    def clear(self):
        """清空图"""
        self.vertices.clear()
        self.edges.clear()
        self.size = 0
        self.edge_count = 0
        self.operation_count += 1
        self.logger.info("图已清空")
    
    def get_vertices(self) -> List[Any]:
        """获取所有顶点
        
        Returns:
            顶点标识列表
        """
        return list(self.vertices.keys())
    
    def get_edges(self) -> List[Tuple[Any, Any, float]]:
        """获取所有边
        
        Returns:
            边列表 [(from_vertex, to_vertex, weight), ...]
        """
        edges = []
        for from_vertex in self.edges:
            for to_vertex, weight in self.edges[from_vertex].items():
                edges.append((from_vertex, to_vertex, weight))
        return edges
    
    def __len__(self) -> int:
        """返回图的顶点数量"""
        return self.size
    
    def __iter__(self) -> Iterator[Any]:
        """支持迭代（遍历顶点）"""
        for vertex_id in self.vertices:
            yield vertex_id
    
    def __contains__(self, vertex_id: Any) -> bool:
        """检查顶点是否存在于图中"""
        return vertex_id in self.vertices
    
    def __str__(self) -> str:
        """字符串表示"""
        vertex_count = len(self.vertices)
        edge_count = self.edge_count
        graph_type = "有向图" if self.directed else "无向图"
        return f"Graph(type={graph_type}, vertices={vertex_count}, edges={edge_count})"
    
    def __repr__(self) -> str:
        """详细字符串表示"""
        return self.__str__()
    
    def get_stats(self) -> dict:
        """获取统计信息"""
        return {
            'name': self.name,
            'type': self.data_type.value,
            'directed': self.directed,
            'vertex_count': len(self.vertices),
            'edge_count': self.edge_count,
            'operation_count': self.operation_count,
            'access_count': self.access_count,
            'modification_count': self.modification_count
        } 