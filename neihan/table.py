CREATE TABLE `meinvTable` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `digg_count` varchar(255) DEFAULT NULL COMMENT '赞数',
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `url` varchar(255) DEFAULT NULL COMMENT '网址',
  `category_name` varchar(255) DEFAULT NULL COMMENT '类别',
  `comments` varchar(255) DEFAULT NULL COMMENT '神评',
  `time_param` varchar(255) DEFAULT NULL COMMENT '时间参数',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='美女表';

def insertChatContent(create_time,digg_count,content,url,category_name,comments,maxtime):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='127.0.0.1',
		port=3306,  
		user='root',  
		passwd='123456',  
		db='duanzi',  
		charset='utf8mb4'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO meinvTable (create_time,digg_count,content,url,category_name,comments,time_param) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s')"  
	print sql
	savecontent = pymysql.escape_string(content)
	downUrl = pymysql.escape_string(url)
	category = pymysql.escape_string(category_name)
	comment = pymysql.escape_string(comments)
	time_param = pymysql.escape_string(maxtime)

	data = (createtime,digg_count,savecontent,downUrl,category,comment,time_param)  
	# print data
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')