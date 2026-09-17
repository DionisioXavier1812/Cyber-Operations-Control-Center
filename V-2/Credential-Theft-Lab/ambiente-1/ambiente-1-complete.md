# Ambiente 1 — Estação de Trabalho Comprometida (V-2)

## 1. Sobre o Cenário

Este ambiente representa o ponto inicial do ataque: uma estação de trabalho Windows pertencente ao domínio corporativo.  
O atacante obtém acesso inicial (simulado) e executa comandos PowerShell para coletar informações, identificar usuários, processos e possíveis caminhos para credential theft.

---

## 2. Arquitetura

- Windows 10/11 Workstation  
- Membro do domínio corp.local  
- Usuário padrão: corp\\usuario  
- PowerShell habilitado  
- Sysmon instalado e configurado  

---

## 3. Cadeia de Ataque (Ambiente 1)

1. Acesso inicial à estação de trabalho (simulado).  
2. Execução de PowerShell com comandos suspeitos.  
3. Enumeração de processos, usuários e chaves de registro sensíveis.  
4. Criação de processos PowerShell registrada pelo Sysmon.  
5. Tentativa conceitual de credential dumping.  

---

## 4. Incidente

Eventos suspeitos identificados:

- Execução de PowerShell com parâmetros incomuns.  
- Script Block Logging indicando comandos de enumeração.  
- Criação de processos PowerShell com ExecutionPolicy Bypass.  
- Tentativa de acesso a chaves de registro sensíveis.  

---

## 5. Impacto

- Exposição potencial de credenciais de usuário.  
- Possível uso da estação como ponto inicial para movimento lateral.  
- Risco de escalonamento de privilégios caso credenciais sejam obtidas.  

---

## 6. Logs Simulados (Formato Real)

### ?? Windows Event Log — PowerShell (Event ID 4104)

`xml
<Event>
  <System>
    <Provider Name="Microsoft-Windows-PowerShell"/>
    <EventID>4104</EventID>
    <TimeCreated SystemTime="2024-11-12T14:22:31.1234567Z"/>
  </System>
  <EventData>
    <Message>Script block logging: suspicious PowerShell command executed.</Message>
    <ScriptBlockText>Get-Process; Get-LocalUser; Get-Item HKLM:\SECURITY</ScriptBlockText>
    <User>corp\\usuario</User>
    <Computer>WS-001.corp.local</Computer>
  </EventData>
</Event>

<Event>
  <System>
    <Provider Name="Microsoft-Windows-Sysmon"/>
    <EventID>1</EventID>
    <TimeCreated SystemTime="2024-11-12T14:23:10.9876543Z"/>
  </System>
  <EventData>
    <RuleName>Suspicious PowerShell Execution</RuleName>
    <Image>C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe</Image>
    <CommandLine>powershell.exe -NoProfile -ExecutionPolicy Bypass -Command Get-Process</CommandLine>
    <User>corp\\usuario</User>
    <Computer>WS-001.corp.local</Computer>
  </EventData>
</Event>
