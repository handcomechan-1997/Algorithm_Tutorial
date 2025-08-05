"""
配置管理模块 - 提供平台配置管理功能
"""

import json
import os
from typing import Any, Dict, Optional

class Config:
    """配置管理类
    
    该类提供平台配置的管理功能，包括：
    - 配置文件读写
    - 默认配置设置
    - 配置验证
    - 环境变量支持
    """
    
    def __init__(self, config_file: str = "config.json"):
        """初始化配置管理器
        
        Args:
            config_file: 配置文件路径
        """
        self.config_file = config_file
        self.config = self._load_default_config()
        self._load_config()
    
    def _load_default_config(self) -> Dict[str, Any]:
        """加载默认配置"""
        return {
            'platform': {
                'name': 'Algorithm Tutorial',
                'version': '1.0.0',
                'debug': False
            },
            'visualization': {
                'animation_speed': 1.0,
                'auto_play': False,
                'show_steps': True,
                'color_theme': 'default'
            },
            'performance': {
                'enable_profiling': True,
                'memory_tracking': True,
                'detailed_logging': False
            },
            'learning': {
                'difficulty_level': 'beginner',
                'show_hints': True,
                'auto_explanation': True
            },
            'interface': {
                'language': 'zh_CN',
                'theme': 'light',
                'font_size': 'medium'
            }
        }
    
    def _load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    self._merge_config(user_config)
            except Exception as e:
                print(f"加载配置文件失败: {e}")
    
    def _merge_config(self, user_config: Dict[str, Any]):
        """合并用户配置到默认配置"""
        def merge_dict(base: Dict[str, Any], update: Dict[str, Any]):
            for key, value in update.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    merge_dict(base[key], value)
                else:
                    base[key] = value
        
        merge_dict(self.config, user_config)
    
    def save_config(self):
        """保存配置到文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存配置文件失败: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值
        
        Args:
            key: 配置键（支持点号分隔的嵌套键）
            default: 默认值
            
        Returns:
            配置值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """设置配置值
        
        Args:
            key: 配置键（支持点号分隔的嵌套键）
            value: 配置值
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def get_platform_config(self) -> Dict[str, Any]:
        """获取平台配置"""
        return self.config.get('platform', {})
    
    def get_visualization_config(self) -> Dict[str, Any]:
        """获取可视化配置"""
        return self.config.get('visualization', {})
    
    def get_performance_config(self) -> Dict[str, Any]:
        """获取性能配置"""
        return self.config.get('performance', {})
    
    def get_learning_config(self) -> Dict[str, Any]:
        """获取学习配置"""
        return self.config.get('learning', {})
    
    def get_interface_config(self) -> Dict[str, Any]:
        """获取界面配置"""
        return self.config.get('interface', {})
    
    def reset_to_default(self):
        """重置为默认配置"""
        self.config = self._load_default_config()
        self.save_config()
    
    def validate_config(self) -> bool:
        """验证配置有效性
        
        Returns:
            配置是否有效
        """
        # TODO: 实现配置验证逻辑
        return True 