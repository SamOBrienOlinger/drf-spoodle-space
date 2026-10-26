from django.db import IntegrityError, transaction
from rest_framework.exceptions import ValidationError


class OneDogRecordMixin:
    """Translate an existing owner's one-to-one record into an actionable 400."""
    def create(self, request, *args, **kwargs):
        model = self.get_serializer_class().Meta.model
        if model.objects.filter(owner=request.user).exists():
            raise ValidationError({'non_field_errors': ['You already have this dog record. Open My dog to edit it.']})
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        model = serializer.Meta.model
        if model.objects.filter(owner=self.request.user).exists():
            raise ValidationError({'non_field_errors': ['You already have this dog record. Open My dog to edit it.']})
        try:
            with transaction.atomic():
                serializer.save(owner=self.request.user)
        except IntegrityError:
            if model.objects.filter(owner=self.request.user).exists():
                raise ValidationError({'non_field_errors': ['You already have this dog record. Open My dog to edit it.']})
            raise
