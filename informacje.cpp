#include "informacje.h"
#include "ui_informacje.h"
#include <QFont>
#include <QFontDatabase>

Informacje::Informacje(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Informacje)
{
    ui->setupUi(this);

    int id = QFontDatabase::addApplicationFont(":/font/fonts/roboto-condensed/Roboto-Condensed-Light.ttf");
    QString family = QFontDatabase::applicationFontFamilies(id).at(0);
    QFont font1(family);
    QFont font2(family);
    font1.setPixelSize(20);
    font1.setWeight(300);
    font2.setPixelSize(30);
    font2.setWeight(300);

    ui->gazeta->setFont(font1);
    ui->gazeta->setStyleSheet("QLabel { color : #666; }");
    ui->gazeta->setText("TVN24 Najnowsze, 7 godzin temu");

    ui->title->setFont(font2);
    ui->title->setStyleSheet("QLabel { color : #fff; }");
    ui->title->setText(QString::fromUtf8("Gwałt jako 'strategia wojskowa'. Kobiety zeznają o rosyjskich żołnierzach wyposażonych w viagrę"));

    ui->description->setFont(font1);
    ui->description->setStyleSheet("QLabel { color : #aaa; }");
    ui->description->setText(QString::fromUtf8("O Możliwości zablokowania unijnych środków dla Polski z Funduszu Spójności rozmawiali goście Kropki nad i. Według posła Pawła Kowala (KO) niedługo naprawdę Polacy będą w domach klepać biedę, a rząd nie będzie robił nic w sprawie, która do niego należy. Jak mówił poseł Krzysztof Śmiszek (Lewica), działania polskich władz to jest pierwszy krok do wyprowadzania Polski z Unii Europejs..."));
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
