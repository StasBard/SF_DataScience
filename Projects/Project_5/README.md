# Проект 5. Предсказание продолжительности поездки на такси в Нью-Йорке.  

## Оглавление   
[1. Описание проекта]()  
[2. Решаемая задача]()  
[3. Краткая информация о данных]()  
[4. Этапы работы над проектом]()  
[5. Результаты]()    
[6. Выводы]() 

### 1. Описание проекта    
Автоматизация бизнес-процессов сервисов такси города Нью-Йорк путем создания модели машинного обучения, способной предсказывать продолжительность поездки в зависимости от различных факторов.  
Решаемая задача была представлена в качестве [Data Science-соревнования на платформе Kaggle](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview) в 2017 году с призовым фондом в $30'000.

:bookmark_tabs: [к оглавлению]()


### 2. Решаемая задача    
Последовательно пройти все этапы задачи Data Science: обработать, отобрать и подготовить для подачи на вход модели МО признаки поездок, обучить несколько моделей и сравнить их по значению метрики качества, выбрать лучшую, с ее помощью сделать предсказание и загрузить его на страницу соревнования на платформе kaggle.  

**Условия решения задачи:**  
1. Обработать входные данные: провести разведывательный анализ, отобрать признаки, нормализовать и подготовить на вход модели МО; гипотезы и выводы сопроводить иллюстрациями.  
2. Обучить несколько моделей из библиотеки sklearn: логистическая регрессия, полномиальная регрессия,случайный лес, градиентный бустинг - и сравнить их по метрике качества.  
3. Построить прогноз и загрузить его на платформу kaggle.  

**Метрика качества**     
- Для сравнения моделей используется метрика $RMSLE$ - Root Mean Squared Log Error, которая вычисляется на основе целевой переменной в логарифмическом масштабе.  
- Для контроля хода выполнения проекта требуется заносить получаемые данные в специальные поля на платформе SkillFactory, сравнивая их с эталонными значениями.  
- **Итоговый ноутбук в формате .ipynb не проверяется менторами SkillFactory, поэтому качество его оформления говорит об отношении автора к выполняемой работе.**  

**Практикуемые навыки:**     
- развыдывательный анализ;  
- построение диаграмм с помощью библиотеки seaborn, matplotlib и plotly;
- обучение моделей и оптимизация их гиперпараметров;  
- понимание и использование метрик качества моделей; 
- работа с kaggle, Git и GitHub посредством добавления отчета о проделанной работе в портфолио.

:bookmark_tabs: [к оглавлению]()


### 3. Краткая информация о данных  
Организаторами соревнования предоставлен набор данных, содержащий информацию о поездках на жёлтом такси в Нью-Йорке за 2016 год. Первоначально данные были выпущены Комиссией по Такси и Лимузинам Нью-Йорка и включают в себя информацию о времени поездки, географических координатах, количестве пассажиров и несколько других переменных.  

Кроме этого, для решения задачи использованы вспомогательные данные из других источников, такие как: национальные праздники, сведения о погоде и данные из Open Source Routing Machine (сервиса, позволяющего строить кратчайшие маршруты по координатам и оценивать примерную длительность маршрута).  

Все датасеты доступны на платформе kaggle и подключены к ноутбуку.  

Информация о признаках главного датасета с 1.5 млн поездок приведена в начале ноутбука.  
  
:bookmark_tabs: [к оглавлению]()


### 4. Этапы работы над проектом  
1. Первичная обработка данных.  
2. Разведывательный анализ данных (EDA).  
3. Отбор и преобразование признаков.  
4. Решение задачи регрессии: линейная регрессия и деревья решений.  
5. Решение задачи регрессии: ансамблевые методы и построение прогноза.  
6. Загрузка предсказания на kaggle.  

:bookmark_tabs: [к оглавлению]()


### 5. Результаты  
1. Проведена обработка данных, выполнен разведывательный анализ с использованием иллюстраций.  
2. Признаки отобраны и подготовлены к подаче на вход модели.  
3. Обучены модели машинного обучения: LinearRegression, Ridge, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, XGboost (в качестве бонуса).  
4. Модели сравнены по метрике RMSLE, результаты сведены в таблицу, сделаны выводы.  
5. Предсказание загружено на страницу соревнования на платформе kaggle.  
6. Отчет в формате Jupiter Notebook загружен на GitHub.  

:bookmark_tabs: [к оглавлению]()


### 6. Выводы  
Проект позволил примерить роль Data Scientist в сфере транспортных перевозок: провести полноценное исследование собранных данных, предсказать время поездки на такси с помощью различных современных моделей и отобрать наиболее точную по значению заданной метрики.  

Конечно, текущий результат (примерно 471 место в рейтинге соревнования) далеко лучший, однако последующее углубление знаний в области машинного обучения и их применение к этой и подобным задачам, бесспорно, позволят занимать более высокие места в подобных соревнованиях.  

В ходе реализации проекта улучшены навыки разведывательного анализа, работы с моделями МО, написан эффективный воспроизводимый код на python в соответствии с PEP-8.

:bookmark_tabs: [к оглавлению]()


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!