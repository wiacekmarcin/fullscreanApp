#ifndef POGODA_H
#define POGODA_H

#include <QWidget>
#include "blackwidget.h"
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QTime>
#include <QFont>
#include <QLabel>

//https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units-metric

constexpr char citiStyle[] = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";
constexpr char windBStyle[] = "font-size:45px;line-height:45px;color:#aaa;text-align:left;background:#000;font-weight:400;";
constexpr char windDStyle[] = "font-size:25px;line-height:30px;color:#999;text-align:left;background:#000;font-weight:500;";
constexpr char windSStyle[] = "font-size:16px;line-height:18px;color:#666;text-align:left;background:#000;font-weight:300;";
constexpr char iconWiStyle[] = "font-size:65px;line-height:65px;color:#aaa;text-align:right;background:#000;font-weight:400;";
constexpr char feelTempStyle[] = "font-size:30px;line-height:35px;color:#999;text-align:right;background:#000;font-weight:800;";
constexpr char conditionalStyle[] = "font-size:22px;line-height:20px;color:#ccc;text-align:right;background:#000;font-weight:600;";


class Pogoda : public BlackWidget
{
    Q_OBJECT

public:
    explicit Pogoda(QWidget *parent = 0);
    ~Pogoda();

    QRect getRect();
    virtual void timeout(const QDateTime &);

signals:
    void setSunrise(int h, int m);
    void setSunset(int h, int m);
    
    
protected:
    void setCitiLabel();
    int ms2Beaufort(const float &ms);
    QString deg2Cardinal(const float &deg);
    QString toBeaufortChar(int b);
    QString toDescrSilaWiatru(const float & ms);
    bool isDayTime();
private slots:
    void parseMessage(QNetworkReply *reply);

private:
    QString getTimeRemaing(int h, int m);
    void setupUi(QWidget *Pogoda);

    int m_h;
    int m_m;
    QNetworkAccessManager netMng;
    QNetworkRequest request;
    QTime sunrise;
    QTime sunset;

    QLabel *windB;
    QLabel *windD;
    QLabel *windS;
    QLabel *wIcon;
    QLabel *wTemp;
    QLabel *wTempMin;
    QLabel *wTempMax;
    QLabel *citydate;
    QLabel *feelTemp;
    QLabel *maxTemp;
    QLabel *minTemp;
    QLabel *wCond;
    QLabel *humiTemp;
    QLabel *presTemp;

    QString citiname;
    int pog_h;
    int pog_m;

    QFont weatherFont;
    QFont windDescr;
    QFont tempFont;
    QFont warunkiFont;

    QMap<QString, QString> iconMap;
};

#endif // POGODA_H

