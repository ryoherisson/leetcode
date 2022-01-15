// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        vector<int> dict(256, -1);
        int start = -1;

        for (int i = 0; i < s.size(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            res = max(res, i - start);
        }
        return res;
    }
};