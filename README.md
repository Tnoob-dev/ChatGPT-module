# ChatGPT-module

## Modulo sencillo haciendo peticiones a la API de ChatGPT establecida en https://freechatgpt.chat/

### Requerimientos:
- requests -> https://requests.readthedocs.io/

### Uso:

```python
from ChatGPT.chatgpt import ChatGPT

question = input("Introduzca su pregunta")

ai = ChatGPT(question)
print(ai.chatgpt())

```

#### Importante: 
No usar demasiadas veces seguidas, esperar al menos 5 segundos hasta la proxima peticion
