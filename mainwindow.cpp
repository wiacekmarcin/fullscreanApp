#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "zegar.h"


#include <QPainter>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    QPalette pal = palette();
    pal.setColor(QPalette::Background, Qt::black);
    pal.setColor(QPalette::Window, Qt::black);

    pal.setColor(QPalette::WindowText, Qt::white);
    pal.setColor(QPalette::Text, Qt::white);
    pal.setColor(QPalette::BrightText, Qt::white);

    setAutoFillBackground(true);
    setPalette(pal);
    ui->setupUi(this);

    //zegar = new Zegar(ui->lgodzina, ui->lminuta, ui->ldzien, ui->lnazwaDnia);

    ui->analogClock->setWschod(7,15);
    ui->analogClock->setZachod(19,01);

    resize(1080, 1920);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::paintEvent(QPaintEvent * e)
{
    QPainter painter(this);
    // draw foreground image over the background
    // draws the foreground starting from the top left at point 0,0 of the label.
    // You can supply a different offset or source/destination rects to achieve the
    // blitting effect you want.
    // painter.drawPixmap(QPoint(0,0),QPixmap(QString::fromUtf8(":/new/prefix1/tlo")));

    QMainWindow::paintEvent(e);
}




