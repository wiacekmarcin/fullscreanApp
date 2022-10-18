#include "pogoda.h"
#include "ui_pogoda.h"
#include <QFont>
#include <QFontDatabase>

Pogoda::Pogoda(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Pogoda)
{
    ui->setupUi(this);
    int id = QFontDatabase::addApplicationFont(":/font/weathericons-regular-webfont.ttf");
    QString family = QFontDatabase::applicationFontFamilies(id).at(0);
    QFont weather(family);
    weather.setPixelSize(30);
    ui->wind->setFont(weather);
    ui->wind->setStyleSheet("QLabel { color : #666; }");
    ui->wind->setText("\uf050");
//#\f050
}

Pogoda::~Pogoda()
{
    delete ui;
}

void Pogoda::update(int , int , int , int , int , int , int )
{

}

QRect Pogoda::getRect()
{
    return QRect(0,200,width(),height());
}
