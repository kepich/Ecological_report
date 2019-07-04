from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Report
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .forms import ReportForm
import pandas as pd

# Create your views here.
def index_page(request):
	return render(request, 'index_page/index.html')

def report_list(request):
	reports = Report.objects.all()
	df = pd.DataFrame(list(reports.values()))
	am = df['ph'].count()
	meanPH = df['ph'].mean()
	minimal = df['ph'].min()
	maximal = df['ph'].max()
	quant = df['ph'].quantile(.5)
	return render(request, 'report_list/report_list.html', context={'reports': reports, 'amount': am, 'mean': meanPH, 'min': minimal, 'max': maximal, 'quant': quant})

class ReportDetail(View):
	"""docstring for ReportDetail"""
	def get(self, request, slug):
		report_details = get_object_or_404(Report, slug__iexact=slug)
		return render(request, 'report_list/report_detail.html', context={'report_details': report_details})

class ReportCreate(View):
	def get(self, request):
		form = ReportForm()
		return render(request, 'create_report/create_report.html', context={'form':form})

	def post(self, request):
		report = ReportForm(request.POST)

		if report.is_valid():
			new_report = report.save()
			return redirect(new_report)
		else:
			return render(request, 'create_report/create_report.html', context={'form' : report})

class ReportUpdate(View):
	def get(self, request, slug):
		temp_report = Report.objects.get(slug__iexact=slug)
		bound_form = ReportForm(instance=temp_report)
		return render(request, 'update_report/update_report.html', context={'form': bound_form, 'report': temp_report})

	def post(self, request, slug):
		temp_report = Report.objects.get(slug__iexact=slug)
		bound_form = ReportForm(request.POST)

		if bound_form.is_valid():
			temp_report.delete()
			new_report = bound_form.save()
			return redirect(new_report)
		else:
			return render(request, 'update_report/update_report.html', context={'form' : bound_form, 'report': temp_report})

class ReportDelete(View):
	def get(self, request, slug):
		temp_report = Report.objects.get(slug__iexact=slug)
		return render(request, 'delete_report/delete_report.html', context={'report': temp_report})

	def post(self, request, slug):
		temp_report = Report.objects.get(slug__iexact=slug)
		temp_report.delete()
		return redirect(reverse('report_list'))
