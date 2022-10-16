#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtCore/QVariant>
#include <QAction>
#include <QApplication>
#include <QButtonGroup>
#include <QHeaderView>
#include <QMainWindow>
#include <QWidget>
#include "analogclock.h"
#include "zegar.h"

namespace Ui {

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    ::Zegar *digitalClock;
    ::AnalogClock *analogClock;

    void setupUi(QMainWindow *MainWindow);

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MagicMirrorQt", 0));
    } // retranslateUi

};

class MainWindow: public Ui_MainWindow {};

}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void paintEvent(QPaintEvent * e);

private:
    Ui::MainWindow *ui;
    //Zegar * zegar;
};

#endif // MAINWINDOW_H
