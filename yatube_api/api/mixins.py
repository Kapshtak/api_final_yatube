from rest_framework import viewsets, status
from rest_framework.response import Response


class CRUD_mixin(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response(
                {
                    "detail": "У вас недостаточно прав "
                    + "для выполнения данного действия."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response(
                {
                    "detail": "У вас недостаточно прав "
                    + "для выполнения данного действия."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        elif self.request.user != self.get_object().author:
            return Response(
                {
                    "detail": "У вас недостаточно прав "
                    + "для выполнения данного действия."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response(
                {
                    "detail": "У вас недостаточно прав "
                    + "для выполнения данного действия."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        elif self.request.user != self.get_object().author:
            return Response(
                {
                    "detail": "У вас недостаточно прав "
                    + "для выполнения данного действия."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)
