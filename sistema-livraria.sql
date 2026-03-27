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
