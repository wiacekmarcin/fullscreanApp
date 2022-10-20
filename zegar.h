#ifndef ZEGAR_H
#define ZEGAR_H

#include <QWidget>
#include <QTimer>
#include "blackwidget.h"
class QLabel;

constexpr char dateStyle[] = "font-size:30px;line-height:35px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";
constexpr char timeStyle[] = "font-size:65px;line-height:65px;color:#fff;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
constexpr char secsStyle[] = "font-size:50%;line-height:50%;color:#666;vertical-align:super;text-align:left;background:#000;font-family:\"Roboto Condensed\",sans-serif;font-weight:300;";
constexpr char minStyle[]  = "font-size:24px;line-height:25px;color:#999;text-align:left;background:#000;font-family:\"Ariel\",sans-serif;font-weight:400;";

class Zegar : public BlackWidget
{
    Q_OBJECT

public:
    explicit Zegar(QWidget *parent = nullptr);
    ~Zegar();

    virtual void timeout(const QDateTime &);
    QRect getRect();

public slots:
    void setWschod(int h, int m);
    void setZachod(int h, int m);

private:
    QLabel *ldate;
    QLabel *ltime;
    QLabel *wschod;
    QLabel *zachod;
    void setupUi(QWidget *Zegar);
    QString days[8];
    QString monts[13];
};

#endif // ZEGAR_H
