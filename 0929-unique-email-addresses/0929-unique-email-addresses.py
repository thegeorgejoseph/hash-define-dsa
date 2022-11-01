'''
test.email+alex@leetcode.com

[test.email+alex, leetcode.com]
find index of + if -1 good else slice till that index
split on "." and join using ""
join the original together and add that to a hashset
return list(hashset)

'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for url in emails:
            local, domain = url.split("@")
            plusIdx = -1
            for i, c in enumerate(local):
                if c == '+':
                    plusIdx = i
                    break
            if plusIdx != -1:
                local = local[:plusIdx]
            local = "".join(local.split('.'))
            res.add(local + "@" + domain)
        return len(res)
            