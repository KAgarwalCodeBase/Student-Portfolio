from django.shortcuts import render

from rest_framework import generics
from .models import Student
from .serializers import *
import requests

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotAllowed


# StudentSerializer, StudentByBnumberSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# views.py

class StudentByBnumberAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentByBnumberSerializer
    lookup_field = 'bnumber'

class StudentByEmailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentByEmailSerializer
    lookup_field = 'email'

class StudentByMajorAPIView(generics.ListAPIView):
    serializer_class = StudentByMajorSerializer

    def get_queryset(self):
        major = self.kwargs['major']
        return Student.objects.filter(major=major)


class StudentDetailByBnumberAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'bnumber'


def my_view(request, bnumber):
    url = f"http://127.0.0.1:8000/students/bnumber/{bnumber}"
    
    # Make a GET request to the API endpoint
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract student data from the response
        student_data = response.json()
        # Pass the student data to the template context
        context = {'student': student_data}
    else:
        # If request was not successful, handle the error
        context = {'error_message': 'Failed to fetch student data'}

    # Render the template with the provided context
    return render(request, 'student_template.html', context)


from django.http import JsonResponse

# def send_email_view(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         recipient_email = request.POST.get('recipient_email')

#         # Send email
#         try:
#             send_mail(
#                 subject,
#                 f"Name: {name}\nEmail: {email}\nMessage: {message}",
#                 email,  # From email address
#                 [recipient_email],  # To email address
#                 fail_silently=False,
#             )
#             # Return a success response
#             return JsonResponse({'message': 'Email sent successfully!'})
#         except Exception as e:
#             # Return an error response
#             return JsonResponse({'message': f'Error sending email: {e}'}, status=500)
#     else:
#         return HttpResponseNotAllowed(['POST'])
from django.http import JsonResponse

def send_email_view(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_email = request.POST.get('recipient_email')

        # Send email
        try:
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,  # From email address
                [recipient_email],  # To email address
                fail_silently=False,
            )
            # Return a success response
            return JsonResponse({'message': 'Email sent successfully!'})
        except Exception as e:
            # Return an error response
            return JsonResponse({'message': f'Error sending email: {e}'}, status=500)
    else:
        return HttpResponseNotAllowed(['POST'])