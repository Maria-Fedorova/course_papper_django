# Основы веб-разработки на Django

## Критерии

- Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание рассылки,
  удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
- Реализовали всю требуемую логику работы системы.
- Интерфейс понятен и соответствует базовым требованиям системы.
- Все интерфейсы для изменения и создания сущностей, не относящиеся к стандартной админке, реализовали с помощью
  Django-форм.
- Все настройки прав доступа реализовали верно.
- Приложены фикстуры или созданы команды для заполнения базы данных (минимум — для рассылок, сообщений, клиентов, групп
  пользователей, блога)


## Задачи

1. Разработка сервиса
- Реализуйте интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками.
- Реализуйте скрипт рассылки, который работает как из командной строки, так и по расписанию.
- Добавьте настройки конфигурации для периодического запуска задачи при необходимости.
- Рассылка (настройки):
  - дата и время первой отправки рассылки;
  - периодичность: раз в день, раз в неделю, раз в месяц;
  - статус рассылки (например, завершена, создана, запущена).
- Сообщение для рассылки:
  - тема письма,
  - тело письма.
- Попытка рассылки:
  - дата и время последней попытки;
  - статус попытки (успешно / не успешно);
  - ответ почтового сервера, если он был
- Логика работы системы:
  - После создания новой рассылки, если текущие дата и время больше даты и времени начала и меньше даты и времени окончания, должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
  - Если создается рассылка с временем старта в будущем, отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя сервиса.
  - По ходу отправки рассылки должна собираться статистика (см. описание сущностей «Рассылка» и «Попытка» выше) по каждой рассылке для последующего формирования отчетов. Попытка создается одна для одной рассылки. Формировать попытки рассылки для всех клиентов отдельно не нужно.
  - Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
2. Доработка сервиса
- Расширьте модель пользователя для регистрации по почте, а также верификации.
- Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика.
- Реализуйте ограничение доступа к рассылкам для разных пользователей.
- Реализуйте интерфейс менеджера.
- Создайте блог для продвижения сервиса.
- Функционал менеджера:
  - Может просматривать любые рассылки.
  - Может просматривать список пользователей сервиса.
  - Может блокировать пользователей сервиса.
  - Может отключать рассылки.
  - Не может редактировать рассылки.
  - Не может управлять списком рассылок.
  - Не может изменять рассылки и сообщения.
- Функционал пользователя
  - Весь функционал дублируется из первой части курсовой работы, но теперь нужно следить за тем, чтобы пользователь не мог случайным образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.
- Продвижение:
  - Блог:
    - Реализуйте приложение для ведения блога. При этом отдельный интерфейс реализовывать не требуется, но необходимо настроить административную панель для контент-менеджера. В сущность блога добавьте следующие поля:
      - заголовок,
      - содержимое статьи,
      - изображение,
      - количество просмотров,
      - дата публикации.
  - Главная страница
    - Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:
      - количество рассылок всего,
      - количество активных рассылок,
      - количество уникальных клиентов для рассылок,
      - три случайные статьи из блога.
  - Кеширование
    - Для блога и главной страницы самостоятельно выберите, какие данные необходимо кешировать, а также каким способом необходимо произвести кеширование.
