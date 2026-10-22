# Wero1Wager — Integração multioperadora e baixa latência

Data: 2026-10-21. Status: arquitetura aprovada para planejamento; integrações externas ainda não ativadas.

## Objetivo
Navegação rápida, informações atualizadas e integração desacoplada com provedores licenciados. Latência zero não é tecnicamente garantível.

## Fluxo
Provedores autorizados -> conectores individuais -> fila/event bus -> normalização de esportes/eventos/mercados -> cache compartilhado -> API pública somente leitura -> interface multilíngue.

## Categorias
Esportes tradicionais, eSports e, somente onde permitido, mercados virtuais/cassino. Cada vertical exige fontes e licenças próprias. O sistema não processa apostas, depósitos, saques ou liquidação de apostas.

## SLOs iniciais para homologação (metas, não medições)
- API pública: p95 <= 250 ms dentro da região de hospedagem, excluindo rede do usuário.
- Carregamento da página: não bloquear renderização esperando dados de operadoras.
- Atualização: registrar timestamp do provedor e de ingestão; expor idade do dado.
- Provedor indisponível: circuit breaker, timeout, backoff exponencial e conteúdo marcado como indisponível/desatualizado.
- Cache: TTL por tipo de dado e política de invalidação, sem servir odds expiradas como atuais.
- IA: processamento assíncrono; nenhuma inferência bloqueia resposta crítica.
- Telemetria: p50/p95/p99, taxa de erros, idade do dado, fila, reconnects, health e disponibilidade por parceiro.

## Conectores e governança
- Usar apenas APIs oficiais/licenciadas e contratos autorizados.
- Isolar credenciais em secret manager; rate limit por parceiro e idempotência.
- Padronizar IDs internos, preservando IDs externos e origem por parceiro.
- Separar feeds de dados, atribuição de afiliado e relatórios de comissões.
- Sem cliques artificiais ou automação de apostas; o usuário decide o encaminhamento.
- Bloqueio geográfico, idade mínima, consentimento e conformidade publicitária por jurisdição.

## Gates de entrega
1. Mock adapters e testes de contrato em staging isolado.
2. Simular latência, quedas, dados fora de ordem, duplicações, picos e falhas parciais.
3. Teste de carga com métricas documentadas, inclusive dispositivos móveis.
4. Double Check de segurança e isolamento financeiro.
5. Canary e rollback, somente após autorização e validação; não afetar produção.
6. Identidade visual premium final permanece congelada.

## Estado real
Não há operadoras nem provedores de odds conectados. A interface existente usa eventos sintéticos de demonstração; não afirmar que são resultados ao vivo.
