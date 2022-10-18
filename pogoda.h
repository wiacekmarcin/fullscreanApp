#ifndef POGODA_H
#define POGODA_H

#include <QWidget>

//https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units-metric

namespace Ui {
class Pogoda;
}

class Pogoda : public QWidget
{
    Q_OBJECT

public:
    explicit Pogoda(QWidget *parent = 0);
    ~Pogoda();

private:
    Ui::Pogoda *ui;
};

#endif // POGODA_H
