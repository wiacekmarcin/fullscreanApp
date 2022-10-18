#ifndef INFORMACJE_H
#define INFORMACJE_H

#include "blackwidget.h"
#include <QWidget>

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

private:
    Ui::Informacje *ui;
};

#endif // INFORMACJE_H
