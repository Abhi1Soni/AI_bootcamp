"""Collect normalized landmark rows: python collect_data.py; keys 1-7 select labels, q quits."""
import cv2,csv,os
from modules.hand_tracker import HandTracker
from utils.geometry import normalize_landmarks
labels={'1':'fist','2':'open_palm','3':'thumbs_up','4':'thumbs_down','5':'index','6':'peace','7':'pinch'}
os.makedirs('data',exist_ok=True); cap=cv2.VideoCapture(0); tracker=HandTracker(); label=None
with open('data/gestures.csv','a',newline='') as file:
 w=csv.writer(file)
 while True:
  ok,frame=cap.read();
  if not ok: break
  frame=cv2.flip(frame,1); lm=tracker.process(frame)
  if lm and label:w.writerow([label,*normalize_landmarks(lm)]); file.flush()
  cv2.putText(frame,f'LABEL: {label or "press 1-7"}',(20,40),0,.8,(0,255,0),2); cv2.imshow('Collect',frame); k=cv2.waitKey(1)&255
  if k==ord('q'):break
  if chr(k) in labels:label=labels[chr(k)]
cap.release();tracker.close();cv2.destroyAllWindows()
