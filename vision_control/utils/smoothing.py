class ExponentialSmoother:
    def __init__(self,alpha=0.3): self.alpha=alpha; self.value=None
    def update(self,value):
        self.value=value if self.value is None else tuple(self.alpha*a+(1-self.alpha)*b for a,b in zip(value,self.value)); return self.value
