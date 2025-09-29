#!/usr/bin/env python3
"""
Sistema de Notificação para Pipeline CI/CD
Sistema de Cotação de Moedas - Inatel

Envia notificações por email sobre o status do pipeline
Autor: Roger Pereira
Email: roger.pereira@ges.inatel.br
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json


class NotificadorPipeline:
    """Classe responsável por enviar notificações do pipeline CI/CD"""
    
    def __init__(self):
        self.email_destino = os.getenv('EMAIL_DESTINO', 'roger.pereira@ges.inatel.br')
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.smtp_user = os.getenv('SMTP_USER', '')
        self.smtp_password = os.getenv('SMTP_PASSWORD', '')
    
    def gerar_relatorio_detalhado(self):
        """Gera relatório detalhado do status do pipeline"""
        pipeline_status = os.getenv('PIPELINE_STATUS', 'UNKNOWN')
        tests_status = os.getenv('TESTS_STATUS', 'UNKNOWN')
        build_status = os.getenv('BUILD_STATUS', 'UNKNOWN')
        security_status = os.getenv('SECURITY_STATUS', 'UNKNOWN')
        quality_status = os.getenv('QUALITY_STATUS', 'UNKNOWN')
        
        # Determina ícones baseado no status
        status_icons = {
            'success': '✅',
            'failure': '❌', 
            'cancelled': '⚪',
            'skipped': '⏭️',
            'UNKNOWN': '❓'
        }
        
        def get_icon(status):
            return status_icons.get(status.lower(), status_icons['UNKNOWN'])
        
        pipeline_icon = get_icon(pipeline_status)
        
        # Gera conteúdo HTML do email
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f5f5f5; }}
                .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .header {{ text-align: center; border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 20px; }}
                .status-success {{ color: #28a745; }}
                .status-failure {{ color: #dc3545; }}
                .status-unknown {{ color: #ffc107; }}
                .job-item {{ padding: 10px; margin: 5px 0; background: #f8f9fa; border-radius: 4px; }}
                .info-section {{ margin: 15px 0; }}
                .footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; color: #666; }}
                table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
                th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>{pipeline_icon} Pipeline CI/CD - Sistema de Cotação</h1>
                    <h2 class="status-{pipeline_status.lower()}">Status: {pipeline_status}</h2>
                </div>
                
                <div class="info-section">
                    <h3>📊 Resumo da Execução</h3>
                    <table>
                        <tr>
                            <th>Informação</th>
                            <th>Valor</th>
                        </tr>
                        <tr>
                            <td><strong>Data/Hora</strong></td>
                            <td>{datetime.now().strftime('%d/%m/%Y %H:%M:%S UTC')}</td>
                        </tr>
                        <tr>
                            <td><strong>Repositório</strong></td>
                            <td>roger-inatel/Testes_cotacao</td>
                        </tr>
                        <tr>
                            <td><strong>Branch</strong></td>
                            <td>{os.getenv('GITHUB_REF_NAME', 'main')}</td>
                        </tr>
                        <tr>
                            <td><strong>Commit</strong></td>
                            <td>{os.getenv('GITHUB_SHA', 'N/A')[:8]}...</td>
                        </tr>
                        <tr>
                            <td><strong>Workflow ID</strong></td>
                            <td>{os.getenv('GITHUB_RUN_ID', 'N/A')}</td>
                        </tr>
                    </table>
                </div>
                
                <div class="info-section">
                    <h3>🔧 Status dos Jobs</h3>
                    <div class="job-item">
                        {get_icon(tests_status)} <strong>Testes Unitários:</strong> {tests_status}
                    </div>
                    <div class="job-item">
                        {get_icon(security_status)} <strong>Análise de Segurança:</strong> {security_status}
                    </div>
                    <div class="job-item">
                        {get_icon(quality_status)} <strong>Qualidade do Código:</strong> {quality_status}
                    </div>
                    <div class="job-item">
                        {get_icon(build_status)} <strong>Build e Empacotamento:</strong> {build_status}
                    </div>
                </div>
                
                <div class="info-section">
                    <h3>📈 Métricas do Pipeline</h3>
                    <ul>
                        <li><strong>Total de Testes:</strong> 23+ testes unitários</li>
                        <li><strong>Cobertura de Código:</strong> Relatório gerado</li>
                        <li><strong>Jobs Executados:</strong> 6 jobs (testes, segurança, qualidade, build, notificação, deploy)</li>
                        <li><strong>Artefatos Gerados:</strong> Relatórios de teste, pacotes de distribuição</li>
                        <li><strong>Duração Estimada:</strong> ~2-3 minutos</li>
                    </ul>
                </div>
                
                <div class="info-section">
                    <h3>🔗 Links Úteis</h3>
                    <ul>
                        <li><a href="https://github.com/roger-inatel/Testes_cotacao">📁 Repositório</a></li>
                        <li><a href="https://github.com/roger-inatel/Testes_cotacao/actions">⚙️ GitHub Actions</a></li>
                        <li><a href="https://github.com/roger-inatel/Testes_cotacao/actions/runs/{os.getenv('GITHUB_RUN_ID', '')}">🔍 Esta Execução</a></li>
                    </ul>
                </div>
                
                <div class="footer">
                    <p><em>Notificação automática gerada pelo GitHub Actions</em></p>
                    <p>Sistema de Cotação de Moedas - Projeto Inatel C14 - Engenharia de Software</p>
                    <p>🤖 Desenvolvido com CI/CD Best Practices</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Gera versão texto simples
        text_content = f"""
        PIPELINE CI/CD - SISTEMA DE COTAÇÃO DE MOEDAS
        ============================================
        
        Status Geral: {pipeline_status}
        Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S UTC')}
        
        JOBS EXECUTADOS:
        - Testes Unitários: {tests_status}
        - Análise de Segurança: {security_status}  
        - Qualidade do Código: {quality_status}
        - Build e Empacotamento: {build_status}
        
        REPOSITÓRIO:
        - Nome: roger-inatel/Testes_cotacao
        - Branch: {os.getenv('GITHUB_REF_NAME', 'main')}
        - Commit: {os.getenv('GITHUB_SHA', 'N/A')[:8]}
        
        MÉTRICAS:
        - Total de Testes: 23+ testes unitários
        - Jobs Executados: 6 jobs
        - Artefatos: Relatórios e pacotes gerados
        
        GitHub Actions: https://github.com/roger-inatel/Testes_cotacao/actions
        
        Notificação automática do GitHub Actions
        Sistema de Cotação de Moedas - Projeto Inatel C14 - Engenharia de Software
        """
        
        return html_content, text_content
    
    def enviar_email_smtp(self, html_content, text_content):
        """Envia email via SMTP (requer configuração de credenciais)"""
        try:
            # Configura mensagem
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"Pipeline CI/CD - {os.getenv('PIPELINE_STATUS', 'UNKNOWN')} - Sistema Cotação"
            msg['From'] = self.smtp_user
            msg['To'] = self.email_destino
            
            # Anexa versões texto e HTML
            part1 = MIMEText(text_content, 'plain', 'utf-8')
            part2 = MIMEText(html_content, 'html', 'utf-8')
            
            msg.attach(part1)
            msg.attach(part2)
            
            # Conecta e envia
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"❌ Erro no envio SMTP: {str(e)}")
            return False
    
    def enviar_email_simulado(self, html_content, text_content):
        """Simula envio de email para demonstração"""
        print("=" * 80)
        print("📧 SIMULAÇÃO DE ENVIO DE EMAIL - NOTIFICAÇÃO DE PIPELINE")
        print("=" * 80)
        print(f"📬 Destinatário: {self.email_destino}")
        print(f"📋 Assunto: Pipeline CI/CD - {os.getenv('PIPELINE_STATUS', 'UNKNOWN')} - Sistema Cotação")
        print(f"🕐 Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print()
        print("📄 CONTEÚDO (Versão Texto):")
        print("-" * 40)
        print(text_content)
        print("-" * 40)
        print()
        print("🌐 CONTEÚDO HTML: Formatação rica disponível no email")
        print("✅ Email simulado enviado com sucesso!")
        print("=" * 80)
        
        return True
    
    def executar_notificacao(self):
        """Executa o processo completo de notificação"""
        try:
            print("🚀 Iniciando sistema de notificação...")
            
            # Gera conteúdo
            html_content, text_content = self.gerar_relatorio_detalhado()
            
            # Tenta envio real se credenciais disponíveis
            if self.smtp_user and self.smtp_password:
                print("📧 Tentando envio via SMTP...")
                sucesso = self.enviar_email_smtp(html_content, text_content)
                if sucesso:
                    print("✅ Email enviado via SMTP com sucesso!")
                    return True
                else:
                    print("⚠️ Falha no SMTP, executando simulação...")
            
            # Executa simulação
            return self.enviar_email_simulado(html_content, text_content)
            
        except Exception as e:
            print(f"❌ Erro na notificação: {str(e)}")
            return False


def main():
    """Função principal"""
    print("🎯 Sistema de Notificação - Pipeline CI/CD")
    print("📧 Sistema de Cotação de Moedas - Inatel")
    print()
    
    notificador = NotificadorPipeline()
    
    try:
        resultado = notificador.executar_notificacao()
        
        if resultado:
            print()
            print("🎉 Notificação de pipeline executada com sucesso!")
            exit(0)
        else:
            print()
            print("⚠️ Falha na execução da notificação!")
            exit(1)
            
    except KeyboardInterrupt:
        print("\n⚠️ Execução interrompida pelo usuário")
        exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()