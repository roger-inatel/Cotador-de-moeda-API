"""
Testes unitários para o sistema de cotação de moedas
Cobertura completa com mocks para APIs externas
"""

import pytest
import re
from unittest.mock import Mock, patch
import requests
from typer.testing import CliRunner
import sys
import os

# Adiciona o diretório src ao path para importação
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cotacao import app

runner = CliRunner()


# =============================
# Fixtures
# =============================

@pytest.fixture
def mock_response():
    """Retorna um mock de resposta padrão de API"""
    resp = Mock()
    resp.raise_for_status.return_value = None
    return resp


# =============================
# Testes funcionais básicos
# =============================

class TestCotacaoFuncional:
    """Testes funcionais básicos (sem mock)"""

    def test_help_comando_principal(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Ferramenta de cotação" in result.output

    def test_help_cotacao(self):
        result = runner.invoke(app, ["cotacao", "--help"])
        assert result.exit_code == 0
        assert "Busca cotação de moeda" in result.output

    def test_help_stats(self):
        result = runner.invoke(app, ["stats-cmd", "--help"])
        assert result.exit_code == 0
        assert "estatísticas" in result.output

    @pytest.mark.parametrize("args", [
        (["stats-cmd", "1", "2", "3", "4", "5"]),   # positivos
        (["stats-cmd", "42"]),                      # único
        (["stats-cmd", "1.5", "2.7", "3.2"]),       # decimais
        (["stats-cmd", "1000000", "2000000"]),      # grandes
        (["stats-cmd", "0", "1", "2"]),             # mistos
    ])
    def test_stats_variados(self, args):
        result = runner.invoke(app, args)
        assert result.exit_code == 0
        assert "Quantidade" in result.output

    def test_stats_sem_argumentos_falha(self):
        result = runner.invoke(app, ["stats-cmd"])
        assert result.exit_code != 0

    def test_comando_inexistente_falha(self):
        result = runner.invoke(app, ["comando-inexistente"])
        assert result.exit_code != 0


# =============================
# Testes de cotação com mock
# =============================

class TestCotacaoComMock:
    """Testes de cotação usando mocks para simular API"""

    @patch("cotacao.requests.get")
    def test_cotacao_sucesso_usd_brl(self, mock_get, mock_response):
        mock_response.json.return_value = {"rates": {"BRL": 5.2}}
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["cotacao", "100", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        assert result.exit_code == 0
        mock_get.assert_called_once()

    @patch("cotacao.requests.get")
    def test_cotacao_moeda_inexistente(self, mock_get, mock_response):
        mock_response.json.return_value = {"rates": {"EUR": 0.9}}  # BRL não existe
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["cotacao", "100", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        assert result.exit_code == 0
        assert "não encontrada" in result.output

    @pytest.mark.parametrize("side_effect, expected_msg", [
        (requests.exceptions.ConnectionError("Erro de rede"), "Erro ao buscar cotação"),
        (requests.exceptions.Timeout("Timeout"), "Erro ao buscar cotação"),
    ])
    @patch("cotacao.requests.get")
    def test_cotacao_erros_api(self, mock_get, side_effect, expected_msg):
        mock_get.side_effect = side_effect
        result = runner.invoke(app, ["cotacao", "100", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        assert result.exit_code == 0
        assert expected_msg in result.output

    @patch("cotacao.requests.get")
    def test_cotacao_http_error(self, mock_get, mock_response):
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404")
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["cotacao", "100", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        assert result.exit_code == 0
        assert "Erro ao buscar cotação" in result.output

    @patch("cotacao.requests.get")
    def test_cotacao_valor_zero(self, mock_get, mock_response):
        mock_response.json.return_value = {"rates": {"BRL": 5.2}}
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["cotacao", "0", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        assert result.exit_code == 0

    @patch("cotacao.requests.get")
    def test_cotacao_eur_para_brl(self, mock_get, mock_response):
        mock_response.json.return_value = {"rates": {"BRL": 6.1}}
        mock_get.return_value = mock_response

        result = runner.invoke(app, ["cotacao", "50", "--moeda-origem", "EUR", "--moeda-destino", "BRL"])
        assert result.exit_code == 0

    @patch("cotacao.requests.get")
    def test_cotacao_chamada_api_url_correta(self, mock_get, mock_response):
        mock_response.json.return_value = {"rates": {"BRL": 5.2}}
        mock_get.return_value = mock_response

        runner.invoke(app, ["cotacao", "100", "--moeda-origem", "USD", "--moeda-destino", "BRL"])
        mock_get.assert_called_with("https://api.exchangerate-api.com/v4/latest/USD")


# =============================
# Testes detalhados de estatísticas
# =============================

class TestEstatisticasDetalhadas:
    """Testes detalhados de estatísticas"""

    def test_stats_calculo_media(self):
        result = runner.invoke(app, ["stats-cmd", "1", "2", "3"])
        assert result.exit_code == 0
        assert re.search(r"2\.00", result.output)

    def test_stats_calculo_mediana(self):
        result = runner.invoke(app, ["stats-cmd", "1", "2", "3", "4", "5"])
        assert result.exit_code == 0
        assert re.search(r"3\.00", result.output)

    def test_stats_min_max(self):
        result = runner.invoke(app, ["stats-cmd", "10", "20", "30"])
        assert result.exit_code == 0
        assert "10" in result.output  # mínimo
        assert "30" in result.output  # máximo

    def test_stats_quantidade_elementos(self):
        result = runner.invoke(app, ["stats-cmd", "1", "2", "3", "4"])
        assert result.exit_code == 0
        assert "4" in result.output  # quantidade
