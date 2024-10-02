#include <QApplication>
#include <QMainWindow>
#include <QToolBar>
#include <QAction>
#include <QLineEdit>
#include <QWebEngineView>
#include <QUrl>

class MainScreen : public QMainWindow {
    Q_OBJECT

public:
    MainScreen() {
        // Set up the web engine view
        Browser = new QWebEngineView(this);
        Browser->setUrl(QUrl("https://google.com"));
        setCentralWidget(Browser);

        // Set up the navigation bar
        QToolBar *NavBar = new QToolBar(this);
        addToolBar(NavBar);

        // Back button
        QAction *BackButton = new QAction("Back", this);
        connect(BackButton, &QAction::triggered, Browser, &QWebEngineView::back);
        NavBar->addAction(BackButton);

        // Forward button
        QAction *ForwardButton = new QAction("Forward", this);
        connect(ForwardButton, &QAction::triggered, Browser, &QWebEngineView::forward);
        NavBar->addAction(ForwardButton);

        // Reload button
        QAction *ReloadButton = new QAction("Reload", this);
        connect(ReloadButton, &QAction::triggered, Browser, &QWebEngineView::reload);
        NavBar->addAction(ReloadButton);

        // Home button
        QAction *HomeButton = new QAction("Home", this);
        connect
