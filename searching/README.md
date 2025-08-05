# 搜索算法模块

这个模块包含了各种经典的搜索算法实现，从基本的线性搜索到高级的启发式搜索算法。

## 算法列表

### 数组搜索算法

#### 1. 线性搜索 (LinearSearch)
- **时间复杂度**: O(n)
- **空间复杂度**: O(1)
- **适用场景**: 小数据集、无序数据
- **特点**: 最基本的搜索算法，逐个检查每个元素

**功能特性**:
- 基本线性搜索
- 搜索所有出现位置
- 条件搜索
- 哨兵搜索（优化版本）

```python
from searching import LinearSearch

linear_search = LinearSearch()
result = linear_search.search([1, 2, 3, 4, 5], 3)  # 返回 2
```

#### 2. 二分搜索 (BinarySearch)
- **时间复杂度**: O(log n)
- **空间复杂度**: O(1)
- **适用场景**: 有序数组、大数据集
- **特点**: 高效的有序数组搜索算法

**功能特性**:
- 基本二分搜索
- 搜索第一次出现位置
- 搜索最后一次出现位置

```python
from searching import BinarySearch

binary_search = BinarySearch()
result = binary_search.search([1, 2, 3, 4, 5], 3)  # 返回 2
```

#### 3. 跳跃搜索 (JumpSearch)
- **时间复杂度**: O(√n)
- **空间复杂度**: O(1)
- **适用场景**: 有序数组、中等规模数据
- **特点**: 介于线性搜索和二分搜索之间的算法

**功能特性**:
- 基本跳跃搜索
- 自定义步长搜索
- 最优步长计算

```python
from searching import JumpSearch

jump_search = JumpSearch()
result = jump_search.search([1, 2, 3, 4, 5], 3)  # 返回 2
```

#### 4. 插值搜索 (InterpolationSearch)
- **时间复杂度**: O(log log n) 平均情况, O(n) 最坏情况
- **空间复杂度**: O(1)
- **适用场景**: 均匀分布的有序数据
- **特点**: 适用于均匀分布数据的改进二分搜索

**功能特性**:
- 基本插值搜索
- 带边界检查的搜索
- 数据分布检查

```python
from searching import InterpolationSearch

interpolation_search = InterpolationSearch()
result = interpolation_search.search([0, 5, 10, 15, 20], 10)  # 返回 2
```

#### 5. 指数搜索 (ExponentialSearch)
- **时间复杂度**: O(log n)
- **空间复杂度**: O(1)
- **适用场景**: 无界数据、流数据
- **特点**: 适用于无界搜索的算法

**功能特性**:
- 基本指数搜索
- 无界搜索
- 结合线性搜索和二分搜索

```python
from searching import ExponentialSearch

exponential_search = ExponentialSearch()
result = exponential_search.search([1, 2, 3, 4, 5], 3)  # 返回 2
```

### 图搜索算法

#### 6. 深度优先搜索 (DepthFirstSearch)
- **时间复杂度**: O(V + E)
- **空间复杂度**: O(V)
- **适用场景**: 图遍历、拓扑排序
- **特点**: 深度优先图遍历算法

**功能特性**:
- 基本深度优先搜索
- 路径查找
- 连通分量检测

```python
from searching import DepthFirstSearch
from data_structures.graph import Graph

graph = Graph()
# 添加顶点和边...
dfs = DepthFirstSearch()
result = dfs.search(graph, 'A', 'F')
```

#### 7. 广度优先搜索 (BreadthFirstSearch)
- **时间复杂度**: O(V + E)
- **空间复杂度**: O(V)
- **适用场景**: 最短路径、层次遍历
- **特点**: 广度优先图遍历算法

**功能特性**:
- 基本广度优先搜索
- 最短路径查找
- 层次遍历

```python
from searching import BreadthFirstSearch

bfs = BreadthFirstSearch()
shortest_path = bfs.find_shortest_path(graph, 'A', 'F')
```

#### 8. A*搜索 (AStarSearch)
- **时间复杂度**: O(E log V)
- **空间复杂度**: O(V)
- **适用场景**: 路径规划、游戏AI
- **特点**: 启发式搜索算法，结合Dijkstra和启发式函数

**功能特性**:
- 基本A*搜索
- 多目标搜索
- 自定义启发式函数
- 曼哈顿距离和欧几里得距离启发式函数

```python
from searching import AStarSearch

astar = AStarSearch()
heuristic = astar.create_manhattan_heuristic()
path = astar.search(graph, 'A', 'F', heuristic)
```

## 使用示例

### 基本使用

```python
from searching import LinearSearch, BinarySearch, JumpSearch

# 创建测试数据
data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 1, 45, 67, 89, 23, 45]
target = 67

# 线性搜索
linear_search = LinearSearch()
result = linear_search.search(data, target)
print(f"线性搜索结果: {result}")

# 二分搜索（需要有序数据）
sorted_data = sorted(data)
binary_search = BinarySearch()
result = binary_search.search(sorted_data, target)
print(f"二分搜索结果: {result}")

# 跳跃搜索
jump_search = JumpSearch()
result = jump_search.search(sorted_data, target)
print(f"跳跃搜索结果: {result}")
```

### 高级功能

