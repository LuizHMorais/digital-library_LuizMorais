# Relatório do Projeto

# Relatório de Testes e Feedback

## Metodologia de Testes

Os testes foram implementados com a biblioteca `pytest`, simulando diretórios e arquivos temporários por meio do fixture `tmp_path`.

Cada função do sistema foi testada individualmente:
- `listar_documentos`: verificando a estrutura esperada por tipo e ano.
- `adicionar_documento`: assegurando a cópia correta para a pasta de destino.
- `renomear_documento`: validando a renomeação sem perda de conteúdo.
- `remover_documento`: confirmando a exclusão do arquivo.

## Feedback Simulado

> O bibliotecário relatou que a interface de linha de comando foi fácil de usar, porém sugeriu que as mensagens de erro fossem mais claras.

## Melhorias aplicadas com base no feedback

- Mensagens de erro foram ajustadas no `biblioteca_digital.py` para orientar corretamente o usuário quando argumentos obrigatórios estão ausentes.

## Conclusão

O sistema foi validado com testes automatizados e ajustado com base em feedback. Está funcional, modular e preparado para uso básico em ambiente de simulação acadêmica.