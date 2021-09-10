class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_key_idx = {'type': 0, 'color': 1, 'name': 2}
        count = 0

        for item in items:
            count += int(item[rule_key_idx[ruleKey]] == ruleValue)

        return count
