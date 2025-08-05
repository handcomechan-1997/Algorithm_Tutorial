"""
搜索算法可视化演示

使用matplotlib展示各种搜索算法的执行过程。
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from typing import List, Any, Dict, Optional
import time

from linear_search import LinearSearch
from binary_search import BinarySearch
from jump_search import JumpSearch
from interpolation_search import InterpolationSearch
from exponential_search import ExponentialSearch


class SearchVisualizer:
    """搜索算法可视化器"""
    
    def __init__(self):
        """初始化可视化器"""
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.colors = {
            'default': 'lightblue',
            'current': 'red',
            'visited': 'orange',
            'found': 'green',
            'target': 'purple'
        }
    
    def visualize_linear_search(self, data: List[Any], target: Any, save_path: str = None):
        """可视化线性搜索过程"""
        self.ax.clear()
        self.ax.set_title('线性搜索可视化', fontsize=16)
        
        # 创建数据可视化
        x = range(len(data))
        colors = [self.colors['default']] * len(data)
        
        # 执行线性搜索并记录步骤
        linear_search = LinearSearch()
        result = linear_search.search(data, target)
        
        # 创建动画
        def animate(frame):
            self.ax.clear()
            self.ax.set_title(f'线性搜索 - 步骤 {frame + 1}', fontsize=16)
            
            # 更新颜色
            for i in range(len(data)):
                if i < frame:
                    colors[i] = self.colors['visited']
                elif i == frame:
                    colors[i] = self.colors['current']
                else:
                    colors[i] = self.colors['default']
                
                if data[i] == target:
                    colors[i] = self.colors['target']
            
            # 绘制条形图
            bars = self.ax.bar(x, data, color=colors, alpha=0.7)
            
            # 添加数值标签
            for i, (bar, val) in enumerate(zip(bars, data)):
                height = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{val}', ha='center', va='bottom')
            
            self.ax.set_xlabel('索引')
            self.ax.set_ylabel('值')
            self.ax.set_ylim(0, max(data) * 1.1)
            
            # 添加目标值线
            self.ax.axhline(y=target, color='red', linestyle='--', alpha=0.5, label=f'目标: {target}')
            self.ax.legend()
            
            if frame < len(data):
                self.ax.text(0.02, 0.98, f'检查索引 {frame}: {data[frame]}', 
                           transform=self.ax.transAxes, fontsize=12,
                           verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # 创建动画
        anim = animation.FuncAnimation(self.fig, animate, frames=len(data), 
                                     interval=1000, repeat=False)
        
        if save_path:
            anim.save(save_path, writer='pillow')
        
        plt.tight_layout()
        plt.show()
        
        return result
    
    def visualize_binary_search(self, data: List[Any], target: Any, save_path: str = None):
        """可视化二分搜索过程"""
        self.ax.clear()
        self.ax.set_title('二分搜索可视化', fontsize=16)
        
        # 确保数据有序
        data = sorted(data)
        x = range(len(data))
        
        # 执行二分搜索并记录步骤
        binary_search = BinarySearch()
        result = binary_search.search(data, target)
        
        # 创建动画
        def animate(frame):
            self.ax.clear()
            self.ax.set_title(f'二分搜索 - 步骤 {frame + 1}', fontsize=16)
            
            colors = [self.colors['default']] * len(data)
            
            # 根据搜索步骤更新颜色
            if frame < len(binary_search.steps):
                step = binary_search.steps[frame]
                if step['type'] == 'compare':
                    mid = step['mid']
                    colors[mid] = self.colors['current']
                    
                    # 标记已访问的范围
                    left, right = step['left'], step['right']
                    for i in range(left, right + 1):
                        if i != mid:
                            colors[i] = self.colors['visited']
            
            # 绘制条形图
            bars = self.ax.bar(x, data, color=colors, alpha=0.7)
            
            # 添加数值标签
            for i, (bar, val) in enumerate(zip(bars, data)):
                height = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{val}', ha='center', va='bottom')
            
            self.ax.set_xlabel('索引')
            self.ax.set_ylabel('值')
            self.ax.set_ylim(0, max(data) * 1.1)
            
            # 添加目标值线
            self.ax.axhline(y=target, color='red', linestyle='--', alpha=0.5, label=f'目标: {target}')
            self.ax.legend()
            
            # 显示当前搜索范围
            if frame < len(binary_search.steps):
                step = binary_search.steps[frame]
                if step['type'] == 'compare':
                    left, right, mid = step['left'], step['right'], step['mid']
                    self.ax.text(0.02, 0.98, f'范围 [{left}, {right}], 中点 {mid}: {data[mid]}', 
                               transform=self.ax.transAxes, fontsize=12,
                               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # 创建动画
        anim = animation.FuncAnimation(self.fig, animate, frames=len(binary_search.steps), 
                                     interval=1500, repeat=False)
        
        if save_path:
            anim.save(save_path, writer='pillow')
        
        plt.tight_layout()
        plt.show()
        
        return result
    
    def visualize_jump_search(self, data: List[Any], target: Any, save_path: str = None):
        """可视化跳跃搜索过程"""
        self.ax.clear()
        self.ax.set_title('跳跃搜索可视化', fontsize=16)
        
        # 确保数据有序
        data = sorted(data)
        x = range(len(data))
        
        # 执行跳跃搜索并记录步骤
        jump_search = JumpSearch()
        result = jump_search.search(data, target)
        
        # 创建动画
        def animate(frame):
            self.ax.clear()
            self.ax.set_title(f'跳跃搜索 - 步骤 {frame + 1}', fontsize=16)
            
            colors = [self.colors['default']] * len(data)
            
            # 根据搜索步骤更新颜色
            if frame < len(jump_search.steps):
                step = jump_search.steps[frame]
                if step['type'] == 'jump':
                    # 跳跃阶段
                    to_index = step['to_index']
                    colors[to_index] = self.colors['current']
                    
                    # 标记跳跃路径
                    step_size = step['step']
                    for i in range(0, min(to_index, len(data)), step_size):
                        if i != to_index:
                            colors[i] = self.colors['visited']
                            
                elif step['type'] == 'linear_search':
                    # 线性搜索阶段
                    index = step['index']
                    colors[index] = self.colors['current']
                    
                    # 标记线性搜索范围
                    step_size = int(len(data) ** 0.5)
                    start = (index // step_size) * step_size
                    for i in range(start, min(start + step_size, len(data))):
                        if i != index:
                            colors[i] = self.colors['visited']
            
            # 绘制条形图
            bars = self.ax.bar(x, data, color=colors, alpha=0.7)
            
            # 添加数值标签
            for i, (bar, val) in enumerate(zip(bars, data)):
                height = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{val}', ha='center', va='bottom')
            
            self.ax.set_xlabel('索引')
            self.ax.set_ylabel('值')
            self.ax.set_ylim(0, max(data) * 1.1)
            
            # 添加目标值线
            self.ax.axhline(y=target, color='red', linestyle='--', alpha=0.5, label=f'目标: {target}')
            self.ax.legend()
            
            # 显示当前步骤信息
            if frame < len(jump_search.steps):
                step = jump_search.steps[frame]
                if step['type'] == 'jump':
                    self.ax.text(0.02, 0.98, f'跳跃到索引 {step["to_index"]}: {step["current_element"]}', 
                               transform=self.ax.transAxes, fontsize=12,
                               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
                elif step['type'] == 'linear_search':
                    self.ax.text(0.02, 0.98, f'线性搜索索引 {step["index"]}: {step["current_element"]}', 
                               transform=self.ax.transAxes, fontsize=12,
                               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # 创建动画
        anim = animation.FuncAnimation(self.fig, animate, frames=len(jump_search.steps), 
                                     interval=1200, repeat=False)
        
        if save_path:
            anim.save(save_path, writer='pillow')
        
        plt.tight_layout()
        plt.show()
        
        return result
    
    def compare_search_algorithms(self, data: List[Any], target: Any):
        """比较不同搜索算法的性能"""
        algorithms = {
            'Linear Search': LinearSearch(),
            'Binary Search': BinarySearch(),
            'Jump Search': JumpSearch(),
            'Interpolation Search': InterpolationSearch(),
            'Exponential Search': ExponentialSearch()
        }
        
        results = {}
        
        # 执行所有算法
        for name, algorithm in algorithms.items():
            start_time = time.time()
            result = algorithm.search(data, target)
            end_time = time.time()
            
            results[name] = {
                'result': result,
                'time': (end_time - start_time) * 1000,  # 毫秒
                'operations': algorithm.operation_count,
                'comparisons': algorithm.comparison_count
            }
        
        # 创建比较图表
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # 执行时间比较
        names = list(results.keys())
        times = [results[name]['time'] for name in names]
        ax1.bar(names, times, color='skyblue')
        ax1.set_title('执行时间比较 (毫秒)')
        ax1.set_ylabel('时间 (ms)')
        ax1.tick_params(axis='x', rotation=45)
        
        # 操作次数比较
        operations = [results[name]['operations'] for name in names]
        ax2.bar(names, operations, color='lightcoral')
        ax2.set_title('操作次数比较')
        ax2.set_ylabel('操作次数')
        ax2.tick_params(axis='x', rotation=45)
        
        # 比较次数比较
        comparisons = [results[name]['comparisons'] for name in names]
        ax3.bar(names, comparisons, color='lightgreen')
        ax3.set_title('比较次数比较')
        ax3.set_ylabel('比较次数')
        ax3.tick_params(axis='x', rotation=45)
        
        # 算法效率雷达图
        categories = ['时间效率', '操作效率', '比较效率', '空间效率']
        
        # 归一化数据 (0-1)
        max_time = max(times) if times else 1
        max_ops = max(operations) if operations else 1
        max_comps = max(comparisons) if comparisons else 1
        
        # 计算效率分数 (越低越好)
        efficiency_scores = {}
        for name in names:
            time_score = 1 - (results[name]['time'] / max_time)
            ops_score = 1 - (results[name]['operations'] / max_ops)
            comps_score = 1 - (results[name]['comparisons'] / max_comps)
            space_score = 1.0  # 所有算法都是O(1)空间复杂度
            
            efficiency_scores[name] = [time_score, ops_score, comps_score, space_score]
        
        # 绘制雷达图
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]  # 闭合图形
        
        for name in names:
            values = efficiency_scores[name] + efficiency_scores[name][:1]
            ax4.plot(angles, values, 'o-', linewidth=2, label=name)
            ax4.fill(angles, values, alpha=0.25)
        
        ax4.set_xticks(angles[:-1])
        ax4.set_xticklabels(categories)
        ax4.set_ylim(0, 1)
        ax4.set_title('算法效率雷达图')
        ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        plt.tight_layout()
        plt.show()
        
        return results


def main():
    """主函数 - 演示可视化功能"""
    visualizer = SearchVisualizer()
    
    # 创建测试数据
    data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 1, 45, 67, 89, 23, 45]
    target = 67
    
    print("搜索算法可视化演示")
    print("=" * 50)
    print(f"测试数据: {data}")
    print(f"目标元素: {target}")
    
    # 可视化线性搜索
    print("\n1. 线性搜索可视化")
    result = visualizer.visualize_linear_search(data, target)
    print(f"搜索结果: {result}")
    
    # 可视化二分搜索
    print("\n2. 二分搜索可视化")
    sorted_data = sorted(data)
    result = visualizer.visualize_binary_search(sorted_data, target)
    print(f"搜索结果: {result}")
    
    # 可视化跳跃搜索
    print("\n3. 跳跃搜索可视化")
    result = visualizer.visualize_jump_search(sorted_data, target)
    print(f"搜索结果: {result}")
    
    # 算法性能比较
    print("\n4. 算法性能比较")
    results = visualizer.compare_search_algorithms(sorted_data, target)
    
    print("\n性能比较结果:")
    for name, result in results.items():
        print(f"{name:20} | 时间: {result['time']:8.3f}ms | 操作: {result['operations']:6d} | 比较: {result['comparisons']:6d}")


if __name__ == "__main__":
    main() 