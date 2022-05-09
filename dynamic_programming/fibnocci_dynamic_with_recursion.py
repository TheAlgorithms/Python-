'''
This program provides the addition of fibnocci series with recursion, using memoization technique in dynamic programming
'''

memo={}

def fib(fibvalue :int,memorise: dict={} ) -> int:
    if(fibvalue in memorise.keys()):
        return memorise[fibvalue]
    if(fibvalue<=1):
        return 1
    
    memorise[fibvalue] =fib(fibvalue-1)+fib(fibvalue-2)

    return memorise[fibvalue]

#returns integer
def fibslow(fibvalue :int) -> int:
    
    if(fibvalue<=1):
        return 1
    
    return fibslow(y-1)+fibslow(fibvalue-2)


#return integer
def test_fib(max_value:int) -> int:
    return fib(max_value)
    
if __name__ == "__main__":
    for i in range(10):
        print(f"Fibnocci addition till number {i} is {test_fib(i)}")



