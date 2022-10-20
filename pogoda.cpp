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

QString Pogoda::getWindName(float windDirection)
{
    if (windDirection > 11.25 && windDirection <= 33.75) {
        return "NNE";
    } else if (windDirection > 33.75 && windDirection <= 56.25) {
        return "NE";
    } else if (windDirection > 56.25 && windDirection <= 78.75) {
        return "ENE";
    } else if (windDirection > 78.75 && windDirection <= 101.25) {
        return "E";
    } else if (windDirection > 101.25 && windDirection <= 123.75) {
        return "ESE";
    } else if (windDirection > 123.75 && windDirection <= 146.25) {
        return "SE";
    } else if (windDirection > 146.25 && windDirection <= 168.75) {
        return "SSE";
    } else if (windDirection > 168.75 && windDirection <= 191.25) {
        return "S";
    } else if (windDirection > 191.25 && windDirection <= 213.75) {
        return "SSW";
    } else if (windDirection > 213.75 && windDirection <= 236.25) {
        return "SW";
    } else if (windDirection > 236.25 && windDirection <= 258.75) {
        return "WSW";
    } else if (windDirection > 258.75 && windDirection <= 281.25) {
        return "W";
    } else if (windDirection > 281.25 && windDirection <= 303.75) {
        return "WNW";
    } else if (windDirection > 303.75 && windDirection <= 326.25) {
        return "NW";
    } else if (windDirection > 326.25 && windDirection <= 348.75) {
        return "NNW";
    } else {
        return "N";
    }
}

int Pogoda::getBeafort(float speedms)
{
    static float B[] = {1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117};
    int index = 0;
    float speedkmh  = speedms * 3.6;
    if (speedkmh > 117) 
        return 12;
    while (speedkmh < B[index])
    {
        ++index;
    }
    return index;
}

bool Pogoda::isDayTime() {
    QTime act = QTime::currentTime();
    if (act > sunrise && act < sunset) 
        return true;
    return false;
}