# Проект 5. Предсказание продолжительности поездки на такси в Нью-Йорке.  

[Go to English](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#project-5-predicting-nyc-taxi-trip-duration) :us:  

## Оглавление   
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### 1. Описание проекта    
Автоматизация бизнес-процессов сервисов такси города Нью-Йорк путем создания модели машинного обучения, способной предсказывать продолжительность поездки в зависимости от различных факторов.  
Решаемая задача была представлена в качестве [Data Science-соревнования на платформе Kaggle](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview) в 2017 году с призовым фондом в $30'000.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


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
- разведывательный анализ;  
- построение диаграмм с помощью библиотеки seaborn, matplotlib и plotly;
- обучение моделей и оптимизация их гиперпараметров;  
- понимание и использование метрик качества моделей; 
- работа с kaggle, Git и GitHub посредством добавления отчета о проделанной работе в портфолио.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
Организаторами соревнования предоставлен набор данных, содержащий информацию о поездках на жёлтом такси в Нью-Йорке за 2016 год. Первоначально данные были выпущены Комиссией по Такси и Лимузинам Нью-Йорка и включают в себя информацию о времени поездки, географических координатах, количестве пассажиров и несколько других переменных.  

Кроме этого, для решения задачи использованы вспомогательные данные из других источников, такие как: национальные праздники, сведения о погоде и данные из Open Source Routing Machine (сервиса, позволяющего строить кратчайшие маршруты по координатам и оценивать примерную длительность маршрута).  

Все датасеты доступны на платформе kaggle и подключены к ноутбуку.  

Информация о признаках главного датасета с 1.5 млн поездок приведена в начале ноутбука.  
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Первичная обработка данных.  
2. Разведывательный анализ данных (EDA).  
3. Отбор и преобразование признаков.  
4. Решение задачи регрессии: линейная регрессия и деревья решений.  
5. Решение задачи регрессии: ансамблевые методы и построение прогноза.  
6. Загрузка предсказания на kaggle.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Проведена обработка данных, выполнен разведывательный анализ с использованием иллюстраций.  
2. Признаки отобраны и подготовлены к подаче на вход модели.  
3. Обучены модели машинного обучения: LinearRegression, Ridge, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, XGboost (в качестве бонуса).  
4. Модели сравнены по метрике RMSLE, результаты сведены в таблицу, сделаны выводы.  
5. Предсказание загружено на страницу соревнования на платформе kaggle.  
6. [Отчет](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/Project-5_ML_NYC_taxi_trip_duration_regression_task.ipynb) в формате Jupiter Notebook загружен на GitHub.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
Проект позволил примерить роль Data Scientist в сфере транспортных перевозок: провести полноценное исследование собранных данных, предсказать время поездки на такси с помощью различных современных моделей и отобрать наиболее точную по значению заданной метрики.  

Конечно, текущий результат (примерно 471 место в рейтинге соревнования) далеко лучший, однако последующее углубление знаний в области машинного обучения вкупе с более эвристическими приемами предварительной обработки и разведывательного анализа имеющихся данных, бесспорно, позволят улучшать положение в рейтинге подобных соревнований.  

В ходе реализации проекта улучшены навыки разведывательного анализа, работы с моделями МО, написан эффективный воспроизводимый код на python в соответствии с PEP 8.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_5#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Project 5. Predicting NYC taxi trip duration.  

[К описанию на русском](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-5-%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B4%D0%BE%D0%BB%D0%B6%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4%D0%BA%D0%B8-%D0%BD%D0%B0-%D1%82%D0%B0%D0%BA%D1%81%D0%B8-%D0%B2-%D0%BD%D1%8C%D1%8E-%D0%B9%D0%BE%D1%80%D0%BA%D0%B5) :ru:  

## Table of Contents
[1. Project Description](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#1-project-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#3-brief-data-overview)  
[4. Project Work Stages](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#4-project-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#6-conclusions)  

### 1. Project Description    
Automation of business processes for taxi services in the city of New York through the creation of a machine learning model capable of predicting trip duration based on various factors.  

The problem addressed was presented as a [Data Science competition on the Kaggle platform](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview) in 2017 with a prize pool of $30,000.

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


### 2. Problem Statement   
Sequentially go through all stages of the Data Science task: process, select, and prepare the trip features for input into the ML-model, train multiple models and compare them based on the quality metric, choose the best one, use it to make predictions, and upload them to the competition page on the Kaggle platform.  

**Problem Solving Conditions**  
1. Process the input data: perform exploratory data analysis, select features, normalize, and prepare them for the ML-model; support hypotheses and conclusions with illustrations.  
2. Train several models from the sklearn library, including logistic regression, polynomial regression, random forest, and gradient boosting; compare their performance based on a quality metric.  
3. Make predictions using the chosen best model and upload them to the Kaggle competition platform.  

**Quality Metric**     
- For model comparison, the $RMSLE$ (Root Mean Squared Log Error) metric is used, which is calculated based on the target variable in logarithmic scale.  
- To monitor the progress of the project, it is required to enter the obtained data into special fields on the SkillFactory platform and compare them with reference values.  
- **The final Jupyter Notebook in .ipynb format is not reviewed by SkillFactory mentors, so its quality of presentation reflects the author's attitude toward the work.**  

**Skills to Practice**     
- Exploratory analysis;  
- Construction of diagrams using the seaborn, matplotlib, and plotly libraries;  
- Model training and optimization of hyperparameters;  
- Understanding and use of model quality metrics;  
- Working with Kaggle, Git, and GitHub by adding a report of the work done to the portfolio.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


### 3. Brief Data Overview  
The competition organizers provided a dataset containing information about yellow taxi trips in New York City in 2016. Initially, the data was released by the New York City Taxi and Limousine Commission and includes information about trip times, geographical coordinates, the number of passengers, and several other variables.  

In addition, to solve the problem, auxiliary data from other sources were used, such as national holidays, weather information, and data from the Open Source Routing Machine (a service that allows for routing between coordinates and estimates route duration).  

All datasets are available on the Kaggle platform and are connected to the notebook.  

Information about the features of the main dataset with 1.5 million trips is provided at the beginning of the notebook.  
  
:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


### 4. Project Work Stages  
1. Initial Data Processing.  
2. Exploratory Data Analysis (EDA).  
3. Feature Selection and Transformation.  
4. Regression Problem Solving: Linear Regression and Decision Trees.  
5. Regression Problem Solving: Ensemble Methods and Forecasting.  
6. Uploading Predictions to Kaggle.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


### 5. Results  
1. Data processing was carried out, and exploratory data analysis was conducted with the use of illustrations.  
2. Features were selected and prepared for input to the model.  
3. Machine learning models were trained: LinearRegression, Ridge, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, XGBoost (as a bonus).  
4. Models were compared using the $RMSLE$ metric, and the results were compiled into a table with conclusions.  
5. Predictions were uploaded to the competition page on the Kaggle platform.  
6. The [report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/Project-5_ML_NYC_taxi_trip_duration_regression_task.ipynb) in Jupyter Notebook format was uploaded to GitHub.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


### 6. Conclusions  
The project allowed me to step into the role of a Data Scientist in the field of transportation: to conduct a comprehensive study of the collected data, predict taxi trip times using various modern models, and select the most accurate model based on the specified metric.  

Certainly, the current result (roughly 471st place in the competition ranking) is far from the best. However, further deepening of knowledge in the field of machine learning, coupled with more heuristic approaches to data preprocessing and exploratory data analysis, will undoubtedly allow for improving rankings in similar competitions.  

Throughout the project's implementation, I improved my skills in exploratory data analysis, working with machine learning models, and writing efficient, reproducible Python code following PEP 8 guidelines.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_5/README.md#table-of-contents)


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!