create database agenda

use agenda

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50),
    telefone VARCHAR(20),
    mensegem VARCHAR(255)
);

select * from usuarios

INSERT INTO usuarios
(nome, email, telefone, mensegem)
values("Gabriel", "anjosgabriel86@gmail.com", "11 97777-7777","primeiro cadastro")