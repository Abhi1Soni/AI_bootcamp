import cv2,os,time
class AirDrawing:
    def __init__(self,w,h,size=5): self.canvas=cv2.cvtColor(cv2.imread(__file__) if False else (0*__import__('numpy').ones((h,w,3),dtype='uint8')),cv2.COLOR_BGR2BGRA)[:,:,:3]; self.prev=None; self.size=size
    def update(self,f,gesture):
        if gesture=='index':
            x,y=int(f['landmarks'][8][0]*self.canvas.shape[1]),int(f['landmarks'][8][1]*self.canvas.shape[0])
            if self.prev: cv2.line(self.canvas,self.prev,(x,y),(0,255,0),self.size)
            self.prev=(x,y)
        else:self.prev=None
        if gesture=='fist': self.canvas[:]=0
        return self.canvas
    def save(self): os.makedirs('output/drawings',exist_ok=True); return cv2.imwrite(f'output/drawings/drawing_{int(time.time())}.png',self.canvas)
