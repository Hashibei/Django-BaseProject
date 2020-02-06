from django.views.generic import TemplateView
from django.shortcuts import render
from account.forms import ProfileEditForm


class RegisterView(TemplateView):
    template_name = 'account/register.html'

    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        args = {
            'title': f"{request.user}'s account profile",
            'user': request.user
        }
        return render(request, self.template_name, args)


class ProfileEditView(TemplateView):
    template_name = 'account/profile_edit.html'

    def post(self, request, *args):
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, self.template_name, args)

    def get(self, request, *args, **kwargs):
        args = {
            "form": ProfileEditForm(instance=request.user)
        }
        return render(request, self.template_name, args)
