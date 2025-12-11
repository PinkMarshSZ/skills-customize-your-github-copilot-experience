
```markdown

# 🎮 Jogos em Python — Forca (Hangman)

## 🎯 Objetivo

Construir uma versão jogável da Forca em Python para praticar manipulação de strings, estruturas de repetição, condicionais e entrada do usuário.

## ⏱️ Duração estimada

1–2 horas

## ⚙️ Nível

Intermediário

## 🧠 Habilidades praticadas

- Manipulação de strings
- Estruturas de repetição (`for` / `while`)
- Condicionais (`if` / `else`)
- Uso de listas e funções
- Entrada/saída no terminal

## 📁 Arquivos

- `starter-code.py` — esqueleto inicial com pontos para completar

## 📝 Tarefas

### 🛠️ Implementar o jogo da Forca

#### Descrição
Implemente a lógica principal do jogo: seleção aleatória de palavra, recebimento de palpites do jogador, atualização do estado exibido e controle de tentativas restantes.

#### Requisitos
O programa completo deve:

- Selecionar aleatoriamente uma palavra a partir de uma lista definida no código.
- Mostrar o estado atual da palavra com letras descobertas e underlines para letras não adivinhadas (ex.: `_ a _ _ m a n`).
- Aceitar palpites de letras do usuário (uma letra por vez) e atualizar o estado.
- Rastrear letras já chutadas e impedir chutadas repetidas sem penalidade adicional.
- Diminuir o número de tentativas ao errar (ex.: 6 tentativas iniciais).
- Terminar o jogo com mensagem de vitória quando todas as letras forem descobertas.
- Terminar o jogo com mensagem de derrota quando as tentativas acabarem e revelar a palavra correta.

### 🛠️ Melhorias opcionais (extra)

#### Descrição
Adicione funcionalidades extras para exercitar organização do código e recursos adicionais de jogo.

#### Requisitos (opcionais)

- Implementar níveis de dificuldade que alteram o número de tentativas ou o conjunto de palavras.
- Salvar/mostrar um placar simples em um arquivo (`scores.txt`).
- Exibir arte ASCII progressiva da forca a cada erro.
- Carregar a lista de palavras a partir de um arquivo externo.

## ▶️ Como executar

No terminal, dentro da pasta do exercício, rode:

```bash
python3 starter-code.py
```

## ✅ Critérios de avaliação

- O jogo executa sem erros e segue os requisitos mínimos.
- A interface no terminal é clara e informa tentativas, letras chutadas e estado atual da palavra.
- O código é organizado em funções e fácil de ler.

## 🔗 Recursos

- Documentação Python: https://docs.python.org/3/
- Módulo `random`: https://docs.python.org/3/library/random.html

Boa prática: comente partes do código e escreva funções pequenas para facilitar testes e reuso.

```

# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
