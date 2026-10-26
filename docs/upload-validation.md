# Community upload and error contract

Posts, member photos and dog photos accept JPEG, PNG, WebP and GIF images up to 2 MiB (shown as “2 MB” in the interface), and up to 4096 pixels on either side. Image content is decoded and checked; the filename or MIME header alone does not establish validity. The frontend post composer prepares oversized JPEG/PNG photos before upload; the API still enforces every limit.

A new post can omit `image`. An edit can send an empty multipart `image` to remove it. Migration `posts.0002_optional_post_photo` removes the automatic stock image for new text-only posts. Existing uploads and older default images are retained. Run `python manage.py migrate` with the backend release before releasing the new frontend.

Validation responses retain DRF field arrays, such as `{"image": ["This image is larger than 2 MB. Choose a smaller image."]}`. Cross-field errors use `non_field_errors`; authentication, permission, missing-resource and server errors use `detail` with the original HTTP status. Unexpected API exceptions return a generic JSON 500 and are logged server-side. Expired authentication does not imply that a mutation succeeded.

The one-dog-per-account model remains unchanged. Duplicate records produce actionable 400 responses, including concurrent creation protected by the existing one-to-one database constraint. Profile-to-dog links resolve through the owner relationship instead of assuming user and profile primary keys match. No record visibility or privacy policy changes are included.

## Verification

Run `python manage.py test --settings=spoodle_space.test_settings` and `python manage.py makemigrations --check --dry-run --settings=spoodle_space.test_settings`. By default, tests use an in-memory SQLite database and temporary local media. Set `TEST_DATABASE_URL` only to a dedicated test database to run against PostgreSQL, as CI does. Test settings never inherit the application's `DATABASE_URL` for test connections.

Regression coverage includes the image boundary, invalid content, optional photos, removal, cross-endpoint validation, duplicate dog records, mismatched user/profile IDs, permissions, missing records and cookie authentication. Legacy post tests now sign in through the application's actual cookie endpoint, and invalid placeholder test modules have been repaired so full discovery works.
