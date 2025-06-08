# Script principal para execução da aplicação via linha de comando

import argparse
from app.gerenciador import listar_documentos, adicionar_documento, renomear_documento, remover_documento

# Função principal que configura e executa a interface de linha de comando
def main():
    # Cria o parser de argumentos
    parser = argparse.ArgumentParser(description="Sistema de Gerenciamento de Biblioteca Digital")

    # Define a ação obrigatória que o usuário deve informar
    parser.add_argument("acao", choices=["listar", "adicionar", "renomear", "remover"], help="Ação a ser executada")

    # Argumentos adicionais que podem ser usados dependendo da ação escolhida
    parser.add_argument("--ano", help="Ano do documento")
    parser.add_argument("--arquivo", help="Nome do arquivo (para renomear ou remover)")
    parser.add_argument("--novo_nome", help="Novo nome para o arquivo (para renomear)")
    parser.add_argument("--origem", help="Caminho de origem do arquivo a ser adicionado")

    # Faz o parsing dos argumentos passados na linha de comando
    args = parser.parse_args()

    # Executa a ação correspondente
    if args.acao == "listar":
        resultado = listar_documentos()
        for extensao, anos in resultado.items():
            print(f"\nArquivos .{extensao}:")
            for ano, arquivos in anos.items():
                print(f"  {ano}: {', '.join(arquivos)}")

    elif args.acao == "adicionar":
        if args.origem and args.ano:
            adicionar_documento(args.origem, args.ano)
            print("Documento adicionado com sucesso.")
        else:
            print("Erro: argumentos '--origem' e '--ano' são obrigatórios para adicionar.")

    elif args.acao == "renomear":
        if args.ano and args.arquivo and args.novo_nome:
            renomear_documento(args.ano, args.arquivo, args.novo_nome)
            print("Documento renomeado com sucesso.")
        else:
            print("Erro: argumentos '--ano', '--arquivo' e '--novo_nome' são obrigatórios para renomear.")

    elif args.acao == "remover":
        if args.ano and args.arquivo:
            remover_documento(args.ano, args.arquivo)
            print("Documento removido com sucesso.")
        else:
            print("Erro: argumentos '--ano' e '--arquivo' são obrigatórios para remover.")

# Executa a função main se o arquivo for chamado diretamente
if __name__ == "__main__":
    main()