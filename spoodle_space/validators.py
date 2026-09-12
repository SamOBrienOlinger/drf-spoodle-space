"""Username character policy shared with django-allauth.

An explicit empty list removes Django's letters/digits/@/./+/-/_ whitelist.
Registration and account serializers still require a non-blank, unique
username within the existing 150-character database field.
"""

username_validators = []
