from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import TicketCart
from .serializers import TicketCartSerializer
from .helpers import TicketCartHelper


# Create your views here.
class TicketCartViewSet(viewsets.ModelViewSet):
    queryset = TicketCart.objects.all().order_by('id')
    serializer_class = TicketCartSerializer
    # permission_classes = (IsAuthenticated,)


    @action(methods='GET', detail=False, url_path='checkout/', url_name='checkout')
    def checkout(self, request, *args, **kwargs):

        try:
            user = self.request.user

            if user:
                cart_helper = TicketCartHelper
                checkout_details = TicketCartHelper.prepare_cart_for_checkout()

                if not checkout_details:
                    return Response(
                        status=status.HTTP_404_NOT_FOUND,
                        data={'Error': 'Oops! Your have not selected any event tickets'}
                    )
                return Response(
                    status=status.HTTP_200_OK,
                    data={'Checkout Details': checkout_details}
                )
        except Exception as e:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'Error': str(e)}
            )
