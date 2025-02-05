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
        r.age_text = i + 1
        r.age_nam = 0
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
    all_nam = 0
    for result in result_list:
        all_nam = all_nam + result.age_nam

    all_active = 0
    for result in result_list:
        if result.active_text:
            all_active = all_active + 1

    all_active = all_active / len(result_list) * 100
    all_active = round(all_active, 2)
    context = {"result_list": result_list, "result_nam": all_nam, "result_active": all_active}
    return HttpResponse(template.render(context, request))


def update(request, result_id):
    target_result = Result.objects.get(id=result_id)
    money_id = target_result.money.id
    money_limit = target_result.money.money_text
    target_result.age_nam = request.POST.get("amount", "").replace(",", "")
    target_result.age_nam = int(target_result.age_nam) if target_result.age_nam.isdigit() else 0
    if target_result.age_nam > int(money_limit):
        target_result.active_text = False
    else:
        target_result.active_text = True
    target_result.save()
    return HttpResponseRedirect(reverse("money:result", args=(money_id,)))
