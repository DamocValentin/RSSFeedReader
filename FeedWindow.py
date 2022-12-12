from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class FeedWindow(QWidget):
    def __init__(self):
        # call the superior constructor
        super().__init__()

        # create layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # set window's size
        self.resize(500, 500)

        # set window's title
        self.setWindowTitle("Feed")

        # set window's icon
        self.setWindowIcon(QtGui.QIcon("./Icons/rss_icon.png"))