#ifndef POGODA_H
#define POGODA_H

#include <QWidget>
#include "blackwidget.h"
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
private:
    Ui::Pogoda *ui;
};

#endif // POGODA_H
