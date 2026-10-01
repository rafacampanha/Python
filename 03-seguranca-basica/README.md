# Segurança básica em Python

Dois scripts curtos sobre conceitos de segurança da informação (biblioteca padrão apenas).

- `senhas.py`: avalia a força de uma senha, gera senhas aleatórias e guarda senhas com
  **hash PBKDF2 + sal** (nunca em texto puro).
- `portas.py`: verifica quais portas TCP comuns estão abertas em um computador.

> **Uso ético:** rode o verificador de portas só na sua máquina (`127.0.0.1`) ou onde você
> tem autorização.

## Como rodar
```bash
python senhas.py
python portas.py
python -m unittest -v
```

**O que pratica:** criptografia aplicada (hash e sal), análise de risco de senhas, redes
TCP/IP (sockets) e testes automatizados.
