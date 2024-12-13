from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from tasks.tasks import hello


class HomeViewSet(ViewSet):
    def create(self, request):
        task_result = hello.apply_async()

        return Response(
            {
                "success": True,
                "message": "Task has been queued successfully.",
                "task_id": task_result.id
            },
            status=status.HTTP_202_ACCEPTED
        )
