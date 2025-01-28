from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.template import loader
from .models import Money
from .models import Result

def index(request):
    moneys = Money.objects.all()
    template = loader.get_template("money/index.html")
    context = {"money_list": moneys}
    return HttpResponse(template.render(context, request))

def create(request):
    money_text = request.POST["text"]
    day_text = request.POST["day"]
    purpose_text = request.POST["purpose"]
    m = Money()
    m.money_text = money_text
    m.day_text = day_text
    m.purpose_text = purpose_text
    m.save()
    for i in range(int(day_text)):
        r = Result()
        r.money = m
        r.age_text=i+1
        r.save()
    return HttpResponseRedirect(reverse("money:index"))

def delete(request, money_id):
    target_money = Money.objects.get(id=money_id)
    target_money.delete()

    return HttpResponseRedirect(reverse("money:index"))

def result(request, money_id):
    template = loader.get_template("money/result.html")
    target_money = Money.objects.get(id=money_id)
    result_list = Result.objects.filter(money_id=target_money.id)
    

    context = {"result_list": result_list}
    return HttpResponse(template.render(context, request))