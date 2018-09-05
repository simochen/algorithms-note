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