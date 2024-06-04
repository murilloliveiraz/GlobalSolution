create database db_sustaintravel;

use db_sustaintravel;

create table tbl_viagem(
	id int not null auto_increment primary key,
    lugar varchar(200) not null,
    qtd_dias int not null,
    qtd_noites int not null,
    avaliacao_media float,
    imagem text not null,
    unique index(id)
);


create table tbl_viagem_avaliacao (
	id int not null auto_increment primary key,
    avaliacao float not null,
    id_viagem int not null,
    
    constraint fk_viagem_viagem_avaliacao
    foreign key (id_viagem)
    references tbl_viagem (id),
    
    unique index (id)
);

create table tbl_tag (
	id int not null auto_increment primary key,
    nome varchar(100) not null,
    
    unique index (id)
);

create table tbl_tag_viagem (
	id int not null auto_increment primary key,
	id_viagem int not null,
    id_tag int not null,
    
    constraint fk_viagem_tag_viagem
    foreign key (id_viagem)
    references tbl_viagem (id),
    
    constraint fk_tag_tag_viagem
    foreign key (id_tag)
    references tbl_tag (id),
    
    unique index (id)
);