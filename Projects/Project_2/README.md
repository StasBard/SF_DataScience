# Проект 2. Анализ вакансий из HeadHunter.

[Go to English]() :us:  

## Оглавление  
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  


### 1. Описание проекта    
Анализ базы вакансий HeadHunter с целью ее подготовки для использования в модели машинного обучения, которая будет рекомендовать вакансии клиентам кадрового агентства, претендующим на позицию Data Scientist. 

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 2. Решаемая задача    
Проблематика задачи состоит в том, чтобы понять, что из себя представляют данные и насколько они соответствуют целям более крупного проекта по созданию модели машинного обучения, о которой упомянуто выше (выходит за рамки данного проекта). Таким образом, решаемая задача в литературе, посвященной Machine Learning, называется Data Understanding, или анализ данных.  

**Условия решения задачи**  
В ходе каждого этапа работы над проектом необходимо выполнить блоки практических заданий в jupyter-notebook по предложенному шаблону и ответить на контрольные вопросы на платформе SkillFactory. Посредством ответов на эти вопросы проверяется верность решений в заданиях. Задания выполняются последовательно.  

На каждом из этапов проекта требуется создать SQL-запрос к базе вакансий, сопроводить его кодом на Python для получения ответа на поставленный вопрос и формулирования выводов. Выводы можно дополнительно проиллюстрировать графиками.  

В остальном разрешается использовать только изученные в курсе переменные, структуры данных, циклы, функции, библиотеки, методы, правила и стандарты (включая PEP 8).  

**Метрика качества**     
- За ответы на все контрольные вопросы на платформе можно максимально набрать 23 балла.
- За выводы в jupyter-notebook можно получить еще 8 баллов:
    - 2 балла за правильность решения задач, логичность построения запросов;  
    - 2 балла за читабельность и верное форматирование запросов и кода на Python, наличие комментариев в запросах, аккуратность оформления решения;  
    - 2 балла за логичность и полноту выводов;  
    - 2 балла за дополнительные исследования данных.  

Итого: 31 балл.
Для успешного выполнения проекта необходимо набрать 21 балл.  

**Практикуемые навыки**     
- усвоить последовательность этапов анализа данных;
- закрепить навыки составления запросов с помощью СУБД PostgreSQL для выгрузки и анализа данных;
- улучшить навыки использования BI-инструмента Metabase;  
- улучшить навык формулирования выводов на основе проанализированной информации;
- развивать способность выдвигать гипотезы о зависимостях в данных, подтверждать или опровергать их с помощью данных;
- улучшить навыки использования языка разметки MarkDown;
- улучшить навыки работы с IDE VS Code, Git, GitHub (посредством добавления отчета о проекте в портфолио);
- улучшить навыки составления эффективного воспроизводимого код на Python в соответствии с PEP 8.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 3. Краткая информация о данных  
Для работы над проектом предоставлена база вакансий project_sql в виде нескольких таблиц в схеме public. Параметры подключения к базе данных, использованные при работе над проектом, удалены из jupyter-notebook перед его загрузкой на GitHub в целях безопасности.  
База данных включает следующие таблицы:
- vacancies - таблица данных по вакансиям,  
- areas - справочник кодов городов и их названий,  
- employers - справочник со списком работодателей,  
- industries - справочник вариантов сфер деятельности работодателей,  
- employers_industries - дополнительная таблица для организации связи между работодателями и сферами их деятельности, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их).  
  
:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 4. Этапы работы над проектом  
1. Знакомство с данными.  
2. Предварительный анализ данных.  
3. Детальный анализ вакансий.  
4. Анализ работодателей.  
5. Предметный анализ.  
6. Дополнительный (собственный) анализ.  
7. Оформление проекта и загрузка на GitHub.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 5. Результаты  
По итогам работы над проектом:
- предоставлены ответы на все контрольные вопросы на платформе SkillFactory, за что начислено 23 балла;
- сформулированы развернутые выводы по всем вопросам каждого из первых 5 этапов анализа;  
- проведен дополнительный (собственный) анализ сфер деятельности работодателей с выводами; 
- сформулированы общие выводы по проекту, выявлены тенденции, сделаны прогнозы;  
- сделан упор на SQL-запросы с целью наиболее понятного представления данных для ответа на поставленные вопросы без частого использования графиков;  
- подготовлен и выгружен на  GitHub [отчет](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_2/Project-2_Job_position_analysis.ipynb) об анализе базы вакансий в формате jupiter-notebook.  

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 6. Выводы  
В процессе работы над проектом отработаны способы обращения к базе данных с помощью PostgreSQL и Python, а также улучшены навыки работы с BI-инструментом Metabase; углубилось понимание работы изученных конструкций языка SQL, главным образом - метода JOIN и его разновидностей; приобретены навыки последовательного анализа с целью формирования целостной картины имеющихся данных, формулирования выводов, подкрепленных необходимыми данными, выдвижения гипотез и выявления тенденций; успешно реализованы все обозначенные практики.  

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_2#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!  

---

