# MGSM Commerce Platform

سامانه مستقل فروش محصولات و خدمات دیجیتال از طریق بات تلگرام MGSM.

## معماری پروژه

بات فروش از فروشگاه اصلی سایت مستقل است و اطلاعات زیر را در Backend اختصاصی خود مدیریت می‌کند:

- کاربران بات
- محصولات و دسته‌بندی‌ها
- قیمت‌ها
- موجودی دیجیتال
- سفارش‌ها
- کیف پول
- تحویل محصولات
- تیکت‌های پشتیبانی
- کد تخفیف
- معرفی دوستان
- باشگاه مشتریان
- گزارش‌ها

سایت و WooCommerce فقط برای ایجاد و تأیید پرداخت بانکی استفاده می‌شوند.

## جریان پرداخت

1. کاربر داخل بات سفارش ثبت می‌کند.
2. Backend یک سفارش داخلی و Payment Intent می‌سازد.
3. افزونه Payment Bridge یک لینک پرداخت سایت ایجاد می‌کند.
4. کاربر در سایت وارد درگاه بانکی می‌شود.
5. سایت پرداخت را Verify می‌کند.
6. نتیجه پرداخت با Webhook امضاشده به Backend ارسال می‌شود.
7. Backend سفارش را پرداخت‌شده ثبت می‌کند.
8. محصول تحویل داده می‌شود.

## Project Structure

- `apps/core-api`: Backend اصلی Django
- `apps/telegram-bot`: بات تلگرام با aiogram
- `plugins/mgsm-bot-payment-bridge`: افزونه پرداخت وردپرس
- `packages/api-contracts`: قراردادهای ارتباط Backend و افزونه
- `infrastructure/docker`: تنظیمات Docker
- `infrastructure/nginx`: تنظیمات Nginx
- `docs/architecture`: مستندات معماری
- `docs/adr`: تصمیم‌های معماری
- `docs/api`: مستندات API
- `docs/runbooks`: دستورالعمل‌های نگهداری
- `tests/contract`: تست قرارداد Backend و افزونه
- `tests/e2e`: تست‌های End-to-End

## Git Strategy

- `main`: نسخه Production
- `develop`: شاخه اصلی توسعه
- `feature/*`: توسعه قابلیت
- `fix/*`: اصلاح خطا
- `release/*`: آماده‌سازی انتشار

توسعه قابلیت‌های پروژه مستقیماً روی `main` یا `develop` انجام نمی‌شود.

تنظیمات اولیه Sprint 0 می‌توانند مستقیماً روی `develop` ثبت شوند.

## Main Technologies

- Python
- Django
- Django REST Framework
- aiogram
- PostgreSQL
- Redis
- Celery
- Docker Compose
- WordPress/WooCommerce Plugin
