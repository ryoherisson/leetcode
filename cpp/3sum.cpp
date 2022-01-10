// https://leetcode.com/problems/3sum/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {https://leetcode.com/problems/3sum/
            if (i >= 1 && nums[i] == nums[i - 1]) continue;
            int target = -nums[i];
            int front = i + 1;
            int back = nums.size() - 1;

            while (front < back) {
                int sum = nums[front] + nums[back];

                if (sum < target)
                    front++;

                else if (sum > target)
                    back--;

                else {
                    vector<int> triplet = {nums[i], nums[front], nums[back]};
                    res.push_back(triplet);
                    front++;

                    while(front < back && nums[front] == nums[front - 1]) front++;
                }
            }
        }
        return res;
    }
};