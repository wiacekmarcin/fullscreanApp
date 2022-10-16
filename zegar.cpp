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
    ui->lsec->setText(QString("%1").arg(t.second()));
}
