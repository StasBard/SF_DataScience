# Задание 1. Оптимизация гиперпараметров моделей машинного обучения.

## Оглавление   
[1. Описание задания](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над задачей](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### 1. Описание задания    
Отработка навыков оптимизации гиперпараметров моделей машинного обучения при помощи базовых и продвинутых методов, их сравнение и анализ результатов на примере задачи предсказания биологического ответа молекул по их химическому составу. 

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


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

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
Данные представлены в формате .csv.  Каждая строка представляет молекулу:   
- первый столбец 'Activity' содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1];  
- остальные столбцы 'D1-D1776' представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.  

Предварительная обработка не требуется, данные уже закодированы и нормализованы.
  
:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над заданием  
1. Обучить обе модели и предсказать результат, используя гиперпараметры по умолчанию (baseline-решение).  
2. Оптимизировать гиперпараметры обеих моделей с помощью базовых методов GridSearchCV и RandomizedSearchCV.  
3. Оптимизировать гиперпараметры обеих моделей с помощью продвинутых библиотек Hyperopt и Optuna.  
4. Сравнить полученные результаты, сделать выводы.    

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Обучены обе модели машинного обучения: LogisticRegression и RandomForestClassifier.  
2. Оптимизированы гиперпараметры моделей с помощью четырех методов, использована кросс-валидация.  
3. Написаны подробные выводы по каждому методу, сделан общий вывод на основе результатов.  
4. Отчет в формате Jupiter Notebook загружен на GitHub.  

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В процессе работы над проектом успешно реализованы обозначенные практики:
- улучшены навыки работы с моделями МО;  
- проведено знакомство на практике с базовыми и продвинутыми методами оптимизации гиперпараметров;  
- получено понимание особенностей применения каждого из методов оптимизации для последующих задач;  
- углублены навыки работы в среде Google Colab;  
- написан эффективный воспроизводимый код на python;  
- код составлен в соответствии с PEP8.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Tasks/Task_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по заданию представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!