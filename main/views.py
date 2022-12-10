from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class ConditionPageView(TemplateView):
    template_name = "condition.html"

class RegistrationPageView(TemplateView):
    template_name = "registration.html"

class RegimePageView(TemplateView):
    template_name = "regime.html"
