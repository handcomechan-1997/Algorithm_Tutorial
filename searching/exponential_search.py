"""
指数搜索算法实现

指数搜索是一种搜索算法，适用于在无界或非常大的有序数组中搜索元素。
它首先找到目标元素可能存在的范围，然后在该范围内使用二分搜索。
时间复杂度：O(log n)，空间复杂度：O(1)

学习目标：
1. 理解指数搜索的适用范围
2. 掌握指数增长和二分搜索的结合
3. 学会处理无界搜索问题
4. 理解数据生成器的使用
"""

from typing import Any, List, Optional
from core.algorithm_base import AlgorithmBase, AlgorithmType


class ExponentialSearch(AlgorithmBase):
    """指数搜索算法实现
    
    特性：
    - 适用于无界搜索
    - 时间复杂度 O(log n)
    - 空间复杂度 O(1)
    - 结合了线性搜索和二分搜索
    
    学习要点：
    1. 理解指数增长的概念
    2. 掌握范围确定和二分搜索的结合
    3. 处理无界数据和数据生成器
    4. 理解算法的适用场景
    """
    
    def __init__(self):
        """初始化指数搜索算法"""
        super().__init__("ExponentialSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行指数搜索
        
        TODO: 请实现指数搜索算法
        
        实现思路：
        1. 检查第一个元素是否为目标
        2. 指数增长阶段：从索引1开始，每次乘以2
           - 检查当前位置的值是否小于等于目标
           - 如果是，继续指数增长；如果否，停止增长
        3. 二分搜索阶段：在确定范围内进行二分搜索
           - 左边界：上一次指数增长的位置
           - 右边界：当前指数增长的位置
        
        关键点：
        - 指数增长用于快速确定搜索范围
        - 二分搜索在较小范围内进行精确查找
        - 需要处理数组边界情况
        
        提示：
        - 使用 while 循环进行指数增长
        - 使用 i = i * 2 实现指数增长
        - 调用 _binary_search_range 进行二分搜索
        - 记录指数增长和搜索步骤
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现指数搜索算法
        pass
    
    def _binary_search_range(self, data: List[Any], target: Any, left: int, right: int) -> Optional[int]:
        """在指定范围内进行二分搜索
        
        TODO: 请实现在指定范围内的二分搜索算法
        
        实现思路：
        1. 在 [left, right] 范围内进行标准二分搜索
        2. 计算中间位置 mid = (left + right) // 2
        3. 比较 data[mid] 与 target
        4. 根据比较结果更新搜索范围
        5. 重复直到找到目标或确定不存在
        
        提示：
        - 这是标准的二分搜索算法
        - 注意边界条件：left <= right
        - 记录搜索步骤和比较次数
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            left: 左边界
            right: 右边界
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现在指定范围内的二分搜索算法
        pass
    
    def search_unbounded(self, data_generator, target: Any, max_iterations: int = 1000) -> Optional[int]:
        """无界指数搜索
        
        TODO: 请实现无界指数搜索算法
        
        实现思路：
        1. 检查第一个元素是否为目标
        2. 指数增长阶段：使用数据生成器
           - 调用 data_generator(i) 获取第i个元素
           - 检查元素是否小于目标
           - 如果是，继续指数增长；如果否，停止增长
        3. 二分搜索阶段：在确定范围内进行二分搜索
           - 使用数据生成器进行二分搜索
        
        关键点：
        - 使用数据生成器处理无界数据
        - 处理生成器可能抛出的异常
        - 设置最大迭代次数避免无限循环
        
        提示：
        - 使用 try-except 处理 IndexError 和 StopIteration
        - 使用 while 循环控制迭代次数
        - 调用 _binary_search_unbounded 进行二分搜索
        
        Args:
            data_generator: 数据生成器函数，接受索引参数
            target: 要搜索的目标元素
            max_iterations: 最大迭代次数
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现无界指数搜索算法
        pass
    
    def _binary_search_unbounded(self, data_generator, target: Any, left: int, right: int) -> Optional[int]:
        """在无界范围内进行二分搜索
        
        TODO: 请实现在无界范围内的二分搜索算法
        
        实现思路：
        1. 在 [left, right] 范围内进行二分搜索
        2. 使用数据生成器获取元素
        3. 处理生成器可能抛出的异常
        4. 根据异常调整搜索范围
        
        关键点：
        - 使用数据生成器获取元素
        - 处理 IndexError 和 StopIteration 异常
        - 当超出数据范围时，向左搜索
        
        提示：
        - 使用 try-except 处理生成器异常
        - 当发生异常时，更新 right = mid - 1
        - 记录搜索步骤和比较次数
        
        Args:
            data_generator: 数据生成器函数
            target: 要搜索的目标元素
            left: 左边界
            right: 右边界
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现在无界范围内的二分搜索算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log n)',
                'worst_case': 'O(log n)'
            },
            'space_complexity': 'O(1)',
            'description': '指数搜索先找到目标范围，然后在该范围内进行二分搜索'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'ExponentialSearch',
            'complexity': 'O(log n)',
            'description': '适用于无界搜索的算法',
            'best_for': '无界数据、流数据',
            'methods': ['search']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行指数搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表或数据生成器
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - data_generator: 数据生成器函数（可选）
                
        Returns:
            搜索结果（位置或None）
        """
        target = kwargs.get('target')
        data_generator = kwargs.get('data_generator')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        if data_generator:
            return self.search_unbounded(data_generator, target)
        elif isinstance(data, list):
            return self.search(data, target)
        else:
            raise ValueError("必须提供数据列表或数据生成器") 


def main():
    """测试ExponentialSearch类的实现"""
    print("=" * 60)
    print("🧪 测试指数搜索算法实现")
    print("=" * 60)
    
    # 创建ExponentialSearch实例
    exponential_search = ExponentialSearch()
    
    # 测试数据（有序数组）
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
    small_data = [1, 3, 5, 7, 9]
    empty_data = []
    single_element = [42]
    
    # 数据生成器函数
    def data_generator(index):
        if index < len(test_data):
            return test_data[index]
        else:
            raise IndexError("Index out of range")
    
    test_results = {
        'passed': 0,
        'failed': 0,
        'total': 0,
        'details': []
    }
    
    # 测试用例1: 基本搜索 - 找到目标
    print("\n🔍 测试用例1: 基本搜索 - 找到目标")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(test_data, target=15)
        if result is not None and test_data[result] == 15:
            test_results['passed'] += 1
            test_results['details'].append("✅ 基本搜索(找到目标) - 通过")
            print("✅ 基本搜索(找到目标) - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 基本搜索(找到目标) - 失败")
            print("❌ 基本搜索(找到目标) - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 基本搜索(找到目标) - 异常: {e}")
        print(f"❌ 基本搜索(找到目标) - 异常: {e}")
    
    # 测试用例2: 基本搜索 - 未找到目标
    print("\n🔍 测试用例2: 基本搜索 - 未找到目标")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(test_data, target=40)
        if result is None:
            test_results['passed'] += 1
            test_results['details'].append("✅ 基本搜索(未找到目标) - 通过")
            print("✅ 基本搜索(未找到目标) - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 基本搜索(未找到目标) - 失败")
            print("❌ 基本搜索(未找到目标) - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 基本搜索(未找到目标) - 异常: {e}")
        print(f"❌ 基本搜索(未找到目标) - 异常: {e}")
    
    # 测试用例3: 空数组搜索
    print("\n🔍 测试用例3: 空数组搜索")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(empty_data, target=42)
        if result is None:
            test_results['passed'] += 1
            test_results['details'].append("✅ 空数组搜索 - 通过")
            print("✅ 空数组搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 空数组搜索 - 失败")
            print("❌ 空数组搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 空数组搜索 - 异常: {e}")
        print(f"❌ 空数组搜索 - 异常: {e}")
    
    # 测试用例4: 单元素数组搜索
    print("\n🔍 测试用例4: 单元素数组搜索")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(single_element, target=42)
        if result == 0 and single_element[result] == 42:
            test_results['passed'] += 1
            test_results['details'].append("✅ 单元素数组搜索 - 通过")
            print("✅ 单元素数组搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 单元素数组搜索 - 失败")
            print("❌ 单元素数组搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 单元素数组搜索 - 异常: {e}")
        print(f"❌ 单元素数组搜索 - 异常: {e}")
    
    # 测试用例5: 小数组搜索
    print("\n🔍 测试用例5: 小数组搜索")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(small_data, target=7)
        if result is not None and small_data[result] == 7:
            test_results['passed'] += 1
            test_results['details'].append("✅ 小数组搜索 - 通过")
            print("✅ 小数组搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 小数组搜索 - 失败")
            print("❌ 小数组搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 小数组搜索 - 异常: {e}")
        print(f"❌ 小数组搜索 - 异常: {e}")
    
    # 测试用例6: 边界值测试
    print("\n🔍 测试用例6: 边界值测试")
    test_results['total'] += 1
    try:
        # 测试第一个元素
        first_result = exponential_search.execute(test_data, target=1)
        # 测试最后一个元素
        last_result = exponential_search.execute(test_data, target=39)
        if first_result == 0 and last_result == len(test_data) - 1:
            test_results['passed'] += 1
            test_results['details'].append("✅ 边界值测试 - 通过")
            print("✅ 边界值测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 边界值测试 - 失败")
            print("❌ 边界值测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 边界值测试 - 异常: {e}")
        print(f"❌ 边界值测试 - 异常: {e}")
    
    # 测试用例7: 无界搜索测试
    print("\n🔍 测试用例7: 无界搜索测试")
    test_results['total'] += 1
    try:
        result = exponential_search.execute(None, target=25, data_generator=data_generator)
        if result is not None and test_data[result] == 25:
            test_results['passed'] += 1
            test_results['details'].append("✅ 无界搜索测试 - 通过")
            print("✅ 无界搜索测试 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 无界搜索测试 - 失败")
            print("❌ 无界搜索测试 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 无界搜索测试 - 异常: {e}")
        print(f"❌ 无界搜索测试 - 异常: {e}")
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的指数搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 