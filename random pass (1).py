import random
import string 


class password():
    def __init__(self, length):
        self.length = length
        
        
        #selecting intensity of password
        self.st=input(
            "Select password intensity (1-3):\n1. Weak\n2. Medium\n3. Strong\n"
        )
        self.ss= input("a. easily memorable password\nb. I dont care about memorability\n")
        
        if self.st == "1"and self.ss == "a":
            self.weak_mem()
        
        elif self.st == "1" and self.ss == "b":
            self.weak_unmem()
        
        elif self.st == "2" and self.ss == "a":
            self.medium_mem()
        
        elif self.st == "2" and self.ss == "b":
            self.medium_unmem()
        
        elif self.st == "3" and self.ss == "a": 
            self.strong_mem()
        
        elif self.st == "3" and self.ss == "b":
            self.strong_unmem()
        
        else:   
            print("Invalid input. Please enter a valid option.")
            return
        
        
    def weak_mem(self):
        self.length=6
            # Using lowercase letters and digits to make it memorable
            # This is a weak password, but it is easy to remember
        self.password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=self.length))
        print(f"Your weak memorable password is: {self.password}")
            
            
        
    def weak_unmem(self):
        self.length=6
            # Using punctuation to make it unmemorable
            # This is a weak password, but it is not easy to remember
            # It is still weak because it only uses lowercase letters and digits
            # and also punctuation
        self.password = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=self.length))
        print(f"Your weak unmemorable password is: {self.password}")
        
    def medium_mem(self):
        self.length = 8
            # Using uppercase letters, lowercase letters, and digits to make it memorable
            # This is a medium password, but it is easy to remember
            # It is still medium because it only uses uppercase letters, lowercase letters, and digits
            # and does not use punctuation
        self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
        print(f"Your medium memorable password is: {self.password}")
        
    def medium_unmem(self):
        self.length = 8
            # Using uppercase letters, lowercase letters, digits, and punctuation to make it unmemorable
            # This is a medium password, but it is not easy to remember
            # It is still medium because it uses uppercase letters, lowercase letters, and digits
            # and also punctuation
        self.password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=self.length))
        print(f"Your medium unmemorable password is: {self.password}")
        
    def strong_mem(self):
        self.length = 12
            # Using uppercase letters, lowercase letters, digits, and punctuation to make it memorable
            # This is a strong password, but it is easy to remember
            # It is still strong because it uses uppercase letters, lowercase letters, digits, and punctuation
        self.password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=self.length))
        print(f"Your strong memorable password is: {self.password}")

    def strong_unmem(self): 
        self.length = 12
            # Using uppercase letters, lowercase letters, digits, and punctuation to make it unmemorable
            # This is a strong password, but it is not easy to remember
        self.password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=self.length))
        print(f"Your strong unmemorable password is: {self.password}")
        
        


if __name__ == "__main__":
    # Create an instance of the passwordz class with a specified length 
    # The password will be generated and printed in the class constructor
    feedback = password(length=0)  # length is not used in the class, but can be set if needed1