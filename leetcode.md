# Hash 表

## 1. Two Sum

### 问题描述

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### 分析

- 方法1：暴力，复杂度 O(n²)，会超时
- 方法2：hash. 用一个哈希表，存储每个数对应的下标，复杂度 O(n)

### C++ 代码

```c++
// Time: O(n)
// Space: O(n)
// 往后组合
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> mapping;
        for (int i = 0; i < nums.size(); i++)
            mapping[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++) {
            const int gap = target - nums[i];
            if (mapping.count(gap) && mapping[gap] > i)
                return {i, mapping[gap]};
        }      
    }
};
// 往前组合
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        for (int i = 0; i < nums.size(); ++i) {
            if (lookup.count(target - nums[i])) {
                return {lookup[target - nums[i]], i};
            }
            lookup[nums[i]] = i;
        }
    }
};
```

### 补充

#### `map`

内部建立一棵红黑树（一种非严格意义上的平衡二叉树），这棵树具有对数据（`key` 值）自动排序的功能，所以在 `map` 内部所有的数据都是有序的。

- 查找 `map.find()`

  根据 `key` 值查找记录，复杂度为 logn。`find(key)` 函数返回一个迭代器指向键为 `key` 的元素，如果没找到就返回指向 map 尾部的迭代器（`map.end()`）。

- 删除 `map.erase()`

  根据 `key` 值删除记录。

- `map.begin()`，`map.end()`  返回指向 map 头部和尾部的迭代器

- `map.size()` 返回 map 中元素的个数

- `map.count()` 返回指定元素出现的次数

- `map.empty()` 如果 map 为空则返回 true

- `map.clear()` 删除所有元素

- `map[]`，`map.at()` 访问元素

- `map.insert()` 插入元素

  通过 `make_pair` 函数构造 `(k,v)` 键值对，再通过 `insert` 函数按照 `k` 将 `v` 插入到 `map` 中。

- `map.find()` 查找元素

  根据 `key` 值查找记录，查找复杂度为 O(logn)。`find(key)` 函数返回一个迭代器指向键为 `key` 的元素，如果没找到就返回指向 map 尾部的迭代器（`map.end()`）。

- `map.erase()` 删除元素

  根据 `key` 值删除记录。


#### `unordered_map`

 内部实现了哈希表，查找速度快，查找复杂度为 O(1)。不会根据 `key` 的大小进行排序。遍历顺序与创建该容器时输入元素的顺序不一定一致。

- 查找元素是否存在

  若有 `unordered_map<int, int> lookup` ， 查找 `x` 是否在 `lookup` 中

  - 方法1： 若存在 `lookup.find(x) != lookup.end()`
  - 方法2： 若存在 `lookup.count(x) != 0`

# 数组

## 15. [3 Sum](https://leetcode.com/problems/3sum/description/)

### 问题描述

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**Example:**

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### 分析

先排序，然后左右夹逼，复杂度 O(n²)。

这个方法可以推广到 k-sum, 先排序，然后做 `k-2` 次循环，在最内层循环左右夹逼，时间复杂度是 $O(\max\{n\log n, n^{k-1}\})$

### C++ 代码

```c++
// Time: O(n^2)
// Space: O(1)
// 先排序，然后左右夹逼，注意跳过重复的数
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() < 3) return result;
        // Make nums in increasing order. Time: O(nlogn)
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; i++) {
            int target = -nums[i];
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sum = nums[j] + nums[k];
                if (sum > target) --k;
                else if (sum < target) ++j;
                else {
                    vector<int> triplet = {nums[i], nums[j], nums[k]};
                    result.push_back(triplet);
                    while (j < k && nums[j] == triplet[1]) ++j; // 跳过重复的数
                    while (j < k && nums[k] == triplet[2]) --k;
                }
            }
            while (i+1 < nums.size() && nums[i+1] == nums[i]) ++i;
        }
        return result;
    }
};
```

> 注意选择前向跳过和后向跳过。时间开销不同。

## 16. [3 Sum Closest](https://leetcode.com/problems/3sum-closest/description/)

### 问题描述

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**

