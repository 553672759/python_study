复制项目1，使用mysql存储数据。


1.在设置中启用pipline
	ITEM_PIPELINES={
	'dianying.pipelines.DianyingPipeline':300,
	}

2.在piplines中编写操作
	classDianyingPipeline(object):
	def__init__(self):
	host="127.0.0.1"
	port=27017
	dbname='xx'
	sheetname='test'
	client=MongoClient(host=host,port=port)
	#指定数据库
	mydb=client[dbname]
	#存放数据的数据库表名
	self.post=mydb[sheetname]

	defprocess_item(self,item,spider):
	data=dict(item)
	self.post.insert(data)
	returnitem
3.item中设置属性
	name=scrapy.Field()
	link=scrapy.Field()


