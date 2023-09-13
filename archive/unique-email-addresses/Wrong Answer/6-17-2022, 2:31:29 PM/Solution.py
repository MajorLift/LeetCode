// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for [username, domain] in list(map(lambda x: x.split('@'), emails)):
            username = username[:username.find('+')]
            username = re.sub('\.', '', username)
            email_set.add(username + '@' + domain)
        return len(email_set)