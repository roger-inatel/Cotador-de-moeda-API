# 💰 Cotador de Moedas API

Ferramenta de linha de comando para cotação de moedas e estatísticas simples usando Typer e Rich.

## 🎯 Atividade CI/CD com GitHub Actions

Este projeto foi desenvolvido para demonstrar um pipeline completo de CI/CD com as seguintes características:

### ✅ Requisitos Implementados:
- **20+ Testes Unitários** com mocks para APIs externas
- **Pipeline GitHub Actions** com 3 jobs principais:
  - 🧪 **Testes**: Execução de testes unitários com relatórios
  - 🏗️ **Build**: Empacotamento e geração de artefatos  
  - 📧 **Notificação**: Envio de email automático
- **Execução Paralela** de jobs
- **Armazenamento de Artefatos** (ZIP, TAR.GZ, relatórios)
- **Instalação Automática** de dependências no pipeline

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.13+
- pip ou poetry

### 1. Clone o repositório
```bash
git clone https://github.com/roger-inatel/Cotador-de-moeda-API.git
cd Cotador-de-moeda-API
```

### 2. Instale as dependências
```bash
# Usando pip
pip install typer rich requests pytest pytest-mock

# Ou usando poetry (se disponível)
poetry install
```

### 3. Execute os comandos

#### Cotação de Moedas
```bash
python src/cotacao.py cotacao 100 --moeda-origem USD --moeda-destino BRL
```

#### Estatísticas
```bash
python src/cotacao.py stats-cmd 1 2 3 4 5
```

#### Ajuda
```bash
python src/cotacao.py --help
```

## 🧪 Executar Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com relatório HTML
pytest tests/ -v --html=report.html --self-contained-html

# Executar com cobertura
pytest tests/ -v --cov=src --cov-report=html
```

## 🔄 Pipeline CI/CD

O pipeline é executado automaticamente nos pushes para `master` e inclui:

### Jobs do Pipeline:
1. **🧪 Testes Unitários**
   - Executa 22 cenários de teste
   - Gera relatórios HTML e XML
   - Calcula cobertura de código

2. **🏗️ Build e Empacotamento**
   - Cria arquivos ZIP e TAR.GZ
   - Gera artefatos para distribuição
   - Versionamento automático

3. **📧 Notificação**
   - Envia email com status do pipeline
   - Executa em paralelo com outros jobs
   - HTML e texto simples

4. **✅ Finalização**
   - Confirma sucesso de todos os jobs
   - Exibe estatísticas do pipeline

### Configuração de Email:
- **Email padrão:** roger.pereira@ges.inatel.br
- **Modo simulação** ativo por padrão
- **Secrets necessários:** SENDER_EMAIL, EMAIL_PASSWORD, EMAIL_DESTINO

## 📊 Testes Implementados

### Categorias de Teste:
- **Testes Funcionais**: Comandos de ajuda, validação de entrada
- **Testes com Mock**: Simulação de APIs externas, erros de rede
- **Testes de Estatísticas**: Cálculos matemáticos, casos extremos
- **Testes de Integração**: Fluxos completos, validação de URLs

### Cobertura:
- ✅ Cotação de moedas (USD→BRL, EUR→BRL)
- ✅ Tratamento de erros (timeout, conexão, HTTP)
- ✅ Validação de entrada (moedas inexistentes, valores especiais)
- ✅ Cálculos estatísticos (média, mediana, min, max)
- ✅ Comandos de linha (ajuda, argumentos inválidos)

## 🏗️ Estrutura do Projeto

```
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline GitHub Actions
├── src/
│   └── cotacao.py              # Código principal
├── tests/
│   └── test_cotacao_simples.py # Testes unitários
├── scripts/
│   └── send_notification.py    # Script de notificação
├── pyproject.toml              # Configuração do projeto
├── poetry.lock                 # Lock de dependências
└── README.md                   # Este arquivo
```

## 👥 Desenvolvedor

- **Implementação CI/CD:** Pipeline completo com testes, build e notificações

## 📝 Notas da Atividade

Este projeto demonstra:
- ✅ **20+ cenários de teste** com mocks para APIs externas
- ✅ **3+ jobs no pipeline** (testes, build, notificação)  
- ✅ **Empacotamento automático** com artefatos
- ✅ **Execução paralela** implementada
- ✅ **Notificação por email** configurada
- ✅ **Instalação de dependências** no pipeline

### Tecnologias Utilizadas:
- **Python 3.13** - Linguagem principal
- **Typer** - Framework CLI
- **Rich** - Interface rica no terminal
- **Pytest** - Framework de testes
- **GitHub Actions** - CI/CD
- **ExchangeRate API** - Cotações de moeda

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

🚀 **Pipeline executado automaticamente a cada push!** 📧
