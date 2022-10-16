#include "rssitem.h"

RssItem::RssItem()
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
