def my_dec(n):
    def wrapper():
        print("Hi") 
        n()
        print("Hello")
    return wrapper
        
