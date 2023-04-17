# from users.models import CustomUser
# from django.db import transaction

# from django.contrib.auth.forms import UserCreationForm
# class EmployeeSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
    
#     @transaction.atomic
#     def save(self):
#         user=super().save(commit=False)
#         user.is_employer=False
#         user.save()
#         employee=Employee.objects.create(user=user)
#         return user