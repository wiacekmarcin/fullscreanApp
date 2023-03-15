#ifndef ANALOGCLOCK_H
#define ANALOGCLOCK_H

#include "blackwidget.h"
#include <QWidget>

class AnalogClock : public BlackWidget
{
public:
    AnalogClock(QWidget *parent);

    void setWschod(int hour, int min);
    void setZachod(int hour, int min);
    virtual void timeout(const QDateTime &) override;
    QRect getRect();
protected:
    void paintEvent(QPaintEvent *event) override;
private:
    unsigned int setWschodZachod;
    int startArcWschod;
    int startArcZachod;
    int m_h;
    int m_m;
    int m_s;
};

#endif // ANALOGCLOCK_H
