#ifndef ZEGAR_H
#define ZEGAR_H

#include <QWidget>
#include <QTimer>
#include "blackwidget.h"
namespace Ui {
    class Zegar;
}

class Zegar : public BlackWidget
{
    Q_OBJECT

public:
    explicit Zegar(QWidget *parent = nullptr);
    void setWschod(int h, int m);
    void setZachod(int h, int m);
    ~Zegar();

    virtual void update(int year, int month, int day, int dayweek, int hour, int min, int sec);
    QRect getRect();

private:
    Ui::Zegar *ui;
};

#endif // ZEGAR_H
