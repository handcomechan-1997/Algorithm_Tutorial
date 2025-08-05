"""
图表绘制模块 - 提供算法性能分析的可视化图表
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Any, Optional
import seaborn as sns

from utils.logger import Logger

class PerformancePlotter:
    """性能图表绘制器
    
    该类提供算法性能分析的可视化图表功能，包括：
    - 执行时间对比图
    - 内存使用分析图
    - 复杂度分析图
    - 性能趋势图
    """
    
    def __init__(self):
        """初始化图表绘制器"""
        self.logger = Logger()
        
        # 设置中文字体支持
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 设置图表样式
        sns.set_style("whitegrid")
        plt.style.use('seaborn-v0_8')
        
        self.logger.info("性能图表绘制器初始化完成")
    
    def plot_execution_time_comparison(self, results: Dict[str, Any], title: str = "算法执行时间对比"):
        """绘制执行时间对比图
        
        Args:
            results: 性能测试结果
            title: 图表标题
        """
        try:
            algorithms = []
            execution_times = []
            
            for algorithm_name, result in results.items():
                if isinstance(result, dict) and 'execution_time' in result:
                    algorithms.append(algorithm_name)
                    execution_times.append(result['execution_time'])
            
            if not algorithms:
                self.logger.warning("没有有效的执行时间数据")
                return
            
            plt.figure(figsize=(12, 6))
            
            # 创建柱状图
            bars = plt.bar(algorithms, execution_times, color='skyblue', alpha=0.7)
            
            # 添加数值标签
            for bar, time in zip(bars, execution_times):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.0001,
                        f'{time:.4f}s', ha='center', va='bottom', fontsize=10)
            
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('算法名称', fontsize=12)
            plt.ylabel('执行时间 (秒)', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            # 保存图表
            plt.savefig('execution_time_comparison.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            self.logger.info("执行时间对比图绘制完成")
            
        except Exception as e:
            self.logger.error(f"绘制执行时间对比图失败: {e}")
    
    def plot_memory_usage_comparison(self, results: Dict[str, Any], title: str = "算法内存使用对比"):
        """绘制内存使用对比图
        
        Args:
            results: 性能测试结果
            title: 图表标题
        """
        try:
            algorithms = []
            memory_usages = []
            
            for algorithm_name, result in results.items():
                if isinstance(result, dict) and 'memory_usage' in result:
                    algorithms.append(algorithm_name)
                    memory_usages.append(result['memory_usage'])
            
            if not algorithms:
                self.logger.warning("没有有效的内存使用数据")
                return
            
            plt.figure(figsize=(12, 6))
            
            # 创建柱状图
            bars = plt.bar(algorithms, memory_usages, color='lightcoral', alpha=0.7)
            
            # 添加数值标签
            for bar, memory in zip(bars, memory_usages):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                        f'{memory:,} B', ha='center', va='bottom', fontsize=10)
            
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('算法名称', fontsize=12)
            plt.ylabel('内存使用 (字节)', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            # 保存图表
            plt.savefig('memory_usage_comparison.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            self.logger.info("内存使用对比图绘制完成")
            
        except Exception as e:
            self.logger.error(f"绘制内存使用对比图失败: {e}")
    
    def plot_complexity_analysis(self, complexity_data: Dict[str, List[float]], 
                                data_sizes: List[int], title: str = "算法复杂度分析"):
        """绘制复杂度分析图
        
        Args:
            complexity_data: 复杂度数据 {算法名: [执行时间列表]}
            data_sizes: 数据大小列表
            title: 图表标题
        """
        try:
            plt.figure(figsize=(12, 8))
            
            colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
            
            for i, (algorithm_name, execution_times) in enumerate(complexity_data.items()):
                color = colors[i % len(colors)]
                plt.plot(data_sizes, execution_times, marker='o', label=algorithm_name, 
                        color=color, linewidth=2, markersize=6)
            
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('数据大小', fontsize=12)
            plt.ylabel('执行时间 (秒)', fontsize=12)
            plt.legend(fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            # 保存图表
            plt.savefig('complexity_analysis.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            self.logger.info("复杂度分析图绘制完成")
            
        except Exception as e:
            self.logger.error(f"绘制复杂度分析图失败: {e}")
    
    def plot_operation_counts(self, results: Dict[str, Any], title: str = "算法操作次数对比"):
        """绘制操作次数对比图
        
        Args:
            results: 性能测试结果
            title: 图表标题
        """
        try:
            algorithms = []
            comparison_counts = []
            swap_counts = []
            
            for algorithm_name, result in results.items():
                if isinstance(result, dict):
                    algorithms.append(algorithm_name)
                    comparison_counts.append(result.get('comparison_count', 0))
                    swap_counts.append(result.get('swap_count', 0))
            
            if not algorithms:
                self.logger.warning("没有有效的操作次数数据")
                return
            
            x = np.arange(len(algorithms))
            width = 0.35
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # 创建分组柱状图
            bars1 = ax.bar(x - width/2, comparison_counts, width, label='比较次数', 
                          color='lightblue', alpha=0.7)
            bars2 = ax.bar(x + width/2, swap_counts, width, label='交换次数', 
                          color='lightcoral', alpha=0.7)
            
            # 添加数值标签
            for bar in bars1:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'{int(height):,}', ha='center', va='bottom', fontsize=9)
            
            for bar in bars2:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'{int(height):,}', ha='center', va='bottom', fontsize=9)
            
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel('算法名称', fontsize=12)
            ax.set_ylabel('操作次数', fontsize=12)
            ax.set_xticks(x)
            ax.set_xticklabels(algorithms, rotation=45, ha='right')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
            plt.tight_layout()
            
            # 保存图表
            plt.savefig('operation_counts_comparison.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            self.logger.info("操作次数对比图绘制完成")
            
        except Exception as e:
            self.logger.error(f"绘制操作次数对比图失败: {e}")
    
    def plot_performance_trend(self, trend_data: Dict[str, List[float]], 
                              x_labels: List[str], title: str = "性能趋势分析"):
        """绘制性能趋势图
        
        Args:
            trend_data: 趋势数据 {算法名: [性能值列表]}
            x_labels: X轴标签
            title: 图表标题
        """
        try:
            plt.figure(figsize=(12, 6))
            
            colors = ['red', 'blue', 'green', 'orange', 'purple']
            x = np.arange(len(x_labels))
            
            for i, (algorithm_name, values) in enumerate(trend_data.items()):
                color = colors[i % len(colors)]
                plt.plot(x, values, marker='o', label=algorithm_name, 
                        color=color, linewidth=2, markersize=6)
            
            plt.title(title, fontsize=16, fontweight='bold')
            plt.xlabel('测试场景', fontsize=12)
            plt.ylabel('性能指标', fontsize=12)
            plt.xticks(x, x_labels, rotation=45, ha='right')
            plt.legend(fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            # 保存图表
            plt.savefig('performance_trend.png', dpi=300, bbox_inches='tight')
            plt.show()
            
            self.logger.info("性能趋势图绘制完成")
            
        except Exception as e:
            self.logger.error(f"绘制性能趋势图失败: {e}")
    
    def create_summary_report(self, results: Dict[str, Any], filename: str = "performance_report.html"):
        """创建性能分析报告
        
        Args:
            results: 性能测试结果
            filename: 报告文件名
        """
        try:
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>算法性能分析报告</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    h1 { color: #2c3e50; text-align: center; }
                    table { border-collapse: collapse; width: 100%; margin: 20px 0; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    .metric { font-weight: bold; color: #e74c3c; }
                </style>
            </head>
            <body>
                <h1>算法性能分析报告</h1>
                <table>
                    <tr>
                        <th>算法名称</th>
                        <th>执行时间 (秒)</th>
                        <th>内存使用 (字节)</th>
                        <th>比较次数</th>
                        <th>交换次数</th>
                    </tr>
            """
            
            for algorithm_name, result in results.items():
                if isinstance(result, dict):
                    html_content += f"""
                    <tr>
                        <td>{algorithm_name}</td>
                        <td class="metric">{result.get('execution_time', 0):.6f}</td>
                        <td>{result.get('memory_usage', 0):,}</td>
                        <td>{result.get('comparison_count', 0):,}</td>
                        <td>{result.get('swap_count', 0):,}</td>
                    </tr>
                    """
            
            html_content += """
                </table>
                <p><em>报告生成时间: """ + str(__import__('datetime').datetime.now()) + """</em></p>
            </body>
            </html>
            """
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.logger.info(f"性能分析报告已保存: {filename}")
            
        except Exception as e:
            self.logger.error(f"创建性能分析报告失败: {e}")
    
    def close_all_plots(self):
        """关闭所有图表"""
        plt.close('all')
        self.logger.info("所有图表已关闭") 