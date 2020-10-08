from django.http.response import JsonResponse
from rest_framework import status
from django.http import HttpResponse
from generator.addName import gen_certificate
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import api_view
import pandas as pd


@api_view(['GET'])
def certificate(request, email):
    try:
        details = pd.read_csv('participant_list.csv')
        if email not in details['email'].values:
            return JsonResponse({'message': 'The participant does not exist'}, status=status.HTTP_404_NOT_FOUND)
        name = details.loc[details['email'] == email]['name'].values[0]

    except BaseException as e:
        print(f"{e}")

    if request.method == 'GET':
        gen_certificate(name)
        fs = FileSystemStorage()
        with fs.open('certificate.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
        return response
