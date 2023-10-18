# Проект 1. Анализ резюме из HeadHunter.

[Go to English](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#project-1-analyzing-resumes-from-headhunter) :us: 

## Оглавление  
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  


### 1. Описание проекта    
Анализ базы резюме HeadHunter с целью ее подготовки для использования в модели машинного обучения, определяющей примерный уровень заработной платы, подходящей соискателю на основании информации, которую тот указал о себе.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача    
Проблематика задачи: часть соискателей не указывает желаемую заработную плату, когда составляет своё резюме.
Поэтому имеющуюся в распоряжении базу резюме с сайта поиска вакансий hh.ru необходимо преобразовать, исследовать и очистить.

**Условия решения задачи:**  
В ходе каждого этапа работы над проектом необходимо выполнить блоки практических заданий в jupyter-notebook по предложенному шаблону и ответить на контрольные вопросы на платформе SkillFactory. Посредством ответов на эти вопросы проверяется верность решений в заданиях.
Задания выполняются последовательно.

С целью разведывательного анализа разрешено использовать любую из изученных библиотек визуализации: Matplotlib, Seaborn и Plotly. Однако рекомендуется выбрать Plotly ввиду ее интерактивности.

В остальном разрешается использовать только изученные в курсе переменные, структуры данных, циклы, функции, библиотеки, методы, правила и стандарты (включая PEP 8).

**Метрика качества**     
- За ответы на все контрольные вопросы на платформе можно максимально набрать 30 баллов.
- За выводы по разведывательному анализу в jupyter-notebook можно получить еще 10 баллов: 8 основных и 2 дополнительных (за проверку собственных гипотез).  

Итого: 40 баллов.
Для успешного выполнения проекта необходимо набрать 21 балл.

**Практикуемые навыки**     
- закрепить последовательность этапов предобработки данных;
- улучшить навыки использования изученных методов для преобразования данных;
- углубить знания методов библиотек визуализации и различных типов графиков для исследования зависимостей в данных;
- улучшить навык формулирования выводов на основе проанализированной информации;
- развить способность выдвигать гипотезы о зависимостях в данных, подтверждать или опровергать их с помощью графиков;
- улучшить навыки использования языка разметки MarkDown;
- улучшить навыки работы с IDE VS Code, Git, GitHub (посредством добавления отчета о проекте в портфолио);
- улучшить навыки составления эффективного воспроизводимого код на python в соответствии с PEP 8.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
Для работы предоставляется база резюме, выгруженная с сайта поиска вакансий hh.ru.
Ввиду ее большого размера (434,4 Мб) она не может быть загружена на сайт GitHub, поэтому для воспроизведения кода данного проекта читателю предлагается скачать базу по [ссылке](https://drive.google.com/file/d/1_l4Bbc1xrUnQyDTsLzRP0EOaz-myM3yK/view?usp=share_link) и сохранить ее в папку `data/` проекта.

Дополнительно предоставляетя таблица котировок валют с целью конвертации желаемых зарплат соискателей из базы. Эта таблица находится в [папке проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1/data) и не требует дополнительных действий.
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Базовый анализ структуры данных.
2. Преобразование данных.
3. Разведывательный анализ.
4. Очистка данных.
5. Оформление проекта и загрузка на GitHub.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
По итогам работы над проектом:
- предоставлены ответы на все контрольные вопросы на платформе SkillFactory, за что начислено 30 баллов;
- сформулированы развернутые выводы по 8-ми обязательным пунктам разведывательного анализа, а также по 3-м собственным (один - бонусный);
- подготовлен [отчет](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_1/Project-1_Resumes_Analysis.ipynb) об анализе базы данных резюме в формате jupiter-notebook с рекомендациями, на какие признаки стоит обратить внимание при создании модели машинного обучения.
- проведена очистка данных, позволяющая подать обработанную базу резюме на вход модели обучения.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В процессе работы над проектом укрепилось понимание важности анализа и предобработки данных перед их последующим использованием в моделях машинного обучения, бизнесе; обнаружились возможные "подводные камни" неполноты данных, а вместе с ними отработаны приемы обработки и очистки данных; расширились знания способов визуализации взаимосвязей признаков в данных; успешно реализованы все обозначенные практики.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!

---

# Project 1. Analyzing resumes from HeadHunter.  

[К описанию на русском](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-1-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5-%D0%B8%D0%B7-headhunter) :ru: 

## Table of Contents
[1. Project Description](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#1-project-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#3-brief-data-overview)  
[4. Project Work Stages](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#4-project-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#6-conclusions)  

### 1. Project Description    
This project involves analyzing the HeadHunter resume database to prepare it for use in a machine learning model. The goal is to predict an approximate salary level suitable for job applicants based on the information they provide about themselves.

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


### 2. Problem Statement   
The problem being addressed is that some job applicants do not specify their desired salary when creating their resumes. Therefore, the existing resume database from the job search site hh.ru needs to be transformed, explored, and cleaned.

**Problem Solving Conditions:**  
During each stage of the project it is necessary to complete practical tasks in a Jupyter notebook using the provided template and answer control questions on the SkillFactory platform. The correctness of solutions to the tasks is verified by the answers to these questions. The tasks are to be completed sequentially.  

For exploratory analysis, it is allowed to use any of the studied visualization libraries : Matplotlib, Seaborn, and Plotly. However, it is recommended to choose Plotly for its interactivity.  

Apart from that, it is allowed to use only the variables, data structures, loops, functions, libraries, methods, rules, and standards studied in the course, including PEP 8.  

**Quality Metric**     
- A student can earn a maximum of 30 points for answering all control questions on the SkillFactory platform.  
- Additional 10 points are awarded for the exploritary analysis: 8 points for the main analysis and 2 extra points for verifying own hypotheses.  

Total: 40 points.  
To successfully complete the project, one needs to earn at least 21 points.  

**Skills to Practice**      
- Consolidating the sequence of data preprocessing stages.  
- Enhancing the use of learned methods for data transformation.  
- Deepening knowledge of visualization library methods and various types of graphs for exploring data dependencies.  
- Improving the skill of drawing conclusions based on analyzed information.  
- Developing the ability to formulate hypotheses about data dependencies, validating or disproving them using graphs.  
- Enhancing skills in using Markdown markup language.  
- Improving proficiency with IDE VS Code, Git, GitHub (by adding project reports to the portfolio).  
- Enhancing the skills of composing efficient and reproducible Python code in accordance with PEP 8.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


### 3. Brief Data Overview  
For this project, a resume database has been provided, which was extracted from the job search website hh.ru. Due to its large size (434.4 MB), it cannot be uploaded to the GitHub site. Therefore, to reproduce the code of this project, the reader is recommended to download the database from the [link](https://drive.google.com/file/d/1_l4Bbc1xrUnQyDTsLzRP0EOaz-myM3yK/view?usp=share_link) and save it in the project's `data/` folder.

Additionally, a currency exchange rate table is provided to convert the desired salaries of job applicants from the database. This table is located in the [project folder](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1/data) and does not require any additional actions.

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


### 4. Project Work Stages  
1. Basic analysis of data structure.  
2. Data transformation.  
3. Exploratory data analysis.  
4. Data cleaning.  
5. Project documentation and uploading to GitHub.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


### 5. Results  
Based on the project's results:
- Answers were provided to all the assessment questions on the SkillFactory platform, earning 30 points;  
- Detailed conclusions were formulated based on the 8 mandatory issues of exploratory data analysis, as well as 3 additional ones (one of which is a bonus);  
- [Report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_1/Project-1_Resumes_Analysis.ipynb) on the analysis of the resume database was prepared in jupyter notebook format, including recommendations on which features to pay attention to when creating a machine learning model;  
- Data cleaning was performed, enabling the processed resume database to be used as input for the training model.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


### 6. Conclusions  
During the project, the understanding of the importance of data analysis and preprocessing before their use in machine learning models and business applications was significantly strengthened. Possible "pitfalls" of data incompleteness were identified, and techniques for data processing and cleaning were effectively applied. Knowledge regarding methods of visualizing feature relationships in data expanded, and all outlined practices were successfully implemented.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_1#table-of-contents)


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!