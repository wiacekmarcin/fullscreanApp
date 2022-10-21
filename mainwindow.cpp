#include "mainwindow.h"

#include "zegar.h"
#include "ip.h"
#include <QDateTime>

#include <QPainter>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    QPalette pal = palette();
    //pal.setColor(QPalette::Background, Qt::black);
    pal.setColor(QPalette::Window, Qt::black);

    pal.setColor(QPalette::WindowText, Qt::white);
    pal.setColor(QPalette::Text, Qt::white);
    pal.setColor(QPalette::BrightText, Qt::white);

    setAutoFillBackground(true);
    setPalette(pal);
    ui->setupUi(this);
    ui->centralWidget->setCursor(Qt::BlankCursor);

    widgets.push_back(ui->analogClock);
    widgets.push_back(ui->digitalClock);
    widgets.push_back(ui->ipWidget);
    widgets.push_back(ui->infoWidget);
    widgets.push_back(ui->pogodaInfo);
    widgets.push_back(ui->pogodaPrognoza);

    connect(&timer, SIGNAL(timeout()), this, SLOT(update()));
    timer.setInterval(1000);
    timer.start();

    //zegar = new Zegar(ui->lgodzina, ui->lminuta, ui->ldzien, ui->lnazwaDnia);

    ui->analogClock->setWschod(7,15);
    ui->analogClock->setZachod(19,01);
    ui->digitalClock->setWschod(7,15);
    ui->digitalClock->setZachod(19,01);

    resize(1080, 1920);

    connect(ui->pogodaInfo, SIGNAL(setSunrise(int,int)), ui->digitalClock, SLOT(setWschod(int,int)));
    connect(ui->pogodaInfo, SIGNAL(setSunset(int,int)), ui->digitalClock, SLOT(setZachod(int,int)));
    
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::update()
{
    QDateTime dt = QDateTime::currentDateTime();
    for(auto it = widgets.begin(); it != widgets.end(); ++it) {
        (*it)->timeout(dt);

    }
}

void Ui::Ui_MainWindow::setupUi(QMainWindow *MainWindow)
{
    if (MainWindow->objectName().isEmpty())
        MainWindow->setObjectName(QString("MainWindow"));
    MainWindow->resize(1080, 1920);
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
    MainWindow->setSizePolicy(sizePolicy);
    QPalette palette;
    QBrush brush(QColor(255, 255, 255, 255));
    brush.setStyle(Qt::SolidPattern);
    palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
    palette.setBrush(QPalette::Active, QPalette::Button, brush);
    QBrush brush1(QColor(0, 0, 0, 255));
    brush1.setStyle(Qt::SolidPattern);
    palette.setBrush(QPalette::Active, QPalette::Midlight, brush1);
    palette.setBrush(QPalette::Active, QPalette::Dark, brush1);
    palette.setBrush(QPalette::Active, QPalette::Mid, brush1);
    palette.setBrush(QPalette::Active, QPalette::Text, brush);
    palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
    palette.setBrush(QPalette::Active, QPalette::Base, brush1);
    palette.setBrush(QPalette::Active, QPalette::Window, brush1);
    palette.setBrush(QPalette::Active, QPalette::Shadow, brush1);
    palette.setBrush(QPalette::Active, QPalette::Highlight, brush1);
    palette.setBrush(QPalette::Active, QPalette::Link, brush1);
    palette.setBrush(QPalette::Active, QPalette::LinkVisited, brush1);
    palette.setBrush(QPalette::Active, QPalette::AlternateBase, brush1);
    palette.setBrush(QPalette::Active, QPalette::ToolTipBase, brush1);
    QBrush brush2(QColor(255, 255, 255, 128));
    brush2.setStyle(Qt::NoBrush);
    //palette.setBrush(QPalette::Active, QPalette::PlaceholderText, brush2);
    palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
    palette.setBrush(QPalette::Inactive, QPalette::Button, brush);
    palette.setBrush(QPalette::Inactive, QPalette::Midlight, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Dark, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Mid, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
    palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
    palette.setBrush(QPalette::Inactive, QPalette::Base, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Shadow, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Highlight, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::Link, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::LinkVisited, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush1);
    palette.setBrush(QPalette::Inactive, QPalette::ToolTipBase, brush1);
    QBrush brush3(QColor(255, 255, 255, 128));
    brush3.setStyle(Qt::NoBrush);
    //palette.setBrush(QPalette::Inactive, QPalette::PlaceholderText, brush3);
    palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Button, brush);
    palette.setBrush(QPalette::Disabled, QPalette::Midlight, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Dark, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Mid, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Text, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::Shadow, brush1);
    QBrush brush4(QColor(145, 141, 126, 255));
    brush4.setStyle(Qt::SolidPattern);
    palette.setBrush(QPalette::Disabled, QPalette::Highlight, brush4);
    palette.setBrush(QPalette::Disabled, QPalette::Link, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::LinkVisited, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
    palette.setBrush(QPalette::Disabled, QPalette::ToolTipBase, brush1);
    QBrush brush5(QColor(255, 255, 255, 128));
    brush5.setStyle(Qt::NoBrush);
    //palette.setBrush(QPalette::Disabled, QPalette::PlaceholderText, brush5);
    MainWindow->setPalette(palette);
    MainWindow->setMouseTracking(false);
    MainWindow->setAutoFillBackground(false);
    MainWindow->setStyleSheet(QString(""));
    centralWidget = new QWidget(MainWindow);
    centralWidget->setObjectName(QString("centralWidget"));

    digitalClock = new ::Zegar(centralWidget);
    digitalClock->setObjectName(QString("digitalClock"));
    digitalClock->setGeometry(digitalClock->getRect());

    analogClock = new AnalogClock(centralWidget);
    analogClock->setObjectName(QString("analogClock"));
    analogClock->setGeometry(analogClock->getRect());

    ipWidget = new ::IP(centralWidget);
    ipWidget->setObjectName(QString("ip"));
    ipWidget->setGeometry(ipWidget->getRect());

    infoWidget = new ::Informacje(centralWidget);
    infoWidget->setObjectName(QString("feds"));
    infoWidget->setGeometry(infoWidget->getRect());

    pogodaInfo = new ::Pogoda(centralWidget);
    pogodaInfo->setObjectName(QString("weather"));
    pogodaInfo->setGeometry(pogodaInfo->getRect());

    pogodaPrognoza = new ::Pogoda5Day(centralWidget);
    pogodaPrognoza->setObjectName(QString("forecast"));
    pogodaPrognoza->setGeometry(pogodaPrognoza->getRect());


    MainWindow->setCentralWidget(centralWidget);

    retranslateUi(MainWindow);

    QMetaObject::connectSlotsByName(MainWindow);
} // setupUi


