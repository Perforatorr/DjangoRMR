from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from WebARM.models import Machine,User
from django.http import JsonResponse
import json



class MachineCreateView(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body)
            if not isinstance(data, list):
                return JsonResponse(
                    {"error": "Expected a list of machines"},
                    status=400
                )
            created_id = []
            created_count = 0

            for item in data:
                condition_id = item.get('condition', 0)
                machine = Machine(
                        id=item['id'],
                        name=item['name'],
                        condition_id=condition_id
                    )
                    
                    # Сохраняем
                machine.save()
                created_id.append(item['id'])
                created_count += 1
            
            return JsonResponse({
                "message": "Machines created successfully",
                "created_count": created_count,
                "created_id": created_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        

class MachineDeleteView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if not isinstance(data, list):
                return JsonResponse(
                    {"error": "Expected a list of machines"},
                    status=400
                )
            deleted_id = []
            deleted_count = 0

            for item in data:
                
                machine = Machine.objects.get(id=item['id'])
                machine.delete()
                deleted_id.append(item['id'])
                deleted_count += 1
            
            return JsonResponse({
                "message": "Machines deleted successfully",
                "deleted_count": deleted_count,
                "deleted_id": deleted_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)


class UserCreatView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if not isinstance(data, list):
                return JsonResponse(
                    {"error": "Expected a list of users"},
                    status=400
                )
            created_id = []
            created_count = 0

            for item in data:
                user = User(
                        rfid=item['rfid'],
                        name=item['name'],
                        password = item['password'],
                        role = item['role']
                    )
                    
                    # Сохраняем
                user.save()
                created_id.append(item['rfid'])
                created_count += 1
            
            return JsonResponse({
                "message": "Users created successfully",
                "created_count": created_count,
                "created_rfid": created_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

class UserDeletedView(APIView):
    def post(self,request):
        try:
            data = json.loads(request.body)
            if not isinstance(data, list):
                return JsonResponse(
                    {"error": "Expected a list of machines"},
                    status=400
                )
            deleted_id = []
            deleted_count = 0

            for item in data:
                
                machine = User.objects.get(id=item['rfid'])
                machine.delete()
                deleted_id.append(item['rfid'])
                deleted_count += 1
            
            return JsonResponse({
                "message": "Users deleted successfully",
                "deleted_count": deleted_count,
                "deleted_rfid": deleted_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)