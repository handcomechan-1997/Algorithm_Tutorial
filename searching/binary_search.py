"""
二分搜索算法实现

二分搜索是一种高效的搜索算法，要求数据必须是有序的。
时间复杂度：O(log n)，空间复杂度：O(1)

学习目标：
1. 理解二分搜索的分治思想
2. 掌握有序数组的搜索技巧
3. 学会处理边界情况和重复元素
4. 理解不同二分搜索变体的实现
"""

from typing import Any, List, Optional, Tuple
from core.algorithm_base import AlgorithmBase, AlgorithmType


class BinarySearch(AlgorithmBase):
    """二分搜索算法实现
    
    特性：
    - 要求数据必须有序
    - 时间复杂度 O(log n)
    - 空间复杂度 O(1)
    - 非常高效
    
    学习要点：
    1. 利用数据的有序性进行分治搜索
    2. 通过比较中间元素来缩小搜索范围
    3. 处理重复元素的特殊情况
    4. 理解搜索范围的边界条件
    """
    
    def __init__(self):
        """初始化二分搜索算法"""
        super().__init__("BinarySearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行二分搜索
        
        TODO: 请实现基本的二分搜索算法
        
        实现思路：
        1. 初始化左右边界（left=0, right=len(data)-1）
        2. 当 left <= right 时继续搜索：
           - 计算中间位置 mid = (left + right) // 2
           - 比较 data[mid] 与 target
           - 如果相等，返回 mid
           - 如果 data[mid] < target，更新 left = mid + 1
           - 如果 data[mid] > target，更新 right = mid - 1
        3. 如果没找到，返回 None
        
        提示：
        - 使用 while 循环控制搜索过程
        - 记录比较次数和操作次数
        - 使用 self.add_step() 记录搜索步骤
        - 注意边界条件的处理
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现二分搜索算法
        pass
    
    def search_first_occurrence(self, data: List[Any], target: Any) -> Optional[int]:
        """搜索目标元素的第一次出现位置
        
        TODO: 请实现搜索第一次出现位置的算法
        
        实现思路：
        1. 使用二分搜索找到目标元素
        2. 找到后，继续向左搜索，看是否还有更早的出现
        3. 记录找到的位置，但继续缩小搜索范围
        4. 最终返回第一次出现的位置
        
        关键点：
        - 当找到目标元素时，不要立即返回
        - 继续在左半部分搜索，看是否有更早的出现
        - 使用 result 变量记录当前找到的位置
        
        提示：
        - 当 data[mid] == target 时，更新 result = mid
        - 然后继续搜索左半部分：right = mid - 1
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素第一次出现的位置，如果未找到返回None
        """
        # TODO: 在这里实现搜索第一次出现位置的算法
        pass
    
    def search_last_occurrence(self, data: List[Any], target: Any) -> Optional[int]:
        """搜索目标元素的最后一次出现位置
        
        TODO: 请实现搜索最后一次出现位置的算法
        
        实现思路：
        1. 使用二分搜索找到目标元素
        2. 找到后，继续向右搜索，看是否还有更晚的出现
        3. 记录找到的位置，但继续缩小搜索范围
        4. 最终返回最后一次出现的位置
        
        关键点：
        - 当找到目标元素时，不要立即返回
        - 继续在右半部分搜索，看是否有更晚的出现
        - 使用 result 变量记录当前找到的位置
        
        提示：
        - 当 data[mid] == target 时，更新 result = mid
        - 然后继续搜索右半部分：left = mid + 1
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素最后一次出现的位置，如果未找到返回None
        """
        # TODO: 在这里实现搜索最后一次出现位置的算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息
        
        Returns:
            复杂度信息字典
        """
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log n)',
                'worst_case': 'O(log n)'
            },
            'space_complexity': 'O(1)',
            'description': '二分搜索通过不断缩小搜索范围来快速定位目标元素'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'BinarySearch',
            'complexity': 'O(log n)',
            'description': '高效的有序数组搜索算法',
            'best_for': '有序数组、大数据集',
            'methods': ['search', 'search_first_occurrence', 'search_last_occurrence']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行二分搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - search_type: 搜索类型（'basic', 'first', 'last'）
                
        Returns:
            搜索结果（位置或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        search_type = kwargs.get('search_type', 'basic')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        if search_type == 'first':
            return self.search_first_occurrence(data, target)
        elif search_type == 'last':
            return self.search_last_occurrence(data, target)
        else:
            return self.search(data, target)


def main():
    """测试BinarySearch类的实现"""
    print("=" * 60)
    print("🧪 测试二分搜索算法实现")
    print("=" * 60)
    
    # 创建BinarySearch实例
    binary_search = BinarySearch()
    
    # 测试数据（有序数组）
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    duplicate_data = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    empty_data = []
    single_element = [42]
    
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
        result = binary_search.execute(test_data, target=15, search_type='basic')
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
        result = binary_search.execute(test_data, target=30, search_type='basic')
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
        result = binary_search.execute(empty_data, target=42, search_type='basic')
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
        result = binary_search.execute(single_element, target=42, search_type='basic')
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
    
    # 测试用例5: 搜索第一次出现位置
    print("\n🔍 测试用例5: 搜索第一次出现位置")
    test_results['total'] += 1
    try:
        result = binary_search.execute(duplicate_data, target=2, search_type='first')
        if result is not None and duplicate_data[result] == 2:
            # 验证这是第一次出现的位置
            first_occurrence = duplicate_data.index(2)
            if result == first_occurrence:
                test_results['passed'] += 1
                test_results['details'].append("✅ 搜索第一次出现位置 - 通过")
                print("✅ 搜索第一次出现位置 - 通过")
            else:
                test_results['failed'] += 1
                test_results['details'].append("❌ 搜索第一次出现位置 - 失败")
                print("❌ 搜索第一次出现位置 - 失败")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 搜索第一次出现位置 - 失败")
            print("❌ 搜索第一次出现位置 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 搜索第一次出现位置 - 异常: {e}")
        print(f"❌ 搜索第一次出现位置 - 异常: {e}")
    
    # 测试用例6: 搜索最后一次出现位置
    print("\n🔍 测试用例6: 搜索最后一次出现位置")
    test_results['total'] += 1
    try:
        result = binary_search.execute(duplicate_data, target=5, search_type='last')
        if result is not None and duplicate_data[result] == 5:
            # 验证这是最后一次出现的位置
            last_occurrence = len(duplicate_data) - 1 - duplicate_data[::-1].index(5)
            if result == last_occurrence:
                test_results['passed'] += 1
                test_results['details'].append("✅ 搜索最后一次出现位置 - 通过")
                print("✅ 搜索最后一次出现位置 - 通过")
            else:
                test_results['failed'] += 1
                test_results['details'].append("❌ 搜索最后一次出现位置 - 失败")
                print("❌ 搜索最后一次出现位置 - 失败")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 搜索最后一次出现位置 - 失败")
            print("❌ 搜索最后一次出现位置 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 搜索最后一次出现位置 - 异常: {e}")
        print(f"❌ 搜索最后一次出现位置 - 异常: {e}")
    
    # 测试用例7: 边界值测试
    print("\n🔍 测试用例7: 边界值测试")
    test_results['total'] += 1
    try:
        # 测试第一个元素
        first_result = binary_search.execute(test_data, target=1, search_type='basic')
        # 测试最后一个元素
        last_result = binary_search.execute(test_data, target=29, search_type='basic')
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
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的二分搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 