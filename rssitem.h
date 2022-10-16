#ifndef RSSITEM_H
#define RSSITEM_H
#include <QString>
#include <QImage>
#include <QDateTime>

class RssItem
{
public:
    RssItem();

    QString title() const;
    void setTitle(const QString &title);

    QString description() const;
    void setDescription(const QString &description);

    QDateTime pubDate() const;
    void setPubDate(const QDateTime &pubDate);

    QImage image() const;
    void setImage(const QImage &image);

    QString uid() const;
    void setUid(const QString &uid);

private:
    QString m_title;
    QString m_description;
    QDateTime m_pubDate;
    QImage m_image;
    QString m_uid;
};



#endif // RSSITEM_H
