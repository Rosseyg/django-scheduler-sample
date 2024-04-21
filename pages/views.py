from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    # template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        
        # howitworkstext = open(os.path.join(settings.STATIC_ROOT, 'markdown/howitworks.md'), encoding='utf-8').read()
        # confidentialtext = open(os.path.join(settings.STATIC_ROOT, 'markdown/confidential.md'), encoding='utf-8').read()
        # abouttext = open(os.path.join(settings.STATIC_ROOT, 'markdown/about.md'), encoding='utf-8').read()
    
        context = super().get_context_data(**kwargs)
        # context['markdowntext'] = howitworkstext
        # context['confidentialtext'] = confidentialtext
        # context['abouttext'] = abouttext
        
        return context