# Project 2. Analyzing job openings from HeadHunter.  

[К описанию на русском]() :ru: 

## Table of Contents
[1. Project Description]()  
[2. Problem Statement]()  
[3. Brief Data Overview]()  
[4. Project Work Stages]()  
[5. Results]()  
[6. Conclusions]()  

### 1. Project Description  
Analysis of the HeadHunter job database with the aim of preparing it for use in a machine learning model that will recommend job vacancies to clients of the personnel agency who are applying for the position of Data Scientist.  

:arrow_up: [Back to Table of Contents]()


### 2. Problem Statement  
The problem of the task is to understand what the data represents and how well it aligns with the goals of the larger project of building a machine learning model mentioned earlier (which goes beyond the scope of this project). Thus, the task at hand, in the literature dedicated to Machine Learning, is referred to as "Data Understanding" or data analysis.  

**Problem Solving Conditions**  
During each stage of the project, it is needed to complete practical tasks in Jupyter Notebook following the provided template and answer control questions on the SkillFactory platform. The correctness of the solutions is assessed through the answers to these questions. Tasks should be completed sequentially.  

At each stage of the project, one is required to create SQL queries to the job vacancy database, accompany them with Python code to answer the specified questions, and formulate conclusions. Conclusions can be further illustrated with graphs.  

Otherwise, it is allowed to use only the variables, data structures, loops, functions, libraries, methods, rules, and standards taught in the course, including adhering to the PEP 8 coding style.  

**Quality Metric**   
- One can earn a maximum of 23 points for answering control questions on the platform.  
- One can earn an additional 8 points for their conclusions in the Jupyter Notebook:  
  - 2 points for the correctness of solving tasks and the logical construction of queries;  
  - 2 points for the readability and proper formatting of queries and Python code, including comments in the queries, and the overall clarity of the solution;  
  - 2 points for the logical and comprehensive nature of their conclusions;  
  - 2 points for additional data exploration.  

In total, the maximum achievable score is 31 points.  
To successfully complete the project, one needs to score at least 21 points.  

**Skills to Practice**     
- Understand the sequence of data analysis stages;  
- Strengthen ability to write queries using the PostgreSQL database for data extraction and analysis;  
- Improve skills in using the BI tool Metabase;  
- Enhance ability to draw conclusions based on analyzed information;  
- Develop the skill of formulating hypotheses about data dependencies and confirming or refuting them using data;  
- Improve skills in using Markdown markup language;  
- Enhance skills in working with IDEs like VS Code, Git, and GitHub by adding a project report to a portfolio;  
- Improve skills in writing efficient and reproducible Python code following PEP 8 guidelines.  

:arrow_up: [Back to Table of Contents]()


### 3. Brief Data Overview  
The project is provided with a job vacancy database named "project_sql," which is structured into several tables within the "public" schema. For security reasons, the database connection parameters used in the project have been removed from the Jupyter Notebook before uploading it to GitHub. The database includes the following tables:  
- vacancies - This table contains data about job vacancies.;  
- areas - It serves as a reference for city codes and their names;  
- employers - This is a reference table containing a list of employers;  
- industries - It serves as a reference for different sectors or industries of employers;  
- employers_industries - This table is used to establish the relationships between employers and their industries. It is necessary because one employer can operate in multiple industries, or employers may not specify their industries at all.  

:arrow_up: [Back to Table of Contents]()


### 4. Project Work Stages  
1. Data Familiarization.  
2. Preliminary Data Analysis.  
3. In-Depth Vacancy Analysis.  
4. Employer Analysis.  
5. Subject Analysis.  
6. Additional (Custom) Analysis.  
7. Project Formatting and Uploading to GitHub.  

:arrow_up: [Back to Table of Contents]()


### 5. Results  
Upon completion of the project:  
- All control questions on the SkillFactory platform have been answered, earning 23 points;  
- Detailed conclusions have been formulated for each of the first 5 stages of the analysis;  
- An additional (custom) analysis of the employers' fields of activity has been conducted with conclusions;  
- General conclusions about the project have been formulated, trends have been identified, and forecasts have been made;  
- Emphasis was placed on SQL queries to provide the most understandable data presentation for answering questions without frequent use of graphs;  
- A [report](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_2/Project-2_Job_position_analysis.ipynb) on the analysis of the job vacancy database has been prepared and uploaded to GitHub in Jupyter Notebook format.  

:arrow_up: [Back to Table of Contents]()


### 6. Conclusions  
During the project, various skills and knowledge were acquired and improved:  
- Proficiency in interacting with a PostgreSQL database using Python;  
- Enhanced abilities to work with the BI tool Metabase;  
- A deeper understanding of SQL constructs, with a primary focus on JOIN operations and their variations;  
- The acquisition of skills for step-by-step data analysis to form a comprehensive picture of the available data;  
- The ability to formulate conclusions supported by relevant data, generate hypotheses, and identify trends;  
- The successful application of the practices outlined in the project.  

:arrow_up: [Back to Table of Contents]()


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!