# cascade
# reverse cascade

def reverse_cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        reverse_cascade(n // 10)
        print(n)
        
def inverse_cascade(n):
    
    def f_then_g(f, g, n):
        if n:
            f(n)
            g(n)
            
    grow = lambda n: f_then_g(grow, print, n // 10)    
    shrink = lambda n: f_then_g(print, shrink, n // 10)   
     
    grow(n)
    print(n)
    shrink(n)
    
    
# reverse_cascade(12345)
inverse_cascade(12345)