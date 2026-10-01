"""Sistema simples de chamados de suporte (CRUD com SQLite).

CRUD = Create, Read, Update, Delete (criar, ler, atualizar, apagar).
Usa apenas a biblioteca padrão do Python, então não precisa instalar nada.

Como rodar:  python chamados.py
"""
import sqlite3
from datetime import datetime

BANCO = "chamados.db"
STATUS_VALIDOS = ("aberto", "em andamento", "resolvido")


def conectar(caminho=BANCO):
    """Abre o banco e cria a tabela se ela ainda não existir."""
    conexao = sqlite3.connect(caminho)
    conexao.execute(
        """CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL DEFAULT 'aberto',
            criado_em TEXT NOT NULL
        )"""
    )
    return conexao


def criar(conexao, titulo, descricao=""):
    """CREATE: registra um novo chamado e devolve o id dele."""
    if not titulo.strip():
        raise ValueError("O título não pode ser vazio.")
    agora = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor = conexao.execute(
        "INSERT INTO chamados (titulo, descricao, criado_em) VALUES (?, ?, ?)",
        (titulo.strip(), descricao.strip(), agora),
    )
    conexao.commit()
    return cursor.lastrowid


def listar(conexao, status=None):
    """READ: devolve todos os chamados (ou só os de um status)."""
    if status:
        linhas = conexao.execute(
            "SELECT id, titulo, status, criado_em FROM chamados WHERE status = ? ORDER BY id",
            (status,),
        )
    else:
        linhas = conexao.execute(
            "SELECT id, titulo, status, criado_em FROM chamados ORDER BY id"
        )
    return linhas.fetchall()


def atualizar_status(conexao, id_chamado, novo_status):
    """UPDATE: muda o status de um chamado. Devolve True se achou o chamado."""
    if novo_status not in STATUS_VALIDOS:
        raise ValueError(f"Status inválido. Use: {', '.join(STATUS_VALIDOS)}")
    cursor = conexao.execute(
        "UPDATE chamados SET status = ? WHERE id = ?", (novo_status, id_chamado)
    )
    conexao.commit()
    return cursor.rowcount > 0


def apagar(conexao, id_chamado):
    """DELETE: remove um chamado. Devolve True se achou o chamado."""
    cursor = conexao.execute("DELETE FROM chamados WHERE id = ?", (id_chamado,))
    conexao.commit()
    return cursor.rowcount > 0


def menu():
    conexao = conectar()
    while True:
        print("\n1) Novo chamado  2) Listar  3) Mudar status  4) Apagar  0) Sair")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                print("Chamado criado com id", criar(conexao, titulo, descricao))
            elif opcao == "2":
                for linha in listar(conexao):
                    print(linha)
            elif opcao == "3":
                id_chamado = int(input("Id do chamado: "))
                status = input(f"Novo status ({'/'.join(STATUS_VALIDOS)}): ")
                print("OK" if atualizar_status(conexao, id_chamado, status) else "Id não encontrado.")
            elif opcao == "4":
                id_chamado = int(input("Id do chamado: "))
                print("Apagado." if apagar(conexao, id_chamado) else "Id não encontrado.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print("Erro:", erro)
    conexao.close()


if __name__ == "__main__":
    menu()
