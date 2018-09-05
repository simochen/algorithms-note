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