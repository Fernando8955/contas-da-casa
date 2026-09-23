#!/usr/bin/env python3
"""Gera index.html (PWA completo) a partir de index-body.html (fonte do app).

index-body.html tem só <title>, <style>, o markup e o <script> — é esse mesmo
arquivo que vai para o preview publicado. Aqui ele ganha o <head> do site:
manifesto, favicon, cores da barra de status e as telas de abertura do iPhone.
"""
import os

splash = ''
if os.path.exists('splash/links.html'):
    splash = open('splash/links.html').read().strip() + '\n'

body = open('index-body.html').read()
i = body.index('\n<header class="topbar">')
head, rest = body[:i], body[i:]
head = head.replace('<title>Contas da Casa</title>\n', '')

open('index.html', 'w').write("""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Contas da Casa</title>
<meta name="description" content="Controle simples de entradas e saidas da casa: luz, agua, gas, internet, aluguel e mercado. Funciona offline e guarda tudo no proprio aparelho.">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#F1F4F1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111613" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Contas">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="icons/favicon-32.png" sizes="32x32">
<link rel="icon" type="image/png" href="icons/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="icons/icon-192.png">
""" + splash + head + """<style>
html{color-scheme:light dark}
:root{padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}
</style>
</head>
<body>
""" + rest + """
<script>
/* Service worker: faz o app abrir offline e se atualizar sozinho.
   Quando uma versao nova assume o controle, a pagina recarrega uma vez —
   sem isso o celular continuaria mostrando a versao do cache. */
if ("serviceWorker" in navigator) {
  var jaTinhaSW = !!navigator.serviceWorker.controller;
  var recarregando = false;
  navigator.serviceWorker.addEventListener("controllerchange", function(){
    if (!jaTinhaSW || recarregando) return;
    recarregando = true;
    location.reload();
  });
  window.addEventListener("load", function(){
    navigator.serviceWorker.register("sw.js").catch(function(){});
  });
}
</script>
</body>
</html>
""")
print('index.html gerado (%d links de tela de abertura)' % splash.count('<link'))
