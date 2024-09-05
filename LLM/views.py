from django.shortcuts import render, redirect
from django.views import View
from . forms import RecipeForm
from . langchain import MyAi


class Home(View):
    def get(self, request):
        ai = request.session.get('ai', '')
        form = RecipeForm()
        return render(request, 'LLM/home.html', {'form': form, 'ai': ai})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            my_message = form.cleaned_data['my_message']
            ai_res = MyAi(my_message)
            request.session['ai_recipe'] = ai_res
        form = RecipeForm()
        return redirect('/')
