import time
import sys
from colorama import Fore, Style

class BootAnimation:
    """启动动画类"""
    
    def __init__(self):
        """初始化启动动画（ALGORITHM 大字 + 居中）"""
        # 内框宽度（你原来的边框里是 62 个字符）
        inner_w = 62

        # 5×5 等宽字库（全角方块风格）
        font = {
            'A': [" ███ ", "█   █", "█████", "█   █", "█   █"],
            'L': ["█    ", "█    ", "█    ", "█    ", "█████"],
            'G': [" ███ ", "█    ", "█ ███", "█   █", " ████"],
            'O': [" ███ ", "█   █", "█   █", "█   █", " ███ "],
            'R': ["████ ", "█  █ ", "████ ", "█ █  ", "█  █ "],
            'I': ["█████", "  █  ", "  █  ", "  █  ", "█████"],
            'T': ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
            'H': ["█   █", "█   █", "█████", "█   █", "█   █"],
            'M': ["█   █", "██ ██", "█ █ █", "█   █", "█   █"],
        }

        word = "ALGORITHM"
        rows = [" ".join(font[ch][r] for ch in word) for r in range(5)]

        top =    "╔" + "═" * inner_w + "╗"
        blank =  "║" + " " * inner_w + "║"
        body =   "\n".join("║" + row.center(inner_w) + "║" for row in rows)
        footer = [
            blank,
            "║" + "Algorithm Learning Platform".center(inner_w) + "║",
            blank,
            "║" + "Version 1.0.0 - Educational Project".center(inner_w) + "║",
            blank,
        ]
        bottom = "╚" + "═" * inner_w + "╝"

        self.logo = "\n".join([top, blank, body, *footer, bottom])

    
    def show_boot_screen(self):
        """显示启动画面"""
        print(Fore.CYAN + self.logo + Style.RESET_ALL)
        time.sleep(1)
    
    def show_progress_bar(self, title: str, duration: float = 2.0):
        """显示进度条
        
        Args:
            title: 进度条标题
            duration: 持续时间（秒）
        """
        print(f"\n{Fore.YELLOW}{title}{Style.RESET_ALL}")
        steps = 50
        for i in range(steps + 1):
            progress = i / steps
            bar_length = 50
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            percentage = int(progress * 100)
            
            print(f"\r[{bar}] {percentage}%", end='', flush=True)
            time.sleep(duration / steps)
        
        print()  # 换行

# --- 以下代码保持不变 ---

def show_startup_sequence():
    """显示启动序列"""
    animation = BootAnimation()
    
    # # 首先显示启动画面
    # animation.show_boot_screen()

    # 显示各个组件的初始化进度
    components = [
        "初始化算法管理器",
        "加载数据结构模块",
        "注册排序算法",
        "注册搜索算法",
        "注册图算法",
        "注册动态规划算法",
        "注册贪心算法",
        "初始化可视化引擎",
        "启动性能分析器",
        "准备用户界面"
    ]
    
    total_duration = 3.0 # 总启动模拟时间
    component_duration = total_duration / len(components)
    
    for component in components:
        animation.show_progress_bar(component, component_duration)

def show_welcome_message():
    """显示欢迎信息"""
    welcome_msg = """
============================================================
    🎉 欢迎使用 Algorithm Learning Platform! 🎉
============================================================

这是一个专为计算机专业本科生设计的算法学习平台。

🎯 学习目标：
• 深入理解数据结构与算法原理
• 通过可视化演示掌握算法执行过程
• 通过性能分析比较不同算法的效率
• 通过动手实践巩固理论知识

📚 学习路径：
1. 数据结构基础 → 2. 基础算法 → 3. 高级算法 → 4. 算法优化

🚀 开始你的算法学习之旅吧！
============================================================
    """
    
    print(Fore.GREEN + welcome_msg + Style.RESET_ALL)

# 如果想直接运行查看效果，可以添加以下代码
if __name__ == '__main__':
    # 修复：在显示进度条之前，先显示LOGO
    # 原代码中 show_boot_screen() 是在 show_startup_sequence() 中调用的，但没有被执行
    # 为了演示，我们在这里直接调用
    
    animation = BootAnimation()
    animation.show_boot_screen() # 直接显示LOGO

    # 模拟启动过程
    show_startup_sequence()
    
    # 显示欢迎信息
    show_welcome_message()