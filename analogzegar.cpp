#include "analogzegar.h"
#include "ui_analogzegar.h"

AnalogZegar::AnalogZegar(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::AnalogZegar)
{
    ui->setupUi(this);
}

AnalogZegar::~AnalogZegar()
{
    delete ui;
}
