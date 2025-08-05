"""
用户界面模块 - 提供交互式命令行界面
"""

import sys
from typing import List, Optional
from colorama import Fore, Style

from core.algorithm_manager import AlgorithmManager
from utils.logger import Logger

class UserInterface:
    """用户界面类
    
    该类提供交互式命令行界面，允许用户：
    - 选择要学习的算法类别
    - 运行算法演示
    - 查看性能分析
    - 进行可视化学习
    """
    
    def __init__(self, algorithm_manager: AlgorithmManager):
        """初始化用户界面"""
        self.algorithm_manager = algorithm_manager
        self.logger = Logger()
        self.running = False
        
        # 菜单选项
        self.main_menu_options = {
            '1': ('数据结构基础', self.show_data_structures),
            '2': ('排序算法', self.show_sorting_algorithms),
            '3': ('搜索算法', self.show_searching_algorithms),
            '4': ('图算法', self.show_graph_algorithms),
            '5': ('动态规划', self.show_dynamic_programming),
            '6': ('贪心算法', self.show_greedy_algorithms),
            '7': ('性能分析', self.show_performance_analysis),
            '8': ('退出', self.exit_platform)
        }
        
        self.logger.info("用户界面初始化完成")
    
    def run(self):
        """运行用户界面"""
        self.running = True
        self.logger.info("用户界面启动")
        
        while self.running:
            try:
                self.show_main_menu()
                choice = self.get_user_choice()
                self.handle_main_menu_choice(choice)
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}用户中断操作{Style.RESET_ALL}")
                self.exit_platform()
                break
            except Exception as e:
                print(f"\n{Fore.RED}界面错误: {e}{Style.RESET_ALL}")
                self.logger.error(f"界面错误: {e}")
    
    def show_main_menu(self):
        """显示主菜单"""
        print(f"\n{Fore.CYAN}请选择要学习的算法类别:{Style.RESET_ALL}")
        print("-" * 50)
        
        for key, (title, _) in self.main_menu_options.items():
            print(f"{key}. {title}")
        
        print("-" * 50)
    
    def get_user_choice(self) -> str:
        """获取用户选择"""
        while True:
            try:
                choice = input(f"{Fore.GREEN}请输入选择 (1-{len(self.main_menu_options)}): {Style.RESET_ALL}").strip()
                if choice in self.main_menu_options:
                    return choice
                else:
                    print(f"{Fore.RED}无效选择，请输入 1-{len(self.main_menu_options)} 之间的数字{Style.RESET_ALL}")
            except EOFError:
                raise KeyboardInterrupt
    
    def handle_main_menu_choice(self, choice: str):
        """处理主菜单选择"""
        title, handler = self.main_menu_options[choice]
        print(f"\n{Fore.BLUE}选择: {title}{Style.RESET_ALL}")
        handler()
    
    def show_data_structures(self):
        """显示数据结构选项"""
        print(f"\n{Fore.CYAN}数据结构基础{Style.RESET_ALL}")
        print("=" * 40)
        
        # TODO: 实现数据结构展示
        print("1. 数组 (Array)")
        print("2. 链表 (Linked List)")
        print("3. 栈 (Stack)")
        print("4. 队列 (Queue)")
        print("5. 树 (Tree)")
        print("6. 图 (Graph)")
        print("7. 堆 (Heap)")
        print("8. 哈希表 (Hash Table)")
        print("9. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择数据结构 (1-9): {Style.RESET_ALL}").strip()
        
        if choice == '9':
            return
        
        # TODO: 实现具体数据结构演示
        print(f"{Fore.YELLOW}数据结构演示功能正在开发中...{Style.RESET_ALL}")
    
    def show_sorting_algorithms(self):
        """显示排序算法选项"""
        print(f"\n{Fore.CYAN}排序算法{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. 冒泡排序 (Bubble Sort)")
        print("2. 选择排序 (Selection Sort)")
        print("3. 插入排序 (Insertion Sort)")
        print("4. 归并排序 (Merge Sort)")
        print("5. 快速排序 (Quick Sort)")
        print("6. 堆排序 (Heap Sort)")
        print("7. 计数排序 (Counting Sort)")
        print("8. 基数排序 (Radix Sort)")
        print("9. 桶排序 (Bucket Sort)")
        print("10. 算法比较")
        print("11. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择排序算法 (1-11): {Style.RESET_ALL}").strip()
        
        if choice == '11':
            return
        elif choice == '10':
            self.compare_sorting_algorithms()
        else:
            self.run_sorting_algorithm(choice)
    
    def show_searching_algorithms(self):
        """显示搜索算法选项"""
        print(f"\n{Fore.CYAN}搜索算法{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. 线性搜索 (Linear Search)")
        print("2. 二分搜索 (Binary Search)")
        print("3. 深度优先搜索 (DFS)")
        print("4. 广度优先搜索 (BFS)")
        print("5. A*搜索算法")
        print("6. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择搜索算法 (1-6): {Style.RESET_ALL}").strip()
        
        if choice == '6':
            return
        
        # TODO: 实现具体搜索算法演示
        print(f"{Fore.YELLOW}搜索算法演示功能正在开发中...{Style.RESET_ALL}")
    
    def show_graph_algorithms(self):
        """显示图算法选项"""
        print(f"\n{Fore.CYAN}图算法{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. Dijkstra最短路径")
        print("2. Floyd-Warshall算法")
        print("3. Prim最小生成树")
        print("4. Kruskal最小生成树")
        print("5. 拓扑排序")
        print("6. 强连通分量")
        print("7. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择图算法 (1-7): {Style.RESET_ALL}").strip()
        
        if choice == '7':
            return
        
        # TODO: 实现具体图算法演示
        print(f"{Fore.YELLOW}图算法演示功能正在开发中...{Style.RESET_ALL}")
    
    def show_dynamic_programming(self):
        """显示动态规划选项"""
        print(f"\n{Fore.CYAN}动态规划{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. 背包问题 (Knapsack)")
        print("2. 最长公共子序列 (LCS)")
        print("3. 编辑距离 (Edit Distance)")
        print("4. 矩阵链乘法")
        print("5. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择动态规划问题 (1-5): {Style.RESET_ALL}").strip()
        
        if choice == '5':
            return
        
        # TODO: 实现具体动态规划演示
        print(f"{Fore.YELLOW}动态规划演示功能正在开发中...{Style.RESET_ALL}")
    
    def show_greedy_algorithms(self):
        """显示贪心算法选项"""
        print(f"\n{Fore.CYAN}贪心算法{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. 活动选择问题")
        print("2. 霍夫曼编码")
        print("3. 任务调度")
        print("4. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择贪心算法 (1-4): {Style.RESET_ALL}").strip()
        
        if choice == '4':
            return
        
        # TODO: 实现具体贪心算法演示
        print(f"{Fore.YELLOW}贪心算法演示功能正在开发中...{Style.RESET_ALL}")
    
    def show_performance_analysis(self):
        """显示性能分析选项"""
        print(f"\n{Fore.CYAN}性能分析{Style.RESET_ALL}")
        print("=" * 40)
        
        print("1. 时间复杂度分析")
        print("2. 空间复杂度分析")
        print("3. 实际运行时间测试")
        print("4. 算法效率对比")
        print("5. 返回主菜单")
        
        choice = input(f"{Fore.GREEN}请选择性能分析 (1-5): {Style.RESET_ALL}").strip()
        
        if choice == '5':
            return
        
        # TODO: 实现具体性能分析
        print(f"{Fore.YELLOW}性能分析功能正在开发中...{Style.RESET_ALL}")
    
    def run_sorting_algorithm(self, choice: str):
        """运行排序算法演示"""
        # 生成测试数据
        import random
        test_data = [random.randint(1, 100) for _ in range(10)]
        
        print(f"\n{Fore.YELLOW}测试数据: {test_data}{Style.RESET_ALL}")
        
        # TODO: 根据选择运行具体算法
        print(f"{Fore.YELLOW}排序算法演示功能正在开发中...{Style.RESET_ALL}")
    
    def compare_sorting_algorithms(self):
        """比较排序算法性能"""
        print(f"\n{Fore.CYAN}排序算法性能比较{Style.RESET_ALL}")
        print("=" * 50)
        
        # TODO: 实现算法性能比较
        print(f"{Fore.YELLOW}算法性能比较功能正在开发中...{Style.RESET_ALL}")
    
    def exit_platform(self):
        """退出平台"""
        print(f"\n{Fore.YELLOW}正在退出Algorithm Tutorial...{Style.RESET_ALL}")
        self.running = False
        self.logger.info("用户退出平台")
        print(f"{Fore.GREEN}感谢使用Algorithm Tutorial！{Style.RESET_ALL}")
        sys.exit(0) 