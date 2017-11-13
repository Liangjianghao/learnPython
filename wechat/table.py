# -*- coding: utf-8 -*-

CREATE TABLE `video` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `content_type` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `url` varchar(255) DEFAULT NULL COMMENT '网址',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='内涵视频表';

