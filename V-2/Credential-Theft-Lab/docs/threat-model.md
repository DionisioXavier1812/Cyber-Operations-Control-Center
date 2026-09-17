# Threat Model — Credential Theft Lab (V-2)

## 1. Visão Geral do Cenário

Este threat model descreve o risco de credential theft em um ambiente Windows corporativo, onde um atacante obtém acesso inicial a uma estação de trabalho e tenta escalar privilégios utilizando técnicas de coleta de credenciais, movimento lateral e abuso de contas válidas.

O objetivo é fornecer uma visão clara das ameaças, superfícies de ataque, técnicas MITRE ATT&CK envolvidas e controles de mitigação.

---

## 2. Ativos Críticos

- Credenciais de usuários e administradores.
- Servidor de domínio (Active Directory).
- Servidor de arquivos com dados sensíveis.
- Estações de trabalho corporativas.
- Sessões autenticadas (Kerberos/NTLM).

---

## 3. Superfícies de Ataque

- PowerShell habilitado em endpoints.
- Serviços SMB expostos internamente.
- Sessões RDP internas.
- Armazenamento de credenciais em memória.
- Políticas fracas de autenticação.

---

## 4. Ameaças Principais

- Execução de PowerShell com comandos suspeitos.
- Tentativa de credential dumping (conceitual).
- Uso indevido de credenciais válidas.
- Movimento lateral entre máquinas internas.
- Tentativas de autenticação em serviços administrativos.

---

## 5. Vetores de Ataque

- PowerShell Script Block Logging (Event ID 4104).
- Sysmon Process Creation (Event ID 1).
- Acesso a compartilhamentos SMB (Event ID 5140).
- Falhas de autenticação (Event ID 4625).

---

## 6. MITRE ATT&CK — Técnicas Mapeadas

### **T1059 — Command and Scripting Interpreter (PowerShell)**
Execução de comandos para enumeração e coleta de informações.

### **T1003 — OS Credential Dumping (conceitual)**
Tentativa de acesso a credenciais em memória.

### **T1078 — Valid Accounts**
Uso indevido de credenciais válidas para acessar recursos internos.

### **T1021 — Remote Services**
Movimento lateral via SMB ou RDP.

### **T1041 — Exfiltration Over C2 Channel (conceitual)**
Possível exfiltração de dados sensíveis.

---

## 7. Controles de Mitigação

- Habilitar PowerShell Constrained Language Mode.
- Monitorar Event ID 4104 (Script Block Logging).
- Monitorar Event ID 1 (Sysmon Process Creation).
- Implementar MFA para contas administrativas.
- Segmentar rede e limitar acesso lateral.
- Revis@"
# Threat Model — Credential Theft Lab (V-2)

## 1. Visão Geral do Cenário

Este threat model descreve o risco de credential theft em um ambiente Windows corporativo, onde um atacante obtém acesso inicial a uma estação de trabalho e tenta escalar privilégios utilizando técnicas de coleta de credenciais, movimento lateral e abuso de contas válidas.

O objetivo é fornecer uma visão clara das ameaças, superfícies de ataque, técnicas MITRE ATT&CK envolvidas e controles de mitigação.

---

## 2. Ativos Críticos

- Credenciais de usuários e administradores.
- Servidor de domínio (Active Directory).
- Servidor de arquivos com dados sensíveis.
- Estações de trabalho corporativas.
- Sessões autenticadas (Kerberos/NTLM).

---

## 3. Superfícies de Ataque

- PowerShell habilitado em endpoints.
- Serviços SMB expostos internamente.
- Sessões RDP internas.
- Armazenamento de credenciais em memória.
- Políticas fracas de autenticação.

---

## 4. Ameaças Principais

- Execução de PowerShell com comandos suspeitos.
- Tentativa de credential dumping (conceitual).
- Uso indevido de credenciais válidas.
- Movimento lateral entre máquinas internas.
- Tentativas de autenticação em serviços administrativos.

---

## 5. Vetores de Ataque

- PowerShell Script Block Logging (Event ID 4104).
- Sysmon Process Creation (Event ID 1).
- Acesso a compartilhamentos SMB (Event ID 5140).
- Falhas de autenticação (Event ID 4625).

---

## 6. MITRE ATT&CK — Técnicas Mapeadas

### **T1059 — Command and Scripting Interpreter (PowerShell)**
Execução de comandos para enumeração e coleta de informações.

### **T1003 — OS Credential Dumping (conceitual)**
Tentativa de acesso a credenciais em memória.

### **T1078 — Valid Accounts**
Uso indevido de credenciais válidas para acessar recursos internos.

### **T1021 — Remote Services**
Movimento lateral via SMB ou RDP.

### **T1041 — Exfiltration Over C2 Channel (conceitual)**
Possível exfiltração de dados sensíveis.

---

## 7. Controles de Mitigação

- Habilitar PowerShell Constrained Language Mode.
- Monitorar Event ID 4104 (Script Block Logging).
- Monitorar Event ID 1 (Sysmon Process Creation).
- Implementar MFA para contas administrativas.
- Segmentar rede e limitar acesso lateral.
- Revisar permissões de compartilhamentos SMB.
- Alertas para falhas de autenticação em DCs.

---

## 8. Requisitos de Telemetria

- Windows Event Log (Security, PowerShell).
- Sysmon (Event IDs 1, 3, 10).
- Logs de autenticação (Kerberos/NTLM).
- Logs de acesso a compartilhamentos SMB.

---

## 9. Objetivo do Threat Model

Fornecer uma visão estruturada das ameaças relacionadas a credential theft em ambiente Windows corporativo, permitindo que Blue Team, SOC e DFIR planejem detecções, respostas e melhorias de segurança.

Este documento segue o padrão Dionisio Xavier V-2:  
**documentação consolidada, técnica, objetiva e voltada para portfólio profissional.**
