#!/data/data/com.termux/files/usr/bin/bash
# push_navier_stokes.sh — идемпотентная отправка папки navier-stokes/ в репозиторий.
# Совместим с Termux (Android) и обычным Linux/macOS.
# Первый запуск попросит логин и PAT (classic, scope repo); логин: wild8highlander.
# При настроенном credential.helper store дальше спросит один раз.
set -e

# 1) найти корень репозитория (скрипт можно звать из любой точки)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null || true)"
if [ -z "$REPO" ]; then
    echo "ОШИБКА: скрипт лежит вне git-репозитория. Клонируйте репозиторий и запустите из navier-stokes/."
    exit 1
fi
cd "$REPO"
echo "Репозиторий: $REPO"
echo "Удалённый:  $(git remote get-url origin 2>/dev/null || echo 'не задан')"

# 2) одноразовая настройка окружения Termux (безопасно повторять)
command -v git >/dev/null || { echo "Установите git: pkg install git"; exit 1; }
git config credential.helper store || true

# 3) свежайшая база (offline-безопасно)
git pull --rebase --autostash || echo "  (пропущено: нет сети или нечего тянуть)"

# 4) добавить только папку пакета
git add -A

if git diff --cached --quiet; then
    echo "Нет изменений в navier-stokes/ — коммит не нужен."
else
    MSG="navier-stokes: 7 open problems executed (P1-P7), monograph RU/EN x DOCX/PDF, 5 plots, JSON results"
    git commit -m "$MSG"
fi

# 5) отправка
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
git push origin "$BRANCH" && echo "ОК: отправлено в origin/$BRANCH" || {
    echo "ОШИБКА push. Проверьте PAT (classic, scope repo) и сеть."
    echo "Повторная настройка учётных данных: git push (введёт логин/токен заново)."
    exit 1
}

echo "Рекомендация: git tag v1.5.0-open-problems && git push origin v1.5.0-open-problems"
