"""Landmark geometry and normalized feature helpers."""
import math, numpy as np
TIP_IDS={"thumb":4,"index":8,"middle":12,"ring":16,"pinky":20}
PIP_IDS={"index":6,"middle":10,"ring":14,"pinky":18}
MCP_IDS={"index":5,"middle":9,"ring":13,"pinky":17}
def distance(a,b): return float(np.linalg.norm(np.asarray(a[:2])-np.asarray(b[:2])))
def normalize_landmarks(landmarks):
    base=np.asarray(landmarks[0],dtype=np.float32)
    pts=np.asarray(landmarks,dtype=np.float32)-base
    scale=max(np.linalg.norm(pts[9,:2]),1e-6)
    pts[:,:2]/=scale; pts[:,2]/=scale
    return pts.flatten().tolist()
def finger_states(p):
    return {"thumb": p[4][0]>p[3][0], **{n: p[TIP_IDS[n]][1]<p[PIP_IDS[n]][1] for n in ["index","middle","ring","pinky"]}}
def extract_features(landmarks):
    p=[(x.x,x.y,x.z) if hasattr(x,'x') else tuple(x) for x in landmarks]
    states=finger_states(p)
    return {"landmarks":p,"normalized":normalize_landmarks(p),"fingers":states,
            "pinch":distance(p[4],p[8]),"index_middle":distance(p[8],p[12]),
            "wrist_index":distance(p[0],p[8])}
