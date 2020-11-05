# MySQL Connector

## SQL Queries

### Database

First thing to do is to create a database.
`create database 'hospital'`

### Hospital

First create table
```
create table hospital(
hospital_id int not null auto_increment,
hospital_name varchar(50) not null,
bed_count int(7),
primary key (hospital_id),
unique (hospital_id)
);

```
Making sure it auto increments from 1
`alter table hospital auto_increment=1;`
Add values to the table:
```
insert into hospital (hospital_id, hospital_name, bed_count) 
values (null, Aberdeen Hospital', 300),
(null, 'Birmingham Hospital', 600),
(null, 'Cambridge Hospital', 900),
(null, 'Derby Hospital', 1200),
(null, 'Exeter Hospital', 1500)

```
### Doctor

Creating doctor table:
```

```