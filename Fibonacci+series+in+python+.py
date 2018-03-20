
# coding: utf-8

# In[12]:


def fib(n):
    """print the result of fibonacci"""
    
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b ,a+b
    print()
    
    
my_fibo = fib(2000)
print(my_fibo)
        
    
    


# In[17]:


# return Fibonacci series up to n
def fibo_return(n):
   result = []
   a,b = 0,1
   
   while a<n:
       result.append(a)
       a,b = b , a+b
       
   return result

my_return_fibo = fibo_return(2000)
my_return_fibo

