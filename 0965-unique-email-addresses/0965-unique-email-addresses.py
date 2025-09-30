class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()


        for email in emails:
            local, domian = email.split("@")
            local = local.split("+")
            print(local)

            uniqueEmail = local[0].replace(".", "")
            print(uniqueEmail,domian)

            seen.add((uniqueEmail,domian))

        return len(seen)