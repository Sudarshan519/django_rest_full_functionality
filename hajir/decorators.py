from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import BasePermission

def employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_employee,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

class IsEmployee(BasePermission):
        def has_permission(self, request, view):
            return bool(request.user and request.user.is_employee)


class IsEmployer(BasePermission):
        def has_permission(self, request, view):
            return bool(request.user and request.user.is_employer)