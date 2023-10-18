# Проект 3. Предсказание рейтига отелей на Booking.

[Go to English]() :us:  

## Оглавление  
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  


### 1. Описание проекта    
Представим, что я работаю дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 2. Решаемая задача    
С помощью изученных методов разведовательного анализа (EDA) требуется подготовить имеющуюся базу данных об отелях с сайта Booking.com к подаче на вход модели RandomForestRegressor для обучения и предсказания рейтинга отелей из тестовой выборки. 

**Условия решения задачи:**  
Задача реализована в форме соревнования на платформе kaggle.  

Автором задания подготовлен baseline - jupyter-notebook с основыми этапами обработки данных. В ходе работы над задачей требуется наполнить эти этапы содержимым: выполнить очистку данных, провести разведовательный анализ, обучить модель и предсказать рейтинги тестовой выборки отеля, при этом получив значение итоговой метрики средней абсолютной ошибки ниже 13,5%.

Результаты предсказания в файле submission.csv загружаются на платформу kaggle для оценки рейтинга работы и добавления студента в рейтинг победителей. Ссылка на публичный ноутбук отправляется на проверку ментору. Кроме этого, файл ноутбука следует разместить на платформе GitHub, сопроводив описанием, и также предоставить ссылку на проверку ментору.

В процессе решения студент должен продемонстрировать владение методами разведовательного анализа, умение выдвигать и проверять гипотезы, сопровождать их визуализацией и выводами, оформлять код в соответствии со стандартами PEP 8.

**Метрика качества**     
Выполненная задача должна соответствовать следующим критериям:
- Качество кода (соблюдение стандартов оформления PEP 8, комментирование кода, README к проекту). Оформление проекта на GitHub, GitLab, Kaggle.  
- Очистка данных.  
- Исследование данных (качество визуализации, наличие идей, гипотез, комментариев).  
- Генерация признаков.  
- Отбор признаков.  
- Преобразование признаков.  
- Качество решения: результат метрики MAPE (желательно ниже 13,5%).

За каждый критерий можно получить 3 балла:  
0 - Задание не выполнено или результатами работы невозможно воспользоваться на практике.  
1 - Есть большие неточности в выполнении задания.  
2 - Задача решена, требуются минимальные доработки.  
3 - Задача решена полностью, результат можно использовать на практике.  

Максимально можно набрать таким образом: 21 балл.  
Для успешного выполнения проекта необходимо набрать 12 баллов.  

**Практикуемые навыки**     
- усвоить последовательность разведовательного анализа данных;
- улучшить понимание статистических тестов для отбора сгенерированных данных;    
- развивать способность выдвигать гипотезы о зависимостях в данных, подтверждать или опровергать их, делать выводы;  
- добиться заданной величины метрики MAPE лишь с помощью подготовки данных без изменения параметров модели;  
- практиковать работу на платформах kaggle и GitHub (посредством добавления отчета о проекте в портфолио);  
- практиковать навыки использования языка разметки MarkDown;  
- улучшить навыки составления эффективного воспроизводимого код на Python в соответствии с PEP 8.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 3. Краткая информация о данных  
Для работы над проектом предоставлена база отелей сервиса Booking.com в виде тренировочного и тестового датафреймов, отличающихся наличием признака пользовательской оценки отеля reviewer_score. Описание всех признаков содержится в начале ноутбука с решением.  

В ходе работы разрешается использовать любые внешние источники для генерирования дополнительных признаков в данных.
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 4. Этапы работы над проектом  
1. Знакомство с данными.  
2. Очистка и подготовка данных.  
3. Разведывательный анализ.  
4. Анализ работодателей.  
5. Обучение модели и оценка результатов.  
6. Предсказание рейтинга отелей.  
7. Оформление проекта на kaggle и GitHub.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 5. Результаты  
В ходе работы над проектом последовательно пройдены все этапы обработки данных:
- несмотря на то, что входные данные представлены в хорошо подготовленной форме, проведена дополнительная их очистка, что не могло не повлиять на улучшение итоговой метрики;  
- данные исследованы, намечены шаги EDA, обосновано использование/не использование тех или иных методов обработки;  
- проведен разведовательный анализ данных:  
    - сгенерированы новые признаки (в том числе с использованием внешних источников),  
    - проведено снижение размерности признаков путем кодирования,  
    - оценена их значимость, мультиколлинеарность и принято решение об удалении или оставлении в датафрейме;  
