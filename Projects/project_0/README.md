# Проект 0. Игра "Угадай число"

## Оглавление   
[1. Описание проекта](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#1-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#2-%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#3-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#4-%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результаты](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#5-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)    
[6. Выводы](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#6-%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### 1. Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.  
А также научиться игнорировать .csv-файлы с помощью .gitignore - для этого на Google Disk выложен "большой" [.csv-файл](https://drive.google.com/file/d/1GjoTQiUwWCTPcs0kjPZ_tTzQTShek-4W/view?usp=sharing).

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 2. Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**  
- компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под "угадать", подразумевается "написать программу, которая угадывает число";
- алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений, которое должно быть меньше 20.

**Что практикуем**     
- учимся писать хороший код на python;
- учимся работать с IDE;
- учимся работать с GitHub.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 3. Краткая информация о данных  
На вход функции отгадывания random_predict последовательно подаются "загаданные" числа из листа чисел в 1000 элементов, сгенерированных произвольным образом в интервале от 1 до 100.
С целью воспроизводитости фиксируется значение seed.
  
:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 4. Этапы работы над проектом  
1. Написать код функции random_predict, угадывающей число.
2. Наисать код функции score_game, подсчитывающей среднее количество попыток угадывания за 1000 подходов.
3. Протестировать работу программы и убедиться, что результаты работы удовлетворяют метрике качества, согласно которой среднее количество попыток угадывания не должно превышать 20.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 5. Результаты  
При отгадывании 1000 случайных чисел алгоритм показывает среднее количество попыток, равное 5, что полностью удовлетворяет условиям задачи.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### 6. Выводы  
В процессе работы над проектом успешно реализованы обозначенные практики:
- написан эффективный воспроизводимый код на python;
- код составлен в соответствии с PEP 8;
- улучшены навыки работы в IDE VS Code;
- улучшены навыки использования GitHub и оформления сопроводительной документации.

:bookmark_tabs: [к оглавлению](https://github.com/StasBard/SF_DataScience/tree/master/Projects/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по этому проекту покажется Вам интересной или полезной, то я буду очень Вам благодарен, если отметите репозиторий и профиль звездами ⭐️⭐️⭐️!