#!/usr/bin/env bash
# Publica o app em https://minhascontai.app (Cloudflare).
# Uso: ./deploy.sh
set -euo pipefail
cd "$(dirname "$0")"

python3 build.py

rm -rf dist
mkdir -p dist/icons dist/splash
cp index.html manifest.webmanifest sw.js favicon.ico dist/
cp icons/icon-192.png icons/icon-512.png icons/icon-maskable-512.png icons/favicon-32.png dist/icons/
cp splash/*.png dist/splash/

echo
echo "Lembrete: subiu o número da versão do cache em sw.js? (contas-da-casa-vN)"
echo

npx --yes wrangler@4 deploy
