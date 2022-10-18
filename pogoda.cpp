#include "pogoda.h"
#include "ui_pogoda.h"

Pogoda::Pogoda(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Pogoda)
{
    ui->setupUi(this);
}

Pogoda::~Pogoda()
{
    delete ui;
}
