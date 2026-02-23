#https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    L=-1
    s_L=-1
    sm=float('inf')
    s_sm=float('inf')

    for x in a:
        if x>L:
            s_L=L 
            L=x
        elif x>s_L:
            s_L=x
        if x < sm:
            s_sm=sm
            sm=x
        elif x < s_sm:
            s_sm=x
    return [s_L,s_sm] 
    pass