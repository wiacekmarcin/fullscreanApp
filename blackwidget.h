#ifndef BLACKWIDGET_H
#define BLACKWIDGET_H

#include <QWidget>


class BlackWidget : public QWidget
{
    Q_OBJECT

public:
    explicit BlackWidget(QWidget *parent = 0);
    ~BlackWidget();
    virtual void update(int , int , int , int , int , int , int ) { }
    QRect getRect() { return QRect(0,0,0,0); }
private:

};

#endif // BLACKWIDGET_H
