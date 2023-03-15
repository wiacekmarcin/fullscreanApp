#include "pogodaday.h"
#include "ui_pogodaday.h"

PogodaDay::PogodaDay(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::PogodaDay)
{
    ui->setupUi(this);
}

PogodaDay::~PogodaDay()
{
    delete ui;
}
