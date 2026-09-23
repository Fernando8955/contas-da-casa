# Contas da Casa

PWA de controle de entradas e saídas da casa — luz, água, gás, internet, aluguel
e mercado. Funciona offline, instala como aplicativo no celular e guarda tudo no
próprio aparelho: nada é enviado para servidor nenhum.

**App:** https://fernando8955.github.io/contas-da-casa/

## O que faz

- Saldo do mês com entradas e saídas separadas, navegando mês a mês
- Contas fixas com dia de vencimento e selo *Pago / Vence em X dias / Vencida* —
  o botão **Pagar** já lança a despesa
- Lançamentos agrupados por dia, com filtro de entradas e saídas
- Orçamento mensal com barra que avisa ao passar de 80% e ao estourar
- Gastos por categoria em barras
- Exportar os lançamentos em CSV para Excel ou Google Sheets
- **Backup e restauração** em arquivo `.json` — importante, porque limpar os
  dados do navegador apaga tudo
- Atalhos no ícone do app (segure o ícone): "Nova saída" e "Nova entrada"
- Tela de abertura própria no iPhone, sem o flash branco do Safari
- Tema claro e escuro automático, e funciona offline depois da primeira visita

## Instalar no celular

- **Android / Chrome:** abra o link → menu ⋮ → "Instalar app"
- **iPhone / Safari:** abra o link → compartilhar → "Adicionar à Tela de Início"

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | o app inteiro, sem dependências |
| `index-body.html` | a fonte que o `build.py` usa para gerar o `index.html` |
| `build.py` | regera o `index.html` |
| `manifest.webmanifest` | nome, cores e ícones do app instalado |
| `sw.js` | service worker — é o que faz funcionar offline |
| `icons/` | ícones 192px, 512px, *maskable* e favicon |
| `favicon.ico` | ícone da aba do navegador |
| `splash/` | 17 telas de abertura do iPhone e iPad, e `links.html` com as media queries que o `build.py` injeta |

## Rodar na sua máquina

```
python3 -m http.server 8000
```

Abra `http://localhost:8000`. PWA só instala em `https://` ou em `localhost`.

## Ao mudar o app

Rode `python3 build.py` e suba o número da versão do cache em `sw.js`
(`contas-da-casa-v2` → `v3`), senão o celular continua servindo o que está no cache.
