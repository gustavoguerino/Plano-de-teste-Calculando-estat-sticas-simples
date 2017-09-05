# Plano de teste - Calculando estastísticas simples 

## Identificação

Objetivo: teste unitário
Problema - http://dojopuzzles.com/problemas/exibe/calculando-estatisticas-simples/


## Plano de teste - Sequência de números

| Entrada             | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| seqNumeros          | seqNumeros ]- infinto,+ infinito]   | sizeSqn(seqNumeros) != NULL      | sizeSqn(seqNumeros) == NULL   |
|                     | seqNumeros é do tipo int            | tipo(seqNumeros) == int          | tipo(seqNumeros) != int       |
|                     |                                     |                                  |                               |

```java
public boolean is_sizeSqn(seqNumeros):
  return True
```

### 1º caso de teste (Tipo seqNumeros igual a int)

```java
is_sizeSqn(1) == True
```

### 2º caso de teste (Tipo seqNumeros diferente de int)

```java
is_size("testeDeSoftware") # Lançará uma exceção.
```
```java
is_size("7.0") # Lançará uma exceção.
```

# Dentro da função sizeSqn() 
  #### O sistema pedirá para o usuário inserir os valores.
  #### Assim que o usuário terminar de inserir, o sistema informará os dados com as seguintes funções.
-----------------------------------------------------------------------------------------------------------------------------------------
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
