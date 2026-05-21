/*create database if not exists school;
use school;

create table if not exists students (
 id int primary key auto_increment,
 name varchar(20) not null,
 age int not null,
 gender varchar(4) not null,
 major varchar(30) not null
);

set sql_safe_updates = 0;

insert into students (name, age, gender, major) values
  ('张三', 18, '男', '计算机科学'),
  ('李四', 21, '女', '软件工程'),
  ('王五', 19, '男', '计算机科学'),
  ('赵六', 22, '女', '数据科学'),
  ('孙七', 17, '男', '软件工程'),
  ('周八', 20, '女', '计算机科学'),
  ('吴九', 23, '男', '人工智能'),
  ('郑十', 19, '女', '人工智能'),
  ('钱十一', 25, '女', '数据科学'),
  ('陈十二', 18, '男', '软件工程'),
  ('刘十三', 21, '男', '计算机科学'),
  ('黄十四', 16, '女', '人工智能');
*/

#1. 查询年龄小于20的学生，按年龄升序、姓名降序输出
#select * from students where age < 20 order by age asc, name desc;

#2. 删除年龄大于20岁的女生
#delete from students where age > 20 and gender = '女';

#3. 统计每个专业的人数和平均年龄
#select major, count(*) as 人数, avg(age) as 平均年龄 from students group by major;

#drop table students;