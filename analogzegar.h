#ifndef ANALOGZEGAR_H
#define ANALOGZEGAR_H

#include <QWidget>

namespace Ui {
class AnalogZegar;
}

class AnalogZegar : public QWidget
{
    Q_OBJECT

public:
    explicit AnalogZegar(QWidget *parent = nullptr);
    ~AnalogZegar();

private:
    Ui::AnalogZegar *ui;
};

#endif // ANALOGZEGAR_H
