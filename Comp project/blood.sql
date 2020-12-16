SELECT * FROM user.blood;
LOAD DATA LOCAL INFILE "C:\\Users\\shikh\\OneDrive\\Desktop\\BLOOD.csv" INTO TABLE user.blood
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'

CREATE TABLE blood (id  INTEGER(255) AUTO_INCREMENT Primary key,full_name VARCHAR(255), pass_word VARCHAR(255), gender VARCHAR(255), age VARCHAR(255),mobile_number INTEGER(255),email_id VARCHAR(255),pincode VARCHAR(255),  blood_type VARCHAR(255),number_donations integer(250),volume integer(250))

drop table blood;
drop table admin;
drop table otp;


create table otp (otp_ integer(5), serial integer(1) primary key);
create table admin(admin_name varchar(255), admin_password varchar(255))


update blood set number_donations = number_donations+'1' where id= '1'; 
update blood set volume = volume + (number_donations )where id= '1';

insert into admin values 
('Vidisha',654321);
insert into otp values 
(0,1);


select * from user.admin;
select * from user.otp;
