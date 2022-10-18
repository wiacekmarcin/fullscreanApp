#include "pogoda.h"
#include "ui_pogoda.h"
#include <QFont>
#include <QFontDatabase>
#include "QJsonDocument.h"
#include <QAbstractSocket>
Pogoda::Pogoda(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Pogoda),
    netMng(nullptr),
    request(QUrl("https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units-metric"))
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
    m_h = -1;
}

Pogoda::~Pogoda()
{
    delete ui;
}

void Pogoda::update(int , int , int , int , int h, int , int s)
{
    if (s % 5 == 0 || m_h == h)
        return;
    m_h = h;
    if (netMng) {
        netMng->get(request);
    }
}

void Pogoda::setNetworkManager(QNetworkAccessManager *mnt)
{
    netMng = mnt;
    connect(netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)));
}

void Pogoda::parseMessage(QNetworkReply *reply)
{
    qDebug() << reply->request().url().toDisplayString();
    qDebug() << reply->errorString();
    qDebug() << reply->readAll();
    QJsonDocument doc = QJsonDocument::fromJson(reply->readAll());
    if (doc.isNull() || doc.isEmpty()) {
        //ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));
        return;
    }
    QString citiname, timeweather;
    citiname = doc.toVariant().toMap()["sys"].toMap()["name"].toString();
    qDebug() << "utc" << doc.toVariant().toMap()["dt"].toLongLong();
    timeweather = QDateTime::fromSecsSinceEpoch(doc.toVariant().toMap()["dt"].toLongLong()).toString("HH:mm");

    ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));

    reply->deleteLater();
        //ui->ip->setText(doc.toVariant().toMap()["origin"].toString());
}

QRect Pogoda::getRect()
{
    return QRect(0,200,width(),height());
}
