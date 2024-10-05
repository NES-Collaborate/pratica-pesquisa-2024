-- Tabela de Usuários
CREATE TABLE
  IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    modulo TEXT NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );

-- Tabela de Questões
CREATE TABLE
  IF NOT EXISTS questoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enunciado TEXT NOT NULL,
    dica TEXT,
    exemplo TEXT,
    resposta TEXT NOT NULL
  );

-- Tabela de Progresso dos Alunos
CREATE TABLE
  IF NOT EXISTS progresso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    questao_id INTEGER,
    resposta_submetida TEXT,
    correto BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
    FOREIGN KEY (questao_id) REFERENCES questoes (id)
  );

-- Índices para melhorar a performance
CREATE INDEX IF NOT EXISTS idx_progresso_usuario ON progresso (usuario_id);

CREATE INDEX IF NOT EXISTS idx_progresso_questao ON progresso (questao_id);