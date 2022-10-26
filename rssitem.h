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
    RssItem(const QString &guid, const QString & publisher, const QString & title, const QString & description,
            const QDateTime &pubData, const QString &image = "", const QString &url="nourl");

    QString title() const;
    void setTitle(const QString &title);

    QString description() const;
    void setDescription(const QString &description);

    QDateTime pubDate() const;
    void setPubDate(const QDateTime &pubDate);

    QString image() const;
    void setImage(const QString &image);

    QString uid() const;
    void setUid(const QString &uid);

    QString publisher() const;
    void setPublisher(const QString & pub);

    const QString &www() const;
    void setWww(const QString &newWww);

private:
    QString m_uid;
    QString m_title;
    QString m_description;
    QDateTime m_pubDate;
    QString m_image;
    QString m_publisher;
    QString m_www;
};

class RssList : public QList<RssItem> 
{
public:
    RssList();
    ~RssList();

    void removeOldest();
    bool isItem(const QString & guid);

    void add(const QString &guid, const QString & publisher, const QString & title,
             const QString & description, const QDateTime &pubData, const QString & Image,
             const QString & url);

    void changeIndex();
    const RssItem& getItem() const;
private:
    int actIndex;
};


#endif // RSSITEM_H