```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

### 分析

先排序，然后左右夹逼，复杂度 O(n²)。

### C++ 代码

```c++
// Time: O(n^2)
// Space: O(1)
// 先排序，然后左右夹逼
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int result = 0;
        int min_gap = INT_MAX;
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; i++) {
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum > target) --k;
                else if (sum < target) ++j;
                else return target;
                
                if (abs(sum - target) < min_gap) {
                    min_gap = abs(sum - target);
                    result = sum;
                }
            }
            while (i+1 < nums.size()-1 && nums[i+1] == nums[i]) ++i;
        }
        return result;
    }
};
```

## 18. [4 Sum](https://leetcode.com/problems/4sum/description/)

### 问题描述

Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a*+ *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note:**

The solution set must not contain duplicate quadruplets.

**Example:**

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

### 分析

- 先排序，然后左右夹逼，复杂度 $O(n^3)$。
- 可以用一个 hash 表先缓存两个数的和，最终复杂度 $O(n^2)$。

### C++ 代码

```c++
// Time: O(n^3)
// Space: O(1)
// 先排序，然后左右夹逼，注意跳过重复的数
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if (nums.size() < 4) return result;
        // Make nums in increasing order. Time: O(nlogn)
        sort(nums.begin(), nums.end());
        
        for (int p = 0; p < nums.size() - 3; p++) {
            for (int i = p + 1; i < nums.size() - 2; i++) {
                int tgt = target - nums[p] - nums[i];
                int j = i + 1, k = nums.size() - 1;
                while (j < k) {
                    int sum = nums[j] + nums[k];
                    if (sum > tgt) --k;
                    else if (sum < tgt) ++j;
                    else {
                        vector<int> quadruplet = {nums[p], nums[i], nums[j], nums[k]};
                        result.push_back(quadruplet);
                        while (j < k && nums[j] == quadruplet[2]) ++j; // 跳过重复的数
                        while (j < k && nums[k] == quadruplet[3]) --k;
                    }
                }
                while (i+1 < nums.size()-1 && nums[i+1] == nums[i]) ++i;
            }
            while (p+1 < nums.size()-2 && nums[p+1] == nums[p]) ++p;
        }
        return result;
    }
};

// Time: O(n^2)
// Space: O(n^2)
// 先用一个 hash 表缓存两个数的和
// 实际运行时间比方法1长，由于存在重复
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if (nums.size() < 4) return result;
        // Make nums in increasing order. Time: O(nlogn)
        sort(nums.begin(), nums.end());
        
        unordered_multimap<int, pair<int, int>> cache;
        for (int i = 0; i < nums.size() - 1; i++)
            for (int j = i + 1; j < nums.size(); j++)
                cache.insert(make_pair(nums[i] + nums[j], make_pair(i, j)));
        
        for (auto i = cache.begin(); i != cache.end(); ++i) {
            //while (i != cache.end() && !cache.count(target - i->first)) ++i;
            auto range = cache.equal_range(target - i->first);
            auto a = i->second.first;
            auto b = i->second.second;
            for (auto j = range.first; j != range.second; ++j) {
                auto c = j->second.first;
                auto d = j->second.second;
                if (a != c && a != d && b != c && b != d) {
                    vector<int> vec = {nums[a], nums[b], nums[c], nums[d]};
                    sort(vec.begin(), vec.end());
                    result.push_back(vec);
                }
            }
        }
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result;
    }
};
```

### 补充

#### `multimap`

`map` 只能实现一对一的映射，重复的键会被覆盖；而 `multimap` 能够实现一对多的存储方式，允许重复键。

`equal_range` 是 C++ STL 中的一种二分查找算法（在 `map`， `unordered_map`， `multimap`， `unordered_multimap`中均有实现），试图在已排序的 [first, last) 中寻找value，它返回 `pair(i,j)`，其中 i 是在不破坏次序的前提下，value 可插入的第一个位置 (lower_bound)， j 是在不破坏次序的前提下，value 可插入的最后一个位置 (upper_bound) 。因此，[i, j) 内的每个元素都等于 value，而且 [i, j) 是 [first, last) 中符合此性质的最大子区间。