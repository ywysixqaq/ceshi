/*create database if not exists school2;
USE school2;

create table classes (class_id int primary key, class_name varchar(50));
create table students (id int primary key,name varchar(50),c_id int);

insert into classes values(1,'计算机一班'),(2,'AI二班');
insert into students values(1,'张三',1),(2,'李四',1),(3,'王五',2),(4,'赵六',null);

select s.name,c.class_name from students s inner join classes c on s.c_id=c.class_id;*/