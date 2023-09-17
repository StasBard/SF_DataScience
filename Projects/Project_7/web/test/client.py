import requests

if __name__ == '__main__':
    # Отправляем запрос на сервер с набором данных
    r = requests.post('http://localhost:5000/predict',
        json=[2,1820,3,1,0,1,4,7,3,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1])
    
    print('Статус сервера:', r.status_code)
    
    # Получаем предсказание стоимости недвижимости
    if r.status_code == 200:
        print('Ответ сервера - предсказание:', r.json()['prediction'])
    else:
        print('Ответ сервера:', r.text)