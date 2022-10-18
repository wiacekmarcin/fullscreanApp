#include "analogclock.h"
#include <QPoint>

#include <QTimer>
#include <QTime>
#include <QPainter>

#include <QDebug>

AnalogClock::AnalogClock(QWidget * parent): BlackWidget(parent), setWschodZachod(0x00)
{
    setWindowTitle(tr("Analog Clock"));
    resize(500, 500);
}

QRect AnalogClock::getRect()
{
    return QRect(580, 0, width(), height());
}

void AnalogClock::setWschod(int hour, int min)
{
    startArcWschod = 16.0*360.0*(60.0*hour + min)/(12.0*60.0);
    startArcWschod = (720 - 60.0*hour + min) * 8;
    //qDebug() << s << int(16*360*s);


    setWschodZachod |= 0x01;
   // qDebug() << startArcWschod << 16*360;
}

void AnalogClock::setZachod(int hour, int min)
{
    startArcZachod = 8*(60*(hour - 12) + min);
    setWschodZachod |= 0x02;
    //qDebug() << startArcZachod;
}

void AnalogClock::update(int, int, int, int, int hour, int min, int sec)
{
    m_h = hour;
    m_m = min;
    m_s = sec;
    repaint();
}

void AnalogClock::paintEvent(QPaintEvent *event)
{
    //qDebug("paintEvent");


    static const QPoint hourHand[3] = {
        QPoint(14, 16),
        QPoint(-14, 16),
        QPoint(0, -150)
    };
    static const QPoint minuteHand[3] = {
        QPoint(14, 16),
        QPoint(-14, 16),
        QPoint(0, -200)
    };

    static const QPoint secondHand[3] = {
        QPoint(8, 8),
        QPoint(-8, 8),
        QPoint(0, -200)
    };

    QColor hourColor(225, 225, 225);
    QColor minuteColor(255, 255, 255, 191);
    QColor secondColor(200, 200, 200, 90);
    QColor color(120, 255, 100);

    int side = qMin(width(), height());

    QPainter painter(this);
    //painter.drawPixmap(QPoint(0,0),QPixmap(QString::fromUtf8(":/new/prefix1/analog")));


    painter.setRenderHint(QPainter::Antialiasing);
    painter.translate(width() / 2, height() / 2);
    painter.scale(side / 500.0, side / 500.0);

    painter.setPen(Qt::NoPen);
    painter.setBrush(hourColor);


    painter.save();
    painter.rotate(30.0 * ((m_h + m_m / 60.0)));
    painter.drawConvexPolygon(hourHand, 3);
    painter.restore();

    painter.setPen(hourColor);
    QPen p = painter.pen();
    p.setWidth(5);
    painter.setPen(p);

    for (int i = 0; i < 12; ++i) {
       painter.drawLine(176, 0, 192, 0);
       painter.rotate(30.0);
    }

    painter.setPen(Qt::NoPen);
    painter.setBrush(minuteColor);

    painter.save();
    painter.rotate(6.0 * (m_m + m_s / 60.0));
    painter.drawConvexPolygon(minuteHand, 3);
    painter.restore();

    painter.setPen(minuteColor);

    for (int j = 0; j < 60; ++j) {
        if ((j % 5) != 0)
            painter.drawLine(184, 0, 192, 0);
        painter.rotate(6.0);
    }

    painter.setPen(Qt::NoPen);
    painter.setBrush(secondColor);

    painter.save();
    painter.rotate(360.0 * (1.0 * m_s / 60.0));
    painter.drawConvexPolygon(secondHand, 3);
    painter.restore();

    if (false && setWschodZachod == 0x03) {
        QPen pen(color);
        pen.setWidth(10);

        painter.setPen(pen);
        //painter.drawArc(-100,-100,200,200, startArcWschod, (6)*16*360);
        //painter.drawArc(-100,-100,200,200, startArcWschod - 4*360 , 16*360-startArcWschod );
        painter.drawArc(-100,-100,200,200, 1480, startArcWschod);
        painter.drawArc(-110,-110,220,220, 1400,  -(startArcZachod));
        //qDebug() << startArcWschod  <<  startArcWschod - 3.0/12.0*16*360;
        //painter.drawArc(-125,-125,250,250, (-3)*16*360, startArcWschod );
    }
}
