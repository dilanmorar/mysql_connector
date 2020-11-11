# MySQL Connector

MySQL Connector is a python library that enables Python programs to access MySQL databases using an API. This repository 
is going to use python code to connect to MySQL, and create databases, tables and queries.

## SQL Queries

To create the initial database we can either write our commands straight in MySQL or connect to MySQL and then write the 
commands and run it that way. I used MySQL and created the database and tables and added the values that way. Either way 
you need to have the commands and they are below. This is a simple, small amount of data to get started and is enough to 
write queries and gather information.

#### Database

First thing to do is to create a database.

`create database 'hospital'`

#### Hospital

Creating hospital table:
```
create table hospital(
hospital_id int not null auto_increment,
hospital_name varchar(50) not null,
bed_count int(7),
primary key (hospital_id),
unique (hospital_id)
);

```
Making sure it auto increments from 1:

`alter table hospital auto_increment=1;`


Add values to the hospital table:
```
insert into hospital (hospital_id, hospital_name, bed_count) 
values (null, Aberdeen Hospital', 300),
(null, 'Birmingham Hospital', 600),
(null, 'Cambridge Hospital', 900),
(null, 'Derby Hospital', 1200),
(null, 'Exeter Hospital', 1500)

```

#### Doctor

Creating doctor table:
```
create table doctor(
doctor_id int(3) not null auto_increment,
doctor_name varchar(50),
hospital_id int(1),
joining_date date,
speciality varchar(50),
salary int(10),
experience int(2),
primary key (doctor_id),
unique (doctor_id),
foreign key (hospital_id) references hospital(hospital_id)
);
```

Making sure it auto increments from 101:

`alter table doctor auto_increment=101;`

Adding values to the doctor table:
```
insert into doctor (doctor_id, doctor_name, hospital_id, joining_date,
 speciality, salary, experience)
values (null, 'Adam Smith', 1, ‘2007/10/5’, null, 55000, null),
(null, 'Ben Jones', 3, '2011/3/30', null, 63000, null),
(null, 'Claire James’, 4, '2015/6/19', null, 47000, null),
(null, ‘Daniel Stevens’, 2, '2001/4/27', null, 82000, null),
(null, ‘Emily Lewis’, 1, '2013/1/3', null, 51000, null),
(null, 'Faisal Masood', 5, '2011/3/12', null, 72000, null)

```
## Tasks

I first started by making a connection to the database in the function `get_db()` and then making another function that 
closes the connection to the database `close_db()`. For each function I created it starts by making a connection to the 
database and ends with the closing of the connection.

Each function uses the `.cursor()` which allows python code to execute a sql command. The command that executes the 
command is `.execute()`. This contains the query that we want to perform which in these cases would be what the task 
requires. Then in the function if required the output of the query is printed.

#### Connect to your database server and print its version.

This is the function `db_version()`.

#### Fetch Hospital and Doctor Information using hospital Id and doctor Id

This is the functions `hospital_info()` and `doctor_info()`.

#### Get the list of the doctors as per given specialty and salary 

This is the function `doctor_speciality_salary()`.

#### Get the list of the doctors from a given hospital 

This is the function `hospital_doctors()`.

#### Update doctor experience in years

This is the function `doctor_experience()`.

## Installations

This is what I used:
- MySQL version 8.0.22
- Python version 3.7.3
- Pycharms version 2020.2
- MySQL Connector latest version