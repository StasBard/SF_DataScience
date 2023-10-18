# Проект 4. Классификация клиентов банка.  

[Go to English]() :us:  

## Оглавление   
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### 1. Описание проекта    
Повышение результативности маркетинговой кампании банка за счет определения характеристик клиентов банка, более склонных к открытию депозита в банке, и построения модели машинного обучения, способной на основе предложенных характеристик клиента предсказывать, воспользуется он предложением об открытии депозита или нет.  
**Предложенные данные принадлежат реальному банку!**

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача    
Последовательно пройти все этапы задачи Data Science: обработать, отобрать и подготовить для подачи на вход модели МО признаки клиентов - и получить в результате модель с оптимизированными наилучшим образом гиперпараметрами, а также определить портрет целевой аудитории банка, более склонной к открытию депозита.

**Условия решения задачи:**  
1. Обработать входные данные: провести разведывательный анализ, отобрать признаки, нормализовать и подготовить на вход модели МО; гипотезы и выводы сопроводить иллюстрациями.  
2. Обучить несколько моделей из библиотеки sklearn: логистическая регрессия, случайный лес, градиентный бустинг, стекинг - и сравнить их по метрикам качества.  
3. Для оптимизации гиперпараметров использовать метод GridSearchCV и Optuna.  
4. Построить прогноз и сделать выводы.  

**Метрика качества**     
- Для сравнения моделей использовать: accuracy, precision, recall, $F_1$-score.  
- Для контроля хода выполнения проекта заносить получаемые данные в специальные поля на платформе SkillFactory, сравнивая их с эталонными значениями.  
- **Итоговый ноутбук в формате .ipynb не проверяется менторами SkillFactory, поэтому качество его оформления говорит об отношении автора к выполняемой работе.**  

**Практикуемые навыки:**     
- развыдывательный анализ;  
- построение диаграмм с помощью библиотеки seaborn, matplotlib и pandas;
- обучение моделей и оптимизация их гиперпараметров;  
- понимание и использование метрик качества моделей; 
- работа с Git, GitHub посредством добавления отчета о проделанной работе в портфолио.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
Данные реальные без предварительной обработки представлены в формате .csv и расположены в папке `data/`.  
Информация о признаках приведена в начале ноутбука.  
  
:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Первичная обработка данных.  
2. Разведывательный анализ данных (EDA).  
3. Отбор и преобразование признаков.  
4. Решение задачи классификации: логистическая регрессия и решающие деревья.  
5. Решение задачи классификации: ансамбли моделей и построение прогноза.  

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Проведена обработка данных, выполнен разведывательный анализ с использованием иллюстраций.  
2. Признаки отобраны и подготовлены к подаче на вход модели.  
3. Обучены модели машинного обучения: LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, GradientBoostingClassifier, StackingClassifier.  
4. Для оптимизации гиперпараметров использованы GridSearchCV и Optuna.  
5. Модели сравнены по метрикам, сделаны выводы.
6. [Отчет](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_4/Project-4_ML_Bank_client_classification.ipynb) в формате Jupiter Notebook загружен на GitHub.  

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В процессе работы над проектом решена настоящая задача, которая часто встает перед аналитиками банковского сектора.  
Проделанная работа по выявлению решающих факторов, обучению моделей и построению прогноза способна поднять доходы банка и содействовать пониманию целевой аудитории, которую необходимо привлекать путем рекламы и различных предложений.  

По итогам выполнения задачи улучшены навыки работы с моделями МО и алгоритмами их оптимизации, написан эффективный воспроизводимый код на python в соответствии с PEP 8.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_4#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Project 4. Classification of bank customers.    

[К описанию на русском]() :ru:  

## Table of Contents
[1. Project Description]()  
[2. Problem Statement]()  
[3. Brief Data Overview]()  
[4. Project Work Stages]()  
[5. Results]()  
[6. Conclusions]()  

