#ifndef POGODA_H
#define POGODA_H

#include <QWidget>
#include "blackwidget.h"
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>


//https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units-metric

namespace Ui {
class Pogoda;
}

class Pogoda : public BlackWidget
{
    Q_OBJECT

public:
    explicit Pogoda(QWidget *parent = 0);
    ~Pogoda();

    QRect getRect();
    virtual void update(int, int, int, int, int, int, int);

signals:
    void setSunrise(int h, int m);
    void setSunset(int h, int m);
    
private slots:
    void parseMessage(QNetworkReply *reply);
private:
    Ui::Pogoda *ui;
    int m_h;
    QNetworkAccessManager netMng;
    QNetworkRequest request;
};

#endif // POGODA_H
