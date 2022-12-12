import sys
import RSSWindow

if __name__ == '__main__':
    application = RSSWindow.QApplication(sys.argv)
    window = RSSWindow.RSSWindow()
    window.show()
    sys.exit(application.exec_())

