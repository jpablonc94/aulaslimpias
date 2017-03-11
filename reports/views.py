#coding=utf-8
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from reports.models import Report
from reports.forms import ReportForm

class HomeView(View):

    def get(self, request):
        """
        Esta función devuelve el home de la página
        :param request:
        :return:
        """
        reports = len(Report.objects.all())

        context = {
            'reports_number': reports
        }

        return render(request, 'reports/home.html', context)


class CreateView(View):
    """Muesta un formulario para crear una denuncia y la crea
        si la petición es post"""
    def get(self, request):
        success_message = ''
        form = ReportForm()
        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'reports/new_report.html', context)

    def post(self, request):
        success_message = ''
        report = Report()
        report.school = request.POST.get('centro', '')
        report.name = request.POST.get('name', '')
        report.level = request.POST.get('level', '')
        report.email = request.POST.get('email', '')
        report.description = request.POST.get('description', '')
        report.save()
        """
        if form.is_valid():
            form = ReportForm()
            success_message = u'¡Guardado con éxito!'

            context = {
                'form': form,
                'success_message': success_message
            }
        """
        url = request.GET.get('next', 'home')
        return redirect(url)