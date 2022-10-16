#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QWidget>
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
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MagicMirrorQt", Q_NULLPTR));
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
