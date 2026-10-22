# Wero1Wager — Central mundial de IDs de afiliados e recebimentos

Versão de arquitetura: 2026-10-21. Status: **proposta técnica registrada, sem integrações comerciais ativas**.

## Objetivo
Administrar múltiplos parceiros e países no mesmo aplicativo, mantendo identificação, atribuição, reconciliação e recebimento segregados por contrato e jurisdição.

## Entidades
- partner: partner_id interno, razão social, domínio, país, licença e situação da verificação, tipo de atividade.
- affiliate_account: affiliate_account_id interno, partner_id, external_affiliate_id, país, moeda, status contratual, termos de atribuição.
- campaign: campaign_id interno, affiliate_account_id, external_campaign_id, origem, canal, UTM, aprovação de publicidade.
- tracking_link: tracking_id interno, external_tracking_id, URL aprovada, elegibilidade geográfica e idade mínima, data de expiração.
- conversion: conversion_id interno, external_transaction_id, referência de relatório autenticado, deduplicação, status de qualificação.
- commission: commission_id interno, external_commission_id, modelo CPA/RevShare/Híbrido, base contratual, moeda, valores estimados/aprovados/liquidados, ajustes, proveniência.
- settlement: settlement_id interno, external_payment_id, lote, comprovante emitido pelo parceiro, valor, moeda, data e status validado.
- payout_destination: referência/token do provedor, titular autorizado e moeda. **Não guardar senhas, chaves bancárias, números completos de contas ou credenciais em tabelas de interface.**

## Regras
1. Chave única composta para IDs externos por parceiro e conta; nunca pressupor unicidade global.
2. Ledger append-only para alterações financeiras e conciliação idempotente; manter trilha de auditoria.
3. Relatórios autenticados por API/webhook assinado ou arquivo validado, não por cliques.
4. Separar estimado, pendente, aprovado, liquidado e transferido; só confirmar com fonte verificável.
5. Converter moedas apenas para exibição com taxa, fonte e horário; manter montante original.
6. Perfis de acesso e isolamento por parceiro/país; criptografia de tokens e rotação de credenciais.
7. Não ativar indicação comercial de apostas antes de autorização jurídica, licenças e contratos para a jurisdição do usuário, incluindo regras de publicidade e proteção de menores.
8. Nenhuma aposta, depósito, saque ou transferência bancária do usuário será processada pelo Wero1Wager.
9. Dashboard mostra por parceiro: campanhas, cliques válidos, conversões confirmadas, comissões aprovadas, liquidações e bloqueios.
10. Nunca inventar IDs de parceiros, transações, vendas, comissões ou pagamentos.

## Plano de execução
A. Criar esquema e migrações em banco de staging isolado.
B. Implementar endpoints administrativos autenticados para parceiros/contas/campanhas.
C. Criar adaptadores por parceiro, inicialmente somente leitura, com dados simulados.
D. Adicionar conciliação autenticada, testes de idempotência e de segurança.
E. Validar elegibilidade e contratos por país; fazer Double Check e revisão jurídica.
F. Homologar antes de qualquer integração comercial ou deploy.

**Design visual:** preservar integralmente o protótipo premium final aprovado.
