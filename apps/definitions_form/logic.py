from . import serializers, models, validate
from rest_framework import status
from rest_framework.response import Response


def create_form(request):
    try:
        data = request.data
        form_name = {"name": data['name']}
        serializer_form = serializers.SerializerCreateForm(data=form_name)
        serializer_fields = serializers.SerializerCreateField(data=request.data)
        if serializer_form.is_valid():
            if validate.validate_date(data['date'])==True and validate.validate_phone(data['phone'])==True and validate.validate_email(data['email'])==True:
                if serializer_fields.is_valid():
                    model_form = models.MyForm.objects.create(name=data["name"])
                    model_form.save()
                    model_fields = models.Fields(
                        form=model_form,
                        phone=data['phone'],
                        email=data['email'],
                        text=data['text'],
                        date=data['date']
                    )
                    model_fields.save()
                    return Response({
                        'success': True,
                        'data': {
                            'form_name': request.data["name"],
                            'fileds': {
                                'email': request.data["email"],
                                'phone': request.data['phone'],
                                'text': request.data['text'],
                                'date': request.data['date']
                            }
                        }
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'success': False,
                    'status': "Incorrect data format",
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'success': False,
            }, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response({
            'success': False,
            'status': 'this form already exists or some data was not submitted'
        }, status=status.HTTP_400_BAD_REQUEST)


def get_form(request):
    data = request.data
    try:
        model_form = models.Fields.objects.filter(email=data['email'], phone=data['phone'])
        if model_form:
            list_form = []
            for i in model_form:
                list_form.append({
                    'name': i.form.name,
                    'date': i.date,
                    'text': i.text
                })
            return Response({
                'success': True,
                'forms': list_form,
                'email': data['email'],
                'phone': data['phone'],
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'email': data['email'],
                'phone': data['phone'],
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({
            'success': False,
        }, status=status.HTTP_400_BAD_REQUEST)


