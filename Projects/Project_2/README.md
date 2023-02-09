# Проект 2. Анализ вакансий из HeadHunter.

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

**Условия решения задачи:**  
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