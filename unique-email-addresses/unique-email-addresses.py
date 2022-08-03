class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        
        for email in emails :
            email_list = Email(email)
            email_set.add((email_list.local_name, email_list.domain_name))
        
        print(email_set)
        
        return len(email_set)
        


class Email:
    def __init__(self, email:str) :
        def isNotDot(char) :
            return char != "."
        
        
        local_name, self.domain_name = email.split("@")
        self.local_name = ""
        
        for char in local_name :
            if char == "." :
                continue
            if char == "+" :
                break
            self.local_name += char
        
        