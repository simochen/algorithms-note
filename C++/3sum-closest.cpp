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