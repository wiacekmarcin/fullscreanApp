#ifndef IP_H
#define IP_H

#include <QWidget>
#include "blackwidget.h"
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>

namespace Ui {
class IP;
}

class IP : public BlackWidget
{
    Q_OBJECT

public:
    explicit IP(QWidget *parent = 0);
    ~IP();
    virtual void update(int year, int month, int day, int dayweek, int hour, int min, int sec);
    QRect getRect();
    
private slots:
    void parseMessage(QNetworkReply *reply);
private:
    Ui::IP *ui;
    int m;
    QNetworkAccessManager netMng;
    QNetworkRequest request;

};

#endif // IP_H
