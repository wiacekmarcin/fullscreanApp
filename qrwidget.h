#ifndef QRWIDGET_HPP
#define QRWIDGET_HPP

#include <QWidget>
#include "blackwidget.h"
class QRWidget : public BlackWidget
{
    Q_OBJECT
private:
    QString data;
public:
    explicit QRWidget(QWidget *parent = 0);
    void setQRData(const QString & data);

protected:
    void paintEvent(QPaintEvent *event) override;
};

#endif // QRWIDGET_HPP
