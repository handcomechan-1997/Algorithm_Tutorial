#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithm Tutorial - 算法学习平台主程序入口
"""

import sys
import os
from colorama import init, Fore, Style

# 初始化colorama，用于在终端输出彩色文本
init()

# 为方便模块导入，将项目根目录添加到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.algorithm_manager import AlgorithmManager
from utils.logger import Logger
from utils.boot_animation import BootAnimation, show_startup_sequence, show_welcome_message

def main():
    """主程序入口"""
    logger = Logger()
    boot_anim = BootAnimation()

    try:
        boot_anim.show_boot_screen()
        show_startup_sequence()
        logger.info("Algorithm Tutorial平台启动中...")

        # 初始化算法管理器
        algorithm_manager = AlgorithmManager()
        algorithm_manager.initialize()

        show_welcome_message()

        # 启动交互式界面
        from visualization.interface import UserInterface
        interface = UserInterface(algorithm_manager)
        interface.run()

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}平台被用户中断{Style.RESET_ALL}")
        logger.info("平台被用户中断")
    except Exception as e:
        print(f"\n{Fore.RED}平台错误: {e}{Style.RESET_ALL}")
        logger.error(f"平台错误: {e}")
    finally:
        print(f"\n{Fore.GREEN}感谢使用Algorithm Tutorial！{Style.RESET_ALL}")
        logger.info("Algorithm Tutorial平台关闭")

if __name__ == "__main__":
    main() 