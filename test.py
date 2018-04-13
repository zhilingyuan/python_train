import time
import datetime
str = '2012-08-29 19:45:57'
date = time.strptime(str, "%Y-%m-%d %H:%M:%S") #最小单位0.000001秒
today=datetime.date.today()
print(today)
today=today.strftime('%Y-%m-%d')
allowed_domains = ['http:/www.xicidaili.com']
page=20
url=[]
for _ in range(page):
    url_page=allowed_domains[0]+"/nn/{}".format(_+1)
    url.append(url_page)
'''
db.userInfo.aggregate([
    {
        $group: { _id: {userName: '$userName',age: '$age'},count: {$sum: 1},dups: {$addToSet: '$_id'}}
    },
    {
        $match: {count: {$gt: 1}}
    }
]).forEach(function(doc){
    doc.dups.shift();
    db.userInfo.remove({_id: {$in: doc.dups}});
})

数据过大会报内存错误：Exceeded memory limit for $group, but didn't allow external sort. Pass allowDiskUse:true to opt in

可以在后面添加上这个属性就不会了
引用
db.userInfo.aggregate([ {
$group: { _id: {userName: '$userName',age: '$age'},count: {$sum: 1},dups: {$addToSet: '$_id'}}
},
{
$match: {count: {$gt: 1}}
}
],{
allowDiskUse: true
}).forEach(function(doc){
doc.dups.shift();
db.userInfo.remove({_id: {$in: doc.dups}});
})
'''
