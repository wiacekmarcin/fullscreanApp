#include "informacje.h"
#include "ui_informacje.h"
#include <QFont>
#include <QFontDatabase>
#include <QMutexLocker>
#include <QDomDocument>

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
    

    ui->title->setFont(font2);
    ui->title->setStyleSheet("QLabel { color : #fff; }");
    

    ui->description->setFont(font1);
    ui->description->setStyleSheet("QLabel { color : #aaa; }");
    
    connect(&netMng, SIGNAL(finished(QNetworkReply*)), this, SLOT(parseMessage(QNetworkReply*)));
    connect(&timer, SIGNAL(timeout()), this, SLOT(timeout()));
    timer.setInterval(20000);
    timer.start();

    addresses << "https://www.polsatnews.pl/rss/polska.xml" << "https://www.polsatnews.pl/rss/swiat.xml" << "https://tvn24.pl/najnowsze.xml" << "https://tvn24.pl/najwazniejsze.xml";
    addresses << "https://tvn24.pl/tvnwarszawa/najnowsze.xml";
}

void Informacje::update(int, int, int, int, int h, int, int)
{
    if (inprogress)
        return;
    
    if (!done)
        pobierz();

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
    return QRect(0, 600, width(), height());
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

void Informacje::dodajInfo(const QString &guid, const QString & title, const QString & description, const QDateTime &pubData)
{
    QMutexLocker locker(&mutex);
    newsy.add(guid, title, description, pubData);
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
    for(auto rss : addresses) {
        netMng.get(QNetworkRequest(QUrl(rss)));
    }
}

void Informacje::parseMessage(QNetworkReply *reply)
{
    QByteArray bytes = reply->readAll();
    //qDebug() << reply->request().url().toDisplayString();
    //qDebug() << bytes;

    QDomDocument doc("mydocument");
    doc.setContent(bytes);

    QDomNodeList channels = doc.elementsByTagName("channel");
    if (channels.length() < 1)
    {
        qDebug() << "No channel element found in feed!";
        return;
    }
    for (int c = 0; c < channels.length(); c++)
    {
        QDomNode chan = channels.at(c);
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
            QDateTime pubDate = QDateTime::fromString(psDate, "ddd, dd MMM yyyy HH:mm:ss");
            qDebug() << pubDate.toString();
            newsy.add(guid, title, description, QDateTime::currentDateTime());
         }
    }
    
    --m_requestSize;
    if (m_requestSize == 0)
    {
        inprogress = false;
        done = true;
        if (newsy.size() == 0)
            return;
        ui->description->setText(newsy.at(0).description());
        ui->title->setText(newsy.at(0).title());
        ui->gazeta->setText("Polsat");
    }
}

void Informacje::timeout()
{
    qDebug() << "update"<< newsy.size();
    if (newsy.size() == 0)
        return;

    newsy.changeIndex();
    auto n = newsy.getItem();
    ui->title->setText(n.title());
    ui->description->setText(n.description());
}
