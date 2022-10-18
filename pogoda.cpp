#include "pogoda.h"
#include "ui_pogoda.h"
#include <QFont>
#include <QFontDatabase>
#include "QJsonDocument.h"
#include <QAbstractSocket>
#include <QDateTime>

Pogoda::Pogoda(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Pogoda),
    request(QUrl("https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"))
{
    
    connect(&netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)));

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
    netMng.get(request);
}

void Pogoda::parseMessage(QNetworkReply *reply)
{
    QByteArray bytes = reply->readAll();
    qDebug() << reply->request().url().toDisplayString();
    qDebug() << bytes;
    QJsonDocument doc = QJsonDocument::fromJson(bytes);
    if (doc.isNull() || doc.isEmpty()) {
        //ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));
        return;
    }
    QString citiname, timeweather;
    citiname = doc.toVariant().toMap()["name"].toString();
    qDebug() << "citi" << citiname;
    qDebug() << "utc" << doc.toVariant().toMap()["dt"].toLongLong();
    timeweather = QDateTime::fromSecsSinceEpoch(doc.toVariant().toMap()["dt"].toLongLong()).toString("HH:mm");

    ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));

    QDateTime sunrise = QDateTime::fromSecsSinceEpoch(doc.toVariant().toMap()["sys"].toMap()["sunrise"].toLongLong());
    QDateTime sunset = QDateTime::fromSecsSinceEpoch(doc.toVariant().toMap()["sys"].toMap()["sunset"].toLongLong());
    emit setSunrise(sunrise.time().hour(), sunrise.time().minute());
    emit setSunset(sunset.time().hour(), sunset.time().minute());

    double temp = doc.toVariant().toMap()["main"].toMap()["temp"].toDouble();
    double feels_like = doc.toVariant().toMap()["main"].toMap()["feels_like"].toDouble();
    double temp_min = doc.toVariant().toMap()["main"].toMap()["temp_min"].toDouble();
    double temp_max = doc.toVariant().toMap()["main"].toMap()["temp_max"].toDouble();
    int pressure = doc.toVariant().toMap()["main"].toMap()["pressure"].toInt();
    int huminidity = doc.toVariant().toMap()["main"].toMap()["humidity"].toDouble();

    double wind_speed = doc.toVariant().toMap()["wind"].toMap()["speed"].toDouble();
    double wind_deg = doc.toVariant().toMap()["wind"].toMap()["deg"].toDouble();

    QString weather_main = doc.toVariant().toMap()["weather"].toList()[0].toMap()["main"].toString();
    QString weather_descr = doc.toVariant().toMap()["weather"].toList()[0].toMap()["description"].toString();
    QString weather_icon = doc.toVariant().toMap()["weather"].toList()[0].toMap()["icon"].toString();

    qDebug() << temp << feels_like << temp_min << temp_max << pressure << huminidity << wind_speed << wind_deg;
    qDebug() << weather_main << weather_descr << weather_icon;
    reply->deleteLater();
        //ui->ip->setText(doc.toVariant().toMap()["origin"].toString());
}

QRect Pogoda::getRect()
{
    return QRect(0,200,width(),height());
}

