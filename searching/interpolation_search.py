"""
插值搜索算法实现

插值搜索是二分搜索的改进版本，适用于均匀分布的有序数据。
它通过线性插值来估计目标元素的位置，从而减少搜索次数。
时间复杂度：O(log log n) 平均情况，O(n) 最坏情况

学习目标：
1. 理解插值搜索的数学原理
2. 掌握线性插值的计算方法
3. 学会处理边界情况和异常
4. 理解数据分布对性能的影响
"""

from typing import Any, List, Optional
from core.algorithm_base import AlgorithmBase, AlgorithmType


class InterpolationSearch(AlgorithmBase):
    """插值搜索算法实现
    
    特性：
    - 适用于均匀分布的有序数据
    - 平均时间复杂度 O(log log n)
    - 最坏情况时间复杂度 O(n)
    - 空间复杂度 O(1)
    
    学习要点：
    1. 理解线性插值的数学原理
    2. 掌握插值位置的计算公式
    3. 处理边界情况和除零错误
    4. 理解数据分布对性能的影响
    """
    
    def __init__(self):
        """初始化插值搜索算法"""
        super().__init__("InterpolationSearch", AlgorithmType.SEARCHING)
    
    def search(self, data: List[Any], target: Any) -> Optional[int]:
        """执行插值搜索
        
        TODO: 请实现插值搜索算法
        
        实现思路：
        1. 检查边界条件（目标是否在数据范围内）
        2. 使用插值公式计算估计位置：
           pos = left + ((target - data[left]) * (right - left)) / (data[right] - data[left])
        3. 比较 data[pos] 与 target
        4. 根据比较结果更新搜索范围
        5. 重复直到找到目标或确定不存在
        
        关键点：
        - 插值公式基于线性插值原理
        - 需要处理除零错误（data[right] == data[left]）
        - 需要检查边界条件避免越界
        
        提示：
        - 使用 while 循环控制搜索过程
        - 使用 int() 将插值结果转换为整数
        - 处理除零错误和边界条件
        - 记录搜索步骤和比较次数
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现插值搜索算法
        pass
    
    def search_with_bounds_check(self, data: List[Any], target: Any) -> Optional[int]:
        """带边界检查的插值搜索
        
        TODO: 请实现带边界检查的插值搜索算法
        
        实现思路：
        1. 在每次迭代中检查边界条件
        2. 确保插值位置在有效范围内
        3. 处理除零错误和边界情况
        4. 提供更稳定的搜索过程
        
        改进点：
        - 更严格的边界检查
        - 更好的异常处理
        - 更稳定的性能表现
        
        提示：
        - 在每次计算插值位置前检查边界
        - 使用 max() 和 min() 确保位置在范围内
        - 处理各种边界情况
        
        Args:
            data: 要搜索的有序数据列表
            target: 要搜索的目标元素
            
        Returns:
            目标元素的位置，如果未找到返回None
        """
        # TODO: 在这里实现带边界检查的插值搜索算法
        pass
    
    def is_uniformly_distributed(self, data: List[Any], tolerance: float = 0.1) -> bool:
        """检查数据是否均匀分布
        
        TODO: 请实现数据分布检查算法
        
        实现思路：
        1. 计算相邻元素的差值
        2. 计算平均差值
        3. 检查每个差值是否接近平均值
        4. 根据容差判断是否均匀分布
        
        应用场景：
        - 在搜索前检查数据分布
        - 决定是否使用插值搜索
        - 优化搜索策略选择
        
        提示：
        - 使用列表存储相邻元素的差值
        - 计算平均差值并检查偏差
        - 使用容差参数控制判断标准
        
        Args:
            data: 要检查的数据列表
            tolerance: 容差，用于判断是否均匀分布
            
        Returns:
            如果数据均匀分布返回True，否则返回False
        """
        # TODO: 在这里实现数据分布检查算法
        pass
    
    def get_complexity(self) -> dict:
        """获取算法复杂度信息"""
        return {
            'time_complexity': {
                'best_case': 'O(1)',
                'average_case': 'O(log log n)',
                'worst_case': 'O(n)'
            },
            'space_complexity': 'O(1)',
            'description': '插值搜索通过线性插值估计目标位置，适用于均匀分布的数据'
        }
    
    def get_algorithm_info(self) -> dict:
        """获取算法信息"""
        return {
            'name': 'InterpolationSearch',
            'complexity': 'O(log log n)',
            'description': '适用于均匀分布数据的改进二分搜索',
            'best_for': '均匀分布的有序数据',
            'methods': ['search']
        }
    
    def execute(self, data: Any, **kwargs) -> Any:
        """执行插值搜索算法（实现抽象基类方法）
        
        Args:
            data: 要搜索的有序数据列表
            **kwargs: 额外参数，包括：
                - target: 要搜索的目标元素
                
        Returns:
            搜索结果（位置或None）
        """
        if not isinstance(data, list):
            raise ValueError("输入数据必须是列表类型")
        
        target = kwargs.get('target')
        
        if not target:
            raise ValueError("必须提供target参数")
        
        return self.search(data, target)


def main():
    """测试InterpolationSearch类的实现"""
    print("=" * 60)
    print("🧪 测试插值搜索算法实现")
    print("=" * 60)
    
    # 创建InterpolationSearch实例
    interpolation_search = InterpolationSearch()
    
    # 测试数据（均匀分布的有序数组）
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    uniform_data = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    non_uniform_data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
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
        result = interpolation_search.execute(test_data, target=15)
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
        result = interpolation_search.execute(test_data, target=30)
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
        result = interpolation_search.execute(empty_data, target=42)
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
        result = interpolation_search.execute(single_element, target=42)
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
    
    # 测试用例5: 均匀分布数据搜索
    print("\n🔍 测试用例5: 均匀分布数据搜索")
    test_results['total'] += 1
    try:
        result = interpolation_search.execute(uniform_data, target=50)
        if result is not None and uniform_data[result] == 50:
            test_results['passed'] += 1
            test_results['details'].append("✅ 均匀分布数据搜索 - 通过")
            print("✅ 均匀分布数据搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 均匀分布数据搜索 - 失败")
            print("❌ 均匀分布数据搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 均匀分布数据搜索 - 异常: {e}")
        print(f"❌ 均匀分布数据搜索 - 异常: {e}")
    
    # 测试用例6: 非均匀分布数据搜索
    print("\n🔍 测试用例6: 非均匀分布数据搜索")
    test_results['total'] += 1
    try:
        result = interpolation_search.execute(non_uniform_data, target=64)
        if result is not None and non_uniform_data[result] == 64:
            test_results['passed'] += 1
            test_results['details'].append("✅ 非均匀分布数据搜索 - 通过")
            print("✅ 非均匀分布数据搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 非均匀分布数据搜索 - 失败")
            print("❌ 非均匀分布数据搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 非均匀分布数据搜索 - 异常: {e}")
        print(f"❌ 非均匀分布数据搜索 - 异常: {e}")
    
    # 测试用例7: 边界值测试
    print("\n🔍 测试用例7: 边界值测试")
    test_results['total'] += 1
    try:
        # 测试第一个元素
        first_result = interpolation_search.execute(test_data, target=1)
        # 测试最后一个元素
        last_result = interpolation_search.execute(test_data, target=29)
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
    
    # 测试用例8: 带边界检查的搜索
    print("\n🔍 测试用例8: 带边界检查的搜索")
    test_results['total'] += 1
    try:
        result = interpolation_search.search_with_bounds_check(test_data, target=17)
        if result is not None and test_data[result] == 17:
            test_results['passed'] += 1
            test_results['details'].append("✅ 带边界检查的搜索 - 通过")
            print("✅ 带边界检查的搜索 - 通过")
        else:
            test_results['failed'] += 1
            test_results['details'].append("❌ 带边界检查的搜索 - 失败")
            print("❌ 带边界检查的搜索 - 失败")
    except Exception as e:
        test_results['failed'] += 1
        test_results['details'].append(f"❌ 带边界检查的搜索 - 异常: {e}")
        print(f"❌ 带边界检查的搜索 - 异常: {e}")
    
    # 输出测试总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结")
    print("=" * 60)
    print(f"总测试数: {test_results['total']}")
    print(f"通过测试: {test_results['passed']}")
    print(f"失败测试: {test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 所有测试通过！你的插值搜索实现是正确的！")
    else:
        print(f"\n⚠️  有 {test_results['failed']} 个测试失败，请检查你的实现。")
        print("\n失败的测试详情:")
        for detail in test_results['details']:
            if detail.startswith("❌"):
                print(f"  {detail}")
    
    return test_results['failed'] == 0


if __name__ == "__main__":
    main() 