drop database if exists car_table;

create database car_table;

use car_table;

create table veiculos (
VEICULO_ID integer,
VEICULO_NOME varchar(50) not null,
MONTADORA_ID integer,
primary key(VEICULO_ID)
);

create table montadoras (
MONTADORA_ID integer primary key,
MONTADORA_NOME varchar(50)
);

insert into montadoras values(99,"VW");
insert into montadoras values(01,"GM");
insert into montadoras values(25,"TOYOTA");
insert into montadoras values(89,"HYUNDAI");
insert into montadoras values(90,"KIA");

insert into veiculos values("100","fox",99);
insert into veiculos values(101,"gol",99);
insert into veiculos values(102,"golf",99);
insert into veiculos values(200,"onix",01);
insert into veiculos values(204,"cruze",01);
insert into veiculos values(202,"camaro",01);
insert into veiculos values(303,"etios",25);
insert into veiculos values(302,"corola",25);
insert into veiculos values(802,"hb20",89);
insert into veiculos values(502,"cerato",90);
insert into veiculos values(515,"sorento",90);

select * from montadoras;

-- select * from veiculos;

