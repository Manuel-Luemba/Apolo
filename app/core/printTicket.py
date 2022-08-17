from config import settings
from config.wsgi import *
from weasyprint import HTML, CSS

from django.template.loader import get_template


def printTicket():
   template = get_template("ticket.html")
   context = {"name": "Manuel Matoso Pedro Luemba"}
   html_template = template.render(context)

   css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.4.1-dist/css/bootstrap.min.css')
   print(css_url)

   HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])

printTicket()