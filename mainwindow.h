#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QTimer>
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
#include "ip.h"
#include "informacje.h"
#include "pogoda.h"
#include "pogoda5day.h"
#include <QVector>
#include <QNetworkAccessManager>
namespace Ui {

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    ::Zegar *digitalClock;
    ::AnalogClock *analogClock;
    ::IP *ipWidget;
    ::Informacje * infoWidget;
    ::Pogoda * pogodaInfo;
    ::Pogoda5Day * pogodaPrognoza;

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

private slots:
    void update();

private:
    Ui::MainWindow *ui;
    QTimer timer;
    QVector<BlackWidget*> widgets;
};




#endif // MAINWINDOW_H
