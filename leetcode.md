# Hash 表
##1. Two Sum
### 问题描述
Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.
You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.
**Example:**
```Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].```
### 分析
- 方法1：暴力，复杂度 O(n2)，会超时- 方法2：hash. 用一个哈希表，存储每个数对应的下标，复杂度 O(n)
### C++ 代码
```c++// Time: O(n)// Space: O(n)// 往后组合class Solution {public:    vector<int> twoSum(vector<int> &nums, int target) {        unordered_map<int, int> mapping;        for (int i = 0; i < nums.size(); i++)            mapping[nums[i]] = i;        for (int i = 0; i < nums.size(); i++) {            const int gap = target - nums[i];            if (mapping.count(gap) && mapping[gap] > i)                return {i, mapping[gap]};        }          }};// 往前组合class Solution {public:    vector<int> twoSum(vector<int>& nums, int target) {        unordered_map<int, int> lookup;        for (int i = 0; i < nums.size(); ++i) {            if (lookup.count(target - nums[i])) {                return {lookup[target - nums[i]], i};            }            lookup[nums[i]] = i;        }    }};```
### 补充
#### `unordered_map`
 内部实现了哈希表，查找速度快。
- 查找元素是否存在
  若有 `unordered_map<int, int> mapping` ， 查找 `x` 是否在 `mapping` 中
  - 方法1： 若存在 `mapping.find(x) != mapping.end()`  - 方法2： 若存在 `mapping.count(x) != 0`
# 数组
## 15. [3 Sum](https://leetcode.com/problems/3sum/description/)
### 问题描述
Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.
**Note:**
The solution set must not contain duplicate triplets.
**Example:**
```Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:[  [-1, 0, 1],  [-1, -1, 2]]```
### 分析
先排序，然后左右夹逼，复杂度 $O(n^2)$。
这个方法可以推广到 k-sum, 先排序，然后做 `k-2` 次循环，在最内层循环左右夹逼，时间复杂度是 $O(\max\{n\log n, n^{k-1}\})$
### C++ 代码
```c++// Time: O(n^2)// Space: O(1)// 先排序，然后左右夹逼，注意跳过重复的数class Solution {public:    vector<vector<int>> threeSum(vector<int>& nums) {        vector<vector<int>> result;        if (nums.size() < 3) return result;        // Make nums in increasing order. Time: O(nlogn)        sort(nums.begin(), nums.end());                for (int i = 0; i < nums.size() - 2; i++) {            int target = -nums[i];            int j = i + 1, k = nums.size() - 1;            while (j < k) {                int sum = nums[j] + nums[k];                if (sum > target) --k;                else if (sum < target) ++j;                else {                    vector<int> triplet(3, 0);                    triplet[0] = nums[i];                    triplet[1] = nums[j];                    triplet[2] = nums[k];                    result.push_back(triplet);                    while (j < k && nums[j] == triplet[1]) ++j; // 跳过重复的数                    while (j < k && nums[k] == triplet[2]) --k;                }            }            while (i+1 < nums.size() && nums[i+1] == nums[i]) ++i;        }        return result;    }};```
> 注意选择前向跳过和后向跳过。时间开销不同。
## 16. [3 Sum Closest](https://leetcode.com/problems/3sum-closest/description/)
### 问题描述
Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.
**Example:**
```Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).```
### 分析
先排序，然后左右夹逼，复杂度 $O(n^2)$。
### C++ 代码
```c++// Time: O(n^2)// Space: O(1)// 先排序，然后左右夹逼class Solution {public:    int threeSumClosest(vector<int>& nums, int target) {        int result = 0;        int min_gap = INT_MAX;        sort(nums.begin(), nums.end());                for (int i = 0; i < nums.size() - 2; i++) {            int j = i + 1, k = nums.size() - 1;            while (j < k) {                int sum = nums[i] + nums[j] + nums[k];                if (sum > target) --k;                else if (sum < target) ++j;                else return target;                                if (abs(sum - target) < min_gap) {                    min_gap = abs(sum - target);                    result = sum;                }            }            while (i+1 < nums.size()-1 && nums[i+1] == nums[i]) ++i;        }        return result;    }};```
## 18. [4 Sum](https://leetcode.com/problems/4sum/description/)
### 问题描述
Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a*+ *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.
**Note:**
The solution set must not contain duplicate quadruplets.
**Example:**
```Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:[  [-1,  0, 0, 1],  [-2, -1, 1, 2],  [-2,  0, 0, 2]]```
### 分析
- 先排序，然后左右夹逼，复杂度 $O(n^3)$。- 可以用一个 hash 表先缓存两个数的和，最终复杂度 $O(n^3)$。
### C++ 代码
```c++// Time: O(n^3)// Space: O(1)// 先排序，然后左右夹逼，注意跳过重复的数class Solution {public:    vector<vector<int>> fourSum(vector<int>& nums, int target) {        vector<vector<int>> result;        if (nums.size() < 4) return result;        // Make nums in increasing order. Time: O(nlogn)        sort(nums.begin(), nums.end());                for (int p = 0; p < nums.size() - 3; p++) {         for (int i = p + 1; i < nums.size() - 2; i++) {                int tgt = target - nums[p] - nums[i];                int j = i + 1, k = nums.size() - 1;                while (j < k) {                    int sum = nums[j] + nums[k];                    if (sum > tgt) --k;                    else if (sum < tgt) ++j;                    else {                        vector<int> quadruplet(4, 0);                        quadruplet[0] = nums[p];                        quadruplet[1] = nums[i];                        quadruplet[2] = nums[j];                        quadruplet[3] = nums[k];                        result.push_back(quadruplet);                        while (j < k && nums[j] == quadruplet[2]) ++j; // 跳过重复的数                        while (j < k && nums[k] == quadruplet[3]) --k;                    }                }                while (i+1 < nums.size()-1 && nums[i+1] == nums[i]) ++i;            }            while (p+1 < nums.size()-2 && nums[p+1] == nums[p]) ++p;        }        return result;    }};```
