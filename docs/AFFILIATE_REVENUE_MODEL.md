# Wero1Wager — Modelo de receita por parceiros

Data de registro: 2026-10-21. **Status: proposta de arquitetura, não integrada a operadoras.**

## Papel do sistema
Wero1Wager publica estatísticas e análises esportivas, com identificação de fontes e sem promessa de lucro. O usuário decide se quer visitar um parceiro. Somente operadoras devidamente autorizadas na jurisdição do usuário podem ser consideradas para indicação, sujeito a revisão jurídica e às regras de publicidade locais.

## Modelos de comissão
- CPA: valor fixo por cliente elegível e confirmado pelo parceiro.
- Revenue share: percentual contratual da receita líquida elegível, **não** do valor total apostado.
- Híbrido: CPA + revenue share, quando expressamente contratado.

Exemplos ilustrativos, **não ofertas reais**: 100 clientes qualificados × R$50 CPA = R$5.000; R$10.000 receita líquida elegível × 25% = R$2.500. Descontos, estornos, impostos, prazos e limites dependem de contrato.

## Fluxo de conciliação
1. Cadastro e validação jurídica/comercial do operador e do programa de afiliados.
2. Validar jurisdição, restrições geográficas, idade mínima e consentimento antes de qualquer encaminhamento.
3. Gerar URL de atribuição aprovada pelo parceiro, com transparência de afiliação e sem redirecionamento oculto.
4. Registrar eventos permitidos com minimização de dados e proteção antifraude; não gerar cliques ou cadastros artificiais.
5. Ingerir relatório autenticado da operadora, deduplicar e conciliar conversões.
6. Separar: estimado, pendente, aprovado, liquidado, transferido. Valores confirmados somente com evidência do parceiro financeiro.
7. Exibir dashboards de conversão, receita e comissões com proveniência e data/hora de atualização.

## Gates P0
- Não ativar links comerciais de apostas antes de autorização jurídica e contratual por país.
- Não aceitar depósitos, apostas, saques, carteiras ou repasses de usuários pelo Wero1Wager.
- Não inventar odds ao vivo, resultados, comissões ou transferências.
- Não personalizar marketing de apostas a menores ou pessoas vulneráveis.
- Sem integrações de pagamento, operadores ou parceiros ativas nesta etapa.
- Preservar a arte premium aprovada, sem mudanças visuais sem autorização.

## Próximas implementações
Tabela de parceiros e jurisdições; engine de elegibilidade; cadastro de contratos e modelos CPA/RevShare/Híbrido; ingestão de relatórios autenticados; ledger auditável de comissões; testes isolados; staging; canary; rollback.
