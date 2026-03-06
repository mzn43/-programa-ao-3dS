-- 1. Criação da tabela LIVROS
CREATE TABLE LIVROS (
    ID INT PRIMARY KEY,
    TITULO VARCHAR(100),
    AUTOR VARCHAR(100),
    ANO_PUBLICACAO INT
);

-- 2. Inserção de dados na tabela
INSERT INTO LIVROS (ID, TITULO, AUTOR, ANO_PUBLICACAO)
VALUES
    (1, 'Dom Casmurro', 'Machado de Assis', 1899),
    (2, 'O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943),
    (3, '1984', 'George Orwell', 1949);

-- 3. Exibir a tabela completa
SELECT * FROM LIVROS;
