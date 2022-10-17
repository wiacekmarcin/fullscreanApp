#include "ip.h"
#include "ui_ip.h"

#include <QHostInfo>
#include <QNetworkInterface>
#include <QNetworkAddressEntry>
#include "QJsonDocument.h"

IP::IP(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::IP),
    request(QUrl("http://httpbin.org/ip"))
{
    ui->setupUi(this);
    m = -1;
    ui->wifi->setText("");
    ui->eth->setText("");
    ui->ip->setText("No internet");
    netMng = nullptr;
}

IP::~IP()
{
    delete ui;
}

QRect IP::getRect()
{
    return QRect(10, 580, width(), height());
}

void IP::setNetworkManager(QNetworkAccessManager *mnt)
{
    netMng = mnt;
    //connect(netMng, SIGNAL(finished()), this, SLOT(parseMessage()));
}

void IP::parseMessage()
{

}

void IP::update(int, int, int, int, int, int min, int)
{
    min = min/5;
    if (min == m)
        return;

    m = min;
    //QString eth = "enxb827eb0a4265";
    QString eth = "enp0s31f6";
    //QString wifi = "wlan0";
    QString wifi = "wlp1s0";

    foreach (const QNetworkInterface& networkInterface, QNetworkInterface::allInterfaces()) {
        qDebug() << "interface"<< networkInterface.humanReadableName();
        if (networkInterface.humanReadableName() == eth) {
            foreach (const QNetworkAddressEntry& entry, networkInterface.addressEntries()) {
                if (entry.ip().protocol() == QAbstractSocket::IPv4Protocol) {
                    ui->eth->setText(entry.ip().toString());
                }
            }
        }

        if (networkInterface.humanReadableName() == wifi) {
            foreach (const QNetworkAddressEntry& entry, networkInterface.addressEntries()) {
                if (entry.ip().protocol() == QAbstractSocket::IPv4Protocol) {
                    ui->wifi->setText(entry.ip().toString());
                }
            }
        }
    }
    if (netMng) {
        QNetworkReply* reply = netMng->get(request);
         // connect to signal  when its done using lambda)
        QObject::connect(reply, &QNetworkReply::finished, [reply, this]() {
            QJsonDocument doc = QJsonDocument::fromJson(reply->readAll());
            if (doc.isNull() || doc.isEmpty())
                ui->ip->setText("No internet");
            else {
                ui->ip->setText(doc.toVariant().toMap()["origin"].toString());
            }
        });
    }
}
/*
    QString localhostname =  QHostInfo::localHostName();
    QString localhostIP;
    QList<QHostAddress> hostList = QHostInfo::fromName(localhostname).addresses();
    foreach (const QHostAddress& address, hostList) {
        if (address.protocol() == QAbstractSocket::IPv4Protocol && address.isLoopback() == false) {
             localhostIP = address.toString();
        }
    }
    QString localMacAddress;
    QString localNetmask;
    foreach (const QNetworkInterface& networkInterface, QNetworkInterface::allInterfaces()) {
        qDebug() << "interface"<< networkInterface.humanReadableName();
        foreach (const QNetworkAddressEntry& entry, networkInterface.addressEntries()) {
            qDebug() << "ip"<< entry.ip().toString();
            if (entry.ip().toString() == localhostIP) {
                localMacAddress = networkInterface.hardwareAddress();
                localNetmask = entry.netmask().toString();
                break;
            }
        }
    }
    qDebug() << "Localhost name: " << localhostname;
    qDebug() << "IP = " << localhostIP;
    qDebug() << "MAC = " << localMacAddress;
    qDebug() << "Netmask = " << localNetmask;
*/
