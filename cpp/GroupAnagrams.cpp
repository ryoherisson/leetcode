// https://leetcode.com/problems/group-anagrams/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;

        for (int i = 0; i < strs.size(); i++) {
            string s = strs[i];
            sort(s.begin(), s.end());
            mp[s].push_back(strs[i]);
        }

        vector<vector<string>> res;

        for (auto iter = mp.begin(); iter != mp.end(); iter++) {
            res.push_back(iter->second);
        }
        return res;
    }
};