# Проект 6. Сегментация клиентов онлайн-магазина подарков.  

[Go to English]() :us:  

## Оглавление   
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  

### 1. Описание проекта    
Сегментация клиентов на основе их покупательской способности, частоты совершения заказов и срока давности последнего заказа. В качестве дополнения - построение модели, определяющей сегмент клиента.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача    
Последовательно пройти все этапы DS-задачи обучения без учителя: обработать, отобрать и подготовить для подачи на вход алгоритма кластеризации данные о клиентах онлайн-магазина; сегментировать клиентов в парадигме RFM (Recency, Frequency, Monetary value) и после получения размеченных данных решить дополнительную задачу классификации.

**Условия решения задачи:**  
1. Обработать входные данные: провести разведывательный анализ, отобрать признаки и перевести их в плоскость RFM-анализа; проиллюстрировать наблюдения и гипотезы с помощью графиков.  
2. Понизить размерность получившихся данных с помощью двух различных алгоритмов (PCA и t-SNE), сравнить их эффективность.  
3. Провести кластеризацию клиентов с помощью нескольких алгоритмов и сравнить их эффективность по метрике качества.  
4. Проверить качество кластеризации с помощью решения задачи классификации на размеченных данных.    

**Метрика качества**     
- Для сравнения алгоритмов кластеризации используется значение коэффициента силуэта.  
- При решении дополнительной задачи классификации используется метрика accuracy.  
- Контроль хода выполнения проекта выполняется путем внесения получаемых данных в специальные поля на платформе SkillFactory для сравнения их с эталонными значениями.  
- **Итоговый ноутбук в формате .ipynb не проверяется менторами SkillFactory, поэтому качество его оформления говорит об отношении автора к выполняемой работе.**  

**Практикуемые навыки:**     
- разведывательный анализ;  
- построение диаграмм с помощью библиотеки seaborn и plotly;  
- использование алгоритмов понижения размерности из библиотеки sklearn;  
- использование алгоритмов кластеризации из библиотеки sklearn;  
- использованием метода pipeline;  
- обучение моделей классификациии и оптимизация их гиперпараметров;  
- понимание и использование метрик качества моделей;  
- работа с Git и GitHub посредством добавления отчета о проделанной работе в портфолио.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
В датасете представлены более полумиллиона транзакций некоего онлайн-магазина подарков в Великобритании за годовой период с декабря 2010 по декабрь 2011 года.  
Информация о признаках главного датасета приведена в начале ноутбука.  
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Первичная обработка данных.  
2. Разведывательный анализ данных.  
3. Отбор и создание RFM-признаков.  
4. Понижение размерности с помощью PCA и t-SNE.  
5. Решение задачи кластеризации алгоритмами k-means, EM, AgglomerativeClustering.  
6. Решение дополнительной задачи классификации с помощью RandomForestClassifier и GradientBoostingClassifier.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Проведена обработка данных, выполнен разведывательный анализ с использованием диаграмм.  
2. Рассчитаны RFM-характеристики клиентов.  
3. Выполнено снижение размерности двумя алгоритмами, оценена эффективность каждого.  
4. Проведена кластеризация с помощью нескольких методов и отобран лучший по метрике коэффициента силуэта.  
5. Решена дополнительная задача классификации с помощью моделей RandomForestClassifier и GradientBoostingClassifier.  
6. [Отчет](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/Project_6_ML_Online_customer_segmentation.ipynb) в формате Jupiter Notebook загружен на GitHub.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В рамках проекта удалось решить настояющую бизнес-задачу из области маркетинга. Выявленные сегменты клиентов в реальности позволят определить оптимальную стратегию взаимодействия с ними.  

Удалось наглядно убедиться в пользе и эффективности алгоритмов снижения размерности данных.  

Полученные сегментированные (размеченные данные) позволили дополнительно реализовать задачу обучения с учителем как с целью проверки качества кластеризации, так и с целью предсказания сегмента для новых клиентов.  

Улучшены навыки разведывательного анализа, работы с моделями МО, написан эффективный воспроизводимый код на python в соответствии с PEP 8.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Project 6. Customer segmentation for an online gift store.  

