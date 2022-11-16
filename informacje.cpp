#include "informacje.h"
#include "ui_informacje.h"
#include <QFont>
#include <QFontDatabase>
#include <QMutexLocker>
#include <QDomDocument>
#include <QDebug>
Informacje::Informacje(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Informacje),
    timer(this)
{
    ui->setupUi(this);
    m_h1 = -1;
    m_h2 = -1;

    inprogress = false;
    done = false;

    //int id = QFontDatabase::addApplicationFont(":/font/fonts/robotic/Roboto-Medium.ttf");
    //QString family = QFontDatabase::applicationFontFamilies(id).at(0);
    //qDebug() << "font:informacje" << family;
    QFont font1("RobotoMedium");
    QFont font2("RobotoMedium");
    font1.setPixelSize(20);
    font1.setWeight(QFont::Light);
    font2.setPixelSize(30);
    font2.setWeight(QFont::Light);

    ui->gazeta->setFont(font1);
    ui->gazeta->setStyleSheet("QLabel { color : #666; }");
    

    ui->title->setFont(font2);
    ui->title->setStyleSheet("QLabel { color : #fff; }");
    

    ui->description->setFont(font1);
    ui->description->setStyleSheet("QLabel { color : #aaa; }");
    
    connect(&netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)));
    connect(&timer, SIGNAL(timeout()), this, SLOT(timeout()));
    timer.setInterval(60000);
    timer.start();

    addresses << "https://www.polsatnews.pl/rss/polska.xml" << "https://www.polsatnews.pl/rss/swiat.xml" << "https://tvn24.pl/najnowsze.xml" << "https://tvn24.pl/najwazniejsze.xml";
    addresses << "https://tvn24.pl/tvnwarszawa/najnowsze.xml" << "https://www.rmf24.pl/feed";
    addresses << "http://www.tokfm.pl/pub/rss/tokfmpl_polska.xml";

    ui->qrcode->setBaseSize(150,150);
}

void Informacje::timeout(const QDateTime &dt)
{
    if (inprogress)
        return;
    
    if (!done) {
        pobierz();
        return;
    }

    int h = dt.time().hour();

    if (h < 6)
        return;
    if (h > 20)
        return ;

    if (h == 7 || h == 9 || h == 11 || h == 12 || h == 13 || h == 14 || h == 15 || h == 17 || h == 19)
        return;

    if ((h == 6 || h == 18) && m_h1 != h) {
        m_h1 = h;
        wyczysc();
        return;
    }
    if ((h == 6 || h == 8 || h == 10 || h == 16 || h == 18 || h == 20) && m_h2 != h) {
        m_h2 = h;
        pobierz();
        return;
    }
}

QRect Informacje::getRect()
{
    return QRect(0, 650, width(), height());
}

Informacje::~Informacje()
{
    delete ui;
}

void Informacje::wyczysc()
{
    QMutexLocker locker(&mutex);
    newsy.removeOldest();
}

void Informacje::dodajInfo(const QString &guid, const QString & publisher, const QString & title,
                           const QString & description, const QString &pubData,
                           const QString & img, const QString &url)
{
    QDateTime dt /*= parseDate(pubData)*/;
    QMutexLocker locker(&mutex);
    newsy.add(guid, publisher, title, description, dt, "", url);
}

bool Informacje::isInfo(const QString &guid)
{
    QMutexLocker locker(&mutex);
    return newsy.isItem(guid);
}

void Informacje::pobierz()
{
    inprogress = true;
    m_requestSize = addresses.size();
    qDebug() << m_requestSize;
    for(auto & rss : addresses) {
        qDebug() << "REQUEST" << rss;
        netMng.get(QNetworkRequest(QUrl(rss)));
    }
}

void Informacje::parseMessage(QNetworkReply *reply)
{

    
    QByteArray bytes = reply->readAll();
    //qDebug() << reply->request().url().toDisplayString();
    //qDebug() << bytes;

    
    QDomDocument doc;
    
    doc.setContent(bytes);
    

    QDomNodeList channels = doc.elementsByTagName("channel");
    
    if (channels.length() < 1)
    {
        qDebug() << "No channel element found in feed! : " << reply->request().url().toDisplayString();
        return;
    }
    
    for (int c = 0; c < channels.length(); c++)
    {
        
        QDomNode chan = channels.at(c);
        
        QDomElement rsstitle = chan.firstChildElement("title");
        
        QString newstitle = rsstitle.toElement().text();
        
        QDomElement it = chan.firstChildElement("item");
        for (; !it.isNull(); it = it.nextSiblingElement("item")) {
            
            auto t = it.elementsByTagName("title");
            if (t.isEmpty() || t.length() < 1)
                continue;
            
            QString title = t.item(0).toElement().text();
                
            auto d = it.elementsByTagName("description");
            if (d.isEmpty() || d.length() < 1)
                continue;
            
            QString description = d.item(0).toElement().text();
            
            auto g = it.elementsByTagName("guid");
            if (g.isEmpty() || g.length() < 1)
                continue;
            
            QString guid = g.item(0).toElement().text();
            
            auto p = it.elementsByTagName("pubDate");
            
            if (p.isEmpty() || p.length() < 1)
                continue;
            
            QString psDate = p.item(0).toElement().text();

            QString url = "";
            
            auto u = it.elementsByTagName("link");
            if (p.isEmpty() || p.length() < 1)
                url = "";
            else
                url = u.item(0).toElement().text();

            dodajInfo(guid, newstitle, title, description, psDate, "", url);
         }
    }
    
    --m_requestSize;
    if (m_requestSize == 0 && !done)
    {
        inprogress = false;
        done = true;
        if (newsy.size() == 0)
            return;
        ui->description->setText(newsy.at(0).description());
        ui->title->setText(newsy.at(0).title());
        ui->gazeta->setText(newsy.at(0).publisher());
    }
}

void Informacje::timeout()
{
    qDebug() << "update"<< newsy.size();
    if (newsy.size() == 0)
        return;

    newsy.changeIndex();
    auto n = newsy.getItem();
    ui->gazeta->setText(n.publisher());
    ui->title->setText(n.title());
    ui->description->setText(n.description());
    ui->qrcode->setQRData(n.www());
}

QDateTime Informacje::parseDate(const QString &dt)
{
    //Tue, 18 Oct 2022 21:05:00 +0200
    QStringList dtl = dt.split(" ");
    static QMap<QString, int> mon;
    mon["jan"] = 1;
    mon["feb"] = 2;
    mon["mar"] = 3;
    mon["apr"] = 4;
    mon["may"] = 5;
    mon["jun"] = 6;
    mon["jul"] = 7;
    mon["aug"] = 8;
    mon["sep"] = 9;
    mon["oct"] = 10;
    mon["nov"] = 11;
    mon["dec"] = 12;
    int m = mon[dtl[2].toLower()];
    QDate d = QDate(dtl[3].toInt(), m, dtl[1].toInt());
    QTime t = QTime::fromString(dtl[4]);
    int secs = 0;
    if (dtl[5] != "GMT") {
         secs = dtl[5].toInt()*36;
    }
    QDateTime ddd(d, t);
    ddd = ddd.addSecs(secs);
    return ddd;

}
