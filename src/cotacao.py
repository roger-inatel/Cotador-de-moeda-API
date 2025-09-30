



class CotacaoService:
    """Cotação fixa das moedas em relação ao dólar."""
    def buscar_cotacao(self, moeda: str) -> float:
        cotacoes = {
            'DOLLAR': 1.0,
            'EURO': 1.08,
            'REAL': 0.20
        }
        return cotacoes.get(moeda.upper(), None)


class ConversorMoeda:
    
    def calcular_taxa(self, valor:float) -> float:
        """Calcular a taxa de transação baseada no valor"""
        if valor > 1000.00:
            return 0.005 # 0.5% para grandes columes
        
        return 0.01 # 1 % para volumes normais
    
    """Responsável por converter valores entre moedas."""
    def converter(self, valor: float, moeda_origem: str, moeda_destino: str, cotacao_service: CotacaoService) -> float:
        if valor is None or float(valor) <= 0:
            return None
        # get cotação sem mudança   
        
        cotacao_origem = cotacao_service.buscar_cotacao(moeda_origem)
        cotacao_destino = cotacao_service.buscar_cotacao(moeda_destino)
        
        if cotacao_origem is None or cotacao_destino is None:
            return None
        
        taxa = self.calcular_taxa(valor)
        valor_com_taxa = valor - valor * taxa
        
        valor_em_dolar = float(valor_com_taxa) * cotacao_origem
        valor_convertido = valor_em_dolar / cotacao_destino
        
        return valor_convertido

class ValidadorEntrada:
    """Responsável por validar entradas do usuário."""
    def validar_valor(self, valor) -> bool:
        try:
            valor = float(valor)
            return valor > 0
        except (ValueError, TypeError):
            return False
    def validar_moeda(self, moeda: str) -> bool:
        return moeda.upper() in ['REAL', 'DOLLAR', 'EURO']

class CotadorApp:
    """Classe principal que orquestra o fluxo do cotador de moedas."""
    def __init__(self):
        self.cotacao_service = CotacaoService()
        self.conversor = ConversorMoeda()
        self.validador = ValidadorEntrada()

    def executar(self, valor, moeda_origem, moeda_destino):
        if not self.validador.validar_valor(valor):
            print("Valor inválido!")
            return
        if not self.validador.validar_moeda(moeda_origem) or not self.validador.validar_moeda(moeda_destino):
            print("Moeda inválida!")
            return
        resultado = self.conversor.converter(float(valor), moeda_origem, moeda_destino, self.cotacao_service)
        if resultado is None:
            print("Erro na conversão!")
        else:
            print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")

def main():
    opcoes = ['REAL', 'DOLLAR', 'EURO']
    print("Moedas disponíveis para conversão:")
    for idx, moeda in enumerate(opcoes, 1):
        print(f"{idx}. {moeda}")

    # Escolha da moeda de origem
    while True:
        escolha_origem = input("Escolha o número da moeda de origem: ")
        if escolha_origem.isdigit() and 1 <= int(escolha_origem) <= len(opcoes):
            moeda_origem = opcoes[int(escolha_origem) - 1]
            break
        print("Opção inválida. Tente novamente.")

    # Escolha da moeda de destino
    while True:
        escolha_destino = input("Escolha o número da moeda de destino: ")
        if escolha_destino.isdigit() and 1 <= int(escolha_destino) <= len(opcoes):
            moeda_destino = opcoes[int(escolha_destino) - 1]
            break
        print("Opção inválida. Tente novamente.")

    valor = input("Digite o valor para conversão: ")
    app = CotadorApp()
    print(app.executar(valor, moeda_origem, moeda_destino))

if __name__ == "__main__":
    main()

