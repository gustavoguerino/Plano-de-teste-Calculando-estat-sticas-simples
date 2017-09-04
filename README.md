# Plano de teste - Calculando estastísticas simples 

## Identificação

Objetivo: teste unitário
Problema - http://dojopuzzles.com/problemas/exibe/calculando-estatisticas-simples/

## Plano de teste - valor mínimo

| Entrada             | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| seqNumeros          | sizeSqn(seqNumeros)                 | sizeSqn(seqNumeros) != NULL      | sizeSqn(seqNumeros) == NULL   |
| numeros             | sizeSqn(seqNumeros) == 1            | sizeSqn(seqNumeros) == numeros   | sizeSqn(seqNumeros) != numeros|
|                     | seqNumeros é do tipo int            | valorMínimo(seqNumero) == int   | valorMínimo(seqNumero) != int |
||| ano % 100 = 0 && ano % 400 == 0| ano % 400 != 0 |
|| ano é do tipo Int | tipo(ano) == Int | tipo(ano) != Int |


## Plano de teste - valor máximo

| Entrada             | Condição                            | Classes Válidas                 | Classes Inválidas          |
| -------------       | -------------                       | --------------------------------| ----------------           |
| seqNumeros          | seqNumeros [- infinito, + infinito] | seqNumeros = int ---------------| seqNumeros != int ---------|
|                     |                                     | menorValor = seqNumero          | menor              |
||| ano % 100 = 0 && ano % 400 == 0| ano % 400 != 0 |
|| ano é do tipo Int | tipo(ano) == Int | tipo(ano) != Int |

## Plano de teste - número de elementos na seqüência

| Entrada             | Condição                            | Classes Válidas                 | Classes Inválidas          |
| -------------       | -------------                       | --------------------------------| ----------------           |
| seqNumeros          | seqNumeros [- infinito, + infinito] | seqNumeros = int ---------------| seqNumeros != int ---------|
|                     |                                     | menorValor = seqNumero          | menor              |
||| ano % 100 = 0 && ano % 400 == 0| ano % 400 != 0 |
|| ano é do tipo Int | tipo(ano) == Int | tipo(ano) != Int |

## Plano de teste - valor mínimo

| Entrada             | Condição                            | Classes Válidas                 | Classes Inválidas          |
| -------------       | -------------                       | --------------------------------| ----------------           |
| seqNumeros          | seqNumeros [- infinito, + infinito] | seqNumeros = int ---------------| seqNumeros != int ---------|
|                     |                                     | menorValor = seqNumero          | menor              |
||| ano % 100 = 0 && ano % 400 == 0| ano % 400 != 0 |
|| ano é do tipo Int | tipo(ano) == Int | tipo(ano) != Int |
