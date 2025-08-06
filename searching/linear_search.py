"""
线性搜索算法实现

线性搜索是最基本的搜索算法，逐个检查每个元素直到找到目标。
时间复杂度：O(n)，空间复杂度：O(1)

学习目标：
1. 理解线性搜索的基本思想
2. 掌握逐个比较的搜索方法
3. 学会处理边界情况和异常
4. 理解不同搜索变体的实现
"""

from typing import Any, List, Optional, Callable
from core.algorithm_base import AlgorithmBase, AlgorithmType


class LinearSearch(AlgorithmBase):
    """线性搜索算法实现
    
    特性：
    - 适用于任何数据结构
    - 时间复杂度 O(n)
    - 空间复杂度 O(1)
    - 简单易懂
    
    学习要点：
    1. 逐个遍历数组元素
    2. 比较当前元素与目标元素
    3. 记录搜索步骤用于可视化
    4. 统计比较次数和操作次数
    """
    
    def __init__(self):
        """初始化线性搜索算法"""
        super().__init__("LinearSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行基本线性搜索
        
        TODO: 请实现基本的线性搜索算法
        
        实现思路：
        1. 遍历数组中的每个元素
        2. 比较当前元素与目标元素
        3. 如果找到目标，返回其位置
        4. 如果遍历完整个数组都没找到，返回None
        
        提示：
        - 使用 for 循环和 enumerate() 来遍历数组
        - 记录比较次数：self.comparison_count += 1
        - 记录操作次数：self.operation_count += 1
        - 使用 self.add_step() 记录搜索步骤
        - 使用 self.logger.info() 记录日志
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现线性搜索算法
        pass
    
    def search_with_condition(self, data: List[Any], condition: Callable[[Any], bool]) -> Optional[int]:
        """使用自定义条件进行搜索
        
        TODO: 请实现条件线性搜索算法
        
        实现思路：
        1. 遍历数组中的每个元素
        2. 使用条件函数检查当前元素
        3. 如果条件满足，返回其位置
        4. 如果遍历完整个数组都没找到，返回None
        
        提示：
        - 使用 condition(element) 来检查条件
        - 记录搜索步骤时使用 'check_condition' 类型
        
        Args:
            data: 要搜索的数据列表
            condition: 自定义条件函数
            
        Returns:
            满足条件的第一个元素位置，如果未找到返回None
        """
        # TODO: 在这里实现条件线性搜索算法
        pass
    
    def search_all_occurrences(self, data: List[Any], target: Any) -> List[int]:
        """搜索目标元素的所有出现位置
        
        TODO: 请实现搜索所有出现位置的算法
        
        实现思路：
        1. 遍历数组中的每个元素
        2. 如果当前元素等于目标元素，记录其位置
        3. 继续遍历直到数组结束
        4. 返回所有找到的位置列表
        
        提示：
        - 使用列表来收集所有出现的位置
        - 记录搜索步骤时包含已找到的数量
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素所有出现位置的列表
        """
        # TODO: 在这里实现搜索所有出现位置的算法
        pass
    
    def search_sentinel(self, data: List[Any], target: Any) -> Optional[int]:
        """哨兵线性搜索（优化版本）
        
        TODO: 请实现哨兵线性搜索算法
        
        实现思路：
        1. 在数组末尾添加目标元素作为哨兵
        2. 遍历数组直到找到目标元素
        3. 检查找到的位置是否在原始数组范围内
        4. 移除哨兵元素
        
        优化原理：
        - 通过添加哨兵元素，减少循环中的比较次数
        - 每次循环只需要检查元素是否等于目标，不需要检查边界
        
        提示：
        - 使用 data.append(target) 添加哨兵
        - 使用 data.pop() 移除哨兵
        - 记录搜索步骤时使用 'sentinel_compare' 类型
        
        Args:
            data: 要搜索的数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现哨兵线性搜索算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(n/2)',
                'worst_case': 'O(n)'
            },
            'space_complexity': 'O(1)',
            'description': '线性搜索逐个检查每个元素，直到找到目标或遍历完所有元素'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'LinearSearch',
            'complexity': 'O(n)',
            'description': '最基本的搜索算法，逐个检查每个元素',
            'best_for': '小数据集、无序数据',
            'methods': ['search', 'search_with_condition', 'search_all_occurrences', 'search_sentinel']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行线性搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                - condition: 自定义条件函数（可选）
                - search_type: 搜索类型（'basic', 'condition', 'all', 'sentinel'）
                
        Returns:
            搜索结果（位置、位置列表或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        condition = kwargs.get('condition')
        search_type = kwargs.get('search_type', 'basic')
        
        if search_type == 'condition' and condition:
            return self.search_with_condition(data, condition)
        elif search_type == 'all' and target:
            return self.search_all_occurrences(data, target)
        elif search_type == 'sentinel' and target:
            return self.search_sentinel(data, target)
        elif target:
            return self.search(data, target)
        else:
            raise ValueError("必须提供target参数或condition参数")


def main():
    """测试LinearSearch类的实现"""
    print("=" * 60)
    print("🧪 测试线性搜索算法实现")
    print("=" * 60)
    
    # 创建LinearSearch实例
    linear_search = LinearSearch()
    
    # 测试数据
    test_data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 1, 45, 67, 89, 23, 45]
    empty_data = []
    duplicate_data = [1, 2, 2, 3, 2, 4, 5, 2]
    
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
        result = linear_search.execute(test_data, target=67, search_type='basic')
        if result is not None and test_data[result] == 67:
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
        result = linear_search.execute(test_data, target=999, search_type='basic')
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
        result = linear_search.execute(empty_data, target=42, search_type='basic')
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
    
    # 测试用例4: 条件搜索
    print("\n🔍 测试用例4: 条件搜索")
    test_results['total'] += 1
    try:
        condition = lambda x: x > 50
        result = linear_search.execute(test_data, condition=condition, search_type='condition')
        if result is not None and test_data[result] > 50:
            test_results['passed'] += 1
            test_results['details'].append("✅ 条件搜索 - 通过")
            print("✅ 条件搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 条件搜索 - 失败")
            print("❌ 条件搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 条件搜索 - 异常: {e}")
        print(f"❌ 条件搜索 - 异常: {e}")
    
    # 测试用例5: 搜索所有出现位置
    print("\n🔍 测试用例5: 搜索所有出现位置")
    test_results['total'] += 1
    try:
        result = linear_search.execute(duplicate_data, target=2, search_type='all')
        if isinstance(result, list) and len(result) == 4:
            # 验证所有位置都包含目标元素
            all_correct = all(duplicate_data[pos] == 2 for pos in result)
            if all_correct:
                test_results['passed'] += 1
                test_results['details'].append("✅ 搜索所有出现位置 - 通过")
                print("✅ 搜索所有出现位置 - 通过")
            else:
                test_results['failed'] += 1
                test_results['details'].append("❌ 搜索所有出现位置 - 失败")
                print("❌ 搜索所有出现位置 - 失败")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 搜索所有出现位置 - 失败")
            print("❌ 搜索所有出现位置 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 搜索所有出现位置 - 异常: {e}")
        print(f"❌ 搜索所有出现位置 - 异常: {e}")
    
    # 测试用例6: 哨兵搜索
    print("\n🔍 测试用例6: 哨兵搜索")
    test_results['total'] += 1
    try:
        data_copy = test_data.copy()
        result = linear_search.execute(data_copy, target=67, search_type='sentinel')
        if result is not None and test_data[result] == 67:
            test_results['passed'] += 1
            test_results['details'].append("✅ 哨兵搜索 - 通过")
            print("✅ 哨兵搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 哨兵搜索 - 失败")
            print("❌ 哨兵搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 哨兵搜索 - 异常: {e}")
        print(f"❌ 哨兵搜索 - 异常: {e}")
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的线性搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 