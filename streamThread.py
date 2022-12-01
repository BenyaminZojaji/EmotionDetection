from os import makedirs
from PySide6.QtCore import QThread, Signal
from deepface import DeepFace
import cv2

class StreamThread(QThread):
    signal_frame = Signal(object)

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.win_width  = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.win_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        makedirs(".temp", exist_ok=True)

    def get_emotionInfo(self):
        info = DeepFace.analyze('.temp/image.png', actions=['emotion'], enforce_detection=False, prog_bar=False)
        return info

    def renderbboxAndTxt(self, frame, emotion, x, y, w, h):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4) # bbox
        cv2.putText(frame, emotion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255)) # text
        return frame

    def run(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                break
            cv2.imwrite(".temp/image.png", frame)
            info = self.get_emotionInfo()

            if not (info['region']['x']==0 and info['region']['y']==0 and info['region']['w']==self.win_height and info['region']['h']==self.win_width):
                frame = self.renderbboxAndTxt(frame, info['dominant_emotion'], info['region']['x'],
                                                info['region']['y'], info['region']['w'], info['region']['h'])

            self.signal_frame.emit(frame)