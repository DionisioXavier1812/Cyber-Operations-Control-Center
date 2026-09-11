# Incident Workflow

IOC
 ->
Detection Rule
 ->
Alert
 ->
DFIR
 ->
Playbook
 ->
Recovery

Status:
mkdir soc-unit\labs\detection-lab-001 -Force

@"
# Detection Lab 001

## Cenário

Tower-Satsec-Mitigation

## Objetivo

Simular o fluxo completo:

IOC
 ->
Logs
 ->
Detecção
 ->
Alerta
 ->
DFIR

## Ambiente

- VPN
- Firewall
- Router
- SatCom

## Fontes de Dados

- VPN Logs
- Authentication Logs
- PowerShell Events

Status: OPERACIONAL

