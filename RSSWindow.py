import RSSFeedReader
import FeedWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class RSSWindow(QWidget):
    def __init__(self):
        # call the superior constructor
        super().__init__()

        # initiate local variable for feed window
        self.feed_window = None

        # create layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # set window's size
        self.resize(500, 100)

        # set window's title
        self.setWindowTitle("RSS Feed Reader")

        # set window's icon
        self.setWindowIcon(QtGui.QIcon("./Icons/rss_icon.png"))

        # populate the window
        self.link_label = QLabel("Give the RSS feed URL input:")
        self.layout.addWidget(self.link_label)
        self.link = QLineEdit()
        self.layout.addWidget(self.link)
        self.button = QPushButton("Display info")
        self.layout.addWidget(self.button)

        # add action to button
        self.button.clicked.connect(self.get_rss_link_data)

    def get_rss_link_data(self):
        # get input from form and call the RSS to provide the data
        #data = RSSFeedReader.RSS(self.link)

        # instantiate the feed window
        self.feed_window = FeedWindow.FeedWindow()
        self.feed_window.show()
