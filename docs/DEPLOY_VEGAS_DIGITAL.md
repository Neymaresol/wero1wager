# Wero1Wager Vegas Digital — plano de publicação

Estado: homologação, sem apostas reais.

## Artefato visual aprovado
O pacote `wero1wager-html.zip` inclui `index.html` e `assets/` (logo, Werozinha e demais recortes da imagem aprovada). **Não publicar somente o HTML sem os assets**, pois quebraria o visual.

## Integração com FastAPI
1. Extrair `index.html` e `assets/` do pacote.
2. Colocar o HTML na raiz do projeto e as imagens em `static/assets/`.
3. Atualizar as referências relativas do HTML de `assets/` para `/static/assets/`.
4. Confirmar `/`, `/health`, `/static/assets/logo.webp`, `/static/assets/werozinha.webp` e as demais imagens com HTTP 200.
5. Executar `python -m pytest -q tests`, validar desktop/mobile e revisar os avisos de modo demonstração.
6. Após Double Check, revisão e autorização, fazer merge do PR para `main` (Render faz deploy automático); verificar saúde e rollback.

## Gates
- Preservar exatamente as cores e identidade do protótipo aprovado.
- Não habilitar pagamentos, depósitos, saques, apostas reais ou bônus sem conformidade jurídica e integração licenciada.
- Não declarar odds, receitas ou usuários online como reais sem fonte verificável.
- Render no plano free não assegura disponibilidade 24/7 sem cold start.

Última atualização: 2026-10-21 22:16 BRT.
