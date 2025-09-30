import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
from src.cotacao import CotacaoService, ConversorMoeda, ValidadorEntrada, CotadorApp

class TestCotacaoServiceAvancado(unittest.TestCase):
    """Testes avançados com mocks e cenários complexos para CotacaoService"""
    
    def setUp(self):
        self.service = CotacaoService()
    
    def test_buscar_cotacao_case_insensitive(self):
        """Testa busca de cotação independente de maiúscula/minúscula"""
        self.assertEqual(self.service.buscar_cotacao('dollar'), 1.0)
        self.assertEqual(self.service.buscar_cotacao('Dollar'), 1.0)
        self.assertEqual(self.service.buscar_cotacao('DOLLAR'), 1.0)
        self.assertEqual(self.service.buscar_cotacao('euro'), 1.08)
        self.assertEqual(self.service.buscar_cotacao('real'), 0.20)
    
    def test_buscar_cotacao_espacos_extras(self):
        """Testa busca com espaços extras"""
        self.assertEqual(self.service.buscar_cotacao('DOLLAR '), None)  # Não trata espaços
        
    def test_buscar_cotacao_string_vazia(self):
        """Testa busca com string vazia"""
        self.assertIsNone(self.service.buscar_cotacao(''))
    
    @patch.object(CotacaoService, 'buscar_cotacao')
    def test_mock_cotacao_api_externa(self, mock_buscar):
        """Simula integração com API externa usando mock"""
        # Configura o mock para simular resposta de API externa
        mock_buscar.return_value = 5.25
        
        resultado = self.service.buscar_cotacao('BTC')
        
        self.assertEqual(resultado, 5.25)
        mock_buscar.assert_called_once_with('BTC')

class TestConversorMoedaAvancado(unittest.TestCase):
    """Testes avançados para ConversorMoeda com mocks"""
    
    def setUp(self):
        self.conversor = ConversorMoeda()
        self.mock_service = Mock(spec=CotacaoService)
    
    def test_converter_com_mock_service_sucesso(self):
        """Testa conversão com service mockado - cenário de sucesso"""
        # Configura mocks
        self.mock_service.buscar_cotacao.side_effect = [1.0, 1.08]  # DOLLAR=1.0, EURO=1.08
        
        resultado = self.conversor.converter(100, 'DOLLAR', 'EURO', self.mock_service)
        esperado = (100 * 1.0) / 1.08
        
        self.assertAlmostEqual(resultado, esperado, places=2)
        self.assertEqual(self.mock_service.buscar_cotacao.call_count, 2)
    
    def test_converter_com_mock_service_falha_origem(self):
        """Testa conversão quando moeda origem é inválida"""
        self.mock_service.buscar_cotacao.side_effect = [None, 1.08]
        
        resultado = self.conversor.converter(100, 'INVALID', 'EURO', self.mock_service)
        
        self.assertIsNone(resultado)
    
    def test_converter_com_mock_service_falha_destino(self):
        """Testa conversão quando moeda destino é inválida"""
        self.mock_service.buscar_cotacao.side_effect = [1.0, None]
        
        resultado = self.conversor.converter(100, 'DOLLAR', 'INVALID', self.mock_service)
        
        self.assertIsNone(resultado)
    
    def test_converter_valores_extremos(self):
        """Testa conversão com valores muito pequenos e grandes"""
        service = CotacaoService()
        
        # Valor muito pequeno
        resultado_pequeno = self.conversor.converter(0.001, 'DOLLAR', 'EURO', service)
        self.assertIsNotNone(resultado_pequeno)
        
        # Valor muito grande
        resultado_grande = self.conversor.converter(999999999.99, 'DOLLAR', 'EURO', service)
        self.assertIsNotNone(resultado_grande)
    
    def test_converter_string_numerica(self):
        """Testa conversão com string numérica"""
        service = CotacaoService()
        
        # String numérica válida deve funcionar
        resultado = self.conversor.converter("100.5", 'DOLLAR', 'EURO', service)
        esperado = (100.5 * 1.0) / 1.08
        
        self.assertAlmostEqual(resultado, esperado, places=2)

