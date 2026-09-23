#!/usr/bin/env python3
"""Gera index.html (PWA completo) a partir de index-body.html (fonte do app)."""
body = open('index-body.html').read()
i = body.index('\n<header class="topbar">')
head, rest = body[:i], body[i:]
head = head.replace('<title>Contas da Casa</title>\n', '')
open('index.html','w').write("""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Contas da Casa</title>
<meta name="description" content="Controle simples de entradas e saidas da casa: luz, agua, gas, internet, aluguel e mercado.">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#F1F4F1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111613" media="(prefers-color-scheme: dark)">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Contas">
<link rel="apple-touch-icon" href="icons/icon-192.png">
<link rel="icon" href="icons/icon-192.png">
""" + head + """<style>
html{color-scheme:light dark}
:root{padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}
</style>
</head>
<body>
""" + rest + """
<script>
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function(){
    navigator.serviceWorker.register("sw.js").catch(function(){});
  });
}
</script>
</body>
</html>
""")
print('index.html gerado')
