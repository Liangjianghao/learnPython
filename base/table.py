CREATE TABLE `doubanMovieTable` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` datetime DEFAULT NULL COMMENT '创建时间',
  `attrs` varchar(255) DEFAULT NULL COMMENT '导演',
  `name` varchar(255) DEFAULT NULL COMMENT '电影名',
  `moviescore` float DEFAULT NULL COMMENT '电影评分',
  `category_name` varchar(255) DEFAULT NULL COMMENT '电影类型',
  `movietime` varchar(255) DEFAULT NULL COMMENT '时长',
  `uptime` int(11) DEFAULT NULL COMMENT '上映日期',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='豆瓣电影表';

def insertChatContent(attrs,name,category_name,movietime,uptime):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='127.0.0.1',
		port=3306,  
		user='root',  
		passwd='123456',  
		db='douban',  
		charset='utf8mb4'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO meinvTable (createtime,attrs,name,category_name,movietime,uptime) VALUES ( '%s', '%s', '%s','%s','%s','%s')"  
	print sql
	attrs = pymysql.escape_string(attrs)
	name = pymysql.escape_string(name)
	category_name = pymysql.escape_string(category_name)
	movietime = pymysql.escape_string(movietime)
	uptime = pymysql.escape_string(uptime)

	data = (createtime,attrs,name,category_name,movietime,uptime)  
	# print data
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')