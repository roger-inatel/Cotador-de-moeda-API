# Cotação de Moedas 

Ferramenta de linha de comando para cotação de moedas e estatísticas simples usando Typer e Rich.

## Instalação

1. Instale as dependências com Poetry:
   ```powershell
   poetry install
   ```

2. Execute os comandos via Poetry:
   ```powershell
   poetry run python src/cotacao.py --help
   ```

## Comandos disponíveis

### Cotação de Moedas
Busca a cotação entre duas moedas usando a ExchangeRate API.

```powershell
poetry run python src/cotacao.py cotacao --valor 100 --moeda-origem USD --moeda-destino BRL
```

### Estatísticas Simples
Calcula estatísticas básicas de uma lista de números.

```powershell
poetry run python src/cotacao.py stats-cmd 1 2 3 4 5
```

## Autor
Roger Freitas <roger.pereira@ges.inatel.br>

## Mudanças no arquivo README
Oiii professor, através de muita luta e de muita persistência consegui fazer o que a atividade pedia!
Tudo é um passo a passo né!
Mas da próxima vou utilizar java, com python dá muito trabalho kkkkkkkk
mas fé que com python vai
tirulipa

---
## 🤝 Como Contribuir

Agradecemos o seu interesse em contribuir para este projeto! Sua ajuda é fundamental para que ele cresça e melhore. Abaixo estão algumas diretrizes para começar.

1.  **Faça um Fork do Repositório**: Comece fazendo um fork do projeto para a sua própria conta no GitHub.

2.  **Clone o Repositório**: Depois de fazer o fork, clone o repositório para a sua máquina local.


3.  **Crie uma Branch**: Crie uma nova branch para suas alterações.

4.  **Faça suas Alterações**: Implemente suas mudanças, adicione novos recursos ou corrija bugs.

5.  **Commit e Push**: Faça o commit das suas alterações com uma mensagem clara e descritiva.

6.  **Abra um Pull Request (PR)**: Vá até a página do seu fork no GitHub e clique em "New Pull Request". Descreva suas alterações detalhadamente e mencione qualquer issue relacionada.
