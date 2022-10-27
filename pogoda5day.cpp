#include "pogoda5day.h"
#include "ui_pogoda5day.h"
#include "ui_pogodaday.h"
#include <QFont>
#include <QFontDatabase>
#include <QJsonDocument>
#include <QJsonObject>
#include <QAbstractSocket>
#include <QDateTime>
#include <QDebug>
#include <QPalette>
#include <QStyle>

Pogoda5Day::Pogoda5Day(QWidget *parent) :
    BlackWidget(parent),
    request(QUrl("https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric")),
    days{"", QString::fromUtf8("Pon"),
                    QString::fromUtf8("Wto"),
                    QString::fromUtf8("Śro"),
                    QString::fromUtf8("Czw"),
                    QString::fromUtf8("Pią"),
                    QString::fromUtf8("Sob"),
                    QString::fromUtf8("Nie")}
  , ui(new Ui::Pogoda5Day)
{
    ui->setupUi(this);

    int idf = QFontDatabase::addApplicationFont(":/font/fonts/weathericons-regular-webfont.ttf");
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

    //setupUi(this);
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
    return QRect(0,450,1080,200);
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
    qDebug() << "REPLY:" << reply->request().url().toDisplayString();
    qDebug() << bytes;
    QJsonDocument doc = QJsonDocument::fromJson(bytes);
    if (doc.isNull() || doc.isEmpty()) {
        return;
    }

    m_weatherData.clear();

    int cnt = doc.toVariant().toMap()["cnt"].toInt();
    qDebug() << "CNT" << cnt;
    //QJsonObject jsonObject = doc.toObject();
    QVariantList jsonList = doc.toVariant().toMap()["list"].toList();
    //

    long long lsecs = -1;
    float minTemp = 100;
    float maxTemp = -100;
    for (auto & item : jsonList) 
    {
        neededData nd;
        auto mapItem = item.toMap();
        QString dt_txt = mapItem["dt_txt"].toString();
        auto date_time = dt_txt.split(" ");
        auto dateItems = date_time[0].split("-");
        auto timeItems = date_time[1].split(":");
        QDate dt(dateItems[0].toInt(), dateItems[1].toInt(), dateItems[2].toInt());

        auto secsItem = mapItem["dt"].toLongLong();

        nd.day_month = dt.day();
        nd.nameDay = days[dt.dayOfWeek()];
        nd.time = timeItems[0] + ":" + timeItems[1];
        nd.hour = timeItems[0].toInt();
        if (lsecs < 0) {
            lsecs = secsItem;
            nd.secs = 0;
        } else {
            nd.secs = secsItem - lsecs;
        }


        auto mapWeather = mapItem["weather"].toList()[0].toMap();
        nd.descWeather = mapWeather["description"].toString();
        nd.iconWeather = mapWeather["icon"].toString();

        nd.descWeather = mapWeather["description"].toString();
        nd.iconWeather = mapWeather["icon"].toString();

        auto mapMain = mapItem["main"].toMap();
        nd.temp = mapMain["temp"].toFloat();
        nd.feels_like = mapMain["feels_like"].toFloat();
        if (nd.temp > maxTemp)
            maxTemp = nd.temp;

        if (nd.temp < minTemp)
            minTemp = nd.temp;
            
        nd.pressure = mapMain["pressure"].toInt();
        nd.humidity = mapMain["humidity"].toInt();

        auto rain = mapItem["rain"];
        float rainMM = 0.0;

        if (rain.isNull()) {
            auto rainM = rain.toMap();
            rainMM = rainM["1h"].toFloat();
        }
        nd.rain = rainMM;

        auto snow = mapItem["rain"];
        float snowMM = 0.0;

        if (snow.isNull()) {
            auto snowM = snow.toMap();
            snowMM = snowM["1h"].toFloat();
        }
        nd.snow = snowMM;

        m_weatherData.append(nd);
    }

    int day_nr = 0;
    QString day_name = "";
    PogodaDay * days[] = { ui->day1, ui->day2, ui->day3 /*, ui->day4, ui->day5, ui->day6*/ };
    PogodaDay * day = ui->day1;

    for (auto & i : m_weatherData) {
        if (day_name != i.nameDay) {
            if (day_name=="")
                ui->day1->ui->day->setText(QString("%1, %2").arg(i.nameDay).arg(i.day_month));
            day_name = i.nameDay;
            ++day_nr;
            if (day_nr == 4)
                return;
            day = days[day_nr-1];
            day->ui->day->setText(QString("%1, %2").arg(i.nameDay).arg(i.day_month));
        }
        createDay(day, i);
    }
   
}

void Pogoda5Day::createDay(PogodaDay * day, neededData & data)
{
    QLabel * temp;
    QLabel * press;
    QLabel * cond;
    QLabel * rain;
    switch(data.hour) {
    case 0:
    {
        temp = day->ui->temp_00;
        press = day->ui->pres_00;
        cond = day->ui->wet_00;
        rain = day->ui->rain_00;
        break;
    }
    case 3:
    {
        temp = day->ui->temp_03;
        press = day->ui->pres_03;
        cond = day->ui->wet_03;
        rain = day->ui->rain_03;
        break;
    }
    case 6:
    {
        temp = day->ui->temp_06;
        press = day->ui->pres_06;
        cond = day->ui->wet_06;
        rain = day->ui->rain_06;
        break;
    }
    case 9:
    {
        temp = day->ui->temp_09;
        press = day->ui->pres_09;
        cond = day->ui->wet_09;
        rain = day->ui->rain_09;
        break;
    }
    case 12:
    {
        temp = day->ui->temp_12;
        press = day->ui->pres_12;
        cond = day->ui->wet_12;
        rain = day->ui->rain_12;
        break;
    }
    case 15:
    {
        temp = day->ui->temp_15;
        press = day->ui->pres_15;
        cond = day->ui->wet_15;
        rain = day->ui->rain_15;
        break;
    }
    case 18:
    {
        temp = day->ui->temp_18;
        press = day->ui->pres_18;
        cond = day->ui->wet_18;
        rain = day->ui->rain_18;
        break;
    }
    case 21:
    {
        temp = day->ui->temp_21;
        press = day->ui->pres_21;
        cond = day->ui->wet_21;
        rain = day->ui->rain_21;
        break;
    }
    default:
        return;
    }

    temp->setText(QString::fromUtf8("%1\u00B0 (%2\u00B0)").arg(data.temp, 0, 'f', 1).arg(data.feels_like, 0, 'f', 1));
    press->setText(QString("%1 hPa").arg(data.pressure));
    cond->setText(QString("%1 %").arg(data.humidity));
    rain->setText(QString("%1/%2 mm").arg(data.rain, 0, 'f', 1).arg(data.snow, 0, 'f', 1));
}


