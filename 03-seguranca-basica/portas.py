"""Verificador simples de portas TCP abertas.

USO ÉTICO: use SOMENTE no seu próprio computador (127.0.0.1) ou em máquinas
que você tem autorização para testar. Varrer redes alheias é crime/infração.

Como rodar:  python portas.py
"""
import socket

PORTAS_COMUNS = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 5432: "PostgreSQL", 3389: "RDP"}


def porta_aberta(host, porta, tempo=0.5):
    """True se conseguir conectar na porta."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(tempo)
        return s.connect_ex((host, porta)) == 0


def varrer(host="127.0.0.1", portas=PORTAS_COMUNS):
    return {p: (nome, porta_aberta(host, p)) for p, nome in portas.items()}


if __name__ == "__main__":
    for porta, (nome, aberta) in varrer().items():
        print(f"{porta:>5} {nome:<11} {'ABERTA' if aberta else 'fechada'}")
