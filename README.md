# Frangonauta

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Guilherme Miranda Presot
- Maria Paula Barbosa de Almeida
- Alexandre Ricardo de Moura 
- Ian Souza

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Na tela inicial, deve aparecer para iniciar o jogo e o ranking das jogadas feitas, após iniciar a partida, deve aparecer o frango astronauta, em conjunto com os obstáculos e batatas assadas (pontuação). O jogador controla a movimentação do frangonauta, além disso, ele deve desviar dos obstáculos e coletar o maior número possível de batatas assadas para aumentar a pontuação final. Durante a partida, o jogador deve ter cuidado com um desafio principal, os meteoros (obstáculos).

## Objetivo do jogador

Coletar o maior número possível de itens, evitar obstáculos e chegar até o final.

## Regras do jogo

- Regra 1: Cada batata coletada vale 15 pontos;
- Regra 2: O jogador vence quando chega ao final do mapa;
- Regra 3: O jogador tem 30 segundos para fazer a tentativa;

## Controles

Espaço: salto

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
