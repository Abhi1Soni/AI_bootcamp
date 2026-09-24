import cv2, mediapipe as mp
class HandTracker:
    def __init__(self,det_conf=.7,track_conf=.7,max_hands=1):
        self.mp_hands=mp.solutions.hands
        self.hands=self.mp_hands.Hands(False,max_hands,1,det_conf,track_conf)
        self.drawer=mp.solutions.drawing_utils
    def process(self,frame):
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB); result=self.hands.process(rgb)
        if result.multi_hand_landmarks:
            hand=result.multi_hand_landmarks[0]; self.drawer.draw_landmarks(frame,hand,self.mp_hands.HAND_CONNECTIONS); return hand.landmark
        return None
    def close(self): self.hands.close()
