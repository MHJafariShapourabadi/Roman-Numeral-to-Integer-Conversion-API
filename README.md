
# یک API برای تبدیل عدد رومی به عدد صحیح


این پروژه یک API ساده را با استفاده از FastAPI پیاده‌سازی می‌کند که عددهای رومی را به مقادیر صحیح متناظر آن‌ها تبدیل می‌کند. این پروژه شامل مدیریت خطا برای عددهای رومی نامعتبر است و اطمینان می‌دهد که ورودی‌ها طبق قوانین نگارش عددهای رومی اعتبارسنجی شده‌اند.


## فهرست مطالب
- [ویژگی‌ها](#features)
- [نصب](#installation)
- [استفاده](#usage)
- [نقاط پایانی API](#api-endpoints)
- [آزمایش](#testing)

---


## ویژگی‌ها
- تبدیل عددهای رومی (I, V, X, L, C, D, M) به عددهای صحیح.
- پشتیبانی از عددها بین ۱ تا ۳۹۹۹.
- مدیریت خطا برای عددهای رومی نامعتبر.
- استفاده از FastAPI برای عملکرد بهینه.

---


## نصب

برای راه‌اندازی پروژه به‌صورت محلی، مراحل زیر را دنبال کنید:

1. مخزن را کلون کنید:
    ```bash
    git clone https://github.com/your-repo/roman-numeral-api.git
    cd roman-numeral-api
    ```

2. یک محیط مجازی ایجاد کنید (اختیاری اما توصیه‌شده):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # در ویندوز، از `venv\Scripts\activate` استفاده کنید
    ```

3. وابستگی‌های مورد نیاز را نصب کنید:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

4. برنامه FastAPI را با استفاده از Uvicorn اجرا کنید:
    ```bash
    uvicorn main:app --reload
    ```

این کار برنامه FastAPI را بر روی `http://127.0.0.1:8000` راه‌اندازی خواهد کرد.



---


## استفاده

شما می‌توانید از طریق یک کلاینت HTTP مانند `curl`، Postman، یا به‌طور مستقیم در مرورگر خود با استفاده از مستندات تعاملی FastAPI (Swagger UI) با API تعامل کنید.

برای دسترسی به مستندات، مرورگر خود را باز کرده و به آدرس زیر بروید:
- [Swagger UI](http://127.0.0.1:8000/docs)


---


## نقاط پایانی API

### `POST /convert/`

عدد رومی را به معادل عدد صحیح آن تبدیل می‌کند.

#### بدنه درخواست
- **roman_numeral**: رشته عدد رومی (به‌عنوان مثال، `"XXVII"`).

نمونه:
```json
{
  "roman_numeral": "XXVII"
}
```

#### بدنه پاسخ
- **integer_value**: معادل عدد صحیح عدد رومی.

نمونه:
```json
{
  "integer_value": 27
}
```


---


## تست

شما می‌توانید API را با استفاده از هر کلاینت HTTP (مانند Postman، curl) یا با استفاده از مستندات به‌طور خودکار تولید شده در Swagger UI تست کنید.

به‌عنوان مثال، با استفاده از `curl`:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/convert/' \
  -H 'Content-Type: application/json' \
  -d '{"roman_numeral": "MCMXCIV"}'
```
