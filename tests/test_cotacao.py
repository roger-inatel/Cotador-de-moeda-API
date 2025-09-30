
import unittest
from src.cotacao import CotacaoService, ConversorMoeda, ValidadorEntrada, CotadorApp

class TestCotacaoService(unittest.TestCase):
    # Positivos
    def test_buscar_cotacao_dollar(self):
        service = CotacaoService()
        self.assertEqual(service.buscar_cotacao('DOLLAR'), 1.0)
    def test_buscar_cotacao_euro(self):
        service = CotacaoService()
        self.assertEqual(service.buscar_cotacao('EURO'), 1.08)
    def test_buscar_cotacao_real(self):
        service = CotacaoService()
        self.assertEqual(service.buscar_cotacao('REAL'), 0.20)
    # Negativo
    def test_buscar_cotacao_invalida(self):
        service = CotacaoService()
        self.assertIsNone(service.buscar_cotacao('YEN'))

class TestConversorMoeda(unittest.TestCase):
    # Positivos
    def test_converter_dollar_para_euro(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        # 10 DOLLAR -> EURO
        valor = 10
        esperado = (valor * 1.0) / 1.08
        self.assertAlmostEqual(conversor.converter(valor, 'DOLLAR', 'EURO', service), esperado, places=2)
    def test_converter_euro_para_real(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        valor = 10
        esperado = (valor * 1.08) / 0.20
        self.assertAlmostEqual(conversor.converter(valor, 'EURO', 'REAL', service), esperado, places=2)
    def test_converter_real_para_dollar(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        valor = 10
        esperado = (valor * 0.20) / 1.0
        self.assertAlmostEqual(conversor.converter(valor, 'REAL', 'DOLLAR', service), esperado, places=2)
    # Negativos
    def test_converter_valor_negativo(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        self.assertIsNone(conversor.converter(-10, 'DOLLAR', 'EURO', service))
    def test_converter_valor_zero(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        self.assertIsNone(conversor.converter(0, 'DOLLAR', 'EURO', service))
    def test_converter_moeda_origem_invalida(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        self.assertIsNone(conversor.converter(10, 'YEN', 'EURO', service))
    def test_converter_moeda_destino_invalida(self):
        service = CotacaoService()
        conversor = ConversorMoeda()
        self.assertIsNone(conversor.converter(10, 'DOLLAR', 'YEN', service))

class TestValidadorEntrada(unittest.TestCase):
    # Positivos
    def test_validar_valor_positivo_int(self):
        validador = ValidadorEntrada()
        self.assertTrue(validador.validar_valor(10))
    def test_validar_valor_positivo_float(self):
        validador = ValidadorEntrada()
        self.assertTrue(validador.validar_valor(10.5))
    def test_validar_moeda_valida_dollar(self):
        validador = ValidadorEntrada()
        self.assertTrue(validador.validar_moeda('DOLLAR'))
    def test_validar_moeda_valida_euro(self):
        validador = ValidadorEntrada()
        self.assertTrue(validador.validar_moeda('EURO'))
    # Negativos
    def test_validar_valor_negativo(self):
        validador = ValidadorEntrada()
        self.assertFalse(validador.validar_valor(-5))
    def test_validar_valor_zero(self):
        validador = ValidadorEntrada()
        self.assertFalse(validador.validar_valor(0))
    def test_validar_valor_nao_numerico(self):
        validador = ValidadorEntrada()
        self.assertFalse(validador.validar_valor('abc'))
    def test_validar_moeda_invalida(self):
        validador = ValidadorEntrada()
        self.assertFalse(validador.validar_moeda('YEN'))
    def test_validar_moeda_vazia(self):
        validador = ValidadorEntrada()
        self.assertFalse(validador.validar_moeda(''))

class TestCotadorApp(unittest.TestCase):
    # Positivo
    def test_executar_valido(self):
        app = CotadorApp()
        resultado = app.conversor.converter(100, 'DOLLAR', 'EURO', app.cotacao_service)
        esperado = (100 * 1.0) / 1.08
        self.assertAlmostEqual(resultado, esperado, places=2)
    # Negativos
    def test_executar_valor_invalido(self):
        app = CotadorApp()
        self.assertIsNone(app.conversor.converter(-100, 'DOLLAR', 'EURO', app.cotacao_service))
    def test_executar_moeda_invalida(self):
        app = CotadorApp()
        self.assertIsNone(app.conversor.converter(100, 'DOLLAR', 'YEN', app.cotacao_service))

if __name__ == "__main__":
    unittest.main()
