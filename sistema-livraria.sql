-- 1️⃣ Cria a tabela Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT,
    cidade TEXT
);

-- 2️⃣ Insere dados na tabela Clientes
INSERT INTO Clientes (nome, email, telefone, cidade) VALUES
('Ana Silva', 'ana.silva@email.com', '11999990001', 'São Paulo'),
('Carlos Souza', 'carlos.souza@email.com', '21988880002', 'Rio de Janeiro'),
('Beatriz Lima', 'beatriz.lima@email.com', '31977770003', 'Belo Horizonte'),
('Eduardo Pereira', 'eduardo.pereira@email.com', '41966660004', 'Curitiba');

-- 3️⃣ Consulta todos os dados da tabela Clientes
SELECT * FROM Clientes;

-- 1️⃣ Cria as tabelas

CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (livro_id) REFERENCES Livros(id)
);

-- 2️⃣ Insere dados de exemplo

-- Clientes
INSERT INTO Clientes (nome) VALUES
('Ana Silva'),
('Carlos Souza'),
('Beatriz Lima');

-- Livros
INSERT INTO Livros (nome) VALUES
('O Pequeno Príncipe'),
('Dom Casmurro'),
('Harry Potter');

-- Compras (quem comprou qual livro)
INSERT INTO Compras (cliente_id, livro_id) VALUES
(1, 1), -- Ana Silva comprou "O Pequeno Príncipe"
(1, 3), -- Ana Silva comprou "Harry Potter"
(2, 2), -- Carlos Souza comprou "Dom Casmurro"
(3, 3); -- Beatriz Lima comprou "Harry Potter"

-- 3️⃣ Consulta com INNER JOIN
SELECT 
    Clientes.nome AS Cliente, 
    Livros.nome AS Livro
FROM 
    Compras
INNER JOIN Clientes ON Compras.cliente_id = Clientes.id
INNER JOIN Livros ON Compras.livro_id = Livros.id;
