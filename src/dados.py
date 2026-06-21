def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0
    
def ler_ranking(caminho_arquivo):
    """Lê o arquivo e cria uma lista com todos os elementos dela"""
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().split()
    return conteudo

def salvar_ranking(nome, caminho_arquivo, pontuação):
    """Salva as pontuações em um ranking"""
    if nome != "":
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
            conteudo = arquivo.write(f"{nome} {pontuação}\n")

def reordenar_ranking(caminho_arquivo):
    conteudo = ler_ranking(caminho_arquivo)
    pares = []
    for i in range(0, len(conteudo), 2):
        pares.append((conteudo[i], int(conteudo[i+1])))
    pares.sort(key=lambda x: x[1], reverse=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        conteudo = arquivo.write("")
    for j in range(len(pares)):
        with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
                conteudo = arquivo.write(f"{pares[j][0]} {pares[j][1]}\n")