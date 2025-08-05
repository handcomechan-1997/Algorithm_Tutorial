"""
搜索算法测试套件

包含所有搜索算法的单元测试。
"""

import unittest
import random
import time
from typing import List, Any

from linear_search import LinearSearch
from binary_search import BinarySearch
from jump_search import JumpSearch
from interpolation_search import InterpolationSearch
from exponential_search import ExponentialSearch
from graph_search import DepthFirstSearch, BreadthFirstSearch
from heuristic_search import AStarSearch
from data_structures.graph import Graph


class TestSearchAlgorithms(unittest.TestCase):
    """搜索算法测试类"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.test_data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 1, 45, 67, 89, 23, 45]
        self.sorted_data = sorted(self.test_data)
        self.target = 67
        
        # 创建测试图
        self.graph = Graph()
        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        edges = [
            ('A', 'B', 1), ('A', 'C', 2),
            ('B', 'D', 3), ('B', 'E', 4),
            ('C', 'E', 5), ('D', 'F', 6),
            ('E', 'F', 7)
        ]
        
        for vertex in vertices:
            self.graph.add_vertex(vertex)
        
        for start, end, weight in edges:
            self.graph.add_edge(start, end, weight)
    
    def test_linear_search(self):
        """测试线性搜索"""
        linear_search = LinearSearch()
        
        # 测试基本搜索
        result = linear_search.search(self.test_data, self.target)
        self.assertIsNotNone(result)
        self.assertEqual(self.test_data[result], self.target)
        
        # 测试搜索不存在的元素
        result = linear_search.search(self.test_data, 999)
        self.assertIsNone(result)
        
        # 测试搜索所有出现位置
        occurrences = linear_search.search_all_occurrences(self.test_data, self.target)
        self.assertIsInstance(occurrences, list)
        self.assertGreater(len(occurrences), 0)
        
        # 测试条件搜索
        condition = lambda x: x > 50
        result = linear_search.search_with_condition(self.test_data, condition)
        self.assertIsNotNone(result)
        self.assertGreater(self.test_data[result], 50)
        
        # 测试哨兵搜索
        result = linear_search.search_sentinel(self.test_data.copy(), self.target)
        self.assertIsNotNone(result)
        self.assertEqual(self.test_data[result], self.target)
    
    def test_binary_search(self):
        """测试二分搜索"""
        binary_search = BinarySearch()
        
        # 测试基本搜索
        result = binary_search.search(self.sorted_data, self.target)
        self.assertIsNotNone(result)
        self.assertEqual(self.sorted_data[result], self.target)
        
        # 测试搜索不存在的元素
        result = binary_search.search(self.sorted_data, 999)
        self.assertIsNone(result)
        
        # 测试搜索第一次出现位置
        first_pos = binary_search.search_first_occurrence(self.sorted_data, self.target)
        self.assertIsNotNone(first_pos)
        self.assertEqual(self.sorted_data[first_pos], self.target)
        
        # 测试搜索最后一次出现位置
        last_pos = binary_search.search_last_occurrence(self.sorted_data, self.target)
        self.assertIsNotNone(last_pos)
        self.assertEqual(self.sorted_data[last_pos], self.target)
        
        # 验证第一次位置 <= 最后一次位置
        self.assertLessEqual(first_pos, last_pos)
    
    def test_jump_search(self):
        """测试跳跃搜索"""
        jump_search = JumpSearch()
        
        # 测试基本搜索
        result = jump_search.search(self.sorted_data, self.target)
        self.assertIsNotNone(result)
        self.assertEqual(self.sorted_data[result], self.target)
        
        # 测试搜索不存在的元素
        result = jump_search.search(self.sorted_data, 999)
        self.assertIsNone(result)
        
        # 测试自定义步长搜索
        custom_result = jump_search.search_with_custom_step(self.sorted_data, self.target, 5)
        self.assertIsNotNone(custom_result)
        self.assertEqual(self.sorted_data[custom_result], self.target)
        
        # 测试最优步长计算
        optimal_step = jump_search.find_optimal_step_size(len(self.sorted_data))
        self.assertIsInstance(optimal_step, int)
        self.assertGreater(optimal_step, 0)
    
    def test_interpolation_search(self):
        """测试插值搜索"""
        interpolation_search = InterpolationSearch()
        
        # 创建均匀分布的数据
        uniform_data = list(range(0, 100, 5))  # 0, 5, 10, 15, ...
        target = random.choice(uniform_data)
        
        # 测试基本搜索
        result = interpolation_search.search(uniform_data, target)
        self.assertIsNotNone(result)
        self.assertEqual(uniform_data[result], target)
        
        # 测试搜索不存在的元素
        result = interpolation_search.search(uniform_data, 999)
        self.assertIsNone(result)
        
        # 测试带边界检查的搜索
        result = interpolation_search.search_with_bounds_check(uniform_data, target)
        self.assertIsNotNone(result)
        self.assertEqual(uniform_data[result], target)
        
        # 测试数据分布检查
        is_uniform = interpolation_search.is_uniformly_distributed(uniform_data)
        self.assertTrue(is_uniform)
        
        # 测试非均匀分布数据
        non_uniform_data = [1, 2, 10, 15, 100]
        is_uniform = interpolation_search.is_uniformly_distributed(non_uniform_data)
        self.assertFalse(is_uniform)
    
    def test_exponential_search(self):
        """测试指数搜索"""
        exponential_search = ExponentialSearch()
        
        # 测试基本搜索
        result = exponential_search.search(self.sorted_data, self.target)
        self.assertIsNotNone(result)
        self.assertEqual(self.sorted_data[result], self.target)
        
        # 测试搜索不存在的元素
        result = exponential_search.search(self.sorted_data, 999)
        self.assertIsNone(result)
        
        # 测试无界搜索
        def data_generator(index):
            if index < len(self.sorted_data):
                return self.sorted_data[index]
            else:
                raise IndexError("超出范围")
        
        unbounded_result = exponential_search.search_unbounded(data_generator, self.target)
        self.assertIsNotNone(unbounded_result)
        self.assertEqual(self.sorted_data[unbounded_result], self.target)
    
    def test_depth_first_search(self):
        """测试深度优先搜索"""
        dfs = DepthFirstSearch()
        
        # 测试基本搜索
        result = dfs.search(self.graph, 'A', 'F')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0], 'A')
        
        # 测试路径查找
        path = dfs.find_path(self.graph, 'A', 'F')
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'F')
        
        # 测试不存在的路径
        path = dfs.find_path(self.graph, 'A', 'Z')
        self.assertIsNone(path)
    
    def test_breadth_first_search(self):
        """测试广度优先搜索"""
        bfs = BreadthFirstSearch()
        
        # 测试基本搜索
        result = bfs.search(self.graph, 'A', 'F')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0], 'A')
        
        # 测试最短路径查找
        shortest_path = bfs.find_shortest_path(self.graph, 'A', 'F')
        self.assertIsNotNone(shortest_path)
        self.assertEqual(shortest_path[0], 'A')
        self.assertEqual(shortest_path[-1], 'F')
        
        # 验证路径长度
        self.assertLessEqual(len(shortest_path), len(result))
    
    def test_astar_search(self):
        """测试A*搜索"""
        astar = AStarSearch()
        
        # 创建简单的启发式函数
        def simple_heuristic(vertex1, vertex2):
            return 1 if vertex1 != vertex2 else 0
        
        # 测试基本搜索
        path = astar.search(self.graph, 'A', 'F', simple_heuristic)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'F')
        
        # 测试多目标搜索
        targets = ['B', 'C', 'D']
        results = astar.search_with_multiple_goals(self.graph, 'A', targets, simple_heuristic)
        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), len(targets))
        
        for target in targets:
            self.assertIn(target, results)
            self.assertIsNotNone(results[target])
    
    def test_algorithm_complexity(self):
        """测试算法复杂度信息"""
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
            # 测试复杂度信息
            complexity = algorithm.get_complexity()
            self.assertIsInstance(complexity, dict)
            self.assertIn('time_complexity', complexity)
            self.assertIn('space_complexity', complexity)
            
            # 测试算法信息
            info = algorithm.get_algorithm_info()
            self.assertIsInstance(info, dict)
            self.assertIn('name', info)
            self.assertIn('description', info)
            self.assertIn('advantages', info)
            self.assertIn('disadvantages', info)
    
    def test_performance_comparison(self):
        """测试算法性能比较"""
        algorithms = {
            'LinearSearch': LinearSearch(),
            'BinarySearch': BinarySearch(),
            'JumpSearch': JumpSearch(),
            'InterpolationSearch': InterpolationSearch(),
            'ExponentialSearch': ExponentialSearch()
        }
        
        # 创建大数据集进行性能测试
        large_data = sorted([random.randint(1, 10000) for _ in range(1000)])
        target = random.choice(large_data)
        
        results = {}
        
        for name, algorithm in algorithms.items():
            # 重置计数器
            algorithm.operation_count = 0
            algorithm.comparison_count = 0
            
            # 执行搜索并计时
            start_time = time.time()
            result = algorithm.search(large_data, target)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # 毫秒
            
            results[name] = {
                'result': result,
                'time_ms': execution_time,
                'operations': algorithm.operation_count,
                'comparisons': algorithm.comparison_count
            }
            
            # 验证结果正确性
            self.assertIsNotNone(result)
            self.assertEqual(large_data[result], target)
        
        # 验证性能差异
        linear_time = results['LinearSearch']['time_ms']
        binary_time = results['BinarySearch']['time_ms']
        
        # 二分搜索应该比线性搜索快（对于大数据集）
        if len(large_data) > 100:
            self.assertLess(binary_time, linear_time * 10)  # 允许一定的误差
    
    def test_edge_cases(self):
        """测试边界情况"""
        algorithms = [
            LinearSearch(),
            BinarySearch(),
            JumpSearch(),
            InterpolationSearch(),
            ExponentialSearch()
        ]
        
        # 测试空数组
        for algorithm in algorithms:
            result = algorithm.search([], 1)
            self.assertIsNone(result)
        
        # 测试单元素数组
        for algorithm in algorithms:
            result = algorithm.search([1], 1)
            self.assertEqual(result, 0)
            
            result = algorithm.search([1], 2)
            self.assertIsNone(result)
        
        # 测试重复元素
        repeated_data = [1, 1, 1, 1, 1]
        for algorithm in algorithms:
            result = algorithm.search(repeated_data, 1)
            self.assertIsNotNone(result)
            self.assertEqual(repeated_data[result], 1)
    
    def test_error_handling(self):
        """测试错误处理"""
        algorithms = [
            LinearSearch(),
            BinarySearch(),
            JumpSearch(),
            InterpolationSearch(),
            ExponentialSearch()
        ]
        
        # 测试无效输入
        for algorithm in algorithms:
            # 应该能够处理None输入而不崩溃
            try:
                result = algorithm.search(None, 1)
                # 如果算法支持None输入，结果应该是None
                if result is not None:
                    self.fail("算法应该返回None或抛出异常")
            except (TypeError, AttributeError):
                # 这是预期的行为
                pass


def run_performance_benchmark():
    """运行性能基准测试"""
    print("搜索算法性能基准测试")
    print("=" * 50)
    
    algorithms = {
        'LinearSearch': LinearSearch(),
        'BinarySearch': BinarySearch(),
        'JumpSearch': JumpSearch(),
        'InterpolationSearch': InterpolationSearch(),
        'ExponentialSearch': ExponentialSearch()
    }
    
    # 测试不同大小的数据集
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        print(f"\n数据集大小: {size}")
        print("-" * 30)
        
        # 创建测试数据
        data = sorted([random.randint(1, size * 10) for _ in range(size)])
        target = random.choice(data)
        
        results = {}
        
        for name, algorithm in algorithms.items():
            # 重置计数器
            algorithm.operation_count = 0
            algorithm.comparison_count = 0
            
            # 执行搜索并计时
            start_time = time.time()
            result = algorithm.search(data, target)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # 毫秒
            
            results[name] = {
                'result': result,
                'time_ms': execution_time,
                'operations': algorithm.operation_count,
                'comparisons': algorithm.comparison_count
            }
            
            print(f"{name:20} | 时间: {execution_time:8.3f}ms | 操作: {algorithm.operation_count:6d} | 比较: {algorithm.comparison_count:6d}")
    
    return results


if __name__ == "__main__":
    # 运行单元测试
    unittest.main(verbosity=2, exit=False)
    
    # 运行性能基准测试
    print("\n" + "=" * 60)
    run_performance_benchmark() 