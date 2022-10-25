#-------------------------------------------------
#
# Project created by QtCreator 2020-01-27T12:53:53
#
#-------------------------------------------------

QT       += core gui network xml

LIBS += -lqrencode

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
lessThan(QT_MAJOR_VERSION, 5): include($$PWD/qjson4/QJson4.pri)
lessThan(QT_MAJOR_VERSION, 5): INCLUDEPATH += qjson4

TARGET = FullScreanApp
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        mainwindow.cpp \
    blackwidget.cpp \
    qrwidget.cpp \
    rssitem.cpp \
    zegar.cpp \
    analogclock.cpp \
    ip.cpp \
    pogoda.cpp \
    pogoda5day.cpp \
    informacje.cpp

HEADERS += \
        mainwindow.h \
    blackwidget.h \
    qrwidget.h \
    rssitem.h \
    zegar.h \
    analogclock.h \
    ip.h \
    pogoda.h \
    pogoda5day.h \
    informacje.h

FORMS += \
    ip.ui \
    informacje.ui

RESOURCES += \
    ikony.qrc

