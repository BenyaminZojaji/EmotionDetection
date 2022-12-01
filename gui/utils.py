import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap


def convert_cv_image_2_qt_qpixmap(cv_img, size):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    if size==None:
        return QPixmap.fromImage(convert_to_qt_format)
    else:
        p = convert_to_qt_format.scaledToWidth(size, Qt.FastTransformation)
        return QPixmap.fromImage(p)
