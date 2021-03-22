from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@csrf_exempt
def TasksView(request):
    if request.method == 'GET':
        tasks = Task.objects.order_by("-id").all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    else:
        return JsonResponse({}, status=405)

@csrf_exempt
def TaskView(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({}, status=204)
    else:
        return JsonResponse({}, status=405)
