# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient, QImage)
from PySide2.QtWidgets import *
import cv2, imutils

# noinspection PyPep8Naming
from kmeans_clustering import kmeans_clustering
from region_growing import region_growing


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.choose_image_button = QPushButton(self.centralwidget)
        self.choose_image_button.setObjectName(u"choose_image_button")
        self.choose_image_button.setGeometry(QRect(50, 80, 131, 41))
        self.choose_image_button.clicked.connect(self.loadImage)
        self.kmean_label = QLabel(self.centralwidget)
        self.kmean_label.setObjectName(u"kmean_label")
        self.kmean_label.setGeometry(QRect(660, 20, 121, 40))
        font = QFont()
        font.setPointSize(20)
        self.kmean_label.setFont(font)
        self.region_grow_label = QLabel(self.centralwidget)
        self.region_grow_label.setObjectName(u"region_grow_label")
        self.region_grow_label.setGeometry(QRect(660, 410, 181, 40))
        self.region_grow_label.setFont(font)
        self.source_image_frame = QLabel(self.centralwidget)
        self.source_image_frame.setObjectName(u"source_image_frame")
        self.source_image_frame.setGeometry(QRect(50, 260, 256, 256))
        self.source_image_frame.setPixmap(QPixmap(u"incogniton.jpg"))
        self.source_image_frame.setScaledContents(True)
        self.kmean_image_frame = QLabel(self.centralwidget)
        self.kmean_image_frame.setObjectName(u"kmean_image_frame")
        self.kmean_image_frame.setGeometry(QRect(660, 70, 256, 256))
        self.kmean_image_frame.setPixmap(QPixmap(u"incogniton.jpg"))
        self.kmean_image_frame.setScaledContents(True)
        self.region_grow_image_frame = QLabel(self.centralwidget)
        self.region_grow_image_frame.setObjectName(u"region_grow_image_frame")
        self.region_grow_image_frame.setGeometry(QRect(660, 460, 256, 256))
        self.region_grow_image_frame.setPixmap(QPixmap(u"incogniton.jpg"))
        self.region_grow_image_frame.setScaledContents(True)
        self.source_image_label = QLabel(self.centralwidget)
        self.source_image_label.setObjectName(u"source_image_label")
        self.source_image_label.setGeometry(QRect(50, 209, 191, 41))
        self.source_image_label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.filename = None
        self.kmean_photo = None
        self.region_grow_photo = None

    # setupUi

    def loadImage(self):
        """
        Load the image that user selected and display
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        self.setKMeansPhoto(self.image)
        self.setRegionGrowPhoto(self.image)

    def setPhoto(self, image):
        """
        Take image input and resize for display purpose
        :param image:
        :return:
        """
        height, width, _ = image.shape
        image = imutils.resize(image, width=256, height=256)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.source_image_frame.setPixmap(QPixmap.fromImage(image))

    def setKMeansPhoto(self, image):
        """
        Apply K-Means Segmentation to image and display
        :param image:
        :return:
        """

        # Apply algorithm
        self.kmean_photo = kmeans_clustering(image)
        self.kmean_photo = imutils.resize(self.kmean_photo, width=256, height=256)
        frame = cv2.cvtColor(self.kmean_photo, cv2.COLOR_BGR2RGB)
        self.kmean_photo = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.kmean_image_frame.setPixmap(QPixmap.fromImage(self.kmean_photo))

    def setRegionGrowPhoto(self, image):
        """
        Apply Region Grow Segmentation to image and display
        :param image:
        :return:
        """
        self.region_grow_photo = image
        # Apply algorithm
        self.region_grow_photo = region_growing(image, ("mri.jpg" in self.filename or "CT.jpg" in self.filename))
        self.region_grow_photo = imutils.resize(self.region_grow_photo, width=256, height=256)
        frame = cv2.cvtColor(self.region_grow_photo, cv2.COLOR_BGR2RGB)
        self.region_grow_photo = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.region_grow_image_frame.setPixmap(QPixmap.fromImage(self.region_grow_photo))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.choose_image_button.setText(QCoreApplication.translate("MainWindow", u"Chọn ảnh", None))
        self.kmean_label.setText(QCoreApplication.translate("MainWindow", u"ISODATA", None))
        self.region_grow_label.setText(QCoreApplication.translate("MainWindow", u"Region Grow", None))
        self.source_image_frame.setText("")
        self.kmean_image_frame.setText("")
        self.region_grow_image_frame.setText("")
        self.source_image_label.setText(QCoreApplication.translate("MainWindow", u"Source Image", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
