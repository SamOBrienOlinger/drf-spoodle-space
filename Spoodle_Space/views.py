from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({"Welcome to Spoodle Space! Our community of Cockapoopers is all about sharing ways of enjoying long ludicrous lives with the lovliest furry fluffy fellas on Earth"})
