#A program to print the first 100 numbers using function(in-built).
from operator import itruediv

class LoopIn:
    def __init__(self,first,end):
        self.first = first
        self.end= end
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.first <= self.end:
            x=self.first
            self.first+=1
            return x
        else:
            raise StopIteration 
        
def main():
    loop = LoopIn(0,100)
    for i in loop:
        print(i)

main()
    
