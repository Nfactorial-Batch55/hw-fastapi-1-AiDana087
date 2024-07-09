from fastapi import FastAPI

app = FastAPI()




# 1. server-ping-pong
#
# Задание:
# Измените WSGI приложение так, чтобы на запрос GET /ping отвечал pong.
# На все остальные запросы отвечать Not Found
@app.get("/ping")
def say_pong():
    return {"pong"}

# 2. server-request-info
#
# Задание:
# Измените WSGI приложение так, чтобы на запрос GET /info возвращал информацию о запросе:
# HTTP-метод
# URL запроса
# Протокол запроса
@app.get("/info")
def return_info():
    return {
        "HTTP-метод": "GET",
        "URL запроса": "/info",
        "Протокол запроса": "http",
    }

# 3. fastapi-hello
#
# Задание:
# Создать хендлер на GET /, который возвращает {"message": "Hello, nfactorial!"}
@app.get("/")
def return_message():
    return {"message": "Hello, nfactorial!"}

# 4. fastapi-meaning-life
#
# Задание:
# Создать хендлер на POST /meaning-of-life, который возвращает {"meaning": "42"}
@app.post("/meaning-of-life")
def return_message():
    return {"meaning": "42"}

# 5. fastapi-nfactorial 💎
#
# Задание:
# Создать хендлер на GET /{num}, который возвращает факториал числа “num”.
@app.get("/{num}")
def return_factorial(num):
    result = 1
    for i in range(1, int(num)):
        result *= i
    return {result}
