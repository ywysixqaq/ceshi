/*create database if not exists company;
use company;

create table employees(
employees_id int primary key auto_increment comment'员工id',
employees_name varchar(50) not null comment'员工姓名',
position varchar(50) not null comment'职业',
salary int not null comment'工资')comment'员工表';

#添加入职时间
desc employees;
alter table employees add column hire_date date;
alter table employees modify column salary decimal(10,2);
desc employees;

alter table employees modify hire_date timestamp default current_timestamp;
desc employees;
#添加性别
alter table employees add gender enum('男','女') not null comment'性别';
desc employees;

insert into employees(employees_name,position,salary,hire_date)
values
('张三','程序员',15000,'2023-01-15'),
('李四','设计师',12000,'2023-02-20'),
('王五','产品经理',20000,'2022-11-01');

select * from employees;
select employees_name,position from employees;
select employees_name as '姓名',salary as '工资' from employees;

#条件筛选查询
select * from employees where salary >=15000;
#数据排序
select * from employees order by salary desc;
#限制查询条数
select * from employees order by salary desc limit 2;

#select salary,count(*) from employees group by employees_id;
#select employees_id,sum(salary) from employees group by employees_id;
#select max(salary) from employees group by employees_id;
#select min(salary) from employees group by employees_id;
#select avg(salary) from employees group by employees_id;

CREATE DATABASE IF NOT EXISTS company;
USE company;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '员工编号',
    name VARCHAR(20) NOT NULL COMMENT '员工姓名',
    salary DECIMAL(10,2) COMMENT '薪水',
    position VARCHAR(20) COMMENT '职位',
    department VARCHAR(20) COMMENT '部门',
    entry_date DATE COMMENT '入职日期',
    gender CHAR(1) COMMENT '性别'
) COMMENT='员工信息表';

INSERT INTO employees(name, salary, position, department, entry_date, gender)
VALUES
('张三', 15000.00, '开发工程师', '技术部', '2020-03-15', '男'),
('李四', 12000.00, '设计师', '设计部', '2021-07-20', '女'),
('王五', 18000.00, '高级开发', '技术部', '2019-11-05', '男'),
('赵六', 10000.00, '设计师', '设计部', '2022-01-10', '男'),
('钱七', 22000.00, '产品经理', '产品部', '2018-05-12', '女'),
('孙八', 9000.00, '设计师', '设计部', '2023-02-18', '女'),
('周九', 16000.00, '开发工程师', '技术部', '2021-09-01', '男');*/

select * from employees;
