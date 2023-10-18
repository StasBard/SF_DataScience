# Проект 7. Дипломный. Прогнозирование стоимости жилья для агентства недвижимости.

[Go to English](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#project-7-diploma-predicting-housing-prices-for-a-real-estate-agency) :us:  

## Оглавление   
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  

### 1. Описание проекта    
Разработка и продакшен модели машинного обучения для прогнозирования стоимости объектов недвижимости, выставленных на продажу, с целью увеличения скорости реакции и качества работы риелторов в агентстве недвижимости.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача    
Произвести предобработку и разведывательный анализ набора реальных данных рынка недвижимости США, выделить наиболее значимые факторы, влияющие на стоимость недвижимости.  
Построить регрессионную модель для прогнозирования стоимости недвижимости и на ее основе разработать небольшой веб-сервис, на вход которого поступали бы данные о некоторой выставленной на продажу недвижимости, а сервис прогнозировал бы его стоимость.  

**Условия решения задачи:**  
1. Обработать входные данные: пропуски, дубликаты и выбросы, устранить ошибки ввода, расшифровать сокращения.  
2. Провести разведывательный анализ: отыскать закономерности, сгенерировать новые признаки с использованием внешних источников, проиллюстрировать наблюдения и гипотезы с помощью графиков.  
3. Отобрать признаки и подготовить данные для подачи на вход модели.   
4. Обучить несколько моделей регрессии, отобрать лучшую по метрике качества.  
5. Разработать веб-сервис для прогнозирования стоимости объекта недвижимости на основе подаваемых на вход данных.  

**Метрика качества**     
- Являясь дипломным, проект предоставляет студенту право выбора подходящей метрики качества.  
- Для решении задачи регрессии выбраны метрики: `R2`, `MAPE`, `MAE`.  
- Этапы выполнения никак не контролируются менторами или платформой SkillFactory. Ментор выставляет оценку после сдачи проекта.  

**Практикуемые навыки:**     
- предобработка данных;  
- разведывательный анализ;  
- построение диаграмм с помощью библиотеки seaborn и plotly;  
- обучение моделей регрессии;  
- использование алгоритмов оптимизации гиперпараметров RandomizedSearchCV и Optuna;  
- понимание и использование метрик качества моделей;  
- подготовка модели к продакшену и деплой на сервер;  
- работа с Git и GitHub посредством добавления отчета о проделанной работе в портфолио;  
- контейнеризация и работа с Docker и DockerHub.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
В датасете представлены 377 тысяч объектов недвижимости, выставленных на продажу. Данные скачаны из системы мультилистинга MLS США и предоставлены менторами Skillfactory.  

Данные реальные, заранее не обработанные, поэтому содержат всевозможные пропуки, дубли, ошибки ввода и проч.  
Информация о признаках датасета приведена в начале ноутбука.  
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Знакомство с данными и их предобработка.  
2. Формирование baseline-решения.  
3. Разведывательный анализ данных.  
4. Моделирование и решение задачи регрессии.  
5. Подготовка модели к продакшену и деплой.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. В ходе предобработки данных, выявлены многочисленные пропуски, дубли; намечены шаги для EDA.  
2. На основе предобработанных данных сформировано baseline-решение с использованием модели логистичекой регрессии и CatBostRegressor для последующего сравнения.  
3. Выполнен разведывательный анализ, включавший генерацию новых признаков с помощью десериализации имеющихся и привлечения внешних источников; выдвинуты гипотезы о взаимном влиянии данных; выводы проиллюстрированы диаграммами. Первые три этапа заняли до 80% всего времени работы над проектом!   
4. Решена задача регрессии с использованием моделей и алгоритмов: LinearRregression, PolynomialFeatures, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, StackingRegressor, CatBoostRegressor, RandomizedSearchCV, Optuna.  
5. На основе сравнения по метрикам качества выбрана модель GradientBoostingRegressor для продакшена.  
6. Проведена подготовка и деплой модели на сервер с его последующей контейнерезацией. Образ контейнера доступен для скачивания с DockerHub по команде `docker pull stasbard/p7_regres:latest`. Файлы модели, сервера и Dockerfile находятся в папке [web](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7/web).  
7. Воспроизводимый код с соблюдением стандарта PEP 8 и [отчет в формате Jupiter Notebook](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_7/Project_7_Diploma_Real_Estate_Price_Prediction.ipynb) загружен на GitHub.  
8. Выполненный проект [оценен ментором на 25 из 25 баллов](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_7/img/Project_7_Mentor_Review.pdf).

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
Дипломный проект позволил проверить свои силы и приобретенные за время годового курса DS-знания и навыки на реальной задаче.  

Ввиду необработанных данных удалось в полной мере испытать особености модели CRISP-DM, выполняя прогноз, а затем вновь возвращаясь на этап обработки данных с целью улучшить их и повысить качество моделирования (и так несколько раз!).  

В результате удалось существенно повысить качество моделирования и значения метрик. Так, например, значение целевой метрики `R2` составило 0.69. Дальнейшее их улучшение целиком лежит в плоскости обработки и более глубокого разведывательного анализа входных данных (соответствующие шаги намечены в выводах к проекту).

Из обученных моделей была объективно выбрана лучшая и произведен ее деплой на сервер. Образ контейнера загружен на DockerHub, так что любой желающий может запустить его на своем компьютере и протестировать работу модели, предсказывающей стоимость объекта недвижимости.  

Несмотря на простоту сервера и неидеальные показатели качества моделей, выполненный проект позлволил примерить роль Data Scientist и дает все основания на соискание начальной позиции в реальных компаниях.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Project 7. Diploma. Predicting housing prices for a real estate agency.  

[К описанию на русском](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-7-%D0%B4%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC%D0%BD%D1%8B%D0%B9-%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8-%D0%B6%D0%B8%D0%BB%D1%8C%D1%8F-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-%D0%BD%D0%B5%D0%B4%D0%B2%D0%B8%D0%B6%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8) :ru:  

## Table of Contents
[1. Project Description](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#1-project-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#3-brief-data-overview)  
[4. Project Work Stages](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#4-project-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#6-conclusions)  

### 1. Project Description    
The project involves the development and production deployment of a machine learning model to predict the prices of real estate properties listed for sale. The primary goal is to enhance the response time and the quality of work for real estate agents in the agency.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


### 2. Problem Statement   
Preprocess and conduct exploratory data analysis on a real dataset of the US real estate market, identify the most significant factors affecting property prices. Build a regression model for predicting real estate prices and use it to develop a small web service. This service would take data about a property listed for sale as input and provide a price estimate.  

**Problem Solving Conditions**  
1. Preprocess the input data: handle missing values, duplicates, and outliers, correct input errors, and expand abbreviations.  
2. Conduct exploratory data analysis: identify patterns, generate new features using external sources, and illustrate observations and hypotheses with graphs.  
3. Select features and prepare data for input to the model.  
4. Train multiple regression models and select the best one based on the quality metric.  
5. Develop a web service for predicting the price of a real estate property based on the input data.  

**Quality Metric**     
- Since this is a diploma project, students have the right to choose a suitable quality metric.  
- The selected metrics for the regression task are `R2`, `MAPE`, and `MAE`.  
- The project's completion stages are not monitored by mentors or the SkillFactory platform. Mentors assess the project after its submission.  

**Skills to Practice**     
- Data preprocessing;  
- Exploratory data analysis;  
- Creating visualizations using libraries like Seaborn and Plotly;  
- Training regression models;  
- Utilizing hyperparameter optimization algorithms like RandomizedSearchCV and Optuna;  
- Understanding and using model quality metrics;  
- Preparing the model for production and deploying it on a server;  
- Working with Git and GitHub by adding a report of the work to the portfolio;  
- Containerization and working with Docker and DockerHub.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


### 3. Brief Data Overview  
The dataset contains 377 thousand real estate listings. The data was sourced from the Multiple Listing Service (MLS) in the USA and was provided by SkillFactory mentors.  

The data is real and hasn't been preprocessed in advance. It may contain various issues such as missing values, duplicates, input errors, and more. Information about the dataset's features is provided at the beginning of the notebook.  
  
:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


### 4. Project Work Stages  
1. Data Exploration and Preprocessing.  
2. Creating a Baseline Solution.  
3. Exploratory Data Analysis.  
4. Modeling and Solving the Regression Task.  
5. Preparing the Model for Production and Deployment.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


### 5. Results  
1. During data preprocessing, numerous gaps and duplicates were identified, and steps for EDA were outlined.  
2. Based on the preprocessed data, a baseline solution was formed using logistic regression and the CatBoostRegressor model for subsequent comparison.  
3. Exploratory data analysis was performed, which included feature engineering through deserialization of existing data and the incorporation of external sources. Hypotheses about the mutual influence of data were proposed, and conclusions were illustrated with charts. The first three stages accounted for up to 80% of the total project time!
4. The regression task was solved using models and algorithms, including LinearRegression, PolynomialFeatures, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, StackingRegressor, CatBoostRegressor, RandomizedSearchCV, and Optuna.  
5. The GradientBoostingRegressor model was selected for production based on quality metrics comparison.  
6. The model was prepared and deployed on a server, followed by containerization. The container image is available for download on DockerHub using the command `docker pull stasbard/p7_regres:latest`. Model, server, and Dockerfile files can be found in the [web](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7/web) directory.  
7. The reproducible code adhering to the PEP 8 standard and the [report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_7/Project_7_Diploma_Real_Estate_Price_Prediction.ipynb) in Jupiter Notebook format have been uploaded to GitHub.  
8. The completed project was [evaluated by a mentor](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_7/img/Project_7_Mentor_Review.pdf) and received a score of 25 out of 25 points.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


### 6. Conclusions  
The diploma project allowed me to test my abilities and the knowledge and skills I acquired during the year-long data science course on a real problem.  

Due to the unprocessed nature of the data, I had the opportunity to fully experience the nuances of the CRISP-DM model. This involved making predictions and then revisiting the data preprocessing stage multiple times to enhance data quality and modeling performance.  

As a result, significant improvements were achieved in modeling quality, as evidenced by the `R2` metric reaching 0.69, for instance. Further enhancements primarily lie within the realm of data preprocessing and more in-depth exploratory data analysis, as indicated in the project's conclusions.  

From the pool of trained models, the best one was objectively selected and deployed on a server. The container image is available on DockerHub, allowing anyone interested to run it on their computer and test the functionality of the real estate price prediction model.  

Despite the server's simplicity and the models not being flawless, this project provided a firsthand experience of the Data Scientist role, and it establishes a solid foundation for pursuing entry-level positions in actual companies.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_7#table-of-contents)


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!