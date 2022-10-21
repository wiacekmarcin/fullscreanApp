#include "pogoda5day.h"

#include <QFont>
#include <QFontDatabase>
#include "QJsonDocument.h"
#include "QJsonObject.h"
#include <QAbstractSocket>
#include <QDateTime>
#include <QDebug>
#include <QPalette>
#include <QStyle>

Pogoda5Day::Pogoda5Day(QWidget *parent) :
    BlackWidget(parent),
    request(QUrl("https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"))
{
    int idf = QFontDatabase::addApplicationFont(":/font/weathericons-regular-webfont.ttf");
    QString family = QFontDatabase::applicationFontFamilies(idf).at(0);
    weatherFont = QFont(family);
    weatherFont.setPointSize(32);

    idf = QFontDatabase::addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Light.ttf");
    family = QFontDatabase::applicationFontFamilies(idf).at(0);
    windDescr = QFont(family);

    idf = QFontDatabase::addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Regular.ttf");
    family = QFontDatabase::applicationFontFamilies(idf).at(0);
    tempFont = QFont(family);

    m_h = m_m = pog_h = pog_m = -1;

    connect(&netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)));

    setupUi(this);
    //wind->setFont(weather);
    //wind->setStyleSheet("QLabel { color : #666; }");
    //wind->setText("\uf050");
//#\f050
    m_h = -1;

    iconMap["01d"]="\uf00d"; //"wi-day-sunny",
    iconMap["02d"]="\uf002"; //"wi-day-cloudy",
    iconMap["03d"]="\uf013"; //"wi-cloudy",
    iconMap["04d"]="\uf012"; //"wi-cloudy-windy",
    iconMap["09d"]="\uf01a"; //"wi-showers",
    iconMap["10d"]="\uf019"; //"wi-rain",
    iconMap["11d"]="\uf01e"; //"wi-thunderstorm",
    iconMap["13d"]="\uf01b"; //"wi-snow",
    iconMap["50d"]="\uf014"; //"wi-fog",
    iconMap["01n"]="\uf02e"; //"wi-night-clear",
    iconMap["02n"]="\uf031"; //"wi-night-cloudy",
    iconMap["03n"]="\uf031"; //"wi-night-cloudy",
    iconMap["04n"]="\uf031"; //"wi-night-cloudy",
    iconMap["09n"]="\uf037"; //"wi-night-showers",
    iconMap["10n"]="\uf036"; //"wi-night-rain",
    iconMap["11n"]="\uf03b"; //"wi-night-thunderstorm",
    iconMap["13n"]="\uf038"; //"wi-night-snow",
    iconMap["50n"]="\uf023"; //"wi-night-alt-cloudy-windy"

}

Pogoda5Day::~Pogoda5Day()
{

}

QRect Pogoda5Day::getRect()
{
    return QRect(0,480,1080,300);
}

void Pogoda5Day::timeout(const QDateTime &dt)
{
    if (m_h == dt.time().hour()) {
        if (m_m == dt.time().minute())
            return;
    }
    m_h = dt.time().hour();
    m_m = dt.time().minute();
    netMng.get(request);
}


int Pogoda5Day::ms2Beaufort(const float& ms)
{
    float kmh = ms * 60 * 60 / 1000;
    qDebug() << kmh;
    float speeds[] = {1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117};
    if (kmh > 117)
        return 12;

    if (kmh < speeds[0])
        return 0;

    int index = 0;
    while (kmh > speeds[index])
        ++index;
    return index-1;
}

QString Pogoda5Day::toBeaufortChar(int b)
{
    switch(b) {
    case 0: return "\uF0B7";
    case 1: return "\uF0B8";
    case 2: return "\uF0B9";
    case 3: return "\uF0BA";
    case 4: return "\uF0BB";
    case 5: return "\uF0BC";
    case 6: return "\uF0BD";
    case 7: return "\uF0BE";
    case 8: return "\uF0BF";
    case 9: return "\uF0C0";
    case 10: return "\uF0C1";
    case 11: return "\uF0C2";
    case 12: return "\uF0C3";
    default: return "\uF050";
    }
}


QString Pogoda5Day::deg2Cardinal(const float &deg)
{
    if (deg>11.25 && deg<=33.75){
        return "NNE";
    } else if (deg > 33.75 && deg <= 56.25) {
        return "NE";
    } else if (deg > 56.25 && deg <= 78.75) {
        return "ENE";
    } else if (deg > 78.75 && deg <= 101.25) {
        return "E";
    } else if (deg > 101.25 && deg <= 123.75) {
        return "ESE";
    } else if (deg > 123.75 && deg <= 146.25) {
        return "SE";
    } else if (deg > 146.25 && deg <= 168.75) {
        return "SSE";
    } else if (deg > 168.75 && deg <= 191.25) {
        return "S";
    } else if (deg > 191.25 && deg <= 213.75) {
        return "SSW";
    } else if (deg > 213.75 && deg <= 236.25) {
        return "SW";
    } else if (deg > 236.25 && deg <= 258.75) {
        return "WSW";
    } else if (deg > 258.75 && deg <= 281.25) {
        return "W";
    } else if (deg > 281.25 && deg <= 303.75) {
        return "WNW";
    } else if (deg > 303.75 && deg <= 326.25) {
        return "NW";
    } else if (deg > 326.25 && deg <= 348.75) {
        return "NNW";
    } else {
        return "N";
    }
}



