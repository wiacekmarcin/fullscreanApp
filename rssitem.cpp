#include "rssitem.h"
#include <QDateTime>


RssItem::RssItem()
{

}

RssItem::RssItem(const QString & guid, const QString & title, const QString & description, const QDateTime & pubData, const QString image)
 : m_uid(guid), m_title(title), m_description(description), m_pubDate(pubData), m_image(image)
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

QImage RssItem::image() const
{
    return m_image;
}

void RssItem::setImage(const QImage &image)
{
    m_image = image;
}

QString RssItem::uid() const
{
    return m_uid;
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
    long long secs1 = QDateTime::currentDateTime().toSecsSinceEpoch();
    for (int i=0; i < size(); ++i) {
        if (secs1 - at(i).pubDate().toSecsSinceEpoch() > 48*3600)
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

void RssList::add(const QString &guid, const QString & title, const QString & description, const QDateTime &pubData)
{
    RssItem item(guid, title, description, pubData);
    
}

const RssItem& RssList::getItem() const
{
    return operator[](actIndex);
}

