# Ambiente 3 — Servidor de Domínio (Active Directory) — Tentativas de Autenticação (V-2)

## 1. Sobre o Cenário

Este ambiente representa o ponto mais crítico da simulação: o servidor de domínio (Domain Controller).  
Após acessar o servidor de arquivos (Ambiente 2), o atacante tenta autenticar-se no DC utilizando credenciais válidas de um usuário padrão, buscando escalonamento de privilégios.

O DC é o coração da infraestrutura corporativa — qualquer tentativa de autenticação suspeita deve ser tratada como incidente de alta prioridade.

---

## 2. Arquitetura

- Windows Server (Domain Controller)
- Domínio: corp.local
- Serviços críticos:
  - Active Directory
  - Kerberos
  - NTLM
  - LDAP
- Usuário envolvido: corp\\usuario

---

## 3. Cadeia de Ataque (Ambiente 3)

1. Atacante tenta autenticar-se no DC usando credenciais válidas.
2. Múltiplas falhas de autenticação (Event ID 4625).
3. Tentativas de acesso a serviços administrativos.
4. Padrão de brute-force leve (conceitual).
5. Correlação com eventos dos Ambientes 1 e 2.

---

## 4. Incidente

Eventos suspeitos:

- Tentativas de login no DC fora do horário normal.
- Falhas repetidas de autenticação.
- Tentativas de acesso a serviços administrativos.
- Uso de credenciais de usuário padrão em serviços restritos.

---

## 5. Impacto

- Risco de escalonamento de privilégios.
- Possível comprometimento do Active Directory.
- Exposição de toda a infraestrutura corporativa.
- Necessidade de resposta imediata pelo SOC.

---

## 6. Logs Simulados (Formato Real)

### ?? Windows Security Log — Falha de Autenticação (Event ID 4625)

`xml
<Event>
  <System>
    <Provider Name="Microsoft-Windows-Security-Auditing"/>
    <EventID>4625</EventID>
    <TimeCreated SystemTime="2024-11-12T14:40:12.0000000Z"/>
  </System>
  <EventData>
    <TargetUserName>Administrator</TargetUserName>
    <TargetDomainName>corp</TargetDomainName>
    <Status>0xC000006A</Status>
    <SubStatus>0xC0000064</SubStatus>
    <IpAddress>10.0.0.55</IpAddress>
    <WorkstationName>WS-001</WorkstationName>
    <Computer>DC01.corp.local</Computer>
  </EventData>
</Event>
<Event>
  <System>
    <Provider Name="Microsoft-Windows-Security-Auditing"/>
    <EventID>4625</EventID>
    <TimeCreated SystemTime="2024-11-12T14:41:00.0000000Z"/>
  </System>
  <EventData>
    <TargetUserName>corp\\usuario</TargetUserName>
    <TargetDomainName>corp</TargetDomainName>
    <Status>0xC000006A</Status>
    <SubStatus>0xC0000064</SubStatus>
    <IpAddress>10.0.0.55</IpAddress>
    <WorkstationName>WS-001</WorkstationName>
    <Computer>DC01.corp.local</Computer>
    <Service>LDAP</Service>
  </EventData>
</Event>

---

# ?? **PARTE B — Fechamento + Set-Content (cole depois)**

`powershell
Set-Content ".\V-2\Credential-Theft-Lab\ambiente-3\ambiente-3-complete.md"
