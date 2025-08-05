"""
搜索算法模块

包含各种搜索算法的实现：
- 线性搜索
- 二分搜索
- 跳跃搜索
- 插值搜索
- 指数搜索
- 图搜索（DFS、BFS）
- 启发式搜索（A*）
"""

from .linear_search import LinearSearch
from .binary_search import BinarySearch
from .jump_search import JumpSearch
from .interpolation_search import InterpolationSearch
from .exponential_search import ExponentialSearch
from .graph_search import DepthFirstSearch, BreadthFirstSearch
from .heuristic_search import AStarSearch

__all__ = [
    'LinearSearch',
    'BinarySearch', 
    'JumpSearch',
    'InterpolationSearch',
    'ExponentialSearch',
    'DepthFirstSearch',
    'BreadthFirstSearch',
    'AStarSearch'
]

# 算法分类
ARRAY_SEARCH_ALGORITHMS = [
    LinearSearch,
    BinarySearch,
    JumpSearch,
    InterpolationSearch,
    ExponentialSearch
]

GRAPH_SEARCH_ALGORITHMS = [
    DepthFirstSearch,
    BreadthFirstSearch,
    AStarSearch
]

# 算法信息
ALGORITHM_INFO = {
    'LinearSearch': {
        'complexity': 'O(n)',
        'description': '最基本的搜索算法，逐个检查每个元素',
        'best_for': '小数据集、无序数据'
    },
    'BinarySearch': {
        'complexity': 'O(log n)',
        'description': '高效的有序数组搜索算法',
        'best_for': '有序数组、大数据集'
    },
    'JumpSearch': {
        'complexity': 'O(√n)',
        'description': '介于线性搜索和二分搜索之间的算法',
        'best_for': '有序数组、中等规模数据'
    },
    'InterpolationSearch': {
        'complexity': 'O(log log n)',
        'description': '适用于均匀分布数据的改进二分搜索',
        'best_for': '均匀分布的有序数据'
    },
    'ExponentialSearch': {
        'complexity': 'O(log n)',
        'description': '适用于无界搜索的算法',
        'best_for': '无界数据、流数据'
    },
    'DepthFirstSearch': {
        'complexity': 'O(V + E)',
        'description': '深度优先图遍历算法',
        'best_for': '图遍历、拓扑排序'
    },
    'BreadthFirstSearch': {
        'complexity': 'O(V + E)',
        'description': '广度优先图遍历算法',
        'best_for': '最短路径、层次遍历'
    },
    'AStarSearch': {
        'complexity': 'O(E log V)',
        'description': '启发式搜索算法，结合Dijkstra和启发式函数',
        'best_for': '路径规划、游戏AI'
    }
} 