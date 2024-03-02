import string
import random

if __name__ == "__main__" :
    
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    
    password_len = int(input("Enter Password Lenght\n"))
    
    password_store = []
    
    password_store.extend(s1)
    password_store.extend(s2)
    password_store.extend(s3)
    
    random.shuffle(password_store)
    
    print("Your New Password is:")
    
    #by selecting the first n elements of the list
    print("".join(password_store[0:password_len]))
    
    #by selecting random elements from the list
    print("".join(random.sample(password_store , password_len)))