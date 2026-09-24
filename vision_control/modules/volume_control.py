import numpy as np
class VolumeControl:
    def __init__(self):
        self.volume=None
        try:
            from pycaw.pycaw import AudioUtilities
            self.device=AudioUtilities.GetSpeakers(); self.volume=self.device.EndpointVolume
        except Exception: self.volume=None
    def update(self,f):
        if not self.volume:return None
        value=float(np.clip((f["pinch"]-.02)/.22,0,1)); self.volume.SetMasterVolumeLevelScalar(value,None); return int(value*100)
