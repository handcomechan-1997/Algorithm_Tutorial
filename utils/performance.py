"""
性能分析工具 - 提供算法性能分析功能
"""

import time
import psutil
import threading
from typing import Dict, List, Any, Callable
from collections import defaultdict

from utils.logger import Logger

class PerformanceAnalyzer:
    """性能分析器
    
    该类提供算法性能分析功能，包括：
    - 执行时间测量
    - 内存使用分析
    - 复杂度验证
    - 性能对比
    """
    
    def __init__(self):
        """初始化性能分析器"""
        self.logger = Logger()
        self.results = defaultdict(list)
    
    def measure_execution_time(self, func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """测量函数执行时间
        
        Args:
            func: 要测试的函数
            *args: 函数参数
            **kwargs: 函数关键字参数
            
        Returns:
            性能测试结果
        """
        start_time = time.time()
        start_memory = self._get_memory_usage()
        
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            end_memory = self._get_memory_usage()
            
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            
            return {
                'success': True,
                'result': result,
                'execution_time': execution_time,
                'memory_usage': memory_usage,
                'start_time': start_time,
                'end_time': end_time
            }
            
        except Exception as e:
            end_time = time.time()
            return {
                'success': False,
                'error': str(e),
                'execution_time': end_time - start_time,
                'start_time': start_time,
                'end_time': end_time
            }
    
    def benchmark_algorithm(self, algorithm_name: str, algorithm_func: Callable, 
                          test_data_sets: List[Any], iterations: int = 1) -> Dict[str, Any]:
        """对算法进行基准测试
        
        Args:
            algorithm_name: 算法名称
            algorithm_func: 算法函数
            test_data_sets: 测试数据集列表
            iterations: 每个数据集的测试次数
            
        Returns:
            基准测试结果
        """
        self.logger.info(f"开始基准测试: {algorithm_name}")
        
        results = {
            'algorithm_name': algorithm_name,
            'test_data_sets': len(test_data_sets),
            'iterations': iterations,
            'results': []
        }
        
        for i, test_data in enumerate(test_data_sets):
            data_size = len(test_data) if hasattr(test_data, '__len__') else 'N/A'
            self.logger.info(f"测试数据集 {i+1}: 大小 = {data_size}")
            
            dataset_results = []
            for j in range(iterations):
                result = self.measure_execution_time(algorithm_func, test_data)
                dataset_results.append(result)
                
                if not result['success']:
                    self.logger.error(f"算法执行失败: {result['error']}")
                    break
            
            if dataset_results:
                # 计算统计数据
                successful_runs = [r for r in dataset_results if r['success']]
                if successful_runs:
                    avg_time = sum(r['execution_time'] for r in successful_runs) / len(successful_runs)
                    avg_memory = sum(r.get('memory_usage', 0) for r in successful_runs) / len(successful_runs)
                    
                    results['results'].append({
                        'dataset_index': i,
                        'data_size': data_size,
                        'successful_runs': len(successful_runs),
                        'total_runs': len(dataset_results),
                        'avg_execution_time': avg_time,
                        'avg_memory_usage': avg_memory,
                        'min_execution_time': min(r['execution_time'] for r in successful_runs),
                        'max_execution_time': max(r['execution_time'] for r in successful_runs)
                    })
        
        self.logger.info(f"基准测试完成: {algorithm_name}")
        return results
    
    def compare_algorithms(self, algorithms: Dict[str, Callable], 
                          test_data_sets: List[Any], iterations: int = 1) -> Dict[str, Any]:
        """比较多个算法的性能
        
        Args:
            algorithms: 算法字典 {算法名: 算法函数}
            test_data_sets: 测试数据集列表
            iterations: 每个数据集的测试次数
            
        Returns:
            算法比较结果
        """
        self.logger.info("开始算法性能比较")
        
        comparison_results = {
            'algorithms': list(algorithms.keys()),
            'test_data_sets': len(test_data_sets),
            'iterations': iterations,
            'results': {}
        }
        
        for algorithm_name, algorithm_func in algorithms.items():
            benchmark_result = self.benchmark_algorithm(
                algorithm_name, algorithm_func, test_data_sets, iterations
            )
            comparison_results['results'][algorithm_name] = benchmark_result
        
        self.logger.info("算法性能比较完成")
        return comparison_results
    
    def analyze_complexity(self, algorithm_name: str, algorithm_func: Callable,
                          data_sizes: List[int], data_generator: Callable) -> Dict[str, Any]:
        """分析算法复杂度
        
        Args:
            algorithm_name: 算法名称
            algorithm_func: 算法函数
            data_sizes: 数据大小列表
            data_generator: 数据生成函数
            
        Returns:
            复杂度分析结果
        """
        self.logger.info(f"开始复杂度分析: {algorithm_name}")
        
        complexity_results = {
            'algorithm_name': algorithm_name,
            'data_sizes': data_sizes,
            'execution_times': [],
            'memory_usages': []
        }
        
        for size in data_sizes:
            test_data = data_generator(size)
            result = self.measure_execution_time(algorithm_func, test_data)
            
            if result['success']:
                complexity_results['execution_times'].append(result['execution_time'])
                complexity_results['memory_usages'].append(result.get('memory_usage', 0))
            else:
                self.logger.error(f"数据大小 {size} 的测试失败: {result['error']}")
                complexity_results['execution_times'].append(None)
                complexity_results['memory_usages'].append(None)
        
        self.logger.info(f"复杂度分析完成: {algorithm_name}")
        return complexity_results
    
    def _get_memory_usage(self) -> int:
        """获取当前内存使用量"""
        try:
            process = psutil.Process()
            return process.memory_info().rss
        except ImportError:
            return 0
    
    def generate_report(self, results: Dict[str, Any]) -> str:
        """生成性能报告
        
        Args:
            results: 性能测试结果
            
        Returns:
            格式化的报告字符串
        """
        report = []
        report.append("=" * 60)
        report.append("算法性能分析报告")
        report.append("=" * 60)
        
        if 'algorithm_name' in results:
            report.append(f"算法名称: {results['algorithm_name']}")
        
        if 'results' in results:
            for dataset_result in results['results']:
                report.append(f"\n数据集 {dataset_result['dataset_index'] + 1}:")
                report.append(f"  数据大小: {dataset_result['data_size']}")
                report.append(f"  成功运行: {dataset_result['successful_runs']}/{dataset_result['total_runs']}")
                report.append(f"  平均执行时间: {dataset_result['avg_execution_time']:.6f} 秒")
                report.append(f"  平均内存使用: {dataset_result['avg_memory_usage']} 字节")
                report.append(f"  最短执行时间: {dataset_result['min_execution_time']:.6f} 秒")
                report.append(f"  最长执行时间: {dataset_result['max_execution_time']:.6f} 秒")
        
        report.append("\n" + "=" * 60)
        return "\n".join(report) 