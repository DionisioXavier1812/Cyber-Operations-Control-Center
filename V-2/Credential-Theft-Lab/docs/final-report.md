# Final Report — Credential Theft Lab (V-2)

## 1. Visão Geral

Este relatório consolida a simulação de um ataque de credential theft em ambiente Windows corporativo, cobrindo três ambientes distintos: estação de trabalho, servidor de arquivos e servidor de domínio.

O objetivo é demonstrar como telemetria adequada, correlação de eventos e entendimento de MITRE ATT&CK permitem identificar e responder a ameaças de credential theft antes que o atacante obtenha controle total do ambiente.

---

## 2. Resumo Executivo

Um atacante com acesso inicial a uma estação de trabalho executou comandos PowerShell suspeitos, tentou acessar compartilhamentos sensíveis em um servidor de arquivos e realizou tentativas de autenticação no servidor de domínio.

A investigação DFIR correlacionou eventos de PowerShell, Sysmon, SMB e autenticação, permitindo identificar o padrão de ataque e responder de forma eficaz.

---

## 3. Ambientes Envolvidos

### **Ambiente 1 — Estação de Trabalho**
Execução de PowerShell com comandos suspeitos e criação de processos relacionados à enumeração de sistema.

### **Ambiente 2 — Servidor de Arquivos**
Acesso indevido a compartilhamentos sensíveis e tentativas de leitura em diretórios restritos.

### **Ambiente 3 — Servidor de Domínio**
Tentativas de autenticação com credenciais de usuário padrão em serviços administrativos.

---

## 4. Cadeia de Ataque

1. Execução de PowerShell com parâmetros suspeitos (Event ID 4104).
2. Criação de processos PowerShell (Sysmon Event ID 1).
3. Acesso a compartilhamentos SMB sensíveis (Event ID 5140).
4. Tentativas de login no servidor de domínio (Event ID 4625).

---

## 5. MITRE ATT&CK — Técnicas Mapeadas

### **T1059 — Command and Scripting Interpreter (PowerShell)**
Enumeração e coleta de informações.

### **T1003 — OS Credential Dumping (conceitual)**
Tentativa de acesso a credenciais em memória.

### **T1078 — Valid Accounts**
Uso indevido de credenciais válidas.

### **T1021 — Remote Services**
Movimento lateral via SMB ou RDP.

### **T1041 — Exfiltration Over C2 Channel (conceitual)**
Possível exfiltração de dados sensíveis.

---

## 6. Timeline DFIR Consolidada

- **14:22** — Execução de PowerShell na estação de trabalho.  
- **14:23** — Criação de processo PowerShell registrada pelo Sysmon.  
- **14:30** — Acesso ao compartilhamento Financeiro no servidor de arquivos.  
- **14:31** — Tentativas de leitura em diretórios restritos.  
- **14:40** — Tentativas de login no servidor de domínio.  
- **14:42** — Correlação dos eventos pelo analista (simulado).  

---

## 7. Evidências Principais

### **PowerShell — Event ID 4104**
Script Block Logging indicando execução de comandos suspeitos.

### **Sysmon — Event ID 1**
Criação de processo PowerShell com parâmetros incomuns.

### **SMB — Event ID 5140**
Acesso a compartilhamentos sensíveis.

### **Autenticação — Event ID 4625**
Falhas de login no servidor de domínio.

---

## 8. Conclusões

A simulação demonstra que:

- Telemetria adequada é essencial para detectar credential theft.  
- Logs de PowerShell e Sysmon são fundamentais para identificar execução suspeita.  
- A correlação entre eventos de endpoint, servidor de arquivos e servidor de domínio revela a cadeia de ataque.  
- Credential theft pode ser detectado antes que o atacante obtenha privilégios elevados.  

O módulo V-2 reforça a importância de monitoramento contínuo, políticas de acesso rígidas e detecções baseadas em comportamento.

---

## 9. Recomendações Gerais

- Habilitar Script Block Logging (Event ID 4104).  
- Monitorar criação de processos PowerShell (Sysmon Event ID 1).  
- Implementar MFA para contas administrativas.  
- Revisar permissões de compartilhamentos SMB.  
- Criar alertas para falhas de login em servidores de domínio.  
- Integrar logs de todos os ambientes ao SOC.  

---

## 10. Uso em Portfólio

Este módulo foi desenvolvido como parte da evolução do **Cyber Operations Control Center (COCC)**, seguindo o padrão **Dionisio Xavier V-2**, com documentação consolidada, técnica e voltada para Blue Team, SOC e DFIR.

Ele demonstra:

- capacidade de simular incidentes reais  
- domínio de MITRE ATT&CK  
- habilidade em DFIR  
- criação de logs simulados realistas  
- documentação profissional  
- estrutura modular e escalável  

Ideal para apresentação em entrevistas e processos seletivos na área de segurança cibernética.