void Pogoda5Day::parseMessage(QNetworkReply *reply)
{
    QByteArray bytes = reply->readAll();
    //qDebug() << reply->request().url().toDisplayString();
    qDebug() << bytes;
    QJsonDocument doc = QJsonDocument::fromJson(bytes);
    if (doc.isNull() || doc.isEmpty()) {
        //ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));
        return;
    }


    int cnt = doc.toVariant().toMap()["cnt"].toInt();
    //QJsonObject jsonObject = doc.toObject();
    //QJsonObject jsonList = jsonObject["list"].toObject();

    for (int i = 0; i < cnt; ++i) 
    {
        //QJsonObject obj = jsonList[QString::number(i)].toObject();
        //auto mapa = obj.toVariant().toMap();
        //qDebug() << mapa["dt"];
    
    }
    
    //QString weather_main = doc.toVariant().toMap()["weather"].toList()[0].toMap()["main"].toString();
    //QString weather_descr = doc.toVariant().toMap()["weather"].toList()[0].toMap()["description"].toString();
    //QString weather_icon = doc.toVariant().toMap()["weather"].toList()[0].toMap()["icon"].toString();
    //wIcon->setText(iconMap[weather_icon]);
    //wCond->setText(weather_descr);

    //qDebug() << temp << feels_like << /*temp_min << temp_max <<*/ pressure << huminidity << wind_speed << wind_deg;
    //qDebug() << weather_main << weather_descr << weather_icon;
    //reply->deleteLater();
        //ui->ip->setText(doc.toVariant().toMap()["origin"].toString());
}


void Pogoda5Day::setupUi(QWidget *Pogoda)
{
    if (Pogoda->objectName().isEmpty())
        Pogoda->setObjectName(QString::fromUtf8("Pogoda"));
    Pogoda->resize(getRect().width(), getRect().height());
    /*
    citydate = new QLabel(Pogoda);
    citydate->setObjectName(QString::fromUtf8("citydate"));
    citydate->setGeometry(QRect(0, 0, 300, 40));
    citydate->setStyleSheet(citiStyle);
    citydate->setTextFormat(Qt::RichText);

    QFrame * line = new QFrame(Pogoda);
    line->setObjectName(QString::fromUtf8("line"));
    line->setGeometry(QRect(0, 42, 300, 15));
    line->setStyleSheet("color:rgb(145, 148, 148); size:5pt;");
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    windB = new QLabel(Pogoda);
    windB->setObjectName(QString::fromUtf8("windB"));
    windB->setGeometry(QRect(0, 60, 60, 48));
    windB->setStyleSheet(windBStyle);
    windB->setFont(weatherFont);

    windD = new QLabel(Pogoda);
    windD->setObjectName(QString::fromUtf8("windD"));
    windD->setGeometry(QRect(60, 60, 75, 48));
    windD->setStyleSheet(windDStyle);

    windS = new QLabel(Pogoda);
    windS->setObjectName(QString::fromUtf8("windS"));
    windS->setGeometry(QRect(135, 50, 165, 60));
    windS->setWordWrap(true);
    windS->setStyleSheet(windSStyle);
    windS->setFont(windDescr);

    wIcon = new QLabel(Pogoda);
    wIcon->setObjectName(QString::fromUtf8("wIcon"));
    wIcon->setGeometry(QRect(0, 110, 115, 60));
    wIcon->setStyleSheet(iconWiStyle);
    wIcon->setFont(weatherFont);

    wTemp = new QLabel(Pogoda);
    wTemp->setObjectName(QString::fromUtf8("wTemp"));
    wTemp->setGeometry(QRect(120, 110, 165, 60));
    wTemp->setStyleSheet(iconWiStyle);
    wTemp->setFont(tempFont);

    wCond = new QLabel(Pogoda);
    wCond->setObjectName(QString::fromUtf8("lwcond"));
    wCond->setGeometry(QRect(0, 170, 300, 30));
    wCond->setStyleSheet(conditionalStyle);
    wCond->setFont(tempFont);

    QLabel * label_1 = new QLabel(Pogoda);
    label_1->setObjectName(QString::fromUtf8("lfeelTemp"));
    label_1->setGeometry(QRect(0, 200, 165, 30));
    label_1->setText(QString::fromUtf8("Odczuwalna"));
    label_1->setStyleSheet(feelTempStyle);
    label_1->setFont(tempFont);

    feelTemp = new QLabel(Pogoda);
    feelTemp->setObjectName(QString::fromUtf8("feelTemp"));
    feelTemp->setGeometry(QRect(170, 200, 165, 30));
    feelTemp->setStyleSheet(feelTempStyle);
    feelTemp->setFont(tempFont);

    QLabel * label_2 = new QLabel(Pogoda);
    label_2->setObjectName(QString::fromUtf8("lhumiTemp"));
    label_2->setGeometry(QRect(250, 110, 35, 35));
    label_2->setText(QString::fromUtf8("\uf07a"));
    label_2->setStyleSheet(feelTempStyle);
    label_2->setFont(weatherFont);

    humiTemp = new QLabel(Pogoda);
    humiTemp->setObjectName(QString::fromUtf8("humiTemp"));
    humiTemp->setGeometry(QRect(280, 110, 70, 30));
    humiTemp->setStyleSheet(feelTempStyle);
    humiTemp->setFont(tempFont);

    presTemp = new QLabel(Pogoda);
    presTemp->setObjectName(QString::fromUtf8("presTemp"));
    presTemp->setGeometry(QRect(250, 150, 70, 30));
    presTemp->setStyleSheet(feelTempStyle);
    presTemp->setFont(tempFont);
    */
}
