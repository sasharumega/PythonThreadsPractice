# Получаем страницы:
![image](https://user-images.githubusercontent.com/92515117/143667399-20f36d73-5943-44c7-b60f-e447fdbdac70.png)

# Замеряем временные затраты на обработку полученных данных в одном потоке:
![image](https://user-images.githubusercontent.com/92515117/143667804-056add07-922e-4518-a553-33f708fc3707.png)
1 поток, 16 минут
Как видим, процесс очень много времени занимает

# Реализуем многопоточность через ThreadPoolExecutor и замерим время теперь:
![image](https://user-images.githubusercontent.com/92515117/143668106-36267479-5dbb-4b44-8beb-a56eece00add.png)
\n5 потоков, 3 минуты

![image](https://user-images.githubusercontent.com/92515117/143668169-58cced33-0d34-4f35-9b81-7da31b0412ad.png)
10 потоков, 1.5 минуты

![image](https://user-images.githubusercontent.com/92515117/143668189-cf32b9c5-21ee-493f-974a-998da162d3a7.png)
20 потоков, 0.67 минуты

![image](https://user-images.githubusercontent.com/92515117/143668252-572e54f3-4f95-49c2-9352-b8e7c40a2f7f.png)
100 потоков, 1 минута

Как видим, с помощью ThreadPoolExecutor можно значительно ускорить выполнение задач,
но, однако, стоит ограничить число потоков, так как неадекватные значения приводят
к снижению производительности в виде доп затрат на ресурсы компьютера
