#include "zegar.h"
#include <QTimer>
#include <QDateTime>
#include <QVariant>
#include <QLabel>
#include <QWidget>
#include <QFontDatabase>
#include <QDebug>
#include <QFont>

Zegar::Zegar(QWidget *parent) :
    BlackWidget(parent),
    days{"", QString::fromUtf8("Poniedziałek"),
                      QString::fromUtf8("Wtorek"),
                      QString::fromUtf8("Środa"),
                      QString::fromUtf8("Czwartek"),
                      QString::fromUtf8("Piątek"),
                      QString::fromUtf8("Sobota"),
                      QString::fromUtf8("Niedziela")},
    monts{"", QString::fromUtf8("styczeń"),
                   QString::fromUtf8("luty"),
                   QString::fromUtf8("marzec"),
                   QString::fromUtf8("kwiecień"),
                   QString::fromUtf8("maj"),
                   QString::fromUtf8("czerwiec"),
                   QString::fromUtf8("lipiec"),
                   QString::fromUtf8("sierpień"),
                   QString::fromUtf8("wrzesień"),
                   QString::fromUtf8("październik"),
                   QString::fromUtf8("listopad"),
                   QString::fromUtf8("grudzień")}
{
    //int idf = QFontDatabase::addApplicationFont("weathericons-regular-webfont.ttf");
    //QString family = QFontDatabase::applicationFontFamilies(idf).at(0);
    //qDebug() << "font:Zegar" << family;
    weatherFont = QFont("Weather Icons");
    //weatherFont.setPointSize(32);
    setupUi(this);


}

void Zegar::setWschod(int h, int m)
{
    QString ms = QString::number(m);
    if (m < 10)
        ms = "0"+ms;
    QString hs = QString::number(h);
    wschod->setText(QString("%1:%2").arg(hs,ms));
}

void Zegar::setZachod(int h, int m)
{
    QString ms = QString::number(m);
    if (m < 10)
        ms = "0"+ms;
    QString hs = QString::number(h);
    zachod->setText(QString("%1:%2").arg(hs,ms));
}

Zegar::~Zegar()
{
    delete ldate;
    delete ltime;
    delete wschod;
    delete zachod;
}

void Zegar::timeout(const QDateTime &dt)
{

    QString monthname = monts[dt.date().month()];
    QString dayname = days[dt.date().dayOfWeek()];

    ldate->setText(QString("%1, %2 %3 %4").arg(dayname).arg(dt.date().day()).arg(monthname).arg(dt.date().year()));

    int hour = dt.time().hour();
    int min = dt.time().minute();
    int sec = dt.time().second();
    QString hs = QString::number(hour);
    if (hour < 10)
        hs = " " + hs;
    QString ms = QString::number(min);
    if (min < 10)
        ms = "0" + ms;


    QString ss = QString::number(sec);
    if (sec < 10)
        ss = "0" + ss;
    ltime->setText(QString("<span>%1:%2 <sup style=\"%3\">%4</sup><span>").arg(hs, ms, QString(secsStyle), ss));
}

QRect Zegar::getRect()
{
    return QRect(0, 0, 680, 180);
}


void Zegar::setupUi(QWidget *Zegar)
{
    if (Zegar->objectName().isEmpty())
        Zegar->setObjectName(QString::fromUtf8("Zegar"));
    Zegar->resize(getRect().width(), getRect().height());
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    Zegar->setSizePolicy(sizePolicy);
    Zegar->setAutoFillBackground(false);
    Zegar->setStyleSheet(QString::fromUtf8("background-color:rgb(0,0,0);color:rgb(255,255,255);"));
    ldate = new QLabel(Zegar);
    ldate->setObjectName(QString::fromUtf8("ldate"));
    ldate->setGeometry(QRect(0, 0, 680, 50));
    ldate->setStyleSheet(dateStyle);
    ltime = new QLabel(Zegar);
    ltime->setObjectName(QString::fromUtf8("ltime"));
    ltime->setGeometry(QRect(0, 60, 311, 81));
    ltime->setTextFormat(Qt::RichText);
    ltime->setStyleSheet(timeStyle);
    QLabel * label = new QLabel(Zegar);
    label->setObjectName(QString::fromUtf8("label"));
    label->setGeometry(QRect(220, 60, 32, 32));
    //label->setText(QString("\uf051"));
    label->setText(QString("\uf06e"));
    label->setStyleSheet(iconStyle);
    label->setFont(weatherFont);
    //label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/sun.png")));
    //label->setScaledContents(true);
    QLabel * label_2 = new QLabel(Zegar);
    label_2->setObjectName(QString::fromUtf8("label_2"));
    label_2->setGeometry(QRect(225, 100, 32, 32));
    //label_2->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/moon.png")));
    //label_2->setScaledContents(true);
    //label_2->setText(QString("\uf052"));
    label_2->setText(QString("\uf070"));
    label_2->setStyleSheet(iconStyle);
    label_2->setFont(weatherFont);
    wschod = new QLabel(Zegar);
    wschod->setObjectName(QString::fromUtf8("wschod"));
    wschod->setGeometry(QRect(250, 60, 80, 32));
    wschod->setStyleSheet(minStyle);
    zachod = new QLabel(Zegar);
    zachod->setObjectName(QString::fromUtf8("zachod"));
    zachod->setGeometry(QRect(250, 100, 80, 32));
    zachod->setStyleSheet(minStyle);
}


