from django.conf import settings
from django.db import connection
from django.db.utils import OperationalError
from redis import Redis
from redis.exceptions import RedisError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        services = {
            "database": "ok",
            "redis": "ok",
        }

        status_code = 200

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
        except OperationalError:
            services["database"] = "unavailable"
            status_code = 503

        try:
            redis_client = Redis.from_url(
                settings.REDIS_URL,
                socket_connect_timeout=2,
                socket_timeout=2,
            )
            redis_client.ping()
        except RedisError:
            services["redis"] = "unavailable"
            status_code = 503

        overall_status = (
            "ok"
            if status_code == 200
            else "degraded"
        )

        return Response(
            {
                "status": overall_status,
                "services": services,
            },
            status=status_code,
        )
