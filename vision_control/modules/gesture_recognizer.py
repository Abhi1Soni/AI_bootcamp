class GestureRecognizer:
    def predict(self,f):
        s=f["fingers"]; pinch=f["pinch"]<.055
        if pinch and s["index"]: return "pinch",.95
        if not any(s.values()): return "fist",.95
        if all(s.values()): return "open_palm",.95
        if s["thumb"] and not any(s[x] for x in ["index","middle","ring","pinky"]): return "thumbs_up",.85
        if s["index"] and s["middle"] and not s["ring"] and not s["pinky"]: return "peace",.9
        if s["index"] and not any(s[x] for x in ["middle","ring","pinky"]): return "index",.9
        return "unknown",.5
