#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试搜索算法的execute方法实现

验证所有搜索算法类都正确实现了抽象基类要求的execute方法。
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from searching.linear_search import LinearSearch
from searching.binary_search import BinarySearch
from searching.jump_search import JumpSearch
from searching.interpolation_search import InterpolationSearch
from searching.exponential_search import ExponentialSearch
from searching.graph_search import DepthFirstSearch, BreadthFirstSearch
from searching.heuristic_search import AStarSearch
from data_structures.graph import Graph


def test_linear_search():
    """测试线性搜索的execute方法"""
    print("测试 LinearSearch.execute()...")
    search = LinearSearch()
    
    # 测试基本搜索
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    result = search.execute(data, target=7)
    assert result == 3, f"期望位置3，实际位置{result}"
    
    # 测试条件搜索
    result = search.execute(data, condition=lambda x: x > 10, search_type='condition')
    assert result == 5, f"期望位置5，实际位置{result}"
    
    # 测试搜索所有出现位置
    data_with_duplicates = [1, 3, 5, 7, 5, 9, 5, 11]
    result = search.execute(data_with_duplicates, target=5, search_type='all')
    assert result == [2, 4, 6], f"期望位置[2,4,6]，实际位置{result}"
    
    print("✓ LinearSearch.execute() 测试通过")


def test_binary_search():
    """测试二分搜索的execute方法"""
    print("测试 BinarySearch.execute()...")
    search = BinarySearch()
    
    # 测试基本搜索
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    result = search.execute(data, target=7)
    assert result == 3, f"期望位置3，实际位置{result}"
    
    # 测试搜索第一次出现位置
    data_with_duplicates = [1, 3, 5, 5, 5, 7, 9, 11]
    result = search.execute(data_with_duplicates, target=5, search_type='first')
    assert result == 2, f"期望位置2，实际位置{result}"
    
    # 测试搜索最后一次出现位置
    result = search.execute(data_with_duplicates, target=5, search_type='last')
    assert result == 4, f"期望位置4，实际位置{result}"
    
    print("✓ BinarySearch.execute() 测试通过")


def test_jump_search():
    """测试跳跃搜索的execute方法"""
    print("测试 JumpSearch.execute()...")
    search = JumpSearch()
    
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = search.execute(data, target=11)
    assert result == 5, f"期望位置5，实际位置{result}"
    
    print("✓ JumpSearch.execute() 测试通过")


def test_interpolation_search():
    """测试插值搜索的execute方法"""
    print("测试 InterpolationSearch.execute()...")
    search = InterpolationSearch()
    
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = search.execute(data, target=11)
    assert result == 5, f"期望位置5，实际位置{result}"
    
    print("✓ InterpolationSearch.execute() 测试通过")


def test_exponential_search():
    """测试指数搜索的execute方法"""
    print("测试 ExponentialSearch.execute()...")
    search = ExponentialSearch()
    
    # 测试列表搜索
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = search.execute(data, target=11)
    assert result == 5, f"期望位置5，实际位置{result}"
    
    # 测试生成器搜索
    def data_generator(index):
        if index < 10:
            return index * 2 + 1
        return None
    
    result = search.execute(None, target=11, data_generator=data_generator)
    assert result == 5, f"期望位置5，实际位置{result}"
    
    print("✓ ExponentialSearch.execute() 测试通过")


def test_graph_search():
    """测试图搜索的execute方法"""
    print("测试图搜索的execute()方法...")
    
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
    
    # 测试深度优先搜索
    dfs = DepthFirstSearch()
    result = dfs.execute(graph, start_vertex='A', search_type='traversal')
    assert len(result) > 0, "DFS应该返回访问顺序"
    
    result = dfs.execute(graph, start_vertex='A', target_vertex='F', search_type='path')
    assert result is not None, "DFS应该能找到路径"
    
    # 测试广度优先搜索
    bfs = BreadthFirstSearch()
    result = bfs.execute(graph, start_vertex='A', search_type='traversal')
    assert len(result) > 0, "BFS应该返回访问顺序"
    
    result = bfs.execute(graph, start_vertex='A', target_vertex='F', search_type='shortest_path')
    assert result is not None, "BFS应该能找到最短路径"
    
    print("✓ 图搜索execute()方法测试通过")


def test_heuristic_search():
    """测试启发式搜索的execute方法"""
    print("测试 AStarSearch.execute()...")
    
    # 创建测试图
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D']
    edges = [
        ('A', 'B', 1), ('A', 'C', 4),
        ('B', 'D', 2), ('C', 'D', 1)
    ]
    
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    for start, end, weight in edges:
        graph.add_edge(start, end, weight)
    
    # 简单的启发式函数
    def simple_heuristic(vertex1, vertex2):
        return 0  # 简化为0，相当于Dijkstra算法
    
    search = AStarSearch()
    result = search.execute(graph, start_vertex='A', target_vertex='D', 
                           heuristic=simple_heuristic, search_type='traversal')
    assert len(result) > 0, "A*应该返回访问顺序"
    
    result = search.execute(graph, start_vertex='A', target_vertex='D', 
                           heuristic=simple_heuristic, search_type='path')
    assert result is not None, "A*应该能找到路径"
    
    print("✓ AStarSearch.execute() 测试通过")


def test_performance_measurement():
    """测试性能测量功能"""
    print("测试性能测量功能...")
    
    search = LinearSearch()
    data = list(range(1000))
    
    # 使用measure_performance方法
    result = search.measure_performance(data, target=500)
    
    assert 'result' in result, "性能测量应该返回结果"
    assert 'execution_time' in result, "性能测量应该返回执行时间"
    assert 'comparison_count' in result, "性能测量应该返回比较次数"
    assert result['result'] == 500, f"期望位置500，实际位置{result['result']}"
    
    print("✓ 性能测量功能测试通过")


def main():
    """运行所有测试"""
    print("开始测试搜索算法的execute方法实现...\n")
    
    try:
        test_linear_search()
        test_binary_search()
        test_jump_search()
        test_interpolation_search()
        test_exponential_search()
        test_graph_search()
        test_heuristic_search()
        test_performance_measurement()
        
        print("\n🎉 所有测试通过！所有搜索算法类都正确实现了execute方法。")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 