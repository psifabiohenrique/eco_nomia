import ollama


def checa_ollama_esta_executando() -> bool:
    """
    Verifica se o servidor do ollama está sendo executado e retorna True se estiver, ou False se não estiver
    """
    resposta = ollama.ps()
    if isinstance(resposta.models, list) and len(resposta.models) > 0:
        return True
    else:
        return False


def requisicao_ollama(input_usuario: str, input_sistema: str | None = None) -> str:
    """
    Recebe obrigatóriamente um input de usuário e opcionalmente um input de sistema. Envia para um modelo de IA do ollama processar as entradas.
    """

    mensagens = []
    if input_sistema is not None:
        mensagens.append({"role": "system", "content": input_sistema})

    mensagens.append({"role": "user", "content": input_usuario})

    resposta = ollama.chat(model="llama3.1:8b", messages=mensagens)
    if isinstance(resposta.message.content, str):
        return resposta.message.content
    return "Não foi possível processar o input"
