"""
Testes unitários para o sistema de cotação de moedas
Cobertura completa com mocks para APIs externas
"""
import pytest
from unittest.mock import Mock, patch
import requests
from typer.testing import CliRunner
import sys
import os
import statistics

# Adiciona o diretório src ao path para importação
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from cotacao import app

runner = CliRunner()

class TestCotacaoFuncional:
    """Testes funcionais básicos (sem mock)"""
    
    def test_help_comando_principal(self):
        """Teste 1: Comando de ajuda principal"""
        result = runner.invoke(app, ['--help'])
        assert result.exit_code == 0
        assert "Ferramenta de cotação" in result.output

    def test_help_cotacao(self):
        """Teste 2: Comando de ajuda para cotação"""
        result = runner.invoke(app, ['cotacao', '--help'])
        assert result.exit_code == 0
        assert "Busca cotação de moeda" in result.output

    def test_help_stats(self):
        """Teste 3: Comando de ajuda para stats"""
        result = runner.invoke(app, ['stats-cmd', '--help'])
        assert result.exit_code == 0
        assert "estatísticas" in result.output

    def test_stats_numeros_positivos(self):
        """Teste 4: Estatísticas com números positivos"""
        result = runner.invoke(app, ['stats-cmd', '1', '2', '3', '4', '5'])
        assert result.exit_code == 0
        assert "Quantidade" in result.output

    def test_stats_numero_unico(self):
        """Teste 5: Estatísticas com um único número"""
        result = runner.invoke(app, ['stats-cmd', '42'])
        assert result.exit_code == 0
        assert "Quantidade" in result.output

    def test_stats_numeros_decimais(self):
        """Teste 6: Estatísticas com números decimais"""
        result = runner.invoke(app, ['stats-cmd', '1.5', '2.7', '3.2'])
        assert result.exit_code == 0
        assert "Quantidade" in result.output

    def test_stats_sem_argumentos_falha(self):
        """Teste 7: Stats sem argumentos deve falhar"""
        result = runner.invoke(app, ['stats-cmd'])
        assert result.exit_code != 0

    def test_comando_inexistente_falha(self):
        """Teste 8: Comando que não existe deve falhar"""
        result = runner.invoke(app, ['comando-inexistente'])
        assert result.exit_code != 0

    def test_stats_numeros_grandes(self):
        """Teste 9: Estatísticas com números grandes"""
        result = runner.invoke(app, ['stats-cmd', '1000000', '2000000'])
        assert result.exit_code == 0
        assert "Quantidade" in result.output

    def test_stats_numeros_mistos(self):
        """Teste 10: Estatísticas com números diversos"""
        result = runner.invoke(app, ['stats-cmd', '0', '1', '2'])
        assert result.exit_code == 0
        assert "Quantidade" in result.output


class TestCotacaoComMock:
    """Testes de cotação usando mocks para simular API"""
    
    @patch('cotacao.requests.get')
    def test_cotacao_sucesso_usd_brl(self, mock_get):
        """Teste 11: Mock - Cotação USD para BRL bem-sucedida"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'BRL': 5.2}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0
        mock_get.assert_called_once()

    @patch('cotacao.requests.get')
    def test_cotacao_moeda_inexistente(self, mock_get):
        """Teste 12: Mock - Moeda de destino não encontrada"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'EUR': 0.9}}  # BRL não existe
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0
        assert "não encontrada" in result.output

    @patch('cotacao.requests.get')
    def test_cotacao_erro_conexao(self, mock_get):
        """Teste 13: Mock - Erro de conexão"""
        mock_get.side_effect = requests.exceptions.ConnectionError("Erro de rede")
        
        result = runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0
        assert "Erro ao buscar cotação" in result.output

    @patch('cotacao.requests.get')
    def test_cotacao_timeout(self, mock_get):
        """Teste 14: Mock - Timeout"""
        mock_get.side_effect = requests.exceptions.Timeout("Timeout")
        
        result = runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0
        assert "Erro ao buscar cotação" in result.output

    @patch('cotacao.requests.get')
    def test_cotacao_http_error(self, mock_get):
        """Teste 15: Mock - Erro HTTP (404, 500, etc)"""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404")
        mock_get.return_value = mock_response
        
        result = runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0
        assert "Erro ao buscar cotação" in result.output

    @patch('cotacao.requests.get')
    def test_cotacao_valor_zero(self, mock_get):
        """Teste 16: Mock - Cotação com valor zero"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'BRL': 5.2}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = runner.invoke(app, ['cotacao', '0', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0

    @patch('cotacao.requests.get')
    def test_cotacao_eur_para_brl(self, mock_get):
        """Teste 17: Mock - Cotação EUR para BRL"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'BRL': 6.1}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = runner.invoke(app, ['cotacao', '50', '--moeda-origem', 'EUR', '--moeda-destino', 'BRL'])
        assert result.exit_code == 0

    @patch('cotacao.requests.get')
    def test_cotacao_chamada_api_url_correta(self, mock_get):
        """Teste 18: Mock - Verifica URL da API"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'BRL': 5.2}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        runner.invoke(app, ['cotacao', '100', '--moeda-origem', 'USD', '--moeda-destino', 'BRL'])
        mock_get.assert_called_with("https://api.exchangerate-api.com/v4/latest/USD")


class TestEstatisticasDetalhadas:
    """Testes detalhados de estatísticas"""
    
    def test_stats_calculo_media(self):
        """Teste 19: Verificar cálculo da média"""
        # Usar números que têm média conhecida: (1+2+3)/3 = 2
        result = runner.invoke(app, ['stats-cmd', '1', '2', '3'])
        assert result.exit_code == 0
        assert "2.00" in result.output  # média

    def test_stats_calculo_mediana(self):
        """Teste 20: Verificar cálculo da mediana"""
        # Mediana de [1,2,3,4,5] é 3
        result = runner.invoke(app, ['stats-cmd', '1', '2', '3', '4', '5'])
        assert result.exit_code == 0
        assert "3.00" in result.output  # mediana

    def test_stats_min_max(self):
        """Teste 21: Verificar valores min e max"""
        result = runner.invoke(app, ['stats-cmd', '10', '20', '30'])
        assert result.exit_code == 0
        assert "10" in result.output  # mínimo
        assert "30" in result.output  # máximo

    def test_stats_quantidade_elementos(self):
        """Teste 22: Verificar contagem de elementos"""
        result = runner.invoke(app, ['stats-cmd', '1', '2', '3', '4'])
        assert result.exit_code == 0
        assert "4" in result.output  # quantidade