```python
# 搜索所有出现位置
occurrences = linear_search.search_all_occurrences(data, target)
print(f"所有出现位置: {occurrences}")

# 条件搜索
condition = lambda x: x > 50
result = linear_search.search_with_condition(data, condition)
print(f"第一个大于50的元素位置: {result}")

# 搜索第一次和最后一次出现位置
first_pos = binary_search.search_first_occurrence(sorted_data, target)
last_pos = binary_search.search_last_occurrence(sorted_data, target)
print(f"第一次出现: {first_pos}, 最后一次出现: {last_pos}")

# 自定义步长跳跃搜索
custom_result = jump_search.search_with_custom_step(sorted_data, target, 5)
print(f"自定义步长搜索结果: {custom_result}")
```

### 图搜索示例

```python
from searching import DepthFirstSearch, BreadthFirstSearch, AStarSearch
from data_structures.graph import Graph

# 创建图
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

# 深度优先搜索
dfs = DepthFirstSearch()
dfs_result = dfs.search(graph, 'A', 'F')
print(f"DFS访问顺序: {dfs_result}")

# 广度优先搜索
bfs = BreadthFirstSearch()
bfs_result = bfs.search(graph, 'A', 'F')
print(f"BFS访问顺序: {bfs_result}")

# 最短路径
shortest_path = bfs.find_shortest_path(graph, 'A', 'F')
print(f"最短路径: {shortest_path}")

# A*搜索
astar = AStarSearch()
heuristic = astar.create_manhattan_heuristic()
path = astar.search(graph, 'A', 'F', heuristic)
print(f"A*搜索路径: {path}")
```

## 性能比较

### 时间复杂度比较

| 算法 | 最好情况 | 平均情况 | 最坏情况 | 空间复杂度 |
|------|----------|----------|----------|------------|
| 线性搜索 | O(1) | O(n/2) | O(n) | O(1) |
| 二分搜索 | O(1) | O(log n) | O(log n) | O(1) |
| 跳跃搜索 | O(1) | O(√n) | O(√n) | O(1) |
| 插值搜索 | O(1) | O(log log n) | O(n) | O(1) |
| 指数搜索 | O(1) | O(log n) | O(log n) | O(1) |
| DFS | O(1) | O(V + E) | O(V + E) | O(V) |
| BFS | O(1) | O(V + E) | O(V + E) | O(V) |
| A* | O(1) | O(E log V) | O(V log V) | O(V) |

### 适用场景

| 算法 | 最佳适用场景 | 优点 | 缺点 |
|------|-------------|------|------|
| 线性搜索 | 小数据集、无序数据 | 简单、通用 | 效率低 |
| 二分搜索 | 有序数组、大数据集 | 高效、稳定 | 要求有序 |
| 跳跃搜索 | 有序数组、中等规模 | 比线性快、比二分简单 | 不如二分高效 |
| 插值搜索 | 均匀分布数据 | 非常高效 | 对分布敏感 |
| 指数搜索 | 无界数据、流数据 | 适用于无界搜索 | 实现复杂 |
| DFS | 图遍历、拓扑排序 | 内存少、适合深度问题 | 可能不是最短路径 |
| BFS | 最短路径、层次遍历 | 能找到最短路径 | 内存使用多 |
| A* | 路径规划、游戏AI | 高效、最优路径 | 需要启发式函数 |

## 运行演示

### 基本演示

```bash
cd searching
python search_demo.py
```

### 可视化演示

```bash
python search_visualization.py
```

### 运行测试

```bash
python test_search_algorithms.py
```

## 算法选择指南

### 选择数组搜索算法

1. **数据规模小 (< 100)**: 使用线性搜索
2. **数据有序且规模中等 (100-1000)**: 使用跳跃搜索
3. **数据有序且规模大 (> 1000)**: 使用二分搜索
4. **数据均匀分布**: 使用插值搜索
5. **无界数据**: 使用指数搜索

### 选择图搜索算法

1. **需要遍历所有节点**: 使用DFS或BFS
2. **需要最短路径**: 使用BFS
3. **需要路径规划**: 使用A*
4. **内存受限**: 使用DFS
5. **需要层次信息**: 使用BFS

## 扩展和定制

### 添加新的启发式函数

```python
def custom_heuristic(vertex1, vertex2):
    # 实现自定义启发式函数
    return distance(vertex1, vertex2)

astar = AStarSearch()
path = astar.search(graph, start, end, custom_heuristic)
```

### 自定义搜索条件

```python
def custom_condition(element):
    # 实现自定义搜索条件
    return element > 50 and element % 2 == 0

linear_search = LinearSearch()
result = linear_search.search_with_condition(data, custom_condition)
```

## 注意事项

1. **数据预处理**: 某些算法（如二分搜索）要求数据有序
2. **内存使用**: 图搜索算法可能需要较多内存
3. **启发式函数**: A*搜索的效果很大程度上取决于启发式函数的质量
4. **边界情况**: 注意处理空数组、单元素数组等边界情况
5. **性能测试**: 在实际应用中，建议进行性能测试以选择最适合的算法

## 贡献

欢迎提交问题报告、功能请求和代码贡献！

## 许可证

本项目采用 MIT 许可证。 