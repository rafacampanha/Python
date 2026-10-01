# Sistema de chamados de suporte (CRUD com SQLite)

Programa de terminal para registrar e acompanhar chamados de suporte técnico.

**O que pratica:** Python, SQL (`INSERT`, `SELECT`, `UPDATE`, `DELETE`), banco SQLite,
funções, tratamento de erros e testes automatizados.

## Como rodar
Não precisa instalar nada (só Python 3.9+).

```bash
python chamados.py          # abre o menu
python -m unittest -v       # roda os testes
```

## Funcionalidades
- Criar chamado (título e descrição)
- Listar chamados, com filtro por status (`aberto`, `em andamento`, `resolvido`)
- Atualizar o status
- Apagar chamado

## Estrutura
- `chamados.py`: funções do CRUD e o menu
- `test_chamados.py`: testes (usam banco em memória)

## Ideias para evoluir
Adicionar prioridade e responsável, exportar para CSV, criar uma interface gráfica (Tkinter).
