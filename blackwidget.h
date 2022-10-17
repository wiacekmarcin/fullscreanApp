#ifndef BLACKWIDGET_H
#define BLACKWIDGET_H

#include <QWidget>


class BlackWidget : public QWidget
{
    Q_OBJECT

public:
    explicit BlackWidget(QWidget *parent = 0);
    ~BlackWidget();
    virtual void update(int year, int month, int day, int dayweek, int hour, int min, int sec) { }

private:

};

#endif // BLACKWIDGET_H
