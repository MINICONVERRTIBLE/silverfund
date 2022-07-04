from django.shortcuts import render
from main.models import funds1, funds2, funds3, funds4, funds5, funds6, funds7, funds8
import pandas as pd
# 1.퇴직해외채권 2.퇴직해외주식 3.퇴직국내채권 4.퇴직국내주식 5.연금해외채권 6.연금해외주식 7.연금국내채권 8.연금국내주식


def survey(request):
    return render(request, 'survey.html')


def result1(request):
    qs1 = funds4.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(2)
    qs2 = funds3.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(6)
    qs3 = funds1.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3])
    context = {'df' : data.to_html()}

    return render(request, 'result1.html', context)



def result2(request):
    qs1 = funds4.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs2 = funds3.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(4)
    qs3 = funds1.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(3)
    data = pd.concat([data1,data2,data3])
    context = {'df' : data.to_html()}

    return render(request, 'result2.html', context)


def result3(request):
    qs1 = funds4.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs4 = funds2.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(2)
    qs2 = funds3.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(3)
    qs3 = funds1.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}

    return render(request, 'result3.html', context)


def result4(request):
    qs1 = funds4.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs4 = funds2.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(3)
    qs2 = funds3.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(2)
    qs3 = funds1.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}
    

    return render(request, 'result4.html', context)


def result5(request):
    qs1 = funds4.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(4)
    qs4 = funds2.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(4)
    qs2 = funds3.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(1)
    qs3 = funds1.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(1)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}

    return render(request, 'result5.html', context)


def result6(request):
    qs1 = funds8.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(2)
    qs2 = funds7.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(6)
    qs3 = funds5.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3])
    context = {'df' : data.to_html()}

    return render(request, 'result6.html', context)


def result7(request):
    qs1 = funds8.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs2 = funds7.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(4)
    qs3 = funds5.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(3)
    data = pd.concat([data1,data2,data3])
    context = {'df' : data.to_html()}

    return render(request, 'result7.html', context)


def result8(request):
    qs1 = funds8.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs4 = funds6.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(2)
    qs2 = funds7.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(3)
    qs3 = funds5.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}

    return render(request, 'result8.html', context)


def result9(request):
    qs1 = funds8.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(3)
    qs4 = funds6.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(3)
    qs2 = funds7.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(2)
    qs3 = funds5.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(2)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}

    return render(request, 'result9.html', context)


def result10(request):
    qs1 = funds8.objects.all().values()
    data1 = pd.DataFrame(qs1).sort_values('이익1년').head(4)
    qs4 = funds6.objects.all().values()
    data4 = pd.DataFrame(qs4).sort_values('이익1년').head(4)
    qs2 = funds7.objects.all().values()
    data2 = pd.DataFrame(qs2).sort_values('이익1년').head(1)
    qs3 = funds5.objects.all().values()
    data3 = pd.DataFrame(qs3).sort_values('이익1년').head(1)
    data = pd.concat([data1,data2,data3,data4])
    context = {'df' : data.to_html()}

    return render(request, 'result10.html', context)