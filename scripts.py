from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        print(f'Ученик "{name}" не найден.')
        return None
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько записей, уточните имя')
        return None
    return schoolkid

def fix_marks(name):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    Mark.objects.filter(schoolkid=schoolkid).filter(points__in=[2, 3]).update(points=5)
    print(f'Все двойки и тройки ученика "{name}" исправлены на пятерки!')

def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
    print(f'Замечания ученика "{name}" удалены!')

def create_commendation(name, subject, commendation_text = 'Хвалю!'):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter, 
        subject__title__contains=subject
    ).order_by('date').last()
    if not lesson:
        print(f'Урок "{subject}" не найден')
        return None
    Commendation.objects.create(
        text=commendation_text, 
        subject=lesson.subject, 
        teacher=lesson.teacher, 
        schoolkid=schoolkid, 
        created=lesson.date
    )
    print(
        f'"{lesson.date}" по предмету "{lesson.subject.title}" для ученика "{name}" добавлена похвала "{commendation_text}"'
        )