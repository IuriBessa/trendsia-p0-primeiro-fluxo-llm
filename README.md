# Resumidor de textos explicativos

Programa em Python que recebe um texto explicativo pelo terminal e devolve
um resumo curto com os principais pontos, usando um LLM via API.

## Requisitos

- Python 3.14.4
- Uma chave de API de um LLM com formato compatível com OpenAI
  (neste projeto: Google Gemini, modelo `gemini-3.5-flash`)

## Instalação

```
git clone https://github.com/IuriBessa/trendsia-p0-primeiro-fluxo-llm.git
cd trendsia-p0-primeiro-fluxo-llm
python -m venv .venv
```

Ative o ambiente virtual:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Linux/Mac: `source .venv/bin/activate`

Instale as dependências:

```
pip install -r requirements.txt
```

## Configuração

1. Copie o arquivo de exemplo:
   - Windows: `copy .env.example .env`
   - Linux/Mac: `cp .env.example .env`
2. Preencha o `.env`:

| Variável | O que é | Exemplo |
|---|---|---|
| `LLM_BASE_URL` | Endereço base da API | `https://generativelanguage.googleapis.com/v1beta/openai` |
| `LLM_MODEL` | Nome do modelo | `gemini-3.5-flash` |
| `LLM_API_KEY` | Sua chave de API | |

A chave é criada gratuitamente no Google AI Studio (aistudio.google.com/api-keys).
O arquivo `.env` não vai pro Git.

## Como executar

```
python main.py
```

Cole o texto e finalize a entrada com **Ctrl+D** (Linux/Mac) ou
**Ctrl+Z** e Enter (Windows). Também dá pra usar um arquivo:

```
python main.py < meu_texto.txt
```

## Exemplo de saída

RESUMO:
A história da computação começou na Antiguidade com ferramentas como o ábaco e evoluiu até a criação da Máquina Analítica e do primeiro algoritmo no século XIX. No século XX, o avanço dos computadores eletrônicos, impulsionado por invenções como o transistor e o microprocessador, permitiu o surgimento dos computadores pessoais. A partir dos anos 1990, a internet, os smartphones e a inteligência artificial consolidaram a computação como um meio global e conectado.

PONTOS PRINCIPAIS:
- Origem com instrumentos mecânicos antigos e o pioneirismo de Charles Babbage e Ada Lovelace no século XIX.
- Transição para a era eletrônica no século XX com Alan Turing e a construção do ENIAC.
- Invenção do transistor e dos microprocessadores, que tornaram os computadores menores, mais rápidos e pessoais.
- Expansão global a partir da década de 1990 com a internet, a computação em nuvem e os smartphones.
- Nova fase atual marcada pela inteligência artificial, aprendizado de máquina e computação quântica.

## Estrutura do repositório

```
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Limitações conhecidas

- Só aceita texto puro.
- Textos muito longos podem exceder o limite do modelo.
- O resumo pode omitir ou distorcer informações; confira o resultado.
- Erros de rede ou de chave ainda não têm tratamento específico.

## LLM utilizado

Provedor: Google (Gemini API). Modelo: `gemini-3.5-flash`.