from django.shortcuts import render_to_response
from django.template.context import RequestContext
import reporting

def report_list(request):
    reports = reporting.all_reports()
    ret = []
    for it in reports:
        ret.append({
            'slug': it[0],
            'name': it[1].verbose_name
        })
    return render_to_response('reporting/list.html', {'reports': ret},
                              context_instance=RequestContext(request))

def view_report(request, slug):
    report = reporting.get_report(slug)(request)
    data = {'report': report, 'title':report.verbose_name}
    return render_to_response('reporting/view.html', data, 
                              context_instance=RequestContext(request))