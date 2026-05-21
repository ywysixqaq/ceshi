/*create database if not exists dianshang;
use dianshang;

create table users(
user_id int primary key auto_increment comment'用户id',
user_name varchar(50) not null comment'用户名',
email varchar(50) not null unique comment'邮箱',
user_time varchar(50) not null comment'注册时间',
phone varchar(11) not null comment'手机号' );

create table products(
pd_id int primary key auto_increment comment'商品id',
pd_name varchar(100) not null comment'商品名称',
price decimal(10,2) not null comment'价格',
kucun int not null default 0 comment'库存',
fenlei int comment'分类id');

create table orders(
order_id int primary key auto_increment comment'订单id',
user_id int not null comment'用户id',
order_time datetime not null comment'订单时间',
total_amount decimal(10,2) not null comment'总金额',
order_zt varchar(20),
sh_place varchar(50),
foreign key (user_id) references users(user_id));

create table order_items(
id int primary key auto_increment comment'id',
order_id int not null comment'订单id',
pd_id int not null comment'商品id',
buy_numbers int not null comment'购买数量',
unit_price decimal(10,2) not null comment'商品单价',
xj_price decimal(10,2) not null comment'小计金额',
foreign key (order_id) references orders(order_id),
foreign key (pd_id) references products(pd_id));*/
