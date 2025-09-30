class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()


        for email in emails:

            res = ""
            domain  = ""
            seenPlus = False
            seenAt = False

            for j in range(len(email)):

                if email[j]  == "@": seenAt = True

                if email[j] == "+": seenPlus = True

                if not seenPlus and not seenAt and email[j] != "." and email[j] != "+":
                    res += email[j]
                


                

                if seenAt:
                    domain = email[j +1 :]
                    break
            

            print(domain, res)
            seen.add((res, domain))

        return len(seen)

        
        