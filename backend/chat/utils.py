from django.shortcuts import render, redirect
from . import models

import logging
# импортирум встроенный модуль логирования и дополняем его сообщениями
logger = logging.getLogger('django')


# описываем работу с созданием пользователей через вэб интерфейс
class CustomRegisterUser:
    modelForm = None
    modelPerson = None
    redirect_url = None
    template = None

    def get(self, request): # по гету просто передаем форму
        ctx = {}
        form = self.modelForm()
        ctx['form'] = form
        logger.info('GET: CustomRegisterUser')
        return render(request, self.template, ctx)

    def post(self, request):
        ctx = {}
        form = self.modelForm(request.POST) # в случае отправки пользователем заполненной формы получаем эти данные для их дальнейшей обработки
        ctx['form'] = form

        if form.is_valid(): # проверяем форму на соответсвие
            # извлекаем полученные данные из формы
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']

            # для того, что бы потом применить их к нашему кастомному методу создания пользователя
            obj = self.modelPerson.objects.create_user(
                login=login,
                password=password
            )
            obj.name = name
            obj.save()
            logger.info('POST: CustomRegisterUser')
            return redirect('/login/') # в случаем успешной валидации формы и создания модели пользователя, переводим юзера на страницу входа на сайт
        logger.warning('POST: CustomRegisterUser')
        return render(request, self.template, ctx) # если форма была не валидна возвращаем пользователя на страницу регистрации с данными его формы, для их корректировки


