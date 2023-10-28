#ifndef INFORMACJE_H
#define INFORMACJE_H

#include "blackwidget.h"
#include <QWidget>
#include "rssitem.h"

#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QMutex>
#include <QTimer>
#include <QDateTime>

namespace Ui {
class Informacje;
}

class Informacje : public BlackWidget
{
    Q_OBJECT

public:
    explicit Informacje(QWidget *parent = 0);
    virtual void timeout(const QDateTime &);
    QRect getRect();
    ~Informacje();

    void wyczysc();
    void dodajInfo(const QString &guid, const QString &publisher, const QString & title, const QString & description, const QString &pubData, const QString &img, const QString &url);
    void pobierz();
    bool isInfo(const QString &guid);
private slots:    
    void parseMessage(QNetworkReply *reply);
    void timeout();
    QDateTime parseDate(const QString &dt);
private:
    Ui::Informacje *ui;
    RssList newsy;
    QNetworkAccessManager netMng; 
    QMutex mutex;
    int m_h1;
    int m_h2;
    bool inprogress;
    bool done;
    int m_requestSize;
    QStringList addresses;
    QTimer timer;
};

#endif // INFORMACJE_H
