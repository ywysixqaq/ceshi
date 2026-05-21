create database if not exists school;
use school;

create table students(
id int primary key auto_increment,
name varchar(50) not null,
gendet enum('男','女') default '男',
age int, major varchar(100));
