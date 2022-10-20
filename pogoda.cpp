#include "pogoda.h"
#include "ui_pogoda.h"
#include <QFont>
#include <QFontDatabase>
#include "QJsonDocument.h"
#include <QAbstractSocket>
#include <QDateTime>
#include <QDebug>
#include <QPalette>
#include <QStyle>

Pogoda::Pogoda(QWidget *parent) :
    BlackWidget(parent),
    request(QUrl("https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"))
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
    citiname = "Nieznane";
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

Pogoda::~Pogoda()
{

}

QRect Pogoda::getRect()
{
    return QRect(0,180,400,300);
}

void Pogoda::timeout(const QDateTime &dt)
{
    if (m_h == dt.time().hour()) {
        if (m_m == dt.time().minute())
            return;
        setCitiLabel();
    }
    m_h = dt.time().hour();
    m_m = dt.time().minute();
    netMng.get(request);
}

void Pogoda::setCitiLabel()
{
    citydate->setText(QString("%1 <span style=\"font-size:15px;color:#666\">Dane sprzed %2</span>").arg(citiname)
                      .arg(getTimeRemaing(m_h-pog_h, m_m-pog_m)));
}

int Pogoda::ms2Beaufort(const float& ms)
{
    float kmh = ms * 60 * 60 / 1000;
    qDebug() << kmh;
    float speeds[] = {1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117};
    if (kmh > 117)
        return 12;
    int index = 0;
    while (kmh < speeds[index])
        ++index;
    qDebug() << index;
    return index;
}

QString Pogoda::toBeaufortChar(int b)
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

static QString B2Description(int b) {
    switch(b) {
    case 0: return QString::fromUtf8("Cisza");
    case 1: return QString::fromUtf8("Powiew");
    case 2: return QString::fromUtf8("Słaby wiatr");
    case 3: return QString::fromUtf8("Łagodny wiatr");
    case 4: return QString::fromUtf8("Umiarkowany wiatr");
    case 5: return QString::fromUtf8("Dość silny wiatr");
    case 6: return QString::fromUtf8("Silny wiatr");
    case 7: return QString::fromUtf8("Bardzo silny wiatr");
    case 8: return QString::fromUtf8("Wicher");
    case 9: return QString::fromUtf8("Silny sztorm");
    case 10: return QString::fromUtf8("Bardzo silny sztorm");
    case 11: return QString::fromUtf8("Gwałtowny sztorm");
    case 12: return QString::fromUtf8("Bardzo silny sztorm"); //Huragan
    }
    return "";
}

QString Pogoda::toDescrSilaWiatru(const float &ms)
{
    int b = ms2Beaufort(ms);
    QString ret = QString::number(ms, 'f', 1);

    ret += QString("m/s (%1)").arg(B2Description(b));
    return ret;
}



QString Pogoda::deg2Cardinal(const float &deg)
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



void Pogoda::parseMessage(QNetworkReply *reply)
{
    QByteArray bytes = reply->readAll();
    //qDebug() << reply->request().url().toDisplayString();
    qDebug() << bytes;
    QJsonDocument doc = QJsonDocument::fromJson(bytes);
    if (doc.isNull() || doc.isEmpty()) {
        //ui->citydate->setText(QString::fromUtf8("<html><head/><body><p><span style=\"font-size:28pt; color:#aaaaaa;\">%1, </span><span style=\"font-size:28pt; color:#666666;\">%2</span><br/></p></body></html>").arg(citiname, timeweather));
        return;
    }

    citiname = doc.toVariant().toMap()["name"].toString();
    qDebug() << "citi" << citiname;
    qDebug() << "utc" << doc.toVariant().toMap()["dt"].toLongLong();
    QTime dtw = QDateTime::fromMSecsSinceEpoch(doc.toVariant().toMap()["dt"].toLongLong()*1000).time();

    pog_h = dtw.hour();
    pog_m = dtw.minute();
    setCitiLabel();

    QDateTime sunrise = QDateTime::fromMSecsSinceEpoch(doc.toVariant().toMap()["sys"].toMap()["sunrise"].toLongLong()*1000);
    QDateTime sunset = QDateTime::fromMSecsSinceEpoch(doc.toVariant().toMap()["sys"].toMap()["sunset"].toLongLong()*1000);
    emit setSunrise(sunrise.time().hour(), sunrise.time().minute());
    emit setSunset(sunset.time().hour(), sunset.time().minute());

    double wind_speed = doc.toVariant().toMap()["wind"].toMap()["speed"].toDouble();
    double wind_deg = doc.toVariant().toMap()["wind"].toMap()["deg"].toDouble();
    windB->setText(toBeaufortChar(ms2Beaufort(wind_speed)));
    windD->setText(deg2Cardinal(wind_deg));
    windS->setText(toDescrSilaWiatru(wind_speed));

    double temp = doc.toVariant().toMap()["main"].toMap()["temp"].toDouble();
    double feels_like = doc.toVariant().toMap()["main"].toMap()["feels_like"].toDouble();
    //double temp_min = doc.toVariant().toMap()["main"].toMap()["temp_min"].toDouble();
    //double temp_max = doc.toVariant().toMap()["main"].toMap()["temp_max"].toDouble();

    wTemp->setText(QString::number(temp, 'f', 1)+QString("\u00B0"));
    feelTemp->setText(QString::number(feels_like, 'f', 1)+QString("\u00B0"));


    int pressure = doc.toVariant().toMap()["main"].toMap()["pressure"].toInt();
    int huminidity = doc.toVariant().toMap()["main"].toMap()["humidity"].toDouble();


    QString weather_main = doc.toVariant().toMap()["weather"].toList()[0].toMap()["main"].toString();
    QString weather_descr = doc.toVariant().toMap()["weather"].toList()[0].toMap()["description"].toString();
    QString weather_icon = doc.toVariant().toMap()["weather"].toList()[0].toMap()["icon"].toString();
    wIcon->setText(iconMap[weather_icon]);
    wCond->setText(weather_descr);

    qDebug() << temp << feels_like << /*temp_min << temp_max <<*/ pressure << huminidity << wind_speed << wind_deg;
    qDebug() << weather_main << weather_descr << weather_icon;
    reply->deleteLater();
        //ui->ip->setText(doc.toVariant().toMap()["origin"].toString());
}

QString Pogoda::getTimeRemaing(int h, int m)
{

    if (m < 0) {
        --h;
        m+=60;
    }

    if (h < 0)
        h+=24;

    if (h == 0 && m < 30) {
        return QString("%1 min").arg(m);
    } else {
        float hal = 1.0*h + m/60.0;
        int h10 = (int) 10*hal + 5;
        return QString("%1.%2 godz").arg(h10/10).arg(h10%10);
    }
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
void Pogoda::setupUi(QWidget *Pogoda)
{
    if (Pogoda->objectName().isEmpty())
        Pogoda->setObjectName(QString::fromUtf8("Pogoda"));
    Pogoda->resize(getRect().width(), getRect().height());
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

}
