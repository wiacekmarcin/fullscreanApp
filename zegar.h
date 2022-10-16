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
    ~Zegar();
private slots:
    void update();

private:
    Ui::Zegar *ui;
    QTimer timer;
};

#endif // ZEGAR_H
