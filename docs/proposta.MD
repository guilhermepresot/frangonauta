# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

Frangonauta

## 2. Integrantes do grupo

- Nome 1: Guilherme Miranda Presot
- Nome 2: Maria Paula Barbosa de Almeida
- Nome 3: Alexandre Ricardo de Moura 
- Nome 4: Ian Souza

## 3. Tipo de jogo

Jogo de desviar de obstáculos e sobrevivência.

## 4. Descrição geral do jogo

Na tela inicial, deve aparecer para iniciar o jogo e o ranking das jogadas feitas, após iniciar a partida, deve aparecer o frango astronauta, em conjunto com os obstáculos, a temperatura atual do frango, possíveis maneiras de aumentar a temperatura dele e batatas assadas (pontuação). O jogador controla a movimentação do frangonauta, além disso, ele deve desviar dos obstáculos, obter o calor necessário para manter o frango quente para não congelar no espaço e coletar o maior número possível de batatas assadas para aumentar a pontuação final. Durante a partida, o jogador deve ter cuidado com dois principais desafios, os meteoros (obstáculos) e com o frio (sobrevivência).

## 5. Objetivo do jogador

Coletar o maior número possível de itens, evitar obstáculos e chegar até o final.

## 6. Regras principais

- Regra 1: O frangonauda começa com 40°C;
- Regra 2: A partida termina quando o jogador atinge algum obstáculo ou a temperatura chegue a 0°C;
- Regra 3: Cada batata coletada vale 15 pontos;
- Regra 4: O jogador vence quando chega ao final do mapa;
- Regra 5: O jogador tem 90 segundos para fazer a tentativa;
- Regra 6: A temperatura do franngonauta diminui a cada 5 segundos.

## 7. Condição de vitória

Chegar até o final da fase.

## 8. Condição de derrota ou encerramento

Temperatura zerada ou não desviar do meteoro.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Um frangonauta controlado pela barra do espaço do teclado.

## Obstáculos, inimigos ou desafios

Meteóros aparecem em posições aleatórias e devem ser evitados e o frio é uma condição que deve ser evitada.

## Itens, alvos ou objetos de interação

Batatas aparecem na tela e aumentam a pontuação quando coletadas e o fogo coletado aumenta a temperatura do frangonauta.

## Pontuação, vidas, tempo ou progresso

O frangonauta começa com 40°C de temperatura e ganha 20°C por fogo coletado. As batatas fazem o jogador ganhar 15 pontos. O jogador tem no total 90 segundos para completar o percurso
 
## 10. Controles previstos

Espaço: salto e ESC: sair do jogo

## 11. Organização inicial do código

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

## 12. Recursos externos previstos

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência.

## 13. Principais dificuldades esperadas

- Dificuldade 1: colisão entre objetos;
- Dificuldade 2: controle de tempo;
- Dificuldade 3: organização do código;
- Dificuldade 4: uso do GitHub;
- Dificuldade 5: testes;
- Dificuldade 6: posição aleatória de objetos.

## 14. Escopo mínimo para a entrega final

A versão mínima do jogo será o personagem (frangonauta) controlado pela tecla do espaço, obstáculos (meteoros) que vão aparecendo e devem ser evitados, sistema de "vida" (temperatura do frango que deve ser controlada para não atingir 0°C), sistema de pontuação (batatas assadas que devem ser coletadas para aumentar a pontuação do ranking), tela de fim de jogo

## 15. Possíveis melhorias, caso haja tempo

- Melhoria 1: tela inicial;
- Melhoria 2: animações;
- Melhoria 3: aumento de dificuldade;
- Melhoria 4: diferentes personagens;
- Melhoria 5: menu de pausa.