# e_diary_hack_scripts
Набор скриптов, для редактирования базы данных e-diary.

## Как пользоваться
1. Запустите [e-diary](https://github.com/Nebulawalker/e-diary)
(подробная инструкция прилагается)
2. Запустите Django shell:
```bash
python manage.py shell
```
3. Скопируйте содержимое scripts.py в консоль Django shell.
4. Теперь Вам доступны следующие функции:
    - fix_marks('Фролов Иван') - исправляет все двойки и тройки ученика Фролов Иван на пятерки.
    - remove_chastisements('Фролов Иван') - удаляет все замечания ученика Фролов Иван.
    - create_commendation('Фролов Иван', 'Математика', 'Молодец!') - добавит похвалу "Молодец!" (есть значение по умолчанию - "Хвалю!"), по предмету "Математика" к последнему уроку.
    
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
