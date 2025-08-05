"""
搜索算法演示和测试

展示各种搜索算法的使用方法和性能比较。
"""

import time
import random
from typing import List, Any, Dict, Callable
from core.algorithm_manager import AlgorithmManager
from core.visualizer import Visualizer

# 导入所有搜索算法
from linear_search import LinearSearch
from binary_search import BinarySearch
from jump_search import JumpSearch
from interpolation_search import InterpolationSearch
from exponential_search import ExponentialSearch
from graph_search import DepthFirstSearch, BreadthFirstSearch
from heuristic_search import AStarSearch


class SearchDemo:
    """搜索算法演示类"""
    
    def __init__(self):
        """初始化演示类"""
        self.algorithm_manager = AlgorithmManager()
        self.visualizer = Visualizer()
        
        # 注册所有搜索算法
        self._register_algorithms()
    
    def _register_algorithms(self):
        """注册所有搜索算法"""
        algorithms = [
            LinearSearch(),
            BinarySearch(),
            JumpSearch(),
            InterpolationSearch(),
            ExponentialSearch(),
            DepthFirstSearch(),
            BreadthFirstSearch(),
            AStarSearch()
        ]
        
        for algorithm in algorithms:
            self.algorithm_manager.register_algorithm(algorithm)
    
    def demo_linear_search(self):
        """演示线性搜索"""
        print("\n=== 线性搜索演示 ===")
        
        # 创建测试数据
        data = [random.randint(1, 100) for _ in range(20)]
        target = random.choice(data)
        
        print(f"测试数据: {data}")
        print(f"目标元素: {target}")
        
        # 执行线性搜索
        linear_search = LinearSearch()
        result = linear_search.search(data, target)
        
        print(f"搜索结果: {result}")
        print(f"操作次数: {linear_search.operation_count}")
        print(f"比较次数: {linear_search.comparison_count}")
        
        # 演示其他功能
        print("\n--- 搜索所有出现位置 ---")
        occurrences = linear_search.search_all_occurrences(data, target)
        print(f"所有出现位置: {occurrences}")
        
        print("\n--- 条件搜索 ---")
        condition = lambda x: x > 50
        result = linear_search.search_with_condition(data, condition)
        print(f"第一个大于50的元素位置: {result}")
    
    def demo_binary_search(self):
        """演示二分搜索"""
        print("\n=== 二分搜索演示 ===")
        
        # 创建有序测试数据
        data = sorted([random.randint(1, 100) for _ in range(20)])
        target = random.choice(data)
        
        print(f"有序数据: {data}")
        print(f"目标元素: {target}")
        
        # 执行二分搜索
        binary_search = BinarySearch()
        result = binary_search.search(data, target)
        
        print(f"搜索结果: {result}")
        print(f"操作次数: {binary_search.operation_count}")
        print(f"比较次数: {binary_search.comparison_count}")
        
        # 演示其他功能
        print("\n--- 搜索第一次出现位置 ---")
        first_pos = binary_search.search_first_occurrence(data, target)
        print(f"第一次出现位置: {first_pos}")
        
        print("\n--- 搜索最后一次出现位置 ---")
        last_pos = binary_search.search_last_occurrence(data, target)
        print(f"最后一次出现位置: {last_pos}")
    
    def demo_jump_search(self):
        """演示跳跃搜索"""
        print("\n=== 跳跃搜索演示 ===")
        
        # 创建有序测试数据
        data = sorted([random.randint(1, 100) for _ in range(25)])
        target = random.choice(data)
        
        print(f"有序数据: {data}")
        print(f"目标元素: {target}")
        
        # 执行跳跃搜索
        jump_search = JumpSearch()
        result = jump_search.search(data, target)
        
        print(f"搜索结果: {result}")
        print(f"操作次数: {jump_search.operation_count}")
        print(f"比较次数: {jump_search.comparison_count}")
        
        # 演示自定义步长
        print("\n--- 自定义步长搜索 ---")
        custom_result = jump_search.search_with_custom_step(data, target, 5)
        print(f"自定义步长搜索结果: {custom_result}")
    
    def demo_interpolation_search(self):
        """演示插值搜索"""
        print("\n=== 插值搜索演示 ===")
        
        # 创建均匀分布的有序数据
        data = list(range(0, 100, 5))  # 0, 5, 10, 15, ...
        target = random.choice(data)
        
        print(f"均匀分布数据: {data}")
        print(f"目标元素: {target}")
        
        # 检查数据分布
        interpolation_search = InterpolationSearch()
        is_uniform = interpolation_search.is_uniformly_distributed(data)
        print(f"数据是否均匀分布: {is_uniform}")
        
        # 执行插值搜索
        result = interpolation_search.search(data, target)
        
        print(f"搜索结果: {result}")
        print(f"操作次数: {interpolation_search.operation_count}")
        print(f"比较次数: {interpolation_search.comparison_count}")
    
    def demo_exponential_search(self):
        """演示指数搜索"""
        print("\n=== 指数搜索演示 ===")
        
        # 创建有序测试数据
        data = sorted([random.randint(1, 100) for _ in range(30)])
        target = random.choice(data)
        
        print(f"有序数据: {data}")
        print(f"目标元素: {target}")
        
        # 执行指数搜索
        exponential_search = ExponentialSearch()
        result = exponential_search.search(data, target)
        
        print(f"搜索结果: {result}")
        print(f"操作次数: {exponential_search.operation_count}")
        print(f"比较次数: {exponential_search.comparison_count}")
        
        # 演示无界搜索
        print("\n--- 无界搜索演示 ---")
        def data_generator(index):
            if index < len(data):
                return data[index]
            else:
                raise IndexError("超出范围")
        
        unbounded_result = exponential_search.search_unbounded(data_generator, target)
        print(f"无界搜索结果: {unbounded_result}")
    
    def demo_graph_search(self):
        """演示图搜索"""
        print("\n=== 图搜索演示 ===")
        
        from data_structures.graph import Graph
        
        # 创建测试图
        graph = Graph()
        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        edges = [
            ('A', 'B', 1), ('A', 'C', 2),
            ('B', 'D', 3), ('B', 'E', 4),
            ('C', 'E', 5), ('D', 'F', 6),
            ('E', 'F', 7)
        ]
        
        for vertex in vertices:
            graph.add_vertex(vertex)
        
        for start, end, weight in edges:
            graph.add_edge(start, end, weight)
        
        print("图结构:")
        for vertex in vertices:
            neighbors = graph.get_neighbors(vertex)
            print(f"{vertex} -> {neighbors}")
        
        # 深度优先搜索
        print("\n--- 深度优先搜索 ---")
        dfs = DepthFirstSearch()
        dfs_result = dfs.search(graph, 'A', 'F')
        print(f"DFS访问顺序: {dfs_result}")
        
        # 广度优先搜索
        print("\n--- 广度优先搜索 ---")
        bfs = BreadthFirstSearch()
        bfs_result = bfs.search(graph, 'A', 'F')
        print(f"BFS访问顺序: {bfs_result}")
        
        # 最短路径
        shortest_path = bfs.find_shortest_path(graph, 'A', 'F')
        print(f"最短路径: {shortest_path}")
    
    def demo_heuristic_search(self):
        """演示启发式搜索"""
        print("\n=== 启发式搜索演示 ===")
        
        from data_structures.graph import Graph
        
        # 创建带坐标的图（用于启发式搜索）
        graph = Graph()
        vertices_with_coords = {
            'A': (0, 0), 'B': (1, 1), 'C': (2, 0),
            'D': (3, 1), 'E': (4, 0), 'F': (5, 1)
        }
        
        edges = [
            ('A', 'B', 1.4), ('A', 'C', 2),
            ('B', 'D', 2.2), ('B', 'E', 3.2),
            ('C', 'E', 2.8), ('D', 'F', 2.2),
            ('E', 'F', 1.4)
        ]
        
        for vertex, coords in vertices_with_coords.items():
            graph.add_vertex(vertex)
        
        for start, end, weight in edges:
            graph.add_edge(start, end, weight)
        
        print("图结构（带坐标）:")
        for vertex, coords in vertices_with_coords.items():
            neighbors = graph.get_neighbors(vertex)
            print(f"{vertex}{coords} -> {neighbors}")
        
        # A*搜索
        print("\n--- A*搜索 ---")
        astar = AStarSearch()
        
        # 使用曼哈顿距离启发式函数
        heuristic = astar.create_manhattan_heuristic()
        
        # 创建坐标映射函数
        def get_coords(vertex):
            return vertices_with_coords.get(vertex, (0, 0))
        
        def manhattan_heuristic(vertex1, vertex2):
            coords1 = get_coords(vertex1)
            coords2 = get_coords(vertex2)
            return heuristic(coords1, coords2)
        
        path = astar.search(graph, 'A', 'F', manhattan_heuristic)
        print(f"A*搜索路径: {path}")
        print(f"操作次数: {astar.operation_count}")
        print(f"比较次数: {astar.comparison_count}")
    
    def performance_comparison(self):
        """性能比较"""
        print("\n=== 搜索算法性能比较 ===")
        
        # 创建不同大小的测试数据
        sizes = [100, 1000, 10000]
        algorithms = {
            'LinearSearch': LinearSearch(),
            'BinarySearch': BinarySearch(),
            'JumpSearch': JumpSearch(),
            'InterpolationSearch': InterpolationSearch(),
            'ExponentialSearch': ExponentialSearch()
        }
        
        results = {}
        
        for size in sizes:
            print(f"\n数据大小: {size}")
            
            # 创建有序数据
            data = sorted([random.randint(1, size * 10) for _ in range(size)])
            target = random.choice(data)
            
            results[size] = {}
            
            for name, algorithm in algorithms.items():
                # 重置计数器
                algorithm.operation_count = 0
                algorithm.comparison_count = 0
                
                # 执行搜索并计时
                start_time = time.time()
                result = algorithm.search(data, target)
                end_time = time.time()
                
                execution_time = (end_time - start_time) * 1000  # 转换为毫秒
                
                results[size][name] = {
                    'result': result,
                    'time_ms': execution_time,
                    'operations': algorithm.operation_count,
                    'comparisons': algorithm.comparison_count
                }
                
                print(f"{name:20} | 时间: {execution_time:8.3f}ms | 操作: {algorithm.operation_count:6d} | 比较: {algorithm.comparison_count:6d}")
        
        return results
    
    def run_all_demos(self):
        """运行所有演示"""
        print("搜索算法演示程序")
        print("=" * 50)
        
        # 运行各个演示
        self.demo_linear_search()
        self.demo_binary_search()
        self.demo_jump_search()
        self.demo_interpolation_search()
        self.demo_exponential_search()
        self.demo_graph_search()
        self.demo_heuristic_search()
        
        # 性能比较
        self.performance_comparison()
        
        print("\n演示完成！")


def main():
    """主函数"""
    demo = SearchDemo()
    demo.run_all_demos()


if __name__ == "__main__":
    main() 