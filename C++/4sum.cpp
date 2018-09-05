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