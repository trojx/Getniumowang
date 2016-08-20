create table chatcontent
	(
		id int unsigned not null auto_increment, 
		time datetime  null,
		sharesname char(16)  null,
		chattxt text not null,
		datapid int unsigned null default 0,
		primary key(id)
	);

create table users
	(
		id int unsigned not null auto_increment ,
		username char(30) not null,
		userpass char(200) not null,
		level int null default 0,
		createtime datetime null ,
		primary key(id)
	);

create table shares
	(
		id int unsigned not null auto_increment ,
		sharesname char(16) not null,
		reason text  null,
		buyprice int unsigned null ,
                sellprice int unsigned null,
		buytime datetime null ,
		selltime datetime null,
		primary key(id)
	);

