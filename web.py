import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        # Set up the web engine view
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.Browser)

        # Set up the navigation bar
        NavBar = QToolBar()  # Create a toolbar for navigation
        self.addToolBar(NavBar)

        # Back button
        BackButton = QAction('Back', self)
        BackButton.triggered.connect(self.Browser.back)
        NavBar.addAction(BackButton)

        # Forward button
        ForwardButton = QAction('Forward', self)
        ForwardButton.triggered.connect(self.Browser.forward)
        NavBar.addAction(ForwardButton)

        # Reload button
        ReloadButton = QAction('Reload', self)
        ReloadButton.triggered.connect(self.Browser.reload)
        NavBar.addAction(ReloadButton)

        # Home button
        HomeButton = QAction('Home', self)
        HomeButton.triggered.connect(self.NavigateHome)
        NavBar.addAction(HomeButton)

        # URL bar
        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)
        NavBar.addWidget(self.UrlBar)

        # Update the URL bar when the URL changes
        self.Browser.urlChanged.connect(self.UpdateUrl)

        self.showMaximized()

    def NavigateHome(self):
        self.Browser.setUrl(QUrl("http://google.com"))  # Use QUrl for URLs

    def NavigateToUrl(self):
        url = self.UrlBar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url  # Ensure URL is well-formed
        self.Browser.setUrl(QUrl(url))

    def UpdateUrl(self, q):
        self.UrlBar.setText(str(q.toString()))  # Update URL bar text


# Initialize the application
Application = QApplication(sys.argv)
QApplication.setApplicationName('Web Browser by DataFlair')
Window = MainScreen()
Application.exec()
