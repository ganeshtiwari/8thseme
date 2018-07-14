import os
from imp import reload
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from keras import backend as K
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from keras.models import load_model
from .utility.get_result import main
from .serializers import AccelerometerSerializer


def set_keras_backend(backend):
    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        reload(K)


set_keras_backend("theano")

result = ''
label = ['downstair', 'jogging', 'sitting', 'standing', 'upstair', 'walking']
count = 0
model = load_model("sensor/model.h5")


class AccelerometerView(APIView):
    def post(self, request, format=None, *args, **kwargs):
        serializer = AccelerometerSerializer(data=request.data)
        # print(serializer.data)
        if serializer.is_valid():
            data = serializer.data
            # main_thread = threading.Thread(target=_main, args=[data['values']], daemon=True)
            # main_thread.start()
            print("\n\n")
            global count
            count += 1
            print(count)
            global result
            result = main(data['values'], model)
            print(result)
            print("\n\n")
            return Response({'a': count}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_result(request):
    if request.method == 'GET':
        return JsonResponse({'result': result}, safe=False)

