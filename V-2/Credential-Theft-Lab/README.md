# Dionisio Xavier

## ?? Credential Theft Lab — V-2

[![Status](https://img.shields.io/badge/status-active-green)]()
[![Focus](https://img.shields.io/badge/focus-blue%20team-red)]()
[![Domain](https://img.shields.io/badge/domain-Windows%20Enterprise-blue)]()

Simulação completa de um ataque de credential theft em ambiente Windows corporativo, com foco em Blue Team, DFIR, MITRE ATT&CK, logs simulados, IoCs, cadeia de ataque, timeline DFIR e playbooks de resposta.

Inclui:

- DFIR
- MITRE ATT&CK
- Logs simulados (Windows + Sysmon)
- IoCs
- Playbooks
- Threat Modeling
- Incident Response

---

## ?? Objetivo do Projeto

- Simular um cenário realista de credential theft em ambiente Windows corporativo.
- Mapear a cadeia de ataque utilizando MITRE ATT&CK.
- Produzir logs simulados com estrutura real.
- Documentar a investigação DFIR com timeline, evidências e conclusões.
- Criar playbooks de resposta para Blue Team e SOC.
- Consolidar documentação técnica voltada para portfólio profissional.

---

## ?? Estrutura do Repositório

- docs/
  - threat-model.md
  - final-report.md
- ambiente-1/
  - ambiente-1-complete.md
- ambiente-2/
  - ambiente-2-complete.md
- ambiente-3/
  - ambiente-3-complete.md

---

## ?? Conteúdo do Projeto

### ?? Cenário Principal

Ambiente Windows corporativo com estações de trabalho, servidor de arquivos e servidor de domínio (Active Directory).  
O atacante tenta obter credenciais privilegiadas utilizando PowerShell e técnicas de credential dumping.

### ?? Ameaças Simuladas

- Execução de PowerShell com comandos suspeitos.
- Tentativa de credential dumping (simulada).
- Uso indevido de credenciais válidas.
- Movimento lateral entre máquinas internas.

### ?? Cadeia de Ataque

1. Execução de PowerShell na estação de trabalho.
2. Enumeração de sistema e coleta de informações.
3. Acesso indevido ao servidor de arquivos.
4. Tentativas de autenticação no servidor de domínio.

### ?? Ambientes

- Ambiente 1: Estação de trabalho comprometida.
- Ambiente 2: Servidor de arquivos com acesso indevido.
- Ambiente 3: Servidor de domínio@"
# Dionisio Xavier

## ?? Credential Theft Lab — V-2

[![Status](https://img.shields.io/badge/status-active-green)]()
[![Focus](https://img.shields.io/badge/focus-blue%20team-red)]()
[![Domain](https://img.shields.io/badge/domain-Windows%20Enterprise-blue)]()

Simulação completa de um ataque de credential theft em ambiente Windows corporativo, com foco em Blue Team, DFIR, MITRE ATT&CK, logs simulados, IoCs, cadeia de ataque, timeline DFIR e playbooks de resposta.

Inclui:

- DFIR
- MITRE ATT&CK
- Logs simulados (Windows + Sysmon)
- IoCs
- Playbooks
- Threat Modeling
- Incident Response

---

## ?? Objetivo do Projeto

- Simular um cenário realista de credential theft em ambiente Windows corporativo.
- Mapear a cadeia de ataque utilizando MITRE ATT&CK.
- Produzir logs simulados com estrutura real.
- Documentar a investigação DFIR com timeline, evidências e conclusões.
- Criar playbooks de resposta para Blue Team e SOC.
- Consolidar documentação técnica voltada para portfólio profissional.

---

## ?? Estrutura do Repositório

- docs/
  - threat-model.md
  - final-report.md
- ambiente-1/
  - ambiente-1-complete.md
- ambiente-2/
  - ambiente-2-complete.md
- ambiente-3/
  - ambiente-3-complete.md

---

## ?? Conteúdo do Projeto

### ?? Cenário Principal

Ambiente Windows corporativo com estações de trabalho, servidor de arquivos e servidor de domínio (Active Directory).  
O atacante tenta obter credenciais privilegiadas utilizando PowerShell e técnicas de credential dumping.

### ?? Ameaças Simuladas

- Execução de PowerShell com comandos suspeitos.
- Tentativa de credential dumping (simulada).
- Uso indevido de credenciais válidas.
- Movimento lateral entre máquinas internas.

### ?? Cadeia de Ataque

1. Execução de PowerShell na estação de trabalho.
2. Enumeração de sistema e coleta de informações.
3. Acesso indevido ao servidor de arquivos.
4. Tentativas de autenticação no servidor de domínio.

### ?? Ambientes

- Ambiente 1: Estação de trabalho comprometida.
- Ambiente 2: Servidor de arquivos com acesso indevido.
- Ambiente 3: Servidor de domínio alvo de tentativas de escalonamento.

---

## ?? DFIR

A investigação acompanha eventos desde a execução de PowerShell até tentativas de login no servidor de domínio, correlacionando logs Windows, Sysmon e IoCs simulados.

---

## ?? Logs e IoCs

Exemplos:

- Event ID 4104 — PowerShell Script Block Logging  
- Event ID 1 — Sysmon Process Creation  
- Event ID 5140 — Acesso a compartilhamento  
- Event ID 4625 — Falha de autenticação  

---

## ?? MITRE ATT&CK

Técnicas utilizadas:

- T1059 — PowerShell  
- T1003 — Credential Dumping  
- T1078 — Valid Accounts  
- T1021 — Remote Services  
- T1041 — Exfiltration (conceitual)  

---

## ??? Topics do Repositório

- blue-team  
- dfir  
- soc  
- windows-security  
- credential-theft  
- mitre-attack  
- incident-response  
- logs  
- iocs  
- powershell  

---

## ?? Skills Técnicas

- DFIR  
- MITRE ATT&CK  
- Blue Team  
- Threat Hunting  
- Incident Response  
- Logs e Telemetria  
- PowerShell  
- Git  
- Documentação técnica  
- Windows Security  

---

## ?? Documentação Avançada

- docs/threat-model.md  
- docs/final-report.md  

---

## ?? Contato

LinkedIn: https://www.linkedin.com/in/dionisio-xavier  
GitHub: https://github.com/DionisioXavier1812
