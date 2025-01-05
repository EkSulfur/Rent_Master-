-- 使用前，请确保已连接到正确的数据库

-- 禁用外键检查以防止删除时的依赖问题
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- 删除现有的表（如果存在），以免创建新表时发生冲突
DROP TABLE IF EXISTS `admin`;
DROP TABLE IF EXISTS `house`;
DROP TABLE IF EXISTS `tenant`;
DROP TABLE IF EXISTS `lease_records`;

-- 创建管理员表
CREATE TABLE `admin` (
  `admin_id` int AUTO_INCREMENT, -- 管理员ID，自增
  `username` varchar(50) , -- 管理员用户名
  `password` varchar(100) , -- 管理员密码
  PRIMARY KEY (`admin_id`) -- 主键设置为admin_id
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建房屋信息表
CREATE TABLE `house` (
  `house_id` int AUTO_INCREMENT, -- 房屋ID，自增
  `owner_id` int, -- 房东ID
  `house_number` varchar(20) , -- 房屋编号
  `area` float , -- 房屋面积
  `location` varchar(100) , -- 房屋地理位置
  `layout` varchar(50) , -- 房屋布局
  `monthly_rent` float , -- 每月租金
  `status` varchar(20) , -- 房屋当前状态
  `available_from` date, -- 可租赁起始日期
  `lease_terms` varchar(255), -- 租赁条款
  PRIMARY KEY (`house_id`) -- 主键设置为house_id
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建租户信息表
CREATE TABLE `tenant` (
  `tenant_id` int AUTO_INCREMENT, -- 租户ID，自增
  `username` varchar(50) , -- 租户用户名
  `password` varchar(100) , -- 租户密码
  `full_name` varchar(255) , -- 租户全名
  `phone_number` varchar(255) , -- 电话号码
  `email` varchar(255), -- 邮箱地址
  `gender` varchar(30), -- 性别
  PRIMARY KEY (`tenant_id`) -- 主键设置为tenant_id
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 创建租赁记录表
CREATE TABLE `lease_records` (
  `record_id` int AUTO_INCREMENT, -- 记录ID，自增
  `tenant_id` int , -- 租户ID
  `house_id` int , -- 房屋ID
  `start_date` date , -- 租赁开始日期
  `end_date` date , -- 租赁结束日期
  `rent_amount` float , -- 租金金额
  `payment_status` varchar(50) , -- 支付状态
  PRIMARY KEY (`record_id`), -- 主键设置为record_id
  FOREIGN KEY (`tenant_id`) REFERENCES `tenant`(`tenant_id`), -- 外键约束，关联租户ID
  FOREIGN KEY (`house_id`) REFERENCES `house`(`house_id`) -- 外键约束，关联房屋ID
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 重新启用外键检查
SET FOREIGN_KEY_CHECKS = 1;
