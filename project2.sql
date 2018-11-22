-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: eecs118_cs122a_project2
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `name` varchar(50) NOT NULL,
  `A` int(11) DEFAULT NULL,
  `B` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES ('Antes, Sir Gerad Abad',5752,7504),('Ayala, David Sanchez',3955,4251),('Bai, Dayue',4124,5254),('Bhan, Krishen',1425,7875),('Bui, Dennis',3633,9985),('Cai, Yushi',7878,6966),('Cando, Jeffrey Bigcas',4122,7544),('Cao, Jimi',7887,1422),('Catarroja, Aaron Justin Garcia',7588,7888),('Chaudhry, Omar Iqbal',6968,4588),('Chavez, Cheyenne Marie',8756,6322),('Chen, Bolin',2536,2222),('Chen, Hanlu',5558,3633),('Chen, Jessica',8555,7888),('Chen, Luke',4648,2130),('Chiang, Austin',9999,8555),('Chong, Lawrence',2555,3634),('Chow, Pui Yin Roy',7852,8751),('Clark, Conner Jonathan',6387,9825),('Cloutier, Zachary Aidan',1478,9635),('Co, Jonathan Go',3695,3652),('Dobrusky, Justin Jerome',5225,8555),('Duan, Ran',6385,4548),('Dumas, Patrick Lee',4478,4321),('Eleazar, Geraldine Marie',9648,9255),('Ellington, Floranne Tavailau',3685,7852),('Fallejo, Jeffrey Akio',1474,5462),('Feng, Jiarong',5648,1211),('Feng, Lixiong',3652,8955),('Gao, Yulun',8425,6332),('Gonzalez, Cynthia',8524,7412),('Grigoryan, Gyulnara',9685,2536),('Guan, Yingshan',1585,3685),('Guerrero, Joshua Andrew',7566,2585),('Hamilton, Bailey Richard',6385,6887),('Han, Kun',7851,8525),('Hernandez, Amanda Janelle',6952,3685),('Hii, Damian King Yong',8569,2585),('Ho, Julie',4186,3694),('Huai, Yuqi',3785,6478),('Huang, Lei',1582,8564),('Huang, Tianzhi',7528,1568),('Huynh, Andrew Matthew',3785,1586),('Hyun, Hahnara',9458,6485),('Ingal, Jd',2864,2685),('Innabi, Nicholas Alexander',8564,3855),('Ji, An',8596,1588),('Jiang, Kaifu',1548,3785),('Jimenez, Abigail Paula',8569,6485),('Jusman, Shannon May',6485,2580),('Kausheeka, Srinath Suresh',1562,3560),('Kim, Edward',6855,9520),('Kim, Jae Hyun',3785,6852),('Kunbargi, Bisher Bennabi',2585,8388),('Lam, Huu',3585,3568),('Lam, Kevin',2585,3685),('Le, Huy Duc',3784,1568),('Le, Justin Huy',6952,2058),('Lee, Ki Min',3508,3677),('Lee, Timothy Gwangyong',1500,3855),('Lee, Won Joon',6978,7890),('Li, Dennis Tom',2585,3685),('Li, Haoze',1458,4521),('Li, Shawn',5200,8560),('Li, Yinxue',3699,8952),('Li, Yuqing',7852,3695),('Li, Zican',5648,7986),('Lin, Ruoyu',8569,6392),('Lin, Shaolong',8560,6350),('Liu, Jiajun',8591,7561),('Liu, Yishou',9623,3620),('Liu, Zixi',8591,7541),('Lopez, Joshua Alejandro',9765,1345),('Louidor, Richemond',5752,7504),('Lum, Melissa Ann',3955,4251),('Luo, Jacky',4124,5254),('Lyles, William Gerald',1425,7875),('Ma, Yuqi',3633,9985),('Madrigal-Simental, Jesus',7878,6966),('Mahajan, Shubham',4122,7544),('Mainaly, Nitesh',7887,1422),('Martinez Neda, Barbara',7588,7888),('Melendez, Ernesto Buddenbohm III',6968,4588),('Mendoza, Daniel Marcos',8756,6322),('Messerschmidt, Joseph David',2536,2222),('Mikesell, Jacob Dean',5558,3633),('Mo, Xinxin',8555,7888),('Morales, Lazaro Eduardo',4648,2130),('Morton, Bradley Sean',9999,8555),('Nagle, Samantha Clair',2555,3634),('Nakasone, Daniel Shigeru',7852,8751),('Nery, Sarah Castro',6387,9825),('Ngo, Phat',1478,9635),('Nguyen, Chi',3695,3652),('Nguyen, Damon',5225,8555),('Nguyen, Khanh Ngoc',6385,4548),('Nguyen, Khoa Thanh Anh',4478,4321),('Nguyen, Marshall Hoang',9648,9255),('Nguyen, Steven Minh',3685,7852),('Nguyen, Tam Thai',1474,5462),('Nowlen, Austin James',5648,1211),('Ono, Shunichi',3652,8955),('Orchard, Terry',8425,6332),('Ordonez, Eliza Jayne Evangelista',8524,7412),('Otsuka, Mitsuru',9685,2536),('Pan, Yizhou',1585,3685),('Park, Minjae',7566,2585),('Pendleton, Rosetta Hanako',6385,6887),('Peng, Qingyang',7851,8525),('Peraza, Gabriel Sebastian',6952,3685),('Phan, Kelvin Huy-Trung',8569,2585),('Pineda, Rafael Antonio',4186,3694),('Rahman, Farid Syed',3785,6478),('Ramirez, Alex Ivan',1582,8564),('Ren, Jason Zhe',7528,1568),('Richardson, Tyler James',3785,1586),('Robbins, Max Jeremy',9458,6485),('Rosenfeld, Joshua Ian',2864,2685),('Santarosa, Kenneth',8564,3855),('Scotten, William Edward',8596,1588),('Sebastian, Ynah Maris',1548,3785),('Sehdev, Mohit Kumar',8569,6485),('Seo, Daniel Dahoon',6485,2580),('Serrano, Christian Agbayani',1562,3560),('Serrano, Derrick Marty',6855,9520),('Sheikh, Maha Nazish',3785,6852),('Shenouda, Michael Ben',2585,8388),('Singletary, Sarah Beth',3585,3568),('Sirimarco, Anthony Santino',2585,3685),('Sonza, Janzal Karlo Garcia',3784,1568),('Sun, Zexi',6952,2058),('Tan, Conghuai',3508,3677),('Tang, Edwin',1500,3855),('Tat, Kenny',6978,7890),('Tayag, Jeremy Ivan',2585,3685),('Thompson, Tristin Trent',1458,4521),('To, Minh Cong',5200,8560),('Tran, Ashley Vannhi',3699,8952),('Tran, John Thanh-Lam',7852,3695),('Tran, Kelly Chung',5648,7986),('Tran, My Thuan Thi',8569,6392),('Tri, Ryan Thien',8560,6350),('Truong, Brian',8591,7561),('Urrea, Nicolas Antonio',9623,3620),('Valenzuela, Omar',8591,7541),('Vu, Brian Dang',9765,1345),('Wahl, Ian James',5752,7504),('Wang, Chuyi',3955,4251),('Wang, Deyuan',4124,5254),('Wang, Evan',1425,7875),('Wang, Mengqi',3633,9985),('Wang, Michael',7878,6966),('Wang, Vesper',4122,7544),('Wang, Wuchi',7887,1422),('Wang, Yijian',7588,7888),('Washburn, Jacob Stephen',6968,4588),('Widodo, Alfianto Pramana',8756,6322),('Xie, Zhehao',2536,2222),('Xiong, Ciel',5558,3633),('Xu, Jiekai',8555,7888),('Xu, Yanjie',4648,2130),('Xu, Zijian',9999,8555),('Xu, Zinan',2555,3634),('Yadav, Siddharth',7852,8751),('Yakovlev, Alexander Vasilyevich',6387,9825),('Yan, Haixiang',1478,9635),('Yan, Hao',3695,3652),('Yang, Nan',5225,8555),('Yang, Xiaoyan',6385,4548),('Yao, Timothy',4478,4321),('Yi, Xiaopeng',9648,9255),('Yousefi, Neema',3685,7852),('Yu, Kai',1474,5462),('Yu, Liangze',5648,1211),('Yu, Zhenjiang',3652,8955),('Zhang, Chenghao',8425,6332),('Zhao, Yujie',8524,7412),('Zhu, Qingze',9685,2536),('Zhu, Yicheng',1585,3685);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `result` (
  `name` varchar(50) NOT NULL,
  `id2d` int(11) DEFAULT NULL,
  `result` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-27 16:23:58
