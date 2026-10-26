"""Keep DRF field errors compatible with clients and service failures readable."""
import logging
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def community_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        logger.exception('API request failed', exc_info=exc)
        return Response({'detail': 'The service is temporarily unavailable. Please try again.'}, status=500)
    if isinstance(response.data, list):
        response.data = {'non_field_errors': response.data}
    request = context.get('request')
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)) and request and '/login/' not in request.path:
        response.data = {'detail': 'Please sign in again to continue. Your changes have not been saved.'}
    return response
