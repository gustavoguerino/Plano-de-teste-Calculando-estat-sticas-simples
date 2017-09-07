# Plano de teste - Calculando estastísticas simples 

## Identificação

Objetivo: teste unitário
Problema - http://dojopuzzles.com/problemas/exibe/calculando-estatisticas-simples/


## Plano de teste - Sequência de números

| Entrada             | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| seqNumeros          | seqNumeros ]- infinto,+ infinito]   | sizeSqn(seqNumeros) != NULL AND sizeSqn(seqNumeros) > 1  |sizeSqn(seqNumeros) == 1   |
|                     | seqNumeros é do tipo int            | tipo(seqNumeros) == int          | tipo(seqNumeros) != int       |
| valor               | valor é do tipo int                 | tipo(valor) == int               | tipo(valor) != int       |

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
  #### O sistema pedirá ao usuário para inserir os valores.
  
  ### 3º caso de teste (Tipo valor igual a int)

```java
valor(2) == True
```
  ### 4º caso de teste (Tipo valor diferente de int)

```java
valor("testeDeSoftware") # Lançará uma exceção.
```
```java
valor("8.0") # Lançará uma exceção.
```
  
  #### Assim que o usuário terminar de inserir, o sistema informará os dados com as seguintes funções.
-----------------------------------------------------------------------------------------------------------------------------------------
## Plano de teste - valor mínimo

| Saída               | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| minimo               |  minimo ] menor valor]             | minimo < seqNumeros              | minimo > seqNumeros           |

  ### 5º caso de teste (minimo é menor valor da sequencia)
 ```java
minimo < sqlNumeros == true.
```

  ### 6º caso de teste (minimo é diferente do menor valor da sequencia)
 ```java
minimo < sqlNumeros == false.
```

## Plano de teste - valor máximo

| Saída               | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| maximo              |  maximo ] maior valor]              | maximo > seqNumeros              | maximo <  seqNumeros          |

  ### 7º caso de teste (maximo é maior valor da sequencia)
 ```java
maximo > sqlNumeros == true.
```

  ### 8º caso de teste (maximo é diferente do maior valor da sequencia)
 ```java
maximo < sqlNumeros == false.
```

## Plano de teste - número de elementos na seqüência

| Saída               | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| seq                 |  seq ] +sqlNumeros]                 | seq == seqNumeros                | seq != seqNumeros             |

  ### 9º caso de teste (seq possui o mesmo tamanho da sequencia)
 ```java
seq == sqlNumeros == true.
```

  ### 10º caso de teste (seq não possui o mesmo tamanho da sequencia)
 ```java
seq != sqlNumeros == false.
```

## Plano de teste - valor médio

| Saída               | Condição                            | Classes Válidas                  | Classes Inválidas             |
| -------------       | -------------                       | -------------------------------- | ----------------              |
| media               |  media ] +valor]                    | media == (+= valor / 2)          | media != (+= valor / 2)       |

  ### 11º caso de teste (media é a soma dos valores dividido por 2)
 ```java
media(13) == 6.5.
```

  ### 12º caso de teste (media é a soma dos valores dividido por 2, que possui o resultado diferente)
 ```java
media(12) != 6.
```
