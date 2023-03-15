#ifndef POGODA5DAY_H
#define POGODA5DAY_H

#include <QWidget>
#include "blackwidget.h"
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QTime>
#include <QFont>
#include <QLabel>
#include <QRect>
#include <QVector>


//https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units-metric

//constexpr char citiStyle[] = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";
//constexpr char windBStyle[] = "font-size:45px;line-height:45px;color:#aaa;text-align:left;background:#000;font-weight:400;";
//constexpr char windDStyle[] = "font-size:25px;line-height:30px;color:#999;text-align:left;background:#000;font-weight:500;";
//constexpr char windSStyle[] = "font-size:16px;line-height:18px;color:#666;text-align:left;background:#000;font-weight:300;";
//constexpr char iconWiStyle[] = "font-size:65px;line-height:65px;color:#aaa;text-align:right;background:#000;font-weight:400;";
//constexpr char feelTempStyle[] = "font-size:30px;line-height:35px;color:#999;text-align:right;background:#000;font-weight:400;";
//constexpr char conditionalStyle[] = "font-size:22px;line-height:20px;color:#ccc;text-align:right;background:#000;font-weight:600;";


struct neededData {
    int day_month;
    QString time;
    int hour;
    QString nameDay;
    QString descWeather;
    QString iconWeather;
    float temp;
    float feels_like;
    int pressure;
    int humidity;
    int secs;
    float rain;
    float snow;
};

namespace Ui {
class Pogoda5Day;
}

class PogodaDay;

class Pogoda5Day : public BlackWidget
{
    Q_OBJECT

public:
    explicit Pogoda5Day(QWidget *parent = 0);
    ~Pogoda5Day();

    QRect getRect();
    virtual void timeout(const QDateTime &);

 
    
protected:

    int ms2Beaufort(const float &ms);
    QString deg2Cardinal(const float &deg);
    QString toBeaufortChar(int b);
    
    void createDay(PogodaDay *day, neededData &data);
private slots:
    void parseMessage(QNetworkReply *reply);

private:
    void setupUi(QWidget *Pogoda);

    int m_h;
    int m_m;
    QNetworkAccessManager netMng;
    QNetworkRequest request;
    

    int pog_h;
    int pog_m;

    QFont weatherFont;
    QFont windDescr;
    QFont tempFont;

    QMap<QString, QString> iconMap;
    QString days[8];
    QVector<neededData> m_weatherData;
private:
    Ui::Pogoda5Day *ui;
};

#endif // POGODA5DAY_H

