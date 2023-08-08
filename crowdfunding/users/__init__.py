# # crowdfunding/users/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=15, required=False)

#     AVAILABILITY_CHOICES = (
#         ('available', 'Available'),
#         ('not_available', 'Not Available'),
#         ('busy', 'Busy'),
#         ('away', 'Away'),
#         # Add more choices as needed
#     )
#     availability = forms.ChoiceField(choices=AVAILABILITY_CHOICES)

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('phone_number', 'availability')
