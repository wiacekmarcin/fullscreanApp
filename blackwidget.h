#ifndef BLACKWIDGET_H
#define BLACKWIDGET_H

#include <QWidget>

namespace Ui {
class BlackWidget;
}

class BlackWidget : public QWidget
{
    Q_OBJECT

public:
    explicit BlackWidget(QWidget *parent = 0);
    ~BlackWidget();

private:
    Ui::BlackWidget *ui;
};

#endif // BLACKWIDGET_H
