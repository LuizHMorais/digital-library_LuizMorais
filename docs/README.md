# digital-library_LuizMorais
# Sistema de Biblioteca Digital

Este é um projeto acadêmico desenvolvido como parte de uma atividade prática, com o objetivo de simular um sistema de gerenciamento de documentos digitais em uma biblioteca universitária.

## Funcionalidades

- Listar documentos digitais por tipo e ano.
- Adicionar novos arquivos à biblioteca.
- Renomear documentos existentes.
- Remover documentos específicos.

## Como executar

```bash
python biblioteca_digital.py listar
python biblioteca_digital.py adicionar --origem caminho/arquivo.pdf --ano 2023
python biblioteca_digital.py renomear --ano 2023 --arquivo antigo.pdf --novo_nome novo.pdf
python biblioteca_digital.py remover --ano 2023 --arquivo arquivo.pdf
```
## ⚠️ Caminhos com espaços devem ser entre aspas. Exemplo:
python biblioteca_digital.py adicionar --origem "meu arquivo.pdf" --ano 2023
