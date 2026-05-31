# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

Frangonauta

## 2. Integrantes do grupo

- Nome 1: Guilherme Miranda Presot
- Nome 2: Maria Paula Barbosa de Almeida
- Nome 3: Alexandre Ricardo de Moura 
- Nome 4: Ian Souza Maciel

## 3. Tipo de jogo

Jogo de sobrevivência por tempo com desvio de obstáculos.

## 4. Descrição geral do jogo

Na tela inicial aparecem a opção de iniciar o jogo e o ranking das partidas anteriores. Após iniciar, o jogador controla o Frangonauta (um frango astronauta que se move pelo espaço usando as setas do teclado). Na tela aparecem meteoros como obstáculos, itens de fogo para aquecer o frango e batatas assadas para pontuar. O jogador deve sobreviver os 90 segundos completos desviando dos meteoros, coletando fogo para manter a temperatura acima de 0 °C e coletando batatas para maximizar a pontuação final.

## 5. Objetivo do jogador

Sobreviver pelo tempo máximo de 90 segundos, mantendo a temperatura do Frangonauta acima de 0 °C e coletando o maior número possível de batatas assadas para atingir a maior pontuação no ranking.

## 6. Regras principais

- O Frangonauta começa com 40°C de temperatura;
- A temperatura diminui 8 °C a cada 5 segundos;
- Coletar um item de fogo aumenta a temperatura em 20 °C;
- Cada batata assada coletada vale 15 pontos;
- A partida termina se o jogador colidir com um meteoro ou se a temperatura chegar a 0 °C;
- O jogador vence se sobreviver os 90 segundos completos.

## 7. Condição de vitória

Completar os 90 segundos sem que a temperatura chegue a 0 °C.

## 8. Condição de derrota ou encerramento

A partida termina quando o Frangonauta colide com um meteoro ou quando sua temperatura atinge 0 °C.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

O Frangonauta, controlado pelas setas do teclado (cima, baixo, esquerda, direita), movendo-se livremente pela tela.

## Obstáculos, inimigos ou desafios

Meteoros surgem em posições aleatórias na tela e devem ser evitados. O frio é um desafio constante: a temperatura cai a cada 5 segundos de partida.

## Itens, alvos ou objetos de interação

Batatas assadas aparecem na tela e valem 15 pontos cada ao serem coletadas. Itens de fogo aparecem na tela e aumentam a temperatura do Frangonauta em 20 °C ao serem coletados.

## Pontuação, vidas, tempo ou progresso

O Frangonauta começa com 40 °C. A temperatura cai 8 °C a cada 5 segundos. O jogador tem 90 segundos para sobreviver e acumular pontos com as batatas coletadas.
 
## 10. Controles previstos

- tecla de espaço: salto
- ESC: sair do jogo

## 11. Organização inicial do código

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal, usa listas para meteoros, itens de fogo e batatas na tela;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares, inclui funções de colisão e controle de temperatura, que serão testadas;
- `src/dados.py`: contém funções de leitura e escrita de arquivos, salva e carrega o ranking (nome e pontuação) em arquivo .txt ou .json; usa lista de dicionários.

## 12. Recursos externos previstos

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência.

## 13. Testes planejados

- Funcionais: garantir que todas as funcionalidades ocorram
- Jogabilidade: avaliar dificuldade e diversão do jogo
- Desempenho: medir o uso de memória e estabilidade

## 14. Principais dificuldades esperadas

- Colisão entre objetos
- Controle de tempo e queda de temperatura
- Organização do código
- Uso do GitHub
- Testes
- Posicionamento aleatório de objetos na tela

## 15. Escopo mínimo para a entrega final

A versão mínima do jogo contará com: o Frangonauta controlado pelas setas do teclado; meteoros surgindo aleatoriamente e que devem ser desviados; sistema de temperatura (começa em 40 °C, cai 8 °C cada 5 segundos e encerra o jogo ao chegar a 0 °C); itens de fogo que recuperam temperatura; sistema de pontuação com batatas assadas; contador de 90 segundos; e tela de fim de jogo com pontuação.

## 15. Possíveis melhorias, caso haja tempo

- Tela inicial com menu e ranking
- Animações do personagem e dos objetos
- Aumento progressivo de dificuldade (mais meteoros, queda de temperatura mais rápida)
- Diferentes personagens selecionáveis
- Menu de pausa
- Sons e trilha sonora
