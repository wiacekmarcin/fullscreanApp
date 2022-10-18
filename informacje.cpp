#include "informacje.h"
#include "ui_informacje.h"

Informacje::Informacje(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Informacje)
{
    ui->setupUi(this);
}

void Informacje::update(int, int, int, int, int, int, int)
{

}

QRect Informacje::getRect()
{
    return QRect(0, 600, width(), height());
}

Informacje::~Informacje()
{
    delete ui;
}
