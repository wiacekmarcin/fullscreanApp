/********************************************************************************
** Form generated from reading UI file 'pogoda.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_POGODA_H
#define UI_POGODA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Pogoda
{
public:
    QLabel *wind;
    QLabel *citydate;
    QFrame *line;

    void setupUi(QWidget *Pogoda)
    {
        if (Pogoda->objectName().isEmpty())
            Pogoda->setObjectName(QString::fromUtf8("Pogoda"));
        Pogoda->resize(400, 300);
        wind = new QLabel(Pogoda);
        wind->setObjectName(QString::fromUtf8("wind"));
        wind->setGeometry(QRect(50, 150, 58, 18));
        citydate = new QLabel(Pogoda);
        citydate->setObjectName(QString::fromUtf8("citydate"));
        citydate->setGeometry(QRect(0, 0, 250, 40));
        line = new QFrame(Pogoda);
        line->setObjectName(QString::fromUtf8("line"));
        line->setGeometry(QRect(0, 42, 250, 16));
        line->setStyleSheet(QString::fromUtf8("color:rgb(145, 148, 148); size:5pt\n"
""));
        line->setLineWidth(2);
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        retranslateUi(Pogoda);

        QMetaObject::connectSlotsByName(Pogoda);
    } // setupUi

    void retranslateUi(QWidget *Pogoda)
    {
        Pogoda->setWindowTitle(QCoreApplication::translate("Pogoda", "Form", nullptr));
        wind->setText(QCoreApplication::translate("Pogoda", "TextLabel", nullptr));
        citydate->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Pogoda: public Ui_Pogoda {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_POGODA_H