### 1. Project Description    
For this project, the goal is to improve the effectiveness of a bank's marketing campaign by identifying characteristics of bank customers who are more likely to open a deposit and building a machine learning model that can predict, based on these customer characteristics, whether they will accept an offer to open a deposit or not. 
**The provided data is from a real bank!**  

:arrow_up: [Back to Table of Contents]()


### 2. Problem Statement   
The objective is to sequentially go through all the stages of a Data Science project to process, select, and prepare customer features for input into a machine learning model. The ultimate goal is to obtain a model with optimally tuned hyperparameters and to define the profile of the bank's target audience, which is more inclined to open a deposit.  

**Problem Solving Conditions**  
1. Обработать входные данные: провести разведывательный анализ, отобрать признаки, нормализовать и подготовить на вход модели МО; гипотезы и выводы сопроводить иллюстрациями.  
2. Обучить несколько моделей из библиотеки sklearn: логистическая регрессия, случайный лес, градиентный бустинг, стекинг - и сравнить их по метрикам качества.  
3. Для оптимизации гиперпараметров использовать метод GridSearchCV и Optuna.  
4. Построить прогноз и сделать выводы.  

1. Data Processing: Conduct exploratory data analysis (EDA), feature selection, normalization, and prepare data for machine learning. Support hypotheses and findings with illustrations.  
2. Train several models from the sklearn library: logistic regression, random forest, gradient boosting, and stacking. Compare them based on quality metrics.  
3. Use GridSearchCV and Optuna to optimize hyperparameters.  
4. Make predictions and draw conclusions.  

**Quality Metric**   
- To compare models, the following metrics should be used: accuracy, precision, recall, and the $F1$-score.  
- To monitor the progress of the project, keep track of the data in the designated fields on the SkillFactory platform and compare them with the reference values.  
- **Please note that the final Jupyter notebook in .ipynb format is not reviewed by SkillFactory mentors, so its quality of presentation reflects my dedication to the work.**

**Skills to Practice**  
- Exploratory data analysis;  
- Creating visualizations using libraries such as Seaborn, Matplotlib, and Pandas;  
- Model training and optimization of hyperparameters;  
- Understanding and utilizing model evaluation metrics;  
- Working with Git and GitHub by adding a report on the completed work to the portfolio.  

:arrow_up: [Back to Table of Contents]()


### 3. Brief Data Overview  
Real data, without prior processing, is provided in .csv format and located in the `data/` folder. Information about the features is provided at the beginning of the notebook.  
  
:arrow_up: [Back to Table of Contents]()


### 4. Project Work Stages  
1. Initial Data Preprocessing.  
2. Exploratory Data Analysis (EDA).  
3. Feature Selection and Transformation.  
4. Classification Problem Solving: Logistic Regression and Decision Trees.  
5. Classification Problem Solving: Model Ensembles and Making Predictions.  

:arrow_up: [Back to Table of Contents]()


### 5. Results  
1. Data processing was carried out, and exploratory data analysis was conducted using illustrations.  
2. Features have been selected and prepared for input into the model.  
3. Machine learning models have been trained: LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, GradientBoostingClassifier, StackingClassifier.  
4. GridSearchCV and Optuna were used to optimize hyperparameters.  
5. Models were compared using metrics, and conclusions were drawn.  
6. [Report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_4/Project-4_ML_Bank_client_classification.ipynb) in Jupyter Notebook format has been uploaded to GitHub.  

:arrow_up: [Back to Table of Contents]()


### 6. Conclusions  
During the project, a real problem frequently faced by analysts in the banking sector has been addressed. The work done in identifying key factors, training models, and making predictions can enhance the bank's revenue and contribute to a better understanding of the target audience, which can be effectively attracted through advertising and various offers.  

As a result of completing this task, skills in working with machine learning models and optimizing their algorithms have been improved. Additionally, efficient and reproducible Python code has been written in accordance with PEP 8.  

:arrow_up: [Back to Table of Contents]()


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!