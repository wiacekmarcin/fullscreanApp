#ifndef RSSITEM_H
#define RSSITEM_H
#include <QString>
#include <QImage>
#include <QDateTime>
#include <QString>
class RssItem
{
public:
    RssItem();
    RssItem(const QString &guid, const QString & publisher, const QString & title, const QString & description, const QDateTime &pubData, const QString &image = "");

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

    QString publisher() const;
    void setPublisher(const QString & pub);

private:
    QString m_uid;
    QString m_title;
    QString m_description;
    QDateTime m_pubDate;
    QImage m_image;
    QString m_publisher;
    
};

class RssList : public QList<RssItem> 
{
public:
    RssList();
    ~RssList();

    void removeOldest();
    bool isItem(const QString & guid);

    void add(const QString &guid, const QString & publisher, const QString & title, const QString & description, const QDateTime &pubData);

    void changeIndex();
    const RssItem& getItem() const;
private:
    int actIndex;
};


#endif // RSSITEM_H
