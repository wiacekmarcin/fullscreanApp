#include "informacje.h"
#include "ui_informacje.h"
#include <QFont>
#include <QFontDatabase>
#include <QMutexLocker>
#include <QDomDocument>

Informacje::Informacje(QWidget *parent) :
    BlackWidget(parent),
    ui(new Ui::Informacje)
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

    QDomNodeList channel = doc.elementsByTagName("channel");
    if (channel.length() < 1)
    {
        qDebug() << "No channel element found in feed!";
        return "";
    }

    QString titleStr = getXMLValue(channel.at(0), templates[tIndex].feedTitle);
    if (titleStr.isEmpty())
    {
        qDebug() << tr("Title element is empty!") << path;
        return "";
    }



    QDomNodeList items = doc.elementsByTagName("channel").elementsByTagName("item");
    QDomNode itemNode, imgNode, xmlNode, urlNode, tplNode, iurlNode;
    QString imgStr, xmlStr, urlStr, tplStr, iurlStr;


    for (int i = 0; i < items.length(); i++)
    {
        itemNode = items.at(i);
        if (itemNode.isNull() || !itemNode.isElement())
            continue;

        // feed must contain url for updating. all other elements
        // are optional. if no xml then we try to download the
        // feed from the specified url. if no img then we try to
        // download the image from the url specified in the feed.
        urlNode = itemNode.namedItem("url");
        if (urlNode.isNull() || !urlNode.isElement())
            continue;

        urlStr = urlNode.toElement().text();
        if (urlStr.isEmpty())
            continue;

        xmlStr = "";
        xmlNode = itemNode.namedItem("xml");
        if (!xmlNode.isNull() && xmlNode.isElement())
        {
            xmlStr = xmlNode.toElement().text();
            if (!xmlStr.isEmpty())
            {
                //finfo.setFile(tr("%1%2%3").arg(feedsPath).arg(sep).arg(xmlStr));
                //if (!finfo.exists())
                //    xmlStr = "";
                qDebug() << "xmlStr" << xmlStr;
            }
        }

        imgStr = "";
        imgNode = itemNode.namedItem("img");
        if (!imgNode.isNull() && imgNode.isElement())
        {
            imgStr = imgNode.toElement().text();
            qDebug() << "imgStr" << imgStr;
            //if (!imgStr.isEmpty())
            //{
            //    finfo.setFile(tr("%1%2%3").arg(imagesPath).arg(sep).arg(imgStr));
            //    if (!finfo.exists())
            //        imgStr = "";
            //}
        }

        tplStr = "";
        tplNode = itemNode.namedItem("tpl");
        if (!tplNode.isNull() && tplNode.isElement())
        {
            tplStr = tplNode.toElement().text();
            qDebug() << "tplStr" << tplStr;
            //if (!tplStr.isEmpty())
            //{
            //    finfo.setFile(tr("%1%2%3").arg(templatesPath).arg(sep).arg(tplStr));
            //    if (!finfo.exists())
            //    {
            //        tplStr = "";
            //    }
            //    else
            //    {
            //        loadTemplate(tplStr);
            //    }
            //}
        }
    }
    
    
    --m_requestSize;
    if (m_requestSize == 0)
    {
        inprogress = false;
        done = true;
    }    
}