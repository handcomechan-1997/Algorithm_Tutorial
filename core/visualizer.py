"""
可视化引擎 - 提供算法可视化的基础功能
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class Visualizer(ABC):
    """可视化引擎基类
    
    该类定义了算法可视化的通用接口，包括：
    - 动画播放控制
    - 数据状态可视化
    - 交互式操作
    - 性能展示
    
    在学习过程中，可以继承此类来实现具体的可视化功能。
    """
    
    def __init__(self):
        """初始化可视化引擎"""
        self.is_playing = False
        self.current_step = 0
        self.total_steps = 0
        self.animation_speed = 1.0
        
    @abstractmethod
    def visualize_step(self, step_data: Dict[str, Any]):
        """可视化单个步骤
        
        Args:
            step_data: 步骤数据
        """
        pass
    
    @abstractmethod
    def play_animation(self, steps: List[Dict[str, Any]]):
        """播放动画
        
        Args:
            steps: 步骤列表
        """
        pass
    
    @abstractmethod
    def pause_animation(self):
        """暂停动画"""
        pass
    
    @abstractmethod
    def resume_animation(self):
        """恢复动画"""
        pass
    
    @abstractmethod
    def stop_animation(self):
        """停止动画"""
        pass
    
    def set_speed(self, speed: float):
        """设置动画速度
        
        Args:
            speed: 速度倍数
        """
        self.animation_speed = max(0.1, min(5.0, speed))
    
    def get_progress(self) -> float:
        """获取播放进度
        
        Returns:
            进度百分比 (0.0 - 1.0)
        """
        if self.total_steps == 0:
            return 0.0
        return self.current_step / self.total_steps 