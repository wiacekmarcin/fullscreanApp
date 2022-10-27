#include "rssitem.h"
#include <QDateTime>


RssItem::RssItem()
{

}

RssItem::RssItem(const QString & guid, const QString & publ, const QString & title,
                 const QString & description, const QDateTime & pubData, const QString &image,
                 const QString & url)
 : m_uid(guid), m_title(title), m_description(description), m_pubDate(pubData), m_image(image),
   m_publisher(publ), m_www(url)
{

}

QString RssItem::title() const
{
    return m_title;
}

void RssItem::setTitle(const QString &title)
{
    m_title = title;
}

QString RssItem::description() const
{
    return m_description;
}

void RssItem::setDescription(const QString &description)
{
    m_description = description;
}

QDateTime RssItem::pubDate() const
{
    return m_pubDate;
}

void RssItem::setPubDate(const QDateTime &pubDate)
{
    m_pubDate = pubDate;
}

QString RssItem::image() const
{
    return m_image;
}

void RssItem::setImage(const QString &image)
{
    m_image = image;
}

QString RssItem::uid() const
{
    return m_uid;
}

QString RssItem::publisher() const
{
    return m_publisher;
}

void RssItem::setPublisher(const QString & pub)
{
    m_publisher = pub;
}

const QString &RssItem::www() const
{
    return m_www;
}

void RssItem::setWww(const QString &newWww)
{
    m_www = newWww;
}

void RssItem::setUid(const QString &uid)
{
    m_uid = uid;
}

RssList::RssList()
{
    actIndex = 0;
}

RssList::~RssList()
{

}

void RssList::changeIndex()
{
    if (actIndex == size())
    {
        actIndex = 0;
    } else {
        ++actIndex;
    }
}

void RssList::removeOldest()
{
    long long secs1 = QDateTime::currentDateTime().toMSecsSinceEpoch();
    for (int i=0; i < size(); ++i) {
        if (secs1 - at(i).pubDate().toMSecsSinceEpoch() > 48*3600*1000)
            removeAt(i);
    }
}

bool RssList::isItem(const QString & guid)
{
    for (auto it = begin(); it != end(); ++it) {
        if (it->uid() == guid)
            return true;
    }
    return false;
}

void RssList::add(const QString &guid, const QString & publisher, const QString & title,
                  const QString &description, const QDateTime &pubData,
                  const QString &image, const QString &url)
{
    RssItem item(guid, publisher, title, description, pubData, image, url);
    push_back(item);
    
}

const RssItem& RssList::getItem() const
{
    return operator[](actIndex);
}

