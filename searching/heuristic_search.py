"""
启发式搜索算法实现

包含A*搜索算法，这是一种结合了Dijkstra算法和启发式函数的搜索算法。
适用于寻找最优路径的问题。

学习目标：
1. 理解启发式搜索的基本概念
2. 掌握A*算法的实现
3. 学会设计和使用启发式函数
4. 理解优先队列的使用
"""

import heapq
from typing import Any, List, Optional, Set, Dict, Tuple, Callable
from core.algorithm_base import AlgorithmBase, AlgorithmType
from data_structures.graph import Graph
import math


class AStarSearch(AlgorithmBase):
    """A*搜索算法实现
    
    特性：
    - 结合了Dijkstra算法和启发式函数
    - 使用优先队列（最小堆）
    - 时间复杂度取决于启发式函数的质量
    - 空间复杂度 O(V)
    
    学习要点：
    1. 理解f(n) = g(n) + h(n)的评估函数
    2. 掌握优先队列的使用
    3. 学会设计启发式函数
    4. 理解开放集和关闭集的概念
    """
    
    def __init__(self):
        """初始化A*搜索算法"""
        super().__init__("AStarSearch", AlgorithmType.SEARCHING)
    
    def search(self, graph: Graph, start_vertex: Any, target_vertex: Any, 
               heuristic_func: Callable[[Any, Any], float] = None) -> Optional[List[Any]]:
        """执行A*搜索
        
        TODO: 请实现A*搜索算法
        
        实现思路：
        1. 初始化数据结构：
           - open_set: 优先队列，存储待访问的顶点
           - closed_set: 已访问的顶点集合
           - came_from: 记录路径的字典
           - g_score: 从起点到当前顶点的实际距离
           - f_score: f(n) = g(n) + h(n) 评估函数
        2. 将起始顶点加入开放集
        3. 当开放集不为空时：
           - 取出f_score最小的顶点
           - 如果到达目标，重建路径并返回
           - 将顶点加入关闭集
           - 检查所有邻居，更新g_score和f_score
        4. 如果没找到路径，返回None
        
        关键点：
        - 使用优先队列选择f_score最小的顶点
        - 使用启发式函数估计到目标的距离
        - 记录路径信息以便重建
        
        提示：
        - 使用 heapq 模块实现优先队列
        - 使用字典存储 g_score 和 f_score
        - 使用启发式函数计算 h(n)
        - 记录搜索步骤和评估值
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertex: 目标顶点
            heuristic_func: 启发式函数，用于估计从顶点到目标的距离
            
        Returns:
            最优路径列表，如果不存在路径返回None
        """
        # TODO: 在这里实现A*搜索算法
        pass
    
    def _reconstruct_path(self, came_from: Dict[Any, Any], current: Any) -> List[Any]:
        """重建路径
        
        TODO: 请实现路径重建算法
        
        实现思路：
        1. 从当前顶点开始，沿着came_from字典回溯
        2. 将路径顶点加入列表
        3. 反转列表得到正确顺序
        4. 返回路径列表
        
        提示：
        - 使用 while 循环沿着父节点回溯
        - 使用列表存储路径顶点
        - 使用 reverse() 或 [::-1] 反转列表
        
        Args:
            came_from: 路径记录字典
            current: 当前顶点
            
        Returns:
            路径列表
        """
        # TODO: 在这里实现路径重建算法
        pass
    
    def search_with_multiple_goals(self, graph: Graph, start_vertex: Any, 
                                 target_vertices: List[Any],
                                 heuristic_func: Callable[[Any, Any], float] = None) -> Dict[Any, List[Any]]:
        """搜索到多个目标的最短路径
        
        TODO: 请实现多目标A*搜索算法
        
        实现思路：
        1. 对每个目标顶点调用A*搜索
        2. 收集所有搜索结果
        3. 返回目标到路径的映射字典
        
        应用场景：
        - 需要找到到多个目标的最短路径
        - 路径规划中的多点访问问题
        - 游戏AI中的多目标寻路
        
        提示：
        - 使用字典存储每个目标的路径
        - 对每个目标调用 search 方法
        - 处理某些目标可能无法到达的情况
        
        Args:
            graph: 要搜索的图
            start_vertex: 起始顶点
            target_vertices: 目标顶点列表
            heuristic_func: 启发式函数
            
        Returns:
            到每个目标的路径字典
        """
        # TODO: 在这里实现多目标A*搜索算法
        pass
    
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
        
        TODO: 请实现曼哈顿距离启发式函数
        
        实现思路：
        1. 定义曼哈顿距离计算函数
        2. 对于坐标点，计算|x1-x2| + |y1-y2|
        3. 对于数值，计算|a-b|
        4. 返回距离值
        
        应用场景：
        - 网格地图中的路径规划
        - 城市街区距离计算
        - 数值空间中的距离估计
        
        提示：
        - 使用 isinstance() 检查数据类型
        - 使用 zip() 处理坐标对
        - 使用 sum() 和 abs() 计算距离
        
        Returns:
            曼哈顿距离启发式函数
        """
        # TODO: 在这里实现曼哈顿距离启发式函数
        pass
    
    def create_euclidean_heuristic(self) -> Callable[[Any, Any], float]:
        """创建欧几里得距离启发式函数
        
        TODO: 请实现欧几里得距离启发式函数
        
        实现思路：
        1. 定义欧几里得距离计算函数
        2. 对于坐标点，计算√((x1-x2)² + (y1-y2)²)
        3. 对于数值，计算|a-b|
        4. 返回距离值
        
        应用场景：
        - 连续空间中的路径规划
        - 几何距离计算
        - 精确的距离估计
        
        提示：
        - 使用 math.sqrt() 计算平方根
        - 使用 ** 运算符计算幂
        - 使用 zip() 处理坐标对
        
        Returns:
            欧几里得距离启发式函数
        """
        # TODO: 在这里实现欧几里得距离启发式函数
        pass 


def main():
    """测试启发式搜索算法的实现"""
    print("=" * 60)
    print("🧪 测试启发式搜索算法实现")
    print("=" * 60)
    
    # 创建AStarSearch实例
    astar = AStarSearch()
    
    # 创建测试图
    from data_structures.graph import Graph
    graph = Graph()
    
    # 添加顶点（使用坐标表示位置）
    vertices = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # 添加边（网格连接）
    edges = [
        ((0, 0), (1, 0), 1), ((0, 0), (0, 1), 1),
        ((1, 0), (2, 0), 1), ((1, 0), (1, 1), 1),
        ((2, 0), (2, 1), 1),
        ((0, 1), (1, 1), 1), ((0, 1), (0, 2), 1),
        ((1, 1), (2, 1), 1), ((1, 1), (1, 2), 1),
        ((2, 1), (2, 2), 1),
        ((0, 2), (1, 2), 1),
        ((1, 2), (2, 2), 1)
    ]
    
    for start, end, weight in edges:
        graph.add_edge(start, end, weight)
    
    # 创建启发式函数（曼哈顿距离）
    def manhattan_heuristic(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    test_results = {
        'passed': 0,
        'failed': 0,
        'total': 0,
        'details': []
    }
    
    # 测试用例1: 基本A*搜索测试
    print("\n🔍 测试用例1: 基本A*搜索测试")
    test_results['total'] += 1
    try:
        result = astar.execute(graph, start_vertex=(0, 0), target_vertex=(2, 2), heuristic=manhattan_heuristic)
        if isinstance(result, list) and len(result) > 0 and result[0] == (0, 0) and result[-1] == (2, 2):
            test_results['passed'] += 1
            test_results['details'].append("✅ 基本A*搜索测试 - 通过")
            print("✅ 基本A*搜索测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 基本A*搜索测试 - 失败")
            print("❌ 基本A*搜索测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 基本A*搜索测试 - 异常: {e}")
        print(f"❌ 基本A*搜索测试 - 异常: {e}")
    
    # 测试用例2: 短路径测试
    print("\n🔍 测试用例2: 短路径测试")
    test_results['total'] += 1
    try:
        result = astar.execute(graph, start_vertex=(0, 0), target_vertex=(1, 0), heuristic=manhattan_heuristic)
        if isinstance(result, list) and len(result) == 2 and result[0] == (0, 0) and result[1] == (1, 0):
            test_results['passed'] += 1
            test_results['details'].append("✅ 短路径测试 - 通过")
            print("✅ 短路径测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 短路径测试 - 失败")
            print("❌ 短路径测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 短路径测试 - 异常: {e}")
        print(f"❌ 短路径测试 - 异常: {e}")
    
    # 测试用例3: 对角线路径测试
    print("\n🔍 测试用例3: 对角线路径测试")
    test_results['total'] += 1
    try:
        result = astar.execute(graph, start_vertex=(0, 0), target_vertex=(1, 1), heuristic=manhattan_heuristic)
        if isinstance(result, list) and len(result) > 0 and result[0] == (0, 0) and result[-1] == (1, 1):
            test_results['passed'] += 1
            test_results['details'].append("✅ 对角线路径测试 - 通过")
            print("✅ 对角线路径测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 对角线路径测试 - 失败")
            print("❌ 对角线路径测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 对角线路径测试 - 异常: {e}")
        print(f"❌ 对角线路径测试 - 异常: {e}")
    
    # 测试用例4: 不存在的路径测试
    print("\n🔍 测试用例4: 不存在的路径测试")
    test_results['total'] += 1
    try:
        # 添加一个孤立的顶点
        graph.add_vertex((3, 3))
        result = astar.execute(graph, start_vertex=(0, 0), target_vertex=(3, 3), heuristic=manhattan_heuristic)
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
    
    # 测试用例5: 多目标搜索测试
    print("\n🔍 测试用例5: 多目标搜索测试")
    test_results['total'] += 1
    try:
        targets = [(1, 1), (2, 2)]
        result = astar.search_with_multiple_goals(graph, (0, 0), targets, manhattan_heuristic)
        if isinstance(result, dict) and len(result) == 2:
            test_results['passed'] += 1
            test_results['details'].append("✅ 多目标搜索测试 - 通过")
            print("✅ 多目标搜索测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 多目标搜索测试 - 失败")
            print("❌ 多目标搜索测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 多目标搜索测试 - 异常: {e}")
        print(f"❌ 多目标搜索测试 - 异常: {e}")
    
    # 测试用例6: 曼哈顿距离启发式函数测试
    print("\n🔍 测试用例6: 曼哈顿距离启发式函数测试")
    test_results['total'] += 1
    try:
        heuristic_func = astar.create_manhattan_heuristic()
        distance = heuristic_func((0, 0), (2, 2))
        if distance == 4:  # 曼哈顿距离应该是4
            test_results['passed'] += 1
            test_results['details'].append("✅ 曼哈顿距离启发式函数测试 - 通过")
            print("✅ 曼哈顿距离启发式函数测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 曼哈顿距离启发式函数测试 - 失败")
            print("❌ 曼哈顿距离启发式函数测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 曼哈顿距离启发式函数测试 - 异常: {e}")
        print(f"❌ 曼哈顿距离启发式函数测试 - 异常: {e}")
    
    # 测试用例7: 欧几里得距离启发式函数测试
    print("\n🔍 测试用例7: 欧几里得距离启发式函数测试")
    test_results['total'] += 1
    try:
        heuristic_func = astar.create_euclidean_heuristic()
        distance = heuristic_func((0, 0), (3, 4))
        if abs(distance - 5.0) < 0.001:  # 欧几里得距离应该是5
            test_results['passed'] += 1
            test_results['details'].append("✅ 欧几里得距离启发式函数测试 - 通过")
            print("✅ 欧几里得距离启发式函数测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 欧几里得距离启发式函数测试 - 失败")
            print("❌ 欧几里得距离启发式函数测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 欧几里得距离启发式函数测试 - 异常: {e}")
        print(f"❌ 欧几里得距离启发式函数测试 - 异常: {e}")
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的启发式搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 