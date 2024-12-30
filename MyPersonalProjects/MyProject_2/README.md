# Проект 2. Анализ базы данных Ателье Пиньон.

[Go to English](https://github.com/StasBard/SF_DataScience/blob/master/MyPersonalProjects/MyProject_2/README.md#project-2-analyze-atelier-pignons-database) :us:  
[Aller au Français](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#projet-2--analyse-de-la-base-de-donn%C3%A9es-de-latelier-du-pignon) :fr:  

## Оглавление  
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  

### 1. Описание проекта    
Ассоциация по ремонту велосипедов города Нанта Atelier du Pignon, предоставляющая помощь, инструменты и запасные части для самостоятельного ремонта и обслуживания велосипедов в обмен на годовой членский взнос, желает проанализировать состав участников ателье. **Проект выполняется на добровольной и безвозмездной основе**.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача   
Определить взаимосвязь данных об участниках, которые они согласились указать о себе (коммуна проживания, пол, возраст, статус добровольца), и размера их членского взноса. С этой целью проанализировать базы данных за 2023-2024 и 2024-2025 годы, проиллюстрировать гипотезы и выводы о составе участников ателье, ответить на поставленные руководством Ателье вопросы.  
Автор работы в финальной части проекта по собственному желанию поставил себе Data Science-задачу по определению пола участников, которые его по какой-либо причине не указали.  

**Условия решения задачи:**  
1. Произвести предобработку и разведывательный анализ набора данных Ателье.  
2. Ответить на вопросы о зависимости суммы ежегодного взноса от других факторов.  
3. Сравнить динамику регистраций участников за аналогичный период 2023-2024 и 2024-2025 годов. 
4. Проиллюстрировать гипотезы и выводы на графиках, а также карте города.  
5. Построить несколько моделей машинного обучения, выполнить прогноз пола участников Ателье и отобрать лучшую модель по целевой метрике.  
6. Подготовить pdf-отчет с результатами анализа и предсказания.  

**Метрика качества**  
Для сравнения качества предсказания моделей будем использовать две метрики: `precision` и `recall`.  

**Практикуемые навыки**  
- трансформация бизнес-запроса в техническую DS-задачу и обратная коммуникация полученных результатов;  
- предобработка и разведывательный анализ данных;  
- использование библиотеки Matplotlib для демонстрации результатов исследования;  
- использование интерактивных Choropleth-карт библиотеки Plotly для представления данных на карте города;  
- знакомство и использование OpenStreetMap и открытых баз данных администрации города.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
База данных участников Ателье насчитывает 979 записей, собранных в ходе подтверждения членства и внесения годового взноса в течение периода с августа 2023 по июль 2024 года включительно. Данные об участниках собирались посредством заполнения бумажных анкет участниками и их последующей оцифровкой, в результате чего база содержит некоторое число ошибок, неточностей и пропусков.  

Кроме этого, с целью отслеживания динамики сообщества, была также проанализирована формируемая база данных (326 участников) сезона 2024-2025 годов по состоянию на конец ноября (период подписки - с августа по ноябрь 2024 года включительно).
  
Для выполнения проекта базы передается автору в обезличенном виде: столбцы с именами и адресами email удалены, а оставлен лишь  столбец ID для последующего сопоставления (при необходимости).  

Кроме столбца ID база содержит следующие признаки:  
- Date de naissance - дата рождения участника,  
- Genre (F/H/X) - пол участника,  
- CP - почтовый индекс места проживания,  
- Bénévoles - статус добровольца,  
- Montant de l’adhésion - внесенная сумма членского взноса.  

С целью наглядной иллюстрации выводов на картах OpenStreetMaps в проект добавлены открытые базы данных администрации города Нант с названиями, почтовыми индексами и GPS-координатами границ коммун. Базы данных сохранены в папке "data/".  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Обсуждение целей проекта и вопросов, интересующих руководителей Ателье, постановка задач.  
2. Очистка данных, раздведывательный анализ.  
3. Анализ данных, выдвижение гипотез, иллюстрация выводов с помощью графиков.  
4. Подключение открытых баз данных и иллюстрация результатов анализа на интерактивных графиках Plotly с помощью OpenStreepMaps.  
5. Решение задачи классификации несколькими моделями и выбор наилучней по сравнению метрик; формирование прогноза.  
6. Сведение результатов проекта в pdf-отчет и презентация руководству Ателье.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. После предобработки, очистки базы данных и генерации новых признаков, сформулированы выводы о взаимозависимости возраста, пола, места проживания участника Ателье, суммы членского взноса и готовности выступать в роли добровольца при помощи другим участникам.  
2. Проведено сравнение динамики регистрации с августа по ноябрь 2024 с аналогичным периодом 2023 года.  
3. Улучшены навыки работы с библиотекой Matplotlib, отработаны ранее не использовавшиеся методы.  
4. Проведено ознакомление с ресурсом OpenStreetMap и осуществлена его интеграция в проект через библиотеку Plotly для наглядного отображения выводов исследования.  
5. Дополнительно решена DS-задача по предсказанию пола участников, которые указали его в анкете как 'X' или не указали вовсе. Такая задача руководством Ателье не ставилась. С уважением права людей не указывать свой пол (тем более, что база обезличена), автор позволил себе вывести проект за рамки компетенций Data Analyst и решить задачу классификации.  
6. Из 3-х рассмотренных алгоритмов: Logistic Regression, Decision Tree Classifier и Random Forest Classifier с применением GridSearch CV - наилучших показателей целевых метрик удалось достичь с помощью Decision Tree Classifier. `precision` составила 75%, а `recall` - 99%, что позволило сделать вывод, то примерно 75% участников, не указавших свой пол, это - мужчины, а 25% - женщины.  
7. Результаты исследования оформлены в [pdf-презентацию](), и исполняемый код доступен в авторском репозитории GitHub в формате [Jupiter Notebook](https://github.com/StasBard/SF_DataScience/blob/master/MyPersonalProjects/MyProject_2/Pignon.ipynb).

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
Мы проанализировали базу данных Atelier du Pignon за 2023-2024 годы и, несмотря на сравнительно небольшое количество записей (979) и скудный набор признаков сумели составить общую картину по всем участникам, а также сформулировать и проиллюстрировать определенные закономерности, ответить на поставленные вопросы.   
1. Мы определили вклад каждой из коммун Нанта по числу участников, добровольцев и собранных взносов.  
2. Продемонстрировали зависимость размера взноса от пола участника и его статуса добровольца, а также месяца рождения. 
3. Мы также проанализировали формирующуюся базу данных текущего года (2024-2025) по состоянию на конец ноября с 326 записавшимися участниками и показали динамику в сравнении с предыдущим годом.  
4. Проиллюстрировали выводы не только с помощью графиков, но и на интерактивной карте города, обеспечив наглядность.  
5. Определили пол тех участников, которые его по какой-то причине не указали.  

В дальнейшем было бы интересно проследить эволюцию состава участников, как мы это описали в 3-м пункте, выполняя анализ данных на ежегодной основе. Так или иначе, данный анализ, выполненный автором (одним из участников Ателье) **на добровольной основе**, уже позволил лучше понять аудиторию Ателье. 

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!

---

# Project 2: Analyze Atelier Pignon's database.

[Aller au Français](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#projet-2--analyse-de-la-base-de-donn%C3%A9es-de-latelier-du-pignon) :fr:  
[К описанию на русском](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-2-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%B5-%D0%BF%D0%B8%D0%BD%D1%8C%D0%BE%D0%BD) :ru:  

## Table of Contents
[1. Project Description](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#1-project-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#3-brief-data-overview)  
[4. Project Work Stages](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#4-project-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#6-conclusions)  

### 1. Project Description    
The Atelier du Pignon, the bicycle repair association of the city of Nantes, which provides assistance, tools and spare parts for self-repair and maintenance of bicycles in exchange for an annual membership fee, wishes to analyze the composition of atelier members. **The project is carried out on a voluntary and pro bono basis**.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


### 2. Problem Statement   
To determine the relationship between the participants' data they agreed to provide about themselves (community of residence, gender, age, volunteer status) and the amount of their membership fee. To this end, analyze the databases for the years 2023-2024 and 2024-2025, illustrate hypotheses and conclusions about the composition of the Atelier participants, answer the questions posed by the Atelier management.  
The author of the work in the final part of the project, by his own volition, set himself a Data Science task to determine the gender of the participants who did not specify it for any reason.  

**Problem Solving Conditions**  
1. Perform pre-processing and exploratory analysis of the Atelier dataset.  
2. Answer questions about the relationship between the amount of annual contribution and other factors.  
3. Compare the dynamics of participant registrations for the same period in 2023-2024 and 2024-2025.  
4. Illustrate hypotheses and conclusions on charts as well as a map of the city.  
5. Build several machine learning models, perform gender prediction of Atelier participants, and select the best model based on the target metric.  
6. Prepare a pdf report with the results of the analysis and prediction.  

**Quality Metric**     
To compare the prediction quality of the models, we will use two metrics: `precision` and `recall`.  

**Skills to Practice**     
- transforming a business request into a technical DS task and communicating back the results;  
- pre-processing and exploratory data analysis;  
- using the Matplotlib library to demonstrate the results of the research;  
- using Plotly library's interactive Choropleth-maps to present data on a city map;  
- familiarization and use of OpenStreetMap and open databases of the city administration.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


### 3. Brief Data Overview  
Atelier's membership database has 979 records collected during membership confirmation and annual fee payment during the period August 2023 through July 2024, inclusive. Member data was collected by having participants fill out paper questionnaires and then digitizing them, as a result of which the database contains some errors, inaccuracies and omissions.  
  
In addition, in order to track community dynamics, the emerging database (326 participants) of the 2024-2025 season was also analyzed as of the end of November (subscription period is from August to November 2024 inclusive).  
  
For the purpose of the project, the databases are passed to the author in an anonymized form: columns with names and email addresses were removed, and only the ID column was left for further comparison (if necessary).  

In addition to the ID column, the database contains the following attributes:  
- Date de naissance - date of birth of the participant,  
- Genre (F/H/X) - participant's gender,  
- CP - postal code of the place of residence,  
- Bénévoles - volunteer status,  
- Montant de l'adhésion - amount of membership fee paid.  

In order to visualize the findings on OpenStreetMaps, open databases of Nantes city administration with names, postal codes and GPS coordinates of commune boundaries were added to the project. The databases are saved in the folder “data/”.  
  
:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


### 4. Project Work Stages  
1. Discussing project goals and issues of interest to Atelier managers, setting objectives.  
2. Data cleaning, exploratory analysis.  
3. Analyzing data, hypothesizing, illustrating conclusions with graphs.  
4. Connecting open databases and illustrating analysis results on interactive Plotly charts using OpenStreepMaps.  
5. Solving a classification problem with several models and selecting the best metric to compare; generating a prediction.  
6. Summarizing the results of the project into a pdf-report and presentation to the Atelier management.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


### 5. Results  
1. After preprocessing, database cleaning and generation of new features, conclusions about the interdependence of Atelier participant's age, gender, place of residence, amount of membership fee and willingness to volunteer to help other participants were formulated.  
2. Comparison of registration dynamics from August through November 2024 with the same period in 2023 was made.  
3. Improved skills in working with Matplotlib library, practiced previously unused methods.  
4. Familiarized with the OpenStreetMap resource and integrated it into the project through the Plotly library to visualize the findings of the study.  
5. Additionally, the DS-task of predicting the gender of participants who indicated it in the questionnaire as 'X' or did not indicate it at all was solved. Such a task was not set by the Atelier management. Respecting the right of people not to specify their gender (especially since the database is anonymized), the author took the liberty of taking the project beyond the competence of Data Analyst and solving the classification task.  
6. Of the 3 algorithms considered: Logistic Regression, Decision Tree Classifier and Random Forest Classifier using GridSearch CV - the best performance of the target metrics was achieved with Decision Tree Classifier. The `precision' was 75% and `recall' was 99%, which led to the conclusion that approximately 75% of the participants who did not specify their gender were male and 25% were female.  
7. The results of the study are organized in a [pdf presentation]() and the executable code is available in the author's GitHub repository in [Jupiter Notebook](https://github.com/StasBard/SF_DataScience/blob/master/MyPersonalProjects/MyProject_2/Pignon.ipynb) format.

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


### 6. Conclusions  
We analyzed the Atelier du Pignon database and, despite the relatively small number of records (979) and the scarce set of attributes managed to draw a general picture for all participants, as well as to formulate and illustrate certain patterns and answer the questions posed.   
1. We determined the contribution of each of the communes of Nantes by the number of participants, volunteers and contributions collected.  
2. Demonstrated the dependence of the size of the contribution on the participant's gender and volunteer status, as well as the month of birth. 
3. We also analyzed the current year's forming database (2024-2025) as of the end of November with 326 enrolled participants and showed trends compared to the previous year.  
4. Illustrated the findings not only with charts, but also on an interactive map of the city.  
5. identified the gender of those participants who did not indicate it for some reason.  

In the future, it would be interesting to trace the evolution of the composition of the participants as we described in paragraph 3 by analyzing the data on an annual basis. Anyway, this analysis, performed by the author (one of the Atelier participants) **on a voluntary basis**, has already provided a better understanding of the Atelier's audience. 

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-of-contents)


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!

---

# Projet 2 : Analyse de la base de données de l'Atelier du Pignon.

[Go to English](https://github.com/StasBard/SF_DataScience/blob/master/MyPersonalProjects/MyProject_2/README.md#project-2-analyze-atelier-pignons-database) :us:  
[К описанию на русском](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-2-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%B5-%D0%BF%D0%B8%D0%BD%D1%8C%D0%BE%D0%BD) :ru:  

## Table des matières  
[1. Description du projet](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#1-description-du-projet)  
[2. Problème à résoudre](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#2-probl%C3%A8me-%C3%A0-r%C3%A9soudre)  
[3. Informations succinctes sur les données](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#3-informations-succinctes-sur-les-donn%C3%A9es)  
[4. Étapes du projet](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#4-%C3%A9tapes-du-projet)  
[5. Résultats](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#5-r%C3%A9sultats)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#6-conclusions-1)  

### 1. Description du projet  
L’association de réparation de vélos de Nantes, Atelier du Pignon, qui offre assistance, outils et pièces détachées pour l’entretien et la réparation autonome de vélos en échange d’une cotisation annuelle, souhaite analyser la composition de ses membres. **Ce projet est réalisé sur une base volontaire et bénévole.**  

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


### 2. Problème à résoudre  
Déterminer la relation entre les données fournies par les membres qui ont accepté de les indiquer (commune de résidence, genre, âge, statut de bénévole) et le montant de leur cotisation. À cette fin, analyser les bases de données des saisons 2023-2024 et 2024-2025, illustrer les hypothèses et conclusions sur la composition des membres et répondre aux questions posées par la direction de l’Atelier.  
L’auteur du projet, par initiative personnelle, a également décidé d’aborder une problématique de Data Science pour déterminer le genre des membres qui n’ont pas renseigné cette information.  

**Conditions pour résoudre le problème :**  
1. Réaliser un prétraitement et une analyse exploratoire des données.  
2. Répondre aux questions sur la dépendance entre le montant de la cotisation annuelle et d’autres facteurs.  
3. Comparer la dynamique des inscriptions des membres entre les périodes 2023-2024 et 2024-2025.  
4. Illustrer les hypothèses et conclusions par des graphiques ainsi qu’une carte de la ville.  
5. Construire plusieurs modèles de machine learning, prédire le genre des membres et sélectionner le meilleur modèle selon une métrique cible.  
6. Préparer un rapport PDF avec les résultats de l’analyse et des prédictions.  

**Métrique de qualité**  
Pour évaluer la qualité des prédictions des modèles, deux métriques seront utilisées : `precision` et `recall`.  

**Compétences mises en pratique**  
- Traduction d’une demande métier en une problématique technique de Data Science et communication des résultats ;  
- Prétraitement et analyse exploratoire des données ;  
- Utilisation de la bibliothèque Matplotlib pour illustrer les résultats ;  
- Cartographie interactive via Plotly et OpenStreetMap pour représenter les données sur une carte ;  
- Familiarisation avec les bases de données ouvertes de l’administration municipale.  

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


### 3. Informations succinctes sur les données  
La base de données des membres de l’Atelier compte 979 enregistrements, collectés lors de la validation des adhésions et du paiement des cotisations annuelles pour la période d’août 2023 à juillet 2024 inclus. Ces données ont été obtenues via des formulaires papier remplis par les membres puis numérisés, entraînant des erreurs, inexactitudes et valeurs manquantes.  

De plus, pour suivre l’évolution de la communauté, la base en cours de formation pour la saison 2024-2025 (326 membres) a également été analysée pour la période d’août à novembre 2024 inclus.  

Les données ont été fournies à l’auteur de manière anonymisée : les colonnes contenant les noms et adresses email ont été supprimées, ne laissant qu’une colonne d’identifiants (ID) pour d’éventuels croisements futurs.  

Outre l’ID, la base comprend les colonnes suivantes :  
- Date de naissance - date de naissance des membres,  
- Genre (F/H/X) - genre des membres,  
- CP - code postal de résidence,  
- Bénévoles - statut de bénévole,  
- Montant de l’adhésion - montant de la cotisation annuelle.  

Pour illustrer les conclusions sur une carte via OpenStreetMap, des bases ouvertes de la municipalité de Nantes, contenant les noms, codes postaux et coordonnées GPS des communes, ont été ajoutées au projet dans le dossier "data/".  

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


### 4. Étapes du projet  
1. Discussion des objectifs du projet et des questions posées par la direction de l’Atelier ;  
2. Nettoyage et analyse exploratoire des données ;  
3. Analyse des données, formulation d’hypothèses, illustration des conclusions à l’aide de graphiques ;  
4. Intégration de bases ouvertes et illustration des résultats sur des graphiques interactifs via Plotly et OpenStreetMap ;  
5. Résolution d’une problématique de classification avec plusieurs modèles, choix du meilleur selon les métriques, et génération de prédictions ;  
6. Compilation des résultats dans un rapport PDF et présentation à la direction de l’Atelier.  

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


### 5. Résultats  
1. Après nettoyage et enrichissement des données, des conclusions ont été formulées sur la relation entre l’âge, le genre, la commune de résidence, le montant de la cotisation et la disposition à être bénévole.  
2. La dynamique des inscriptions d’août à novembre 2024 a été comparée à la même période en 2023.  
3. Les compétences en Matplotlib ont été renforcées avec l’utilisation de méthodes inédites.  
4. OpenStreetMap a été intégré au projet via Plotly pour une visualisation claire des résultats.  
5. En outre, la tâche DS consistant à prédire le genre des participants qui l'ont indiqué dans le questionnaire en tant que « X » ou qui ne l'ont pas indiqué du tout a été résolue. Cette tâche n'a pas été définie par la direction de l'Atelier. Respectant le droit des personnes à ne pas spécifier leur genre (d'autant plus que la base de données est anonymisée), l'auteur s'est autorisé à porter le projet au-delà des compétences de l'analyste de données et à résoudre la tâche de classification.
6. Parmi les modèles testés (Logistic Regression, Decision Tree Classifier et Random Forest Classifier) en utilisant GridSearch CV, le Decision Tree Classifier a obtenu les meilleurs scores avec `precision` de 75 % et `recall` de 99 %, ce qui permet de conclure qu'environ 75 % des participants qui n'ont pas précisé leur genre étaient des hommes et 25 % des femmes. 7. Les résultats de l'étude sont présentés au [format pdf]() et le code exécutable est disponible dans le dépôt GitHub de l'auteur au format [Jupiter Notebook](https://github.com/StasBard/SF_DataScience/blob/master/MyPersonalProjects/MyProject_2/Pignon.ipynb). 

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


### 6. Conclusions  
Nous avons analysé la base de données d'Atelier du Pignon pour l'année 2023-2024 et, malgré un nombre relativement restreint d'enregistrements (979) et un ensemble limité de variables, nous avons réussi à dresser un tableau général de l'ensemble des membres, à formuler et illustrer certaines corrélations, ainsi qu'à répondre aux questions posées.  
1. Nous avons déterminé la contribution de chaque commune de Nantes en termes de nombre de membres, de bénévoles et de cotisations collectées.  
2. Nous avons mis en évidence la corrélation entre le montant de la cotisation et le sexe du membre, son statut de bénévole, ainsi que son mois de naissance.  
3. Nous avons également analysé la base de données en cours de constitution pour l'année actuelle (2024-2025), comprenant 326 membres inscrits à fin novembre, et comparé la dynamique avec celle de l'année précédente.  
4. Nous avons illustré les conclusions non seulement à l'aide de graphiques, mais aussi sur une carte interactive de la ville, renforçant ainsi leur clarté.  
5. Nous avons déterminé le sexe des membres qui ne l'avaient pas renseigné pour une raison quelconque.  

À l'avenir, il serait intéressant de suivre l'évolution de la composition des membres, comme décrit au point 3, en réalisant une analyse annuelle des données. Quoi qu'il en soit, cette analyse, réalisée par l'auteur (lui-même membre de l'Atelier) **sur une base bénévole**, a déjà permis de mieux comprendre le public de l'Atelier.  

:arrow_up: [Retour à la table des matières](https://github.com/StasBard/SF_DataScience/tree/master/MyPersonalProjects/MyProject_2#table-des-mati%C3%A8res)  


Si les informations sur ce projet vous semblent intéressantes et utiles, je vous serais reconnaissant de marquer mon dépôt et mon profil avec des étoiles ⭐️⭐️⭐️ !
