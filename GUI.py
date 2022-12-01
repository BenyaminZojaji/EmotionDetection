import sys
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from streamThread import StreamThread
from gui.utils import convert_cv_image_2_qt_qpixmap as cv2qtpixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('gui/main.ui')

        self.video = StreamThread()
        self.video.signal_frame.connect(self.show_webcam)
        self.video.start()

        self.ui.show()

    @Slot()    
    def show_webcam(self, frame):
        qpixmap = cv2qtpixmap(frame, None)
        self.ui.stream_label.setPixmap(qpixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

