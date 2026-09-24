import time,pyautogui
class GestureShortcuts:
    def __init__(self): self.last={}
    def apply(self,g):
        now=time.time()
        if now-self.last.get(g,0)<.8:return ''
        keys={'thumbs_up':'playpause','thumbs_down':'prevtrack','peace':'nexttrack','open_palm':'stop'}
        if g in keys: pyautogui.press(keys[g]); self.last[g]=now; return keys[g].upper()
        return ''
