/********************************************************************************
** Form generated from reading UI file 'zegar.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ZEGAR_H
#define UI_ZEGAR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Zegar
{
public:
    QLabel *ldate;
    QLabel *ltime;
    QLabel *lsec;
    QLabel *label;
    QLabel *label_2;
    QLabel *wschod;
    QLabel *zachod;


        
        sizePolicy.setHeightForWidth(ldate->sizePolicy().hasHeightForWidth());
        ldate->setSizePolicy(sizePolicy);
        QFont font;
        font.setFamily(QString::fromUtf8("Serif"));
        font.setPointSize(28);
        ldate->setFont(font);
        
        QFont font1;
        font1.setFamily(QString::fromUtf8("Sans Serif"));
        font1.setPointSize(72);
        font1.setBold(true);
        font1.setWeight(75);
        ltime->setFont(font1);
        ltime->setIndent(0);
        lsec = new QLabel(Zegar);
        lsec->setObjectName(QString::fromUtf8("lsec"));
        lsec->setGeometry(QRect(320, 60, 81, 51));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Sans Serif"));
        font2.setPointSize(36);
        lsec->setFont(font2);
        label = new QLabel(Zegar);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 150, 48, 48));
        label->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/sun.png")));
        label->setScaledContents(true);
        label_2 = new QLabel(Zegar);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(190, 150, 48, 48));
        label_2->setPixmap(QPixmap(QString::fromUtf8(":/new/prefix1/moon.png")));
        label_2->setScaledContents(true);
        wschod = new QLabel(Zegar);
        wschod->setObjectName(QString::fromUtf8("wschod"));
        wschod->setGeometry(QRect(60, 160, 100, 32));
        QFont font3;
        font3.setFamily(QString::fromUtf8("Serif"));
        font3.setPointSize(18);
        wschod->setFont(font3);
        zachod = new QLabel(Zegar);
        zachod->setObjectName(QString::fromUtf8("zachod"));
        zachod->setGeometry(QRect(240, 160, 100, 32));
        zachod->setFont(font3);

        retranslateUi(Zegar);

        QMetaObject::connectSlotsByName(Zegar);
    } // setupUi

    void retranslateUi(QWidget *Zegar)
    {
        Zegar->setWindowTitle(QCoreApplication::translate("Zegar", "Form", nullptr));
        ltime->setText(QCoreApplication::translate("Zegar", "88:88", nullptr));
        lsec->setText(QCoreApplication::translate("Zegar", "00", nullptr));
        label->setText(QString());
        label_2->setText(QString());
        wschod->setText(QCoreApplication::translate("Zegar", "--", nullptr));
        zachod->setText(QCoreApplication::translate("Zegar", "--", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Zegar: public Ui_Zegar {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ZEGAR_H
