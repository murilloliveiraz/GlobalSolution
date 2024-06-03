create database db_sustaintravel;

use db_sustaintravel;

create table tbl_viagem(
	id int not null auto_increment primary key,
    lugar varchar(200) not null,
    qtd_dias int not null,
    qtd_noites int not null,
    avaliacao_media float,
    unique index(id)
);

create table tbl_viagem_avaliacao (
	id int not null auto_increment primary key,
    avaliacao float not null,
    id_viagem int not null,
    
    constraint fk_viagem_viagem_avaliacao
    foreign key (id_viagem)
    references tbl_viagem_avaliacao (id),
    
    unique index (id)
);
