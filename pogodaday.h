#ifndef POGODADAY_H
#define POGODADAY_H

#include <QWidget>

namespace Ui {
class PogodaDay;
}

class PogodaDay : public QWidget
{
    Q_OBJECT

public:
    explicit PogodaDay(QWidget *parent = nullptr);
    ~PogodaDay();

    Ui::PogodaDay *ui;
};

#endif // POGODADAY_H
