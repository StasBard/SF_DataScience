# Проект 8. Предсказание цены акции с помощью глубокой нейронной сети.

[Go to English](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#project-8-predicting-stock-prices-with-deep-neural-network) :us:  

## Оглавление  
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Решаемая задача](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#2-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[6. Выводы](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  

### 1. Описание проекта    
Продолжение [работы экспертов Alpha Vantage](https://www.alphavantage.co/stock-prediction-deep-neural-networks-lstm/) по предсказанию цены акций IBM c помощью глубокой нейронной сети (в частности LSTM) в попытке улучшить точность предсказания за счет добавления дополнительных данных.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Решаемая задача   
В конце свой работы эксперты Alpha Vantage предложили усовершенствовать их прогноз за счет подачи на вход модели дополнительных данных, например, значений технических индикаторов. В нашем проекте мы решили пойти этим путем и добавить в исходные данные цену открытия, максимальную и минимальную цены акции (OHL), объем торгов, а также значения двух технических индикаторов - Полос Боллинжера и Стохастика. Это позволит проверить, как влияет увеличение количества признаков на точность предсказания.  

**Условия решения задачи:**  
1. Добавить (сгенерировать) дополнительные признаки в исходные данные.  
2. Переписать части кода для работы не с одним, а со множеством признаков (10).  
3. Обучить LSTM-модель и оценить точность ее прогноза.

**Метрика качества**     
Для сравнения с результами первоначальной работы, будет использоваться та же самая метрика - `MSE`.  

**Практикуемые навыки**     
- чтение и понимание чужого кода;  
- доработка и оптимизация чужого кода;  
- освоение и практика работы с фреймворком PyTorch;  
- знакомство и использование LTSM-сети;  
- использование библиотеки Plotly для более наглядного представления данных.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
В изначальном проекте использовались биржевые данные о ежедневных ценах закрытия акции IBM за 20-летний период с ноября 1999 года по апрель 2021 года. Причем данные были скорректированными (на случай влияния разделения акций, выплаты дивидендов и проч.). Однако в ходе нашей работы, при добавлении технических индикаторов мы обнаружили, что сырые данные повышают точность прогноза, поэтому от скорректированных данных отказались.  

Также было принято решение отказаться и от данных технических индикаторов, получаемых по API, поскольку они в свою очередь тоже базируются на скорректированных данных. Вместо это мы вручную рассчитали значения выбранных индикаторов в соответствующих функциях.  

В итоге, вместо одного признака (цены закрытия) мы использовали десять: цены OHLC, объем торгов, значения трех полос Боллинжера и двух линий Стохастика.
  
:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Знакомство с изначальным кодом и с API Alpha Vantage.  
2. Получение по API дополнительных данных (OLC и объем) и генерация дополнительных (индикаторы).  
3. Переработка частей кода (в частности классов и объектов PyTorch) для использования 10 признаков в данных.  
4. Добавление интерактивных графиков Plotly Candlesticks для более наглядного отображения биржевых данных.  
5. Обучение и оценка LSTM-модели по метрике `MSE`.   
6. Сравнение результатов с первоначальной работой и выводы.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
1. Проведена доработка изначального кода, использованы более эффективные, безопасные методы и функции; модель способна работать с неограниченным числом признаков (задается в конфигурационной переменной вначале).  
2. Показано, впрочем, что увеличение количества признаков и использование технических индикаторов на дневных биржевых данных не приводит к повышению точности прогноза - снижению `MSE`. Однако на внутридневных данных (15-минутные данные) это оказывает желаемый эффект (это мы происллюстрируем в следующем проекте).  
3. С помощью интерактивных свечных графиков Plotly наглядно удалось показать, что несмотря на низкие значения потерь при обучении и тестировании модели, ее прогнозы не могут быть использованы в реальной торговли без риска потери депозита.  
4. Углублены навыки работы с фреймворком PyTorch и в частности с LTSM-сетью.  
5. Исполняемые код в формате Jupiter Notebook с дневными биржевыми данными доступен в [авторском репозитории GitHub](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/Predict_IBM_Stock_Prices_with_LSTM_daily_data.ipynb).

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
Задача и способ ее решения, предложенные экспертами Alpha Vantage, позволили улучшить навыки работы с фреймворком PyTorch, ближе познакомиться с глубокими нейронными сетями, а именно реккурентными и их разновидностью - LSTM (Long Short Term Memory) для целей прогнозирования негармонических временных рядов.  

Знания автора данного проекта из области биржевой и внутридневной торговли позволили показать, что низкие теоретические потери модели при прогнозировании не являются залогом успешного применения такой модели в реальной торговли в виду существенных расхождений прогноза с реальными данными.  

Вероятннее всего, повышение точности прогноза и надежности модели лежит не только в плоскости увеличения объема анализируемых данных, но и в усложнении самой модели нейронной сети путем добавления дополнительных слоев.  

:arrow_up: [к оглавлению](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по проекту представляется Вам интересной и полезной, я буду Вам благодарен за отметку моего репозитория и профиля звездами ⭐️⭐️⭐️!

---

# Project 8. Predicting stock prices with deep neural network.

[К описанию на русском](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-8-%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5-%D1%86%D0%B5%D0%BD%D1%8B-%D0%B0%D0%BA%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D0%B3%D0%BB%D1%83%D0%B1%D0%BE%D0%BA%D0%BE%D0%B9-%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9-%D1%81%D0%B5%D1%82%D0%B8) :ru:  

## Table of Contents
[1. Project Description](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#1-project-description)  
[2. Problem Statement](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#2-problem-statement)  
[3. Brief Data Overview](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#3-brief-data-overview)  
[4. Project Work Stages](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#4-project-work-stages)  
[5. Results](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#5-results)  
[6. Conclusions](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#6-conclusions)  

### 1. Project Description    
Continuation of [Alpha Vantage experts' work](https://www.alphavantage.co/stock-prediction-deep-neural-networks-lstm/) on IBM stock price prediction using deep neural network (in particular LSTM) in an attempt to improve prediction accuracy by adding more data.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


### 2. Problem Statement   
At the end of their work, Alpha Vantage experts suggested to improve their forecast by feeding additional data, for example, values of technical indicators, to the model input. In our project we decided to follow this way and add the opening price, maximum and minimum share prices (OHL), trading volume, as well as the values of two technical indicators - Bollinger Bands and Stochastics - to the input data. This will allow us to check the effect of increasing the number of features on prediction accuracy.  

**Problem Solving Conditions**  
1. Add (generate) additional features to the original data.  
2. Rewrite parts of the code to work not with one, but with multiple features (10).  
3. Train the LSTM model and evaluate the accuracy of its prediction.  

**Quality Metric**     
The same metric, `MSE`, will be used for comparison with the results of the original work.  

**Skills to Practice**     
- reading and understanding other people's code;  
- refining and optimizing other people's code;  
- mastering and practicing working with PyTorch framework;  
- familiarization and use of LTSM-network;  
- using Plotly library for more visual data representation.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


### 3. Brief Data Overview  
The original project used stock exchange data on daily closing prices of IBM shares for the 20-year period from November 1999 to April 2021. And the data were adjusted (in case of the impact of stock splits, dividend payments, etc.). However, in the course of our work, when adding technical indicators, we found that raw data increases the accuracy of the forecast, so we abandoned the adjusted data.  

We also decided to abandon the data of technical indicators received via API, as they are also based on adjusted data. Instead, we manually calculated the values of the selected indicators in the corresponding functions.  

As a result, instead of one feature (closing prices) we used ten: OHLC prices, trading volume, values of three Bollinger bands and two Stochastic lines.
  
:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


### 4. Project Work Stages  
1. Familiarization with the original code and with the Alpha Vantage API.  
2. Getting additional data (OLC and volume) and generating additional data (indicators) via API.  
3. Reworking parts of the code (PyTorch classes and objects in particular) to utilize the 10 features in the data.  
4. Adding interactive Plotly Candlesticks charts to better visualize stock data.  
5. Training and evaluating the LSTM model on the `MSE' metric.   
6. Comparison of results with the original work and conclusions.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


### 5. Results  
1. The original code was improved, more efficient, safer methods and functions were used; the model is able to work with an unlimited number of features (set in the configuration variable at the beginning).  
2. It is shown, however, that the increase in the number of features and the use of technical indicators on daily stock exchange data does not lead to an increase in the accuracy of the forecast - to a decrease in `MSE`. However, on intraday data (15-minute data) it has the desired effect (we will illustrate this in the next project).  
3. With the help of Plotly interactive candlestick charts we have clearly managed to show that despite the low loss values when training and testing the model, its forecasts cannot be used in real trading without risk of deposit loss.  
4. The skills of working with PyTorch framework and in particular with LTSM-network were deepened.  
5. Executable code in Jupiter Notebook format with daily stock data is available in [author's GitHub repository](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/Predict_IBM_Stock_Prices_with_LSTM_daily_data.ipynb).

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


### 6. Conclusions  
The problem and the way of its solution, proposed by Alpha Vantage experts, allowed to improve skills of working with PyTorch framework, to get acquainted with deep neural networks, namely recurrent and their variant - LSTM (Long Short Term Memory) for the purposes of forecasting non-harmonic time series.  

The knowledge of the author of this project from the field of stock exchange and intraday trading allowed to show that low theoretical losses of the model in forecasting are not a guarantee of successful application of such a model in real trading due to significant discrepancies between the forecast and real data.  

Most likely, the improvement of forecast accuracy and reliability of the model lies not only in increasing the volume of analyzed data, but also in complicating the neural network model itself by adding additional layers.  

:arrow_up: [Back to Table of Contents](https://github.com/StasBard/SF_DataScience/blob/master/Projects/Project_8/README.md#table-of-contents)


If you find the project information interesting and useful, I would appreciate it if you could give my repository and profile stars ⭐️⭐️⭐️!