"""
动画引擎 - 实现算法可视化的动画功能
"""

import time
import threading
from typing import Any, Dict, List, Optional
from colorama import Fore, Style

from core.visualizer import Visualizer
from utils.logger import Logger

class AlgorithmAnimator(Visualizer):
    """算法动画引擎
    
    该类实现算法执行过程的可视化动画，包括：
    - 步骤分解显示
    - 数据状态变化
    - 交互式控制
    - 性能指标展示
    """
    
    def __init__(self):
        """初始化动画引擎"""
        super().__init__()
        self.logger = Logger()
        self.steps = []
        self.current_step_index = 0
        self.auto_play = False
        self.step_delay = 1.0  # 默认步骤延迟时间
        
    def visualize_step(self, step_data: Dict[str, Any]):
        """可视化单个步骤
        
        Args:
            step_data: 步骤数据
        """
        step_num = step_data.get('step', 0)
        description = step_data.get('description', '')
        data_state = step_data.get('data_state', None)
        comparisons = step_data.get('comparisons', 0)
        swaps = step_data.get('swaps', 0)
        
        print(f"\n{Fore.CYAN}步骤 {step_num + 1}:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}描述: {description}{Style.RESET_ALL}")
        
        if data_state is not None:
            self._display_data_state(data_state)
        
        print(f"{Fore.BLUE}比较次数: {comparisons} | 交换次数: {swaps}{Style.RESET_ALL}")
        
        if not self.auto_play:
            input(f"{Fore.GREEN}按回车键继续...{Style.RESET_ALL}")
        else:
            time.sleep(self.step_delay)
    
    def play_animation(self, steps: List[Dict[str, Any]]):
        """播放动画
        
        Args:
            steps: 步骤列表
        """
        self.steps = steps
        self.total_steps = len(steps)
        self.current_step_index = 0
        self.is_playing = True
        
        self.logger.info(f"开始播放动画，共 {self.total_steps} 个步骤")
        
        print(f"\n{Fore.CYAN}开始算法可视化演示{Style.RESET_ALL}")
        print(f"{Fore.BLUE}总步骤数: {self.total_steps}{Style.RESET_ALL}")
        
        for i, step in enumerate(steps):
            if not self.is_playing:
                break
                
            self.current_step_index = i
            self.visualize_step(step)
        
        if self.is_playing:
            print(f"\n{Fore.GREEN}算法执行完成！{Style.RESET_ALL}")
        
        self.is_playing = False
    
    def pause_animation(self):
        """暂停动画"""
        self.is_playing = False
        print(f"\n{Fore.YELLOW}动画已暂停{Style.RESET_ALL}")
    
    def resume_animation(self):
        """恢复动画"""
        if self.steps and self.current_step_index < len(self.steps):
            self.is_playing = True
            print(f"\n{Fore.GREEN}动画已恢复{Style.RESET_ALL}")
            
            # 继续播放剩余步骤
            remaining_steps = self.steps[self.current_step_index:]
            for step in remaining_steps:
                if not self.is_playing:
                    break
                self.visualize_step(step)
                self.current_step_index += 1
        else:
            print(f"{Fore.RED}没有可恢复的动画{Style.RESET_ALL}")
    
    def stop_animation(self):
        """停止动画"""
        self.is_playing = False
        self.current_step_index = 0
        print(f"\n{Fore.YELLOW}动画已停止{Style.RESET_ALL}")
    
    def set_auto_play(self, auto_play: bool, delay: float = 1.0):
        """设置自动播放
        
        Args:
            auto_play: 是否自动播放
            delay: 步骤间延迟时间
        """
        self.auto_play = auto_play
        self.step_delay = delay
        status = "开启" if auto_play else "关闭"
        print(f"{Fore.BLUE}自动播放已{status}，延迟时间: {delay}秒{Style.RESET_ALL}")
    
    def show_summary(self, algorithm_name: str, performance_data: Dict[str, Any]):
        """显示算法执行摘要
        
        Args:
            algorithm_name: 算法名称
            performance_data: 性能数据
        """
        print(f"\n{Fore.CYAN}算法执行摘要{Style.RESET_ALL}")
        print("=" * 50)
        print(f"算法名称: {algorithm_name}")
        print(f"执行时间: {performance_data.get('execution_time', 0):.4f} 秒")
        print(f"内存使用: {performance_data.get('memory_usage', 0)} 字节")
        print(f"比较次数: {performance_data.get('comparison_count', 0)}")
        print(f"交换次数: {performance_data.get('swap_count', 0)}")
        print(f"总步骤数: {performance_data.get('steps_count', 0)}")
        print("=" * 50)
    
    def _display_data_state(self, data_state: Any):
        """显示数据状态
        
        Args:
            data_state: 数据状态
        """
        if isinstance(data_state, list):
            print(f"{Fore.GREEN}数据状态: {data_state}{Style.RESET_ALL}")
        elif isinstance(data_state, dict):
            print(f"{Fore.GREEN}数据状态:{Style.RESET_ALL}")
            for key, value in data_state.items():
                print(f"  {key}: {value}")
        else:
            print(f"{Fore.GREEN}数据状态: {data_state}{Style.RESET_ALL}")
    
    def get_current_step_info(self) -> Dict[str, Any]:
        """获取当前步骤信息
        
        Returns:
            当前步骤信息
        """
        if self.steps and 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return {}
    
    def jump_to_step(self, step_index: int):
        """跳转到指定步骤
        
        Args:
            step_index: 目标步骤索引
        """
        if 0 <= step_index < len(self.steps):
            self.current_step_index = step_index
            print(f"{Fore.BLUE}已跳转到步骤 {step_index + 1}{Style.RESET_ALL}")
            self.visualize_step(self.steps[step_index])
        else:
            print(f"{Fore.RED}无效的步骤索引: {step_index}{Style.RESET_ALL}")
    
    def show_help(self):
        """显示动画控制帮助"""
        help_text = f"""
{Fore.CYAN}动画控制帮助{Style.RESET_ALL}
{Fore.YELLOW}可用命令:{Style.RESET_ALL}
- 回车键: 继续下一步
- 'p': 暂停动画
- 'r': 恢复动画
- 's': 停止动画
- 'a': 切换自动播放
- 'j <数字>': 跳转到指定步骤
- 'h': 显示此帮助
- 'q': 退出动画
        """
        print(help_text) 