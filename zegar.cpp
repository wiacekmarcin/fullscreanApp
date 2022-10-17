#include "zegar.h"
#include "ui_zegar.h"
#include <QTimer>
#include <QDateTime>

Zegar::Zegar(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Zegar)
{
    ui->setupUi(this);
}

void Zegar::setWschod(int h, int m)
{
    QString ms = QString::number(m);
    if (m < 10)
        ms = "0"+ms;
    QString hs = QString::number(h);
    ui->wschod->setText(QString("%1:%2").arg(hs,ms));
}

void Zegar::setZachod(int h, int m)
{
    QString ms = QString::number(m);
    if (m < 10)
        ms = "0"+ms;
    QString hs = QString::number(h);
    ui->zachod->setText(QString("%1:%2").arg(hs,ms));
}

Zegar::~Zegar()
{
    delete ui;
}

void Zegar::update(int year, int month, int day, int dayweek, int hour, int min, int sec)
{
    QString days[] = {"", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"};
    QString dayname = days[dayweek];
    QString monts[] = {"", "styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"};
    QString monthname = monts[month];
    ui->ldate->setText(QString("%1, %2 %3 %4").arg(dayname).arg(day).arg(monthname).arg(year));
    QString hs = QString::number(hour);
    if (hour < 10)
        hs = " " + hs;
    QString ms = QString::number(min);
    if (min < 10)
        ms = "0" + ms;

    ui->ltime->setText(QString("%1:%2").arg(hs, ms));
    QString ss = QString::number(sec);
    if (sec < 10)
        ss = "0" + ss;
    ui->lsec->setText(ss);
}
