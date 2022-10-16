#include "zegar.h"
#include "ui_zegar.h"
#include <QTimer>
#include <QDateTime>

Zegar::Zegar(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Zegar),
    timer(this)
{
    ui->setupUi(this);
    connect(&timer, &QTimer::timeout, this, &Zegar::update);
    timer.setInterval(1000);
    timer.start();
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

void Zegar::update()
{
    QDate d = QDate::currentDate();
    QTime t = QTime::currentTime();
    QString days[] = {"", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"};
    QString dayname = days[d.dayOfWeek()];
    QString monts[] = {"", "styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"};
    QString monthname = monts[d.month()];
    ui->ldate->setText(d.toString("%1, %2 %3 %4").arg(dayname).arg(d.day()).arg(monthname).arg(d.year()));
    ui->ltime->setText(t.toString("HH:mm"));
    QString ms = QString::number(t.second());
    if (t.second() < 10)
        ms = "0" + ms;
    ui->lsec->setText(ms);
}
