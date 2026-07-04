# MGSM Commerce Platform

سامانه فروش چندکاناله MGSM شامل:

- Django Backend API
- Telegram Bot
- Telegram Mini App
- WordPress/WooCommerce Bridge Plugin
- PostgreSQL
- Redis
- Docker Compose

## Project Structure

- `apps/core-api`: هسته Backend
- `apps/telegram-bot`: بات تلگرام
- `apps/mini-app`: Telegram Mini App
- `plugins/mgsm-commerce-bridge`: افزونه اتصال WooCommerce
- `packages/api-contracts`: قراردادهای API
- `packages/shared-types`: Typeهای مشترک
- `infrastructure`: تنظیمات Docker و Nginx
- `docs`: مستندات فنی
- `tests/e2e`: تست‌های End-to-End

## Branches

- `main`: نسخه Production
- `develop`: شاخه اصلی توسعه
- `feature/*`: توسعه قابلیت‌ها
- `fix/*`: اصلاح خطاها
- `release/*`: آماده‌سازی انتشار
