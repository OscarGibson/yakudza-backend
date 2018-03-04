from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from unidecode import unidecode

from xhtml2pdf import pisa

from io import StringIO


# def fetch_pdf_resources(uri, rel):
#     if uri.find(settings.MEDIA_URL) != -1:
#         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
#     elif uri.find(settings.STATIC_URL) != -1:
#         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
#     else:
#         path = None
#     return path


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()

	# result = StringIO()
	encoded = html.encode("utf-8")
	pdf = pisa.pisaDocument(BytesIO(encoded), result, encoding= "utf-8")
	# pdf = pisa.CreatePDF(encoded, result, encoding='UTF-8', show_error_as_pdf=True)

	# print(html.encode().decode("utf-8"))
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None