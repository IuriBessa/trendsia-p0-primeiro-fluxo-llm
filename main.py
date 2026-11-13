import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

PROMPT_SISTEMA = (
    "Você resume textos explicativos em português. "
    "Responda sempre neste formato:\n"
    "RESUMO: até 3 frases.\n"
    "PONTOS PRINCIPAIS:\n"
    "- de 3 a 5 tópicos curtos.\n"
    "Use só informações que estão no texto. Não invente nada."
)


def ler_config():
    base_url = os.getenv("LLM_BASE_URL")
    modelo = os.getenv("LLM_MODEL")
    chave = os.getenv("LLM_API_KEY", "")
    if not base_url or not modelo:
        sys.exit("Configure LLM_BASE_URL e LLM_MODEL no arquivo .env")
    return base_url.rstrip("/"), modelo, chave


def ler_entrada():
    print("Cole o texto e finalize com Ctrl+D (Linux/Mac) ou Ctrl+Z e Enter (Windows):")
    return sys.stdin.read().strip()


def chamar_llm(texto, base_url, modelo, chave):
    url = f"{base_url}/chat/completions"
    headers = {"Content-Type": "application/json"}
    if chave:
        headers["Authorization"] = f"Bearer {chave}"
    corpo = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": PROMPT_SISTEMA},
            {"role": "user", "content": texto},
        ],
    }
    resposta = requests.post(url, headers=headers, json=corpo, timeout=60)
    resposta.raise_for_status()
    dados = resposta.json()
    return dados["choices"][0]["message"]["content"]


def main():
    base_url, modelo, chave = ler_config()
    texto = ler_entrada()
    if not texto:
        sys.exit("Nenhum texto recebido.")
    resultado = chamar_llm(texto, base_url, modelo, chave)
    print("\n" + resultado)


if __name__ == "__main__":
    main()