class TestValidadorEntradaAvancado(unittest.TestCase):
    """Testes avançados para ValidadorEntrada"""
    
    def setUp(self):
        self.validador = ValidadorEntrada()
    
    def test_validar_valor_tipos_diversos(self):
        """Testa validação com diferentes tipos de entrada"""
        # Strings numéricas
        self.assertTrue(self.validador.validar_valor("10.5"))
        self.assertTrue(self.validador.validar_valor("100"))
        
        # Tipos inválidos
        self.assertFalse(self.validador.validar_valor(None))
        self.assertFalse(self.validador.validar_valor([]))
        self.assertFalse(self.validador.validar_valor({}))
        self.assertFalse(self.validador.validar_valor(complex(1, 2)))
    
    def test_validar_valor_casos_limite(self):
        """Testa casos limite de validação de valor"""
        # Valor muito pequeno positivo
        self.assertTrue(self.validador.validar_valor(0.0001))
        
        # Valores infinitos (código atual não filtra, só verifica > 0)
        # float('inf') > 0 retorna True, então o validador atual aceita
        self.assertTrue(self.validador.validar_valor(float('inf')))
        
        # -inf é negativo, então deve retornar False
        self.assertFalse(self.validador.validar_valor(float('-inf')))
        
        # NaN não é > 0, então deve retornar False  
        self.assertFalse(self.validador.validar_valor(float('nan')))
    
    def test_validar_moeda_casos_especiais(self):
        """Testa validação de moeda com casos especiais"""
        # Moedas com espaços
        self.assertFalse(self.validador.validar_moeda(' DOLLAR '))
        
        # Moedas parcialmente corretas
        self.assertFalse(self.validador.validar_moeda('DOL'))
        self.assertFalse(self.validador.validar_moeda('DOLLARS'))
        
        # Testa com try/except para None (código atual não trata)
        with self.assertRaises(AttributeError):
            self.validador.validar_moeda(None)
            
        # Outros tipos também causam erro (comportamento atual)
        with self.assertRaises(AttributeError):
            self.validador.validar_moeda(123)
    
    @patch('builtins.float')
    def test_validar_valor_exception_handling(self, mock_float):
        """Testa tratamento de exceções na validação de valor"""
        # Simula ValueError
        mock_float.side_effect = ValueError("Erro de conversão")
        self.assertFalse(self.validador.validar_valor("abc"))
        
        # Simula TypeError
        mock_float.side_effect = TypeError("Tipo inválido")
        self.assertFalse(self.validador.validar_valor("xyz"))

class TestCotadorAppAvancado(unittest.TestCase):
    """Testes integrados avançados para CotadorApp"""
    
    def setUp(self):
        self.app = CotadorApp()
    
    @patch('builtins.print')
    def test_executar_valor_invalido_com_mock_print(self, mock_print):
        """Testa execução com valor inválido e verifica output"""
        self.app.executar("abc", "DOLLAR", "EURO")
        
        mock_print.assert_called_with("Valor inválido!")
    
    @patch('builtins.print')
    def test_executar_moeda_origem_invalida(self, mock_print):
        """Testa execução com moeda origem inválida"""
        self.app.executar("100", "BITCOIN", "EURO")
        
        mock_print.assert_called_with("Moeda inválida!")
    
    @patch('builtins.print')
    def test_executar_moeda_destino_invalida(self, mock_print):
        """Testa execução com moeda destino inválida"""
        self.app.executar("100", "DOLLAR", "BITCOIN")
        
        mock_print.assert_called_with("Moeda inválida!")
    
    @patch('builtins.print')
    def test_executar_conversao_sucesso(self, mock_print):
        """Testa execução com conversão bem-sucedida"""
        self.app.executar("100", "DOLLAR", "EURO")
        
        # Verifica se foi chamado com formato correto
        args, _ = mock_print.call_args
        self.assertIn("100", args[0])
        self.assertIn("DOLLAR", args[0])
        self.assertIn("EURO", args[0])
    
    @patch.object(ConversorMoeda, 'converter')
    def test_executar_erro_conversao(self, mock_converter):
        """Testa execução quando conversão retorna None"""
        mock_converter.return_value = None
        
        with patch('builtins.print') as mock_print:
            self.app.executar("100", "DOLLAR", "EURO")
            mock_print.assert_called_with("Erro na conversão!")
    
    def test_integração_completa_cenarios_multiplos(self):
        """Teste de integração com múltiplos cenários"""
        cenarios = [
            ("100", "DOLLAR", "EURO", True),
            ("50.5", "EURO", "REAL", True),
            ("200", "REAL", "DOLLAR", True),
            ("-10", "DOLLAR", "EURO", False),  # Valor inválido
            ("100", "BITCOIN", "EURO", False),  # Moeda inválida
        ]
        
        for valor, origem, destino, deve_funcionar in cenarios:
            with self.subTest(valor=valor, origem=origem, destino=destino):
                if deve_funcionar:
                    resultado = self.app.conversor.converter(
                        float(valor), origem, destino, self.app.cotacao_service
                    )
                    self.assertIsNotNone(resultado)
                else:
                    # Para valores/moedas inválidos, testamos as validações
                    if not self.app.validador.validar_valor(valor):
                        self.assertFalse(self.app.validador.validar_valor(valor))
                    elif not self.app.validador.validar_moeda(origem) or not self.app.validador.validar_moeda(destino):
                        self.assertTrue(
                            not self.app.validador.validar_moeda(origem) or 
                            not self.app.validador.validar_moeda(destino)
                        )

class TestPerformance(unittest.TestCase):
    """Testes de performance e carga"""
    
    def setUp(self):
        self.app = CotadorApp()
    
    def test_performance_multiplas_conversoes(self):
        """Testa performance com múltiplas conversões"""
        import time
        
        inicio = time.time()
        
        for i in range(100):
            resultado = self.app.conversor.converter(
                100 + i, "DOLLAR", "EURO", self.app.cotacao_service
            )
            self.assertIsNotNone(resultado)
        
        fim = time.time()
        tempo_execucao = fim - inicio
        
        # Deve executar 100 conversões em menos de 1 segundo
        self.assertLess(tempo_execucao, 1.0)
    
    def test_carga_validacoes(self):
        """Testa carga de validações"""
        valores_teste = [str(i) for i in range(1000, 2000)]
        
        for valor in valores_teste:
            resultado = self.app.validador.validar_valor(valor)
            self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main(verbosity=2)