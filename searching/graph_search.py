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


def main():
    """测试图搜索算法的实现"""
    print("=" * 60)
    print("🧪 测试图搜索算法实现")
    print("=" * 60)
    
    # 创建图搜索实例
    dfs = DepthFirstSearch()
    bfs = BreadthFirstSearch()
    
    # 创建测试图
    from data_structures.graph import Graph
    graph = Graph()
    
    # 添加顶点
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # 添加边
    edges = [
        ('A', 'B', 1), ('A', 'C', 2),
        ('B', 'D', 3), ('B', 'E', 4),
        ('C', 'F', 5), ('C', 'G', 6),
        ('D', 'H', 7), ('E', 'H', 8),
        ('F', 'H', 9), ('G', 'H', 10)
    ]
    
    for start, end, weight in edges:
        graph.add_edge(start, end, weight)
    
    test_results = {
        'passed': 0,
        'failed': 0,
        'total': 0,
        'details': []
    }
    
    # 测试用例1: DFS遍历测试
    print("\n🔍 测试用例1: DFS遍历测试")
    test_results['total'] += 1
    try:
        result = dfs.execute(graph, start_vertex='A', search_type='traversal')
        if isinstance(result, list) and len(result) > 0 and 'A' in result:
            test_results['passed'] += 1
            test_results['details'].append("✅ DFS遍历测试 - 通过")
            print("✅ DFS遍历测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ DFS遍历测试 - 失败")
            print("❌ DFS遍历测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ DFS遍历测试 - 异常: {e}")
        print(f"❌ DFS遍历测试 - 异常: {e}")
    
    # 测试用例2: BFS遍历测试
    print("\n🔍 测试用例2: BFS遍历测试")
    test_results['total'] += 1
    try:
        result = bfs.execute(graph, start_vertex='A', search_type='traversal')
        if isinstance(result, list) and len(result) > 0 and 'A' in result:
            test_results['passed'] += 1
            test_results['details'].append("✅ BFS遍历测试 - 通过")
            print("✅ BFS遍历测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ BFS遍历测试 - 失败")
            print("❌ BFS遍历测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ BFS遍历测试 - 异常: {e}")
        print(f"❌ BFS遍历测试 - 异常: {e}")
    
    # 测试用例3: DFS路径查找测试
    print("\n🔍 测试用例3: DFS路径查找测试")
    test_results['total'] += 1
    try:
        result = dfs.execute(graph, start_vertex='A', target_vertex='H', search_type='path')
        if isinstance(result, list) and len(result) > 0 and result[0] == 'A' and result[-1] == 'H':
            test_results['passed'] += 1
            test_results['details'].append("✅ DFS路径查找测试 - 通过")
            print("✅ DFS路径查找测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ DFS路径查找测试 - 失败")
            print("❌ DFS路径查找测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ DFS路径查找测试 - 异常: {e}")
        print(f"❌ DFS路径查找测试 - 异常: {e}")
    
    # 测试用例4: BFS最短路径查找测试
    print("\n🔍 测试用例4: BFS最短路径查找测试")
    test_results['total'] += 1
    try:
        result = bfs.execute(graph, start_vertex='A', target_vertex='H', search_type='shortest_path')
        if isinstance(result, list) and len(result) > 0 and result[0] == 'A' and result[-1] == 'H':
            test_results['passed'] += 1
            test_results['details'].append("✅ BFS最短路径查找测试 - 通过")
            print("✅ BFS最短路径查找测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ BFS最短路径查找测试 - 失败")
            print("❌ BFS最短路径查找测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ BFS最短路径查找测试 - 异常: {e}")
        print(f"❌ BFS最短路径查找测试 - 异常: {e}")
    
    # 测试用例5: 不存在的路径测试
    print("\n🔍 测试用例5: 不存在的路径测试")
    test_results['total'] += 1
    try:
        # 添加一个孤立的顶点
        graph.add_vertex('Z')
        result = dfs.execute(graph, start_vertex='A', target_vertex='Z', search_type='path')
        if result is None:
            test_results['passed'] += 1
            test_results['details'].append("✅ 不存在的路径测试 - 通过")
            print("✅ 不存在的路径测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 不存在的路径测试 - 失败")
            print("❌ 不存在的路径测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 不存在的路径测试 - 异常: {e}")
        print(f"❌ 不存在的路径测试 - 异常: {e}")
    
    # 测试用例6: 自环测试
    print("\n🔍 测试用例6: 自环测试")
    test_results['total'] += 1
    try:
        # 添加自环
        graph.add_edge('A', 'A', 0)
        result = dfs.execute(graph, start_vertex='A', search_type='traversal')
        if isinstance(result, list) and 'A' in result:
            test_results['passed'] += 1
            test_results['details'].append("✅ 自环测试 - 通过")
            print("✅ 自环测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 自环测试 - 失败")
            print("❌ 自环测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 自环测试 - 异常: {e}")
        print(f"❌ 自环测试 - 异常: {e}")
    
    # 测试用例7: 性能统计测试
    print("\n🔍 测试用例7: 性能统计测试")
    test_results['total'] += 1
    try:
        dfs.reset_stats()
        dfs.execute(graph, start_vertex='A', search_type='traversal')
        if dfs.operation_count > 0:
            test_results['passed'] += 1
            test_results['details'].append("✅ 性能统计测试 - 通过")
            print("✅ 性能统计测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 性能统计测试 - 失败")
            print("❌ 性能统计测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 性能统计测试 - 异常: {e}")
        print(f"❌ 性能统计测试 - 异常: {e}")
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的图搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 