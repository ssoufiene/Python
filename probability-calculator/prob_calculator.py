import copy
import random
class Hat(object):
    def __init__(self,**kwargs):
        self.__dict__.update(**kwargs)
        self.contents=[]
        self.drawn=[]
        keys=kwargs.keys()
        for i in keys :
            for j in range(kwargs[i]):
                self.contents.append((i))
    def draw(self,x):
        if x>len(self.contents):
            return self.contents
        else :
            import random
            for i in range(x):
              y=random.randint(0,len(self.contents)-1)
              self.drawn.append(self.contents[y])
              self.contents.pop(y)
            return self.drawn
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    import copy
    m=0
    if num_balls_drawn>len(hat.contents):
        return 1
    else:
        for i in range(num_experiments):
            new_hat = copy.deepcopy(hat)
            new_hat.draw(num_balls_drawn)
            a=0
            for j in expected_balls.keys():
                if new_hat.drawn.count(j)>=expected_balls[j] :
                    a=a+expected_balls[j]
    
            if a==sum(expected_balls.values()):
                m=m+1
        return m/num_experiments