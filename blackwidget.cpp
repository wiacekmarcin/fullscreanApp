#include "blackwidget.h"
#include "ui_blackwidget.h"

BlackWidget::BlackWidget(QWidget *parent) :
    QWidget(parent)
{
    QPalette pal = palette();
    pal.setColor(QPalette::Background, Qt::black);
    pal.setColor(QPalette::Window, Qt::black);

    pal.setColor(QPalette::WindowText, Qt::white);
    pal.setColor(QPalette::Text, Qt::white);
    pal.setColor(QPalette::BrightText, Qt::white);

    setAutoFillBackground(true);
    setPalette(pal);

}

BlackWidget::~BlackWidget()
{

}
