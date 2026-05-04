class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x_new=init
        for i in range(0,iterations):
            x_old=x_new
            del_L=2*x_old
            x_new=x_old-learning_rate*del_L
            print(x_new)
            if(x_new-x_old==0):
                return round(x_new,5)
        return round(x_new,5)
            
    