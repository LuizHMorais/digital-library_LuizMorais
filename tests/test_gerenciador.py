# test_gerenciador.py
# Arquivo de testes para as funções do gerenciador

import os
from app import gerenciador

# Testa se a função adicionar_documento adiciona corretamente o arquivo ao diretório de destino
def test_adicionar_documento(tmp_path):
    # Cria um arquivo de teste na origem
    origem = tmp_path / "arquivo_teste.txt"
    origem.write_text("Conteúdo de teste")

    # Define o diretório base da biblioteca dentro da pasta temporária
    gerenciador.BASE_DIR = tmp_path / "biblioteca"

    # Executa a função para adicionar o documento ao ano 2022
    gerenciador.adicionar_documento(origem, "2022")

    # Verifica se o arquivo foi copiado corretamente
    destino = gerenciador.BASE_DIR / "2022" / "arquivo_teste.txt"
    assert destino.exists()
    assert destino.read_text() == "Conteúdo de teste"

# Testa se a função listar_documentos retorna os arquivos no formato esperado
def test_listar_documentos(tmp_path):
    # Cria estrutura de arquivos simulada
    base = tmp_path / "biblioteca"
    (base / "2023").mkdir(parents=True)
    (base / "2023" / "doc1.pdf").write_text("PDF 1")
    (base / "2023" / "doc2.pdf").write_text("PDF 2")

    # Redefine o diretório base da biblioteca
    gerenciador.BASE_DIR = base

    # Executa a função e verifica o retorno
    resultado = gerenciador.listar_documentos()
    assert "pdf" in resultado
    assert "2023" in resultado["pdf"]
    assert "doc1.pdf" in resultado["pdf"]["2023"]
    assert "doc2.pdf" in resultado["pdf"]["2023"]

# Testa a função de renomear um documento
def test_renomear_documento(tmp_path):
    base = tmp_path / "biblioteca"
    (base / "2024").mkdir(parents=True)
    original = base / "2024" / "velho_nome.txt"
    original.write_text("arquivo original")

    gerenciador.BASE_DIR = base
    gerenciador.renomear_documento("2024", "velho_nome.txt", "novo_nome.txt")

    novo = base / "2024" / "novo_nome.txt"
    assert novo.exists()
    assert novo.read_text() == "arquivo original"

# Testa a função de remover um documento
def test_remover_documento(tmp_path):
    base = tmp_path / "biblioteca"
    (base / "2025").mkdir(parents=True)
    arquivo = base / "2025" / "deletar.txt"
    arquivo.write_text("deletar isso")

    gerenciador.BASE_DIR = base
    gerenciador.remover_documento("2025", "deletar.txt")

    assert not arquivo.exists()