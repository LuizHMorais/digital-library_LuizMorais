from pathlib import Path
import shutil

# Diretório base onde os documentos da biblioteca serão armazenados.
# Pode conter subpastas com o ano de publicação dos documentos.
BASE_DIR = Path("biblioteca")

# Função para listar todos os documentos, agrupados por extensão e ano de publicação.
def listar_documentos():
    arquivos = {}  # Dicionário que armazenará os arquivos organizados por extensão e ano.

    # Percorre todos os arquivos dentro da estrutura de diretórios da biblioteca.
    for arquivo in BASE_DIR.rglob("*.*"):  # Procura recursivamente por todos os arquivos com extensão.
        if arquivo.is_file():  # Verifica se é realmente um arquivo (ignora diretórios).
            extensao = arquivo.suffix.lstrip(".")  # Extrai a extensão do arquivo (sem o ponto).
            ano = arquivo.parent.name  # Considera o nome da pasta pai como o ano do documento.

            # Organiza os arquivos em um dicionário aninhado: {extensao: {ano: [nomes]}}
            arquivos.setdefault(extensao, {}).setdefault(ano, []).append(arquivo.name)

    if not arquivos:
        print("Nenhum documento encontrado na biblioteca.")
    return arquivos  # Retorna o dicionário com a organização dos arquivos.

# Função para adicionar um novo documento à biblioteca, dentro da pasta correspondente ao ano.
def adicionar_documento(caminho_origem, ano):
    try:
        origem = Path(caminho_origem).resolve(strict=True)  # Resolve o caminho absoluto e verifica se existe
    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho_origem}' não foi encontrado.")
        return

    destino = BASE_DIR / str(ano)  # Cria o caminho de destino usando o ano informado
    destino.mkdir(parents=True, exist_ok=True)  # Garante que a pasta existe (cria se necessário)

    destino_arquivo = destino / origem.name
    shutil.copy(origem, destino_arquivo)  # Copia o arquivo da origem para o destino
    print(f"Arquivo '{origem.name}' adicionado com sucesso em '{destino}/'.")

# Função para renomear um documento existente na pasta do respectivo ano.
def renomear_documento(ano, nome_antigo, nome_novo):
    caminho = BASE_DIR / str(ano) / nome_antigo
    novo_caminho = BASE_DIR / str(ano) / nome_novo

    if not caminho.exists():
        print(f"Erro: o arquivo '{nome_antigo}' não foi encontrado na pasta '{ano}'.")
        return

    caminho.rename(novo_caminho)
    print(f"Arquivo '{nome_antigo}' renomeado para '{nome_novo}' com sucesso.")

# Função para remover um documento da pasta correspondente ao ano.
def remover_documento(ano, nome_arquivo):
    caminho = BASE_DIR / str(ano) / nome_arquivo

    if not caminho.exists():
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado na pasta '{ano}'.")
        return

    caminho.unlink()
    print(f"Arquivo '{nome_arquivo}' removido com sucesso.")