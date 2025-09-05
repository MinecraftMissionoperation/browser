from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)
browser = QWebEngineView()
browser.load("https://google.com")
browser.show()
sys.exit(app.exec_())
