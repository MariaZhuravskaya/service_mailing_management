Сервис управления E-mail рассылками.

При разработки использовала
Python, Django framework, Postgres, Redis, Git.

Установка и запуск
git clone https://github.com/MariaZhuravskaya/coursework_django
Необходимо создать файл .env на основе .env.sample с вашим токеном, аккаунтом для отправки почты, данные для подключения БД
Далее, пожалуйста, обратитесь к <a>requirements.txt</a> для получения обновленного списка необходимых пакетов.

Управление
Админка Django (admin/admin): http://127.0.0.1:8000/admin
Сайт : http://127.0.0.1:8000/

Задание
Необходимо разработать сервис управления рассылками, администрирования и получения статистики, который по заданным правилам запускает рассылку по списку клиентов.

Необходимо реализовать методы создания новой рассылки, просмотра созданных и получения статистики по выполненным рассылкам.
Реализовать сам сервис отправки уведомлений на E-mail.

Сущность "рассылка" имеет атрибуты:
уникальный id рассылки
наименование рассылки
дата и время запуска рассылки
дата и время окончания рассылки
текст сообщения для доставки клиенту
период рассылки
список клиентов
статус рассылки
дата последней отправки


Сущность "клиент" имеет атрибуты:
уникальный id клиента
Фамилия
Имя
Отчество
комментарии
год рождения
почта


Сущность "сообщение" имеет атрибуты:
уникальный id сообщения
тема письма
тело письма
id клиента, которому отправили

Сущность "настройки рассылки" имеет атрибуты:
уникальный id рассылки
наименование рассылки
Дата и время запуска рассылки
Дата и время окончания рассылки
Период рассылки
Сообщение для рассылки
Список клиентов
Статус рассылки
Дата последней отправки
id клиента, которому отправили

Сущность "Логи рассылки" имеет атрибуты:
ID рассылки
дата и время последней попытки
статус попытки
ответ почтового сервера, если он был

Спроектировать и реализовать:

добавления нового клиента в справочник со всеми его атрибутами
обновления данных атрибутов клиента
удаления клиента из справочника
добавления, редактирование, удаление рассылки со всеми её атрибутами
получения статистики отправленных сообщений по конкретной рассылке
обновления атрибутов рассылки
обработки активных рассылок и отправки сообщений клиентам
Логика рассылки
Расширить модель пользователя для регистрации по почте, а также верификации.
Добавить интерфейс для входа, регистрации и подтверждения почтового ящика.
Реализовать ограничение доступа к рассылкам для разных пользователей.
Реализовать интерфейс менеджера:
        Функционал менеджера
        Может просматривать любые рассылки.
        Может просматривать список пользователей сервиса.
        Может блокировать пользователей сервиса.
        Может отключать рассылки.
        Не может редактировать рассылки.
        Не может управлять списком рассылок.
        Не может изменять рассылки и сообщения.
Создать блог для продвижения сервиса.Настроить административную панель для контент-менеджера.

После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть выбраны из справочника все клиенты, которые подходят под значения фильтра, указанного в этой рассылке и запущена отправка для всех этих клиентов.
Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
По ходу отправки сообщений должна собираться статистика (см. описание сущности "сообщение" выше) по каждому сообщению для последующего формирования отчётов.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Необходимо реализовать корректную обработку подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок. Для интеграции с разрабатываемым проектом в данном задании существует внешний сервис, который может принимать запросы на отправку сообщений в сторону клиентов.

Для восстановления в админке команды createsuperuser запустите кастомную команду csu.py
Для запуска автоматической рассылки используйте кастомную команду: runapscheduler.py