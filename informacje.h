#ifndef INFORMACJE_H
#define INFORMACJE_H

#include "blackwidget.h"
#include <QWidget>
#include "rssitem.h"

#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QMutex>

namespace Ui {
class Informacje;
}

class Informacje : public BlackWidget
{
    Q_OBJECT

public:
    explicit Informacje(QWidget *parent = 0);
    virtual void update(int , int , int , int , int , int , int );
    QRect getRect();
    ~Informacje();

    void wyczysc();
    void dodajInfo(const QString &guid, const QString & title, const QString & description, const QDateTime &pubData);
    void pobierz();
    bool isInfo(const QString &guid);
private slots:    
    void parseMessage(QNetworkReply *reply);

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
};

#endif // INFORMACJE_H
