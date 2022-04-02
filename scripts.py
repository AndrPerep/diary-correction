def get_schoolkid():  # ввести и сохранить имя ученика
	from datacenter.models import Schoolkid
	name = input('Введите фамилию и имя:')
	try:
		schoolkid = Schoolkid.objects.get(full_name__contains=name)
		print(schoolkid)
		return schoolkid
	except Schoolkid.MultipleObjectsReturned:
		print(f'Найдено несколько учеников. Уточните данные')
	except Schoolkid.DoesNotExist:
		print(f'Ничего не найдено. Проверьте правильность ввода')


def fix_marks(schoolkid):  # исправить все плохие оценки на пятёрки
	from datacenter.models import Mark
	bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
	for bad_mark in bad_marks:
		bad_mark.points = 5
		bad_mark.save()


def remove_chastisements(schoolkid):  # удалить все замечания
	from datacenter.models import Chastisement
	chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
	chastisements.delete()


def create_commendation(schoolkid):  # создать похвалу для последнего урока по выбранному предмету
	import random
	from datacenter.models import Lesson
	from datacenter.models import Commendation
	commendation_examples = [
		'Молодец!',
		'Отлично!',
		'Хорошо!',
		'Гораздо лучше, чем я ожидал!',
		'Ты меня приятно удивил!',
		'Великолепно!',
		'Прекрасно!',
		'Ты меня очень обрадовал!',
		'Именно этого я давно ждал от тебя!',
		'Сказано здорово – просто и ясно!',
		'Ты, как всегда, точен!',
		'Очень хороший ответ!',
		'Талантливо!',
		'Ты сегодня прыгнул выше головы!',
		'Я поражен!',
		'Уже существенно лучше!',
		'Потрясающе!',
		'Замечательно!',
		'Прекрасное начало!',
		'Так держать!',
		'Ты на верном пути!',
		'Здорово!',
		'Это как раз то, что нужно!',
		'Я тобой горжусь!',
		'С каждым разом у тебя получается всё лучше!',
		'Мы с тобой не зря поработали!',
		'Я вижу, как ты стараешься!',
		'Ты растешь над собой!',
		'Ты многое сделал, я это вижу!',
		'Теперь у тебя точно все получится!'
	]
	subject = input('Введите предмет: ')
	try:
		lesson = Lesson.objects.filter(
			subject__title=subject,
			year_of_study=schoolkid.year_of_study,
			group_letter=schoolkid.group_letter
		).order_by('-date').first()
	except AttributeError:
		print('Предмет не найден. Проверьте правильность ввода. Пример: математика')
	else:
		Commendation.objects.create(
			text=random.choice(commendation_examples),
			created=lesson.date,
			schoolkid=schoolkid,
			subject=lesson.subject,
			teacher=lesson.teacher
		)