[К описанию на русском]() :ru:  

## Table of Contents
[1. Project Description]()  
[2. Problem Statement]()  
[3. Brief Data Overview]()  
[4. Project Work Stages]()  
[5. Results]()  
[6. Conclusions]()  

### 1. Project Description    
Customer segmentation based on their purchasing ability, order frequency, and the time since their last order. Additionally, building a model to determine a customer's segment.  

:arrow_up: [Back to Table of Contents]()


### 2. Problem Statement   
Sequentially go through all the stages of the unsupervised learning Data Science task: process, select, and prepare customer data for input into a clustering algorithm; segment customers in the RFM paradigm (Recency, Frequency, Monetary value), and after obtaining labeled data, solve an additional classification task.  

**Problem Solving Conditions**  
1. Process the input data: perform exploratory data analysis, select features, and transform them into the RFM analysis framework; illustrate observations and hypotheses using graphs.  
2. Reduce the dimensionality of the resulting data using two different algorithms (PCA and t-SNE), and compare their effectiveness.  
3. Cluster customers using several algorithms and compare their effectiveness based on a quality metric.  
4. Assess the quality of clustering by solving a classification task on labeled data.  

**Quality Metric**     
- The silhouette coefficient is used to compare clustering algorithms.  
- For the additional classification task, accuracy is used as the metric.  
- Project progress is monitored by entering the obtained data into special fields on the SkillFactory platform for comparison with benchmark values.  
- **The final notebook in .ipynb format is not reviewed by SkillFactory mentors, so its quality of presentation reflects the author's commitment to the work.**  

**Skills to Practice**     
- Exploratory data analysis;  
- Building diagrams using the Seaborn and Plotly libraries;  
- Using dimensionality reduction algorithms from the sklearn library;  
- Using clustering algorithms from the sklearn library;  
- Utilizing the pipeline method;  
- Training classification models and optimizing their hyperparameters;  
- Understanding and using metrics for model quality;  
- Working with Git and GitHub by adding a report on the completed work to the portfolio.  

:arrow_up: [Back to Table of Contents]()


### 3. Brief Data Overview  
In the dataset, there are more than half a million transactions from an online gift shop in the United Kingdom over a yearly period from December 2010 to December 2011. Information about the features of the main dataset is provided at the beginning of the notebook.  
  
:arrow_up: [Back to Table of Contents]()


### 4. Project Work Stages  
1. Initial data processing.  
2. Exploratory data analysis.  
3. Feature selection and creating RFM features.  
4. Dimensionality reduction using PCA and t-SNE.  
5. Solving the clustering task using k-means, EM, and AgglomerativeClustering algorithms.  
6. Solving the additional classification task using RandomForestClassifier and GradientBoostingClassifier.  

:arrow_up: [Back to Table of Contents]()


### 5. Results  
1. Data processing was conducted, along with exploratory data analysis using visualizations.  
2. RFM characteristics of customers were calculated.  
3. Dimensionality reduction was performed using two algorithms, and their effectiveness was assessed.  
4. Clustering was executed with multiple methods, and the best one was selected based on the silhouette score.  
5. An additional classification task was solved using RandomForestClassifier and GradientBoostingClassifier models.  
6. The [report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_6/Project_6_ML_Online_customer_segmentation.ipynb) in the Jupyter Notebook format has been uploaded to GitHub.  

:arrow_up: [Back to Table of Contents]()


### 6. Conclusions  
Within this project, a genuine business problem in the field of marketing was successfully addressed. The identified customer segments in reality will allow determining the optimal strategy of interaction with them.  

The benefits and effectiveness of dimensionality reduction algorithms were visually evident.  

The segmented and labeled data obtained allowed for the additional achievement of supervised learning tasks, both for assessing clustering quality and predicting segments for new customers.  

Skills in exploratory data analysis, working with machine learning models, and writing efficient, reproducible Python code following PEP 8 standards have been improved.  

:arrow_up: [Back to Table of Contents]()


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!