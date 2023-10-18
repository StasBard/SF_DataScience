# Задание 1. Предсказание биологического ответа молекул.

[Go to English](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#task-1-) :us:  

## Оглавление   
[1. Описание задания](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над задачей](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### 1. Описание задания    
Отработка навыков оптимизации гиперпараметров моделей машинного обучения при помощи базовых и продвинутых методов, их сравнение и анализ результатов на примере задачи предсказания биологического ответа молекул по их химическому составу. 

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача    
Обучить две модели МО и затем выполнить подбор гиперпараметров с целью улучшения целевой метрики $F_1$-score с помощью четырех предложенных методов. Сравнить результаты и оформить решение в виде ноутбука .ipynb.

Задача основана на соревновании [Kaggle: Predicting a Biological Response (Прогнозирование биологического ответа)](https://www.kaggle.com/c/bioresponse).  

**Условия решения задачи:**  
1. Необходимо предсказать биологический ответ молекул (столбец 'Activity') по их химическому составу (столбцы D1-D1776).  
2. Модели машинного обучения для предсказания: логистическая регрессия и случайный лес из библиотеки sklearn.  
3. Методы оптимизации гиперпараметров: базовые - GridSearchCV, RandomizedSearchCV, продвинутые - Hyperopt, Optuna.  
4. Максимальное количество итераций при подборе гиперпараметров не должно превышать 50.  

**Метрика качества**     
- метрика оценки моделей машинного обучения - $F_1$-score;  
- критерии оценки выполнения задания:  

| Балл | Критерий |
|---:|---|
| 0 | Задание не выполнено |
| 1 | Обучено две модели; гипепараметры подобраны при помощи 1 метода |
| 2 | Обучено две модели; гипепараметры подобраны при помощи 2 методов |
| 3 | Обучено две модели; гипепараметры подобраны при помощи 3 методов |
| 4 | Обучено две модели; гипепараметры подобраны при помощи 4 методов |
| 5 | Обучено две модели; гипепараметры подобраны при помощи 4 методов; использована кросс-валидация |

Максимальное количество баллов за выполненное задание, таким образом - 5.  

**Практикуемые навыки:**     
- практиковать навыки работы с моделями МО;  
- освоить на практике работу с базовыми и продвинутыми методами оптимизации гиперпараметров;
- практиковать работу в среде Google Colab;  
- повторить навыки работы с Git, GitHub посредством добавления отчета о проделанной работе в портфолио.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
Данные представлены в формате .csv.  Каждая строка представляет молекулу:  
- первый столбец 'Activity' содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1];  
- остальные столбцы 'D1-D1776' представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.  

Предварительная обработка не требуется, данные уже закодированы и нормализованы.
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над заданием  
1. Обучить обе модели и предсказать результат, используя гиперпараметры по умолчанию (baseline-решение).  
2. Оптимизировать гиперпараметры обеих моделей с помощью базовых методов GridSearchCV и RandomizedSearchCV.  
3. Оптимизировать гиперпараметры обеих моделей с помощью продвинутых библиотек Hyperopt и Optuna.  
4. Сравнить полученные результаты, сделать выводы.    

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Обучены обе модели машинного обучения: LogisticRegression и RandomForestClassifier.  
2. Оптимизированы гиперпараметры моделей с помощью четырех методов, использована кросс-валидация.  
3. Написаны подробные выводы по каждому методу, сделан общий вывод на основе результатов.  
4. [Отчет](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/ML_7_Task_Predicting_a_Biological_Response.ipynb) в формате Jupiter Notebook загружен на GitHub.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В процессе работы над заданием успешно реализованы обозначенные практики:
- улучшены навыки работы с моделями МО;  
- проведено знакомство на практике с базовыми и продвинутыми методами оптимизации гиперпараметров;  
- получено понимание особенностей применения каждого из методов оптимизации для последующих задач;  
- углублены навыки работы в среде Google Colab;  
- написан эффективный воспроизводимый код на python;  
- код составлен в соответствии с PEP 8.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по заданию представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Task 1. Predicting the biological response of molecules.  

[К описанию на русском](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-1-%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B1%D0%B8%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-%D0%BC%D0%BE%D0%BB%D0%B5%D0%BA%D1%83%D0%BB) :ru:  

## Table of Contents
[1. Task Description](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#1-task-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#3-brief-data-overview)  
[4. Task Work Stages](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#4-task-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#6-conclusions)  

### 1. Task Description    
The task focuses on refining skills in hyperparameter optimization for machine learning models using both fundamental and advanced methods. It entails comparing these methods and analyzing their outcomes within the context of predicting a biological response of molecules based on their chemical composition.  

The task is based on the [Kaggle competition titled "Predicting a Biological Response"](https://www.kaggle.com/c/bioresponse).  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


### 2. Problem Statement   
Train two machine learning models and then perform hyperparameter tuning to improve the target metric, $F_1$-score, using four suggested methods. Compare the results and present the solution in the form of a Jupyter Notebook (.ipynb).  

**Problem Solving Conditions**  
1. The task involves predicting the biological response of molecules (the 'Activity' column) based on their chemical composition (columns D1-D1776).  
2. Machine learning models for prediction: logistic regression and random forest from the sklearn library.  
3. Hyperparameter optimization methods: basic methods like GridSearchCV and RandomizedSearchCV, and advanced methods like Hyperopt and Optuna.  
4. The maximum number of iterations for hyperparameter tuning should not exceed 50.  

**Quality Metric**     
- The evaluation metric for machine learning models is the $F_1$-score;   
- Criteria for evaluating the completion of the task:  

| Score | Criterion |
|---:|---|
| 0 | Task not completed |
| 1 | Two models trained; hyperparameters tuned using 1 method |
| 2 | Two models trained; hyperparameters tuned using 2 methods |
| 3 | Two models trained; hyperparameters tuned using 3 methods |
| 4 | Two models trained; hyperparameters tuned using 4 methods |
| 5 | Two models trained; hyperparameters tuned using 4 methods; cross-validation used |

The maximum score for this task is 5.  

**Skills to Practice**     
- Practice machine learning model skills;  
- Gain practical experience in working with basic and advanced hyperparameter optimization methods;  
- Learn how to work with Google Colab;  
- Refresh your skills in using Git and GitHub by adding a report on your completed work to your portfolio.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


### 3. Brief Data Overview  
The data is provided in a .csv format. Each row represents a molecule:  
- The first column 'Activity' contains experimental data describing the actual biological response [0, 1];  
- The other columns 'D1-D1776' are molecular descriptors - computed properties that can capture various characteristics of the molecule, such as size, shape, or the composition of elements.  

No preprocessing is required, as the data is already encoded and normalized.  
  
:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


### 4. Task Work Stages  
1. Train both models and make predictions using default hyperparameters (baseline solution).  
2. Optimize the hyperparameters of both models using basic methods like GridSearchCV and RandomizedSearchCV.  
3. Optimize the hyperparameters of both models using advanced libraries like Hyperopt and Optuna.  
4. Compare the results obtained from these different optimization methods and draw conclusions.  

Please let me know if you need guidance or have specific questions about any of these tasks.

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


### 5. Results  
1. Both machine learning models, LogisticRegression and RandomForestClassifier, have been trained.  
2. The models' hyperparameters have been optimized using four methods, and cross-validation was applied.  
3. Detailed conclusions have been written for each method, and a general conclusion has been made based on the results.  
4. The [report](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/ML_7_Task_Predicting_a_Biological_Response.ipynb) in Jupiter Notebook format has been uploaded to GitHub.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


### 6. Conclusions  
The task has successfully implemented the following practices:  
- Improved skills in working with machine learning models;  
- Practical familiarity with basic and advanced hyperparameter optimization methods;  
- Gained understanding of the specifics of applying each optimization method for future tasks;  
- Enhanced skills in working with the Google Colab environment;  
- Developed efficient and reproducible Python code;  
- Maintained code compliance with PEP 8.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Tasks/Task_1/README.md#table-of-contents)


If you find the task information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!