import cv2,time
from config import *
from modules.hand_tracker import HandTracker
from modules.gesture_recognizer import GestureRecognizer
from modules.virtual_mouse import VirtualMouse
from modules.volume_control import VolumeControl
from modules.air_drawing import AirDrawing
from modules.gesture_shortcuts import GestureShortcuts

def main():
 cap=cv2.VideoCapture(0); cap.set(3,CAMERA_WIDTH); cap.set(4,CAMERA_HEIGHT)
 if not cap.isOpened(): print('Unable to access webcam.'); return
 tracker=HandTracker(DETECTION_CONFIDENCE,TRACKING_CONFIDENCE,MAX_HANDS); recog=GestureRecognizer(); mouse=VirtualMouse(CURSOR_SMOOTHING); volume=VolumeControl(); drawing=AirDrawing(CAMERA_WIDTH,CAMERA_HEIGHT,DEFAULT_BRUSH_SIZE); shortcuts=GestureShortcuts(); mode='mouse'; prev=time.time()
 while True:
  ok,frame=cap.read()
  if not ok: break
  frame=cv2.flip(frame,1); landmarks=tracker.process(frame); gesture='none'; action=''
  if landmarks:
   features=__import__('utils.geometry',fromlist=['extract_features']).extract_features(landmarks); gesture,conf=recog.predict(features)
   if mode=='mouse' and gesture in ('index','pinch'): action=mouse.update(features,frame.shape[:2])
   elif mode=='volume': action=f'Volume: {volume.update(features) or "Unavailable"}%'
   elif mode=='drawing': frame=cv2.addWeighted(frame,.65,drawing.update(features,gesture),.35,0)
   elif mode=='shortcuts': action=shortcuts.apply(gesture)
  fps=1/max(time.time()-prev,1e-6); prev=time.time()
  cv2.rectangle(frame,(0,0),(410,115),(20,20,20),-1); cv2.putText(frame,'VISIONCONTROL',(15,28),0,.75,(0,255,255),2); cv2.putText(frame,f'MODE: {mode.upper()}',(15,55),0,.6,(255,255,255),1); cv2.putText(frame,f'GESTURE: {gesture}  ACTION: {action}',(15,80),0,.5,(255,255,255),1); cv2.putText(frame,f'FPS: {fps:.1f}  M/V/D/S  Q quit  C clear',(15,103),0,.42,(200,200,200),1); cv2.imshow('VisionControl',frame)
  key=cv2.waitKey(1)&255
  if key==ord('q'):break
  if key==ord('m'):mode='mouse'
  if key==ord('v'):mode='volume'
  if key==ord('d'):mode='drawing'
  if key==ord('s'):mode='shortcuts'
  if key==ord('c'): drawing.canvas[:]=0
 cap.release(); tracker.close(); cv2.destroyAllWindows()
if __name__=='__main__': main()
