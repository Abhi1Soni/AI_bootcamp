import time,pyautogui
from utils.smoothing import ExponentialSmoother
class VirtualMouse:
    def __init__(self,alpha=.3): self.smoother=ExponentialSmoother(alpha); self.last_click=0
    def update(self,f,frame_size):
        p=f["landmarks"]; x,y=p[8][0],p[8][1]; sw,sh=pyautogui.size(); sx,sy=self.smoother.update((x*sw,y*sh)); pyautogui.moveTo(int(sx),int(sy),_pause=False)
        if f["pinch"]<.055 and time.time()-self.last_click>.5: pyautogui.click(); self.last_click=time.time(); return "LEFT CLICK"
        return "MOVE"