- достигнуто целевое значение итоговой метрики MAPE (12,56% в ноутбуке);  
- каждый этап сопровожден развернутыми комментариями и выводами, визуализацией данных;  
- файл sumbission.csv с предсказанными рейтингами загружен на kaggle;  
- проект в виде ноутбука оформлен на [kaggle](https://www.kaggle.com/stasbard/project-3-booking-reviews) и [GitHub](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_3/Project_3_EDA_Booking_reviews.ipynb). 

**Эволюция коммитов**  
Улучшение метрики MAPE достигалось с помощью разведовательного анализа. По рекомендации ментора, была применена библиотека анализа естественного языка nltk. При этом в первом подходе из возвращаемых оценок использовались лишь совокупные для отрицательных и положительных отзывов, которые складывались для образование одного признака. Этот прием не дал желаемого улучшения MAPE, в результате чего было принято решение использовать все четыре составляющие для каждого отзыва: положительную, нейтральную, отрицательную и совокупную. Первая версия сабмита сразу содержит именно такое решение.  

На втором сабмите было обнаружено, что излишнее удаление даже кореллирующих признаков негативно сказывается на MAPE, что дало понимание необходимости сохранять баланс в удалении и сохранении даже сильно связанных признаков.  

Последние три сабмита - по сути тонкая доработка финальных результатов и оформление ноутбука, разница между ними невелика. Однако тут открылось негативное влияние метода MinMaxScaler на предсказательный рейтинг с помощью модели RandomForestRegressor, о чем предупреждал ментор на вебинаре: рейтинги оказались на порядок меньше. Я не заметил этого, и загрузил файл на платформу, в результате чего получил оценку 89,7%. Для исправления ситуации я нашел два способа: умножение всех предсказанных оценок на 10 или отказ от использования метода MinMaxScaler. Последнему способу было отдано предпочтение, учитывая его незначительный вклад в улучшение метрики.  

Наконец, интересным стало открытие, что небольшая ошибка в координате центра города (модуль долготы для Лондона) при расчете признака расстояния до отеля приводил к наилучшей итоговой метрике (12,54%). Без понимания устройства модели, мне это показалось странным, поскольку модель подбирает коэффициенты, обусловливающие рейтинг теми или иными признаками - какая разница, будет расстояние до центра составлять 3 км или 2 км, к примеру. Вероятно, мое понимание неверное, и оно углубится в следующем модуле по изучению машинного обучения. Пока же пришлось исправить ошибку и довольствоваться чуть худшим результатом.

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


### 6. Выводы  
1. Несмотря на кажущуюся простоту задачи (очистка данных и генерирование новых признаков за счет здравого смысла и известных инструментов библиотек python без изучения устройства модели машинного обучнения), проект оказался довольно трудоемким и сложным, и занял свыше 40 часов, включая время на изучение учебных материалов и просмотр вводного вебинара.  
2. С точки зрения оформления и визуализации он уступает предыдущим проектам, основной упор которых делался именно на эту составляющую. Впрочем, никто не ограничивал нас в использовании всего имеющегося арсенала приемов визуализации, однако поскольку основная задача была в том, чтобы обучить моделить и добиться улучшения метрики MAPE, на это были брошены все силы. И с учетом затраченного времени, другим составляющим проекта пришлось уделить меньше внимания.  
3. Вместе с тем, данный проект показал значимость подготовки данных перед обучением модели и позволил потренировать полученные навыки разведывательного анализа.  
4. Сюрпризом (на который намекал во время вводного вебинара ментор) стало взаимодействие методов нормализации и стандартизации данных с моделью машинного обучения RandomForestRegressor: использование первых либо ухудшало значение метрики MAPE, либо улучшало ее незначительно, но при этом искажало получаемые предсказания. В результате, от использования этих методов в данном проекте пришлось отказаться.  
5. Особой ценностью проекта стала его реализация на платформе kaggle в атмосфере здоровой конкуренции за высокий рейтинг. Студенты получили действительный инструмент повышения своих навыков Data Scientist'а и, следовательно, шансов на трудоустройство через участие в реальных интересных соревнованиях.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/Project_3#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)  


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля на GitHub звездами ⭐️⭐️⭐️! А также, прошу поставить upvote моему ноутбуку на kaggle. Спасибо!  

---

# Project 3. Predicting hotel ratings on Booking.  

[К описанию на русском]() :ru:  

## Table of Contents
[1. Project Description]()  
[2. Problem Statement]()  
[3. Brief Data Overview]()  
[4. Project Work Stages]()  
[5. Results]()  
[6. Conclusions]()  

### 1. Project Description    
Let's imagine that I work as a data scientist at Booking.com. One of the company's challenges is dealing with dishonest hotels that manipulate their ratings. One way to identify such hotels is to build a model that predicts a hotel's rating. If the model's predictions significantly deviate from the actual rating, it's possible that the hotel is behaving dishonestly and should be investigated.  

:arrow_up: [Back to Table of Contents]()


### 2. Problem Statement   
Using the methods of Exploratory Data Analysis (EDA), the existing database of hotels from Booking.com needs to be prepared for input into the RandomForestRegressor model for training and predicting hotel ratings from the test dataset.  

**Problem Solving Conditions**  
The task is implemented in the form of a competition on the Kaggle platform.  

The author of the task has prepared a baseline - a Jupyter notebook with the main data processing steps. During the work on the task, one needs to fill these steps with content: perform data cleaning, conduct exploratory analysis, train the model, and predict the ratings of hotels in the test dataset, while achieving a final metric value with a mean absolute error of less than 13.5%.  

The prediction results in the submission.csv file are uploaded to the Kaggle platform to assess the rating of the work and include the student in the list of winners. A link to the public notebook should be sent for mentor review. Additionally, the notebook file should be placed on the GitHub platform, accompanied by a description, and the link should also be provided for mentor review.  

In the process of solving the task, the student should demonstrate proficiency in exploratory data analysis methods, the ability to formulate and test hypotheses, support them with visualizations and conclusions, and format the code in accordance with the PEP 8 standards.  

**Quality Metric**     
The completed task should meet the following criteria:  
- Code quality (compliance with PEP 8 code formatting standards, code commenting, and a README for the project). Project presentation on GitHub, GitLab, Kaggle, or a similar platform.  
- Data cleaning.  
- Data exploration (quality of visualization, presence of ideas, hypotheses, comments).  
- Feature generation.  
- Feature selection.  
- Feature transformation.  
- Solution quality: MAPE metric result (preferably below 13.5%).  

For each criterion, one can earn up to 3 points:  
0 - The task is not completed, or the results of the work cannot be practically used.  
1 - There are significant inaccuracies in completing the task.  
2 - The task is completed, but minimal adjustments are needed.  
3 - The task is fully completed, and the results can be used in practice.  

The maximum score achievable is 21 points.  
To successfully complete the project, one needs to earn 12 points.  

**Skills to Practice**   
- Understand the sequence of exploratory data analysis;  
- Improve understanding of statistical tests for feature selection;  
- Develop the ability to formulate and test hypotheses about data dependencies and draw conclusions;  
- Achieve the specified MAPE metric without changing model parameters, relying solely on data preparation;  
- Practice working on platforms like Kaggle and GitHub (by adding the project report to a portfolio);  
- Improve the skills of using the Markdown markup language;  
- Enhance the skills of writing efficient and reproducible Python code in accordance with PEP 8.  

:arrow_up: [Back to Table of Contents]()


### 3. Brief Data Overview  
A dataset of Booking.com hotels is provided for the project, which includes both a training and a test dataset. The difference between them is the presence of the reviewer_score feature. A description of all the features is included at the beginning of the notebook with the solution.  

During the project, one is allowed to use any external sources to generate additional features in the data.  
  
:arrow_up: [Back to Table of Contents]()


### 4. Project Work Stages  
1. Data Exploration.  
2. Data Cleaning and Preparation.  
3. Exploratory Data Analysis.  
4. Employer Analysis.  
5. Model Training and Evaluation.  
6. Hotel Rating Prediction.  
7. Project Presentation on Kaggle and GitHub.  

:arrow_up: [Back to Table of Contents]()


### 5. Results  
Throughout the project, all stages of data processing were sequentially completed:  
- Despite the fact that the input data was well-prepared, additional cleaning was performed, which had a good impact on improving the final metric;  
- The data was explored, steps for exploratory data analysis (EDA) were outlined, and the justification for the use or non-use of specific processing methods was provided;  
- Exploratory data analysis was conducted, involving:  
    - The generation of new features, including the use of external sources,  
    - Dimensionality reduction through encoding,  
    - Evaluation of feature significance and multicollinearity, resulting in decisions regarding feature retention or removal from the dataframe;  
- The target value for the final metric, MAPE (12.56% in the notebook), was achieved;  
- Each stage is accompanied by detailed comments and insights, along with data visualization;  
- The submission.csv file with predicted ratings was uploaded to Kaggle;  
- The project, in the form of a notebook, is available on [Kaggle](https://www.kaggle.com/stasbard/project-3-booking-reviews) and [GitHub](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_3/Project_3_EDA_Booking_reviews.ipynb).  

**Evolution of commits**  
Improvements in the MAPE metric were achieved through exploratory data analysis. Following the mentor's recommendation, the natural language processing library NLTK was applied. In the initial approach, only the overall scores for negative and positive reviews were used, summing up to form a single feature. However, this technique didn't yield the desired improvement in MAPE. As a result, the decision was made to use all four components for each review: positive, neutral, negative, and overall. The first version of the submission immediately implemented this approach.  

In the second submission, it was discovered that excessive removal of even correlated features had a negative impact on MAPE. This realization emphasized the need to maintain a balance between removing and retaining even highly correlated features.  

The last three submissions essentially involved fine-tuning the final results and formatting the notebook. However, a negative impact of the MinMaxScaler method on the predictive rating using the RandomForestRegressor model was revealed, resulting in much lower ratings. I didn't notice this and uploaded the file to the platform, which resulted in a score of 89.7%. To rectify this, I found two solutions: multiplying all predicted scores by 10 or abandoning the use of the MinMaxScaler method. The latter solution was preferred, considering its minimal contribution to improving the metric.  

Finally, an interesting discovery was made: a small error in the city center's coordinate (longitude module for London) when calculating the hotel distance feature led to the best final metric (12.54%). Without a full understanding of the model's workings, this seemed peculiar. After all, the model adjusts coefficients based on ratings with various features. It doesn't seem to matter whether the distance to the city center is 3 km or 2 km, for example. Perhaps my understanding is incorrect, and it will deepen in the next machine learning module. For now, I had to correct the error and accept a slightly worse result.  

:arrow_up: [Back to Table of Contents]()


### 6. Conclusions  
1. Despite the seemingly simple nature of the task (data cleaning and feature engineering using common sense and well-known Python libraries without diving into the inner workings of machine learning models), the project turned out to be quite time-consuming and complex, taking over 40 hours, including time spent on studying educational materials and attending introductory webinars.  
2. From the perspective of presentation and visualization, it falls behind previous projects where the main emphasis was on this component. However, I was not restricted from using the full range of visualization techniques. Still, since the primary goal was to train a model and improve the MAPE metric, most efforts were directed there. Given the time constraints, other aspects of the project received less attention.  
3. Nevertheless, this project highlighted the significance of data preparation before model training and provided an opportunity to practice the acquired exploratory data analysis skills.  
4. An unexpected revelation (hinted at during the introductory webinar by the mentor) was the interaction between data normalization and standardization methods and the machine learning model RandomForestRegressor. Using these methods either worsened the MAPE metric or improved it slightly but distorted the predictions obtained. Consequently, the use of these methods had to be abandoned in this project.  
5. The real value of the project lies in its implementation on the Kaggle platform within the competitive environment for a high rating. Students gained a tangible tool for enhancing their Data Scientist skills and, consequently, increased chances of employment through participation in real and engaging competitions.  

:arrow_up: [Back to Table of Contents]()


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!