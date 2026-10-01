"""Verificador de força de senha e hash seguro de senha (biblioteca padrão).

Conceitos: nunca guardar senha em texto puro; guardar o HASH com "sal" (salt).
"""
import hashlib
import hmac
import secrets
import string


def avaliar_senha(senha):
    """Devolve (pontos, dicas). Pontuação de 0 a 5."""
    dicas = []
    pontos = 0
    if len(senha) >= 12:
        pontos += 1
    else:
        dicas.append("Use pelo menos 12 caracteres.")
    if any(c.islower() for c in senha):
        pontos += 1
    else:
        dicas.append("Inclua letras minúsculas.")
    if any(c.isupper() for c in senha):
        pontos += 1
    else:
        dicas.append("Inclua letras maiúsculas.")
    if any(c.isdigit() for c in senha):
        pontos += 1
    else:
        dicas.append("Inclua números.")
    if any(c in string.punctuation for c in senha):
        pontos += 1
    else:
        dicas.append("Inclua símbolos.")
    return pontos, dicas


def gerar_senha(tamanho=16):
    """Gera senha aleatória usando `secrets` (adequado para segurança)."""
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alfabeto) for _ in range(tamanho))


def gerar_hash(senha, sal=None, iteracoes=200_000):
    """Aplica PBKDF2-SHA256 com sal aleatório. Devolve (sal_hex, hash_hex)."""
    sal = sal or secrets.token_bytes(16)
    resultado = hashlib.pbkdf2_hmac("sha256", senha.encode(), sal, iteracoes)
    return sal.hex(), resultado.hex()


def conferir_senha(senha, sal_hex, hash_hex, iteracoes=200_000):
    """Confere a senha digitada com o hash guardado."""
    _, novo = gerar_hash(senha, bytes.fromhex(sal_hex), iteracoes)
    return hmac.compare_digest(novo, hash_hex)  # comparação segura


if __name__ == "__main__":
    senha = input("Digite uma senha para avaliar: ")
    pontos, dicas = avaliar_senha(senha)
    print(f"Força: {pontos}/5")
    for dica in dicas:
        print(" -", dica)
    sal, h = gerar_hash(senha)
    print("Hash guardado (nunca a senha):", h[:32] + "...")
    print("Confere?", conferir_senha(senha, sal, h))
