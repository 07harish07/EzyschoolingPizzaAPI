from django.shortcuts import render

from .models import PizzaType, PizzaSize, PizzaTopping
from .serializers import PizzaTypeSerializer, PizzaSizeSerializer, PizzaToppingSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import response, status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def PizzaCreateView(request):
	data = request.data

	if data["pizza_type"] == 'Regular' or data["pizza_type"] == 'Square':
		serializer = PizzaTypeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response({'Response':'You can not create any other type of pizza except Regular and Square'})
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def PizzaListView(request):
	try:
		pizza = PizzaType.objects.all()
		serializer = PizzaTypeSerializer(pizza, many=True)
		return Response(serializer.data)
	except PizzaType.DoesNotExist:
		return Response({'Response':'Pizza Not exist'})

@api_view(['PUT'])
@csrf_exempt
def PizzaUpdateView(request, id):
	try:
		pizza = PizzaType.objects.get(id=id)
		serializer = PizzaTypeSerializer(instance=pizza, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	except PizzaType.DoesNotExist:
		return Response({'Response':'Pizza Not exist'})


@api_view(['DELETE'])
@csrf_exempt
def PizzaDeleteView(request, id):
	try:
		pizza = PizzaType.objects.get(id=id)
		pizza.delete()

		return Response('Item Successfully Deleted!')
	except PizzaType.DoesNotExist:
		return Response({'Response':'PizzaType Not exist'})

