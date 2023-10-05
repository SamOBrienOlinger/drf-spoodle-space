# Create, Read, Update and Delete Functionality Testing

Click **[here](README.md)** to return to the **README.md** file.

A series of manual tests were carried out across every app to verify the Create, Read, Update and Delete (CRUD) functionality. Below are the CRUD test cases.


## User Authentication Test Cases

### Test Case 1: User Authentication

**Test Case Description:**
This test case verifies user authentication by sending a POST request to the login endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User accounts exist for testing.
- Correct authentication credentials (username and password) are available for testing.

**Test Steps:**
1. Send a POST request to the login endpoint (`POST /dj-rest-auth/login/`) with valid user authentication credentials (username and password).
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes an authentication token (JWT token) indicating successful login.
4. Use the obtained token for subsequent requests to test authenticated endpoints.

**Expected Results:**
- User authentication should succeed, and an authentication token should be provided.
- The token should be used for authentication in subsequent requests.

**Test Data:**
- Valid user authentication credentials (username and password).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** User authentication succeeded, and an authentication token was obtained.

### Test Case 2: User Logout

**Test Case Description:**
This test case verifies user logout by sending a POST request to the logout endpoint.

**Preconditions:**
- A user is authenticated and has a valid JWT token.

**Test Steps:**
1. Send a POST request to the logout endpoint (`POST /dj-rest-auth/logout/`) with the authenticated JWT token.
2. Verify that the response status code is 200 (OK) or 204 (No Content).

**Expected Results:**
- User logout should succeed, and the JWT token should be invalidated.
- Subsequent requests using the invalidated token should fail.

**Test Data:**
- Authenticated JWT token.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** User logout succeeded, and the JWT token was invalidated.

### Test Case 3: User Authentication with Invalid Credentials

**Test Case Description:**
This test case verifies user authentication by sending a POST request to the login endpoint with invalid user authentication credentials.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User accounts exist for testing.
- Incorrect authentication credentials (e.g., incorrect username or password) are available for testing.

**Test Steps:**
1. Send a POST request to the login endpoint (`POST /dj-rest-auth/login/`) with invalid user authentication credentials (e.g., incorrect username or password).
2. Verify that the response status code is 401 (Unauthorized).
3. Verify that the response does not include an authentication token.
4. Ensure that the user remains unauthenticated.

**Expected Results:**
- User authentication should fail with invalid credentials.
- The response should indicate unauthorized access (401 status code).
- No authentication token should be provided.
- The user should remain unauthenticated.

**Test Data:**
- Invalid user authentication credentials (e.g., incorrect username or password).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** User authentication failed with invalid credentials as expected.

### Test Case 4: User Logout without Authentication

**Test Case Description:**
This test case verifies that a user cannot log out without authentication by sending a POST request to the logout endpoint without a valid JWT token.

**Preconditions:**
- No user is authenticated.

**Test Steps:**
1. Send a POST request to the logout endpoint (`POST /dj-rest-auth/logout/`) without including an authenticated JWT token.
2. Verify that the response status code is 401 (Unauthorized).

**Expected Results:**
- User logout should not be allowed without authentication.
- The response should indicate unauthorized access (401 status code).

**Test Data:**
- No authentication token provided.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** User logout without authentication is not allowed, and the response indicates unauthorized access.


## Comment Model CRUD Test Cases

### Test Case 1: Create Comment with Valid Data

**Test Case Description:**
This test case verifies the creation of a new comment by sending a POST request to the appropriate API endpoint with valid data.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create comments.

**Test Steps:**
1. Send a POST request to the comment creation endpoint (`POST /api/posts/{post_id}/comments/`) with valid data, including the post ID and comment content.
2. Verify that the response status code is 201 (Created).
3. Verify that the created comment exists in the database.
4. Verify that the comment is associated with the logged-in user.

**Expected Results:**
- A new comment should be created successfully.
- The response should include the created comment's data, including its ID, owner, content, and timestamps.
- The comment should be associated with the logged-in user.
- The comment should be retrievable from the database.

**Test Data:**
- Valid data for creating a comment (e.g., post ID, comment content).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The comment was successfully created, and all expected results were met.

### Test Case 2: Create Comment with Invalid Data

**Test Case Description:**
This test case verifies the behavior when creating a comment with invalid data by sending a POST request to the appropriate API endpoint with incomplete or missing data.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create comments.

**Test Steps:**
1. Send a POST request to the comment creation endpoint (`POST /api/posts/{post_id}/comments/`) with invalid data, such as missing comment content or an invalid post ID.
2. Verify that the response status code is 400 (Bad Request).
3. Ensure that no comment is created in the database.

**Expected Results:**
- Comment creation should fail with invalid data.
- The response should indicate a bad request (400 status code).
- No comment should be created in the database.

**Test Data:**
- Invalid data for creating a comment (e.g., missing comment content, invalid post ID).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** Comment creation failed with invalid data as expected.

### Test Case 3: Read Comment

**Test Case Description:**
This test case verifies the ability to retrieve an existing comment by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- An existing comment is available in the database.

**Test Steps:**
1. Send a GET request to the comment retrieval endpoint (`GET /api/comments/{comment_id}/`) with the ID of an existing comment.
2. Verify that the response status code is 200 (OK).
3. Verify that the retrieved comment data matches the expected data from the database.

**Expected Results:**
- The existing comment should be successfully retrieved.
- The response should include the comment's data, including its ID, owner, content, and timestamps.
- The retrieved comment data should match the expected data from the database.

**Test Data:**
- ID of an existing comment.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The existing comment was successfully retrieved, and the data matches the expected data.

### Test Case 4: Update Comment

**Test Case Description:**
This test case verifies the ability to update an existing comment by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- An existing comment is available in the database.

**Test Steps:**
1. Send a PUT request to the comment update endpoint (`PUT /api/comments/{comment_id}/`) with the ID of an existing comment and updated comment content.
2. Verify that the response status code is 200 (OK).
3. Verify that the updated comment content is reflected in the database.

**Expected Results:**
- The existing comment should be successfully updated with the new content.
- The response should include the updated comment's data, including its ID, owner, content, and timestamps.
- The updated comment content should be reflected in the database.

**Test Data:**
- ID of an existing comment.
- Updated comment content.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The existing comment was successfully updated with the new content, and the data matches the expected data.

### Test Case 5: Delete Comment

**Test Case Description:**
This test case verifies the ability to delete an existing comment by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- An existing comment is available in the database.

**Test Steps:**
1. Send a DELETE request to the comment deletion endpoint (`DELETE /api/comments/{comment_id}/`) with the ID of an existing comment.
2. Verify that the response status code is 204 (No Content).
3. Verify that the deleted comment no longer exists in the database.

**Expected Results:**
- The existing comment should be successfully deleted.
- The response status code should indicate success with no content returned.
- The deleted comment should no longer exist in the database.

**Test Data:**
- ID of an existing comment.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The existing comment was successfully deleted, and it no longer exists in the database.




## DogDanger Model CRUD Test Cases

### Test Case 1: Create DogDanger

**Test Case Description:**
This test case verifies the creation of a new `DogDanger` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `DogDanger` objects.

**Test Steps:**
1. Send a POST request to the `DogDanger` creation endpoint (`POST /api/dogdanger/`) with valid data.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `DogDanger` object exists in the database.
4. Verify that the `DogDanger` object is associated with the logged-in user.

**Expected Results:**
- A new `DogDanger` object should be created successfully.
- The response should include the created `DogDanger` object's data.
- The `DogDanger` object should be associated with the logged-in user.
- The `DogDanger` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `DogDanger` object (e.g., values for `bites_babies`, `bites_kids`, `bites_teenagers`, and `bites_burglars`).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogDanger` object was successfully created, and all expected results were met.

---
### Test Case 2: Create DogDanger with Invalid Data
**Test Case Description:** This test case verifies the behavior when creating a DogDanger object with invalid data by sending a POST request to the appropriate API endpoint with incomplete or missing data.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create DogDanger objects.

**Test Steps:**
1. Send a POST request to the DogDanger creation endpoint (POST /api/dogdanger/) with invalid data, such as negative values for bites_babies, non-numeric values for bites_kids, etc.
2. Verify that the response status code is 400 (Bad Request).
3. Verify that no DogDanger object is created in the database.

**Expected Results:**
- DogDanger object creation should fail with invalid data.
- The response should indicate a bad request (400 status code).
- No DogDanger object should be created in the database.

**Test Data:**
- Invalid data for creating a DogDanger object (e.g., negative values for bites_babies, non-numeric values for bites_kids, etc.).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- Outcome: The test has passed.
- Details: DogDanger object creation failed with invalid data as expected.

### Test Case 3: Read DogDanger

**Test Case Description:**
This test case verifies the retrieval of an existing `DogDanger` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `DogDanger` object exists in the database.

**Test Steps:**
1. Send a GET request to the `DogDanger` detail endpoint (`GET /api/dogdanger/{dogdanger_id}/`) with the ID of an existing `DogDanger` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `DogDanger` object.

**Expected Results:**
- The requested `DogDanger` object should be retrieved successfully.
- The response should include the `DogDanger` object's details.

**Test Data:**
- Existing `DogDanger` object ID.

**Test Environment:**
- Django development environment with `DogDanger` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogDanger` object was successfully retrieved, and all expected details were included in the response.

---
### Test Case 4: Update DogDanger

**Test Case Description:**
This test case verifies the update of an existing `DogDanger` object by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogDanger` object exists in the database.
- The logged-in user is the owner of the `DogDanger` object.

**Test Steps:**
1. Send a PUT request to the `DogDanger` detail endpoint (`PUT /api/dogdanger/{dogdanger_id}/`) with the ID of the existing `DogDanger` object and updated data.
2. Verify that the response status code is 200 (OK).
3. Retrieve the `DogDanger` object from the database and verify that its data has been updated.

**Expected Results:**
- The `DogDanger` object should be updated successfully.
- The response should include the updated `DogDanger` object's data.
- The `DogDanger` object's data in the database should be updated accordingly.

**Test Data:**
- Existing `DogDanger` object ID and updated data.

**Test Environment:**
- Django development environment with a `DogDanger` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogDanger` object was successfully updated, and all expected data updates were confirmed.

---

### Test Case 5: Delete DogDanger

**Test Case Description:**
This test case verifies the deletion of an existing `DogDanger` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogDanger` object exists in the database.
- The logged-in user is the owner of the `DogDanger` object.

**Test Steps:**
1. Send a DELETE request to the `DogDanger` detail endpoint (`DELETE /api/dogdanger/{dogdanger_id}/`) with the ID of the existing `DogDanger` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `DogDanger` object from the database and verify that it no longer exists.

**Expected Results:**
- The `DogDanger` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `DogDanger` object should no longer exist in the database.

**Test Data:**
- Existing `DogDanger` object ID.

**Test Environment:**
- Django development environment with a `DogDanger` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogDanger` object was successfully deleted, and it no longer exists in the database.



## DogHealth Model CRUD Test Cases

### Test Case 1: Create DogHealth with Valid Data

**Test Case Description:**
This test case verifies the creation of a new `DogHealth` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `DogHealth` objects.

**Test Steps:**
1. Send a POST request to the `DogHealth` creation endpoint (`POST /api/doghealth/`) with valid data.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `DogHealth` object exists in the database.
4. Verify that the `DogHealth` object is associated with the logged-in user.

**Expected Results:**
- A new `DogHealth` object should be created successfully.
- The response should include the created `DogHealth` object's data.
- The `DogHealth` object should be associated with the logged-in user.
- The `DogHealth` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `DogHealth` object (e.g., values for `vet_name`, `vet_phone`, `vet_email`, `kennel_cough`, `rabies`, and `allergies`).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogHealth` object was successfully created, and all expected results were met.

---

### Test Case 2: Create DogHealth with Invalid Data

**Test Case Description:**
This test case verifies the behavior when creating a `DogHealth` object with invalid data by sending a POST request to the appropriate API endpoint with incomplete or missing data.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `DogHealth` objects.

**Test Steps:**
1. Send a POST request to the `DogHealth` creation endpoint (`POST /api/doghealth/`) with invalid data, such as missing vet information or incomplete health records.
2. Verify that the response status code is 400 (Bad Request).
3. Ensure that no `DogHealth` object is created in the database.

**Expected Results:**
- `DogHealth` object creation should fail with invalid data.
- The response should indicate a bad request (400 status code).
- No `DogHealth` object should be created in the database.

**Test Data:**
- Invalid data for creating a `DogHealth` object (e.g., missing vet information, incomplete health records).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** `DogHealth` object creation failed with invalid data as expected.

---

### Test Case 3: Read DogHealth

**Test Case Description:**
This test case verifies the retrieval of an existing `DogHealth` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `DogHealth` object exists in the database.

**Test Steps:**
1. Send a GET request to the `DogHealth` detail endpoint (`GET /api/doghealth/{doghealth_id}/`) with the ID of an existing `DogHealth` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `DogHealth` object.

**Expected Results:**
- The requested `DogHealth` object should be retrieved successfully.
- The response should include the `DogHealth` object's details.

**Test Data:**
- Existing `DogHealth` object ID.

**Test Environment:**
- Django development environment with `DogHealth` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogHealth` object was successfully retrieved, and all expected details were included in the response.

---

### Test Case 4: Update DogHealth

**Test Case Description:**
This test case verifies the update of an existing `DogHealth` object by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogHealth` object exists in the database.
- The logged-in user is the owner of the `DogHealth` object.

**Test Steps:**
1. Send a PUT request to the `DogHealth` detail endpoint (`PUT /api/doghealth/{doghealth_id}/`) with the ID of the existing `DogHealth` object and updated data.
2. Verify that the response status code is 200 (OK).
3. Retrieve the `DogHealth` object from the database and verify that its data has been updated.

**Expected Results:**
- The `DogHealth` object should be updated successfully.
- The response should include the updated `DogHealth` object's data.
- The `DogHealth` object's data in the database should be updated accordingly.

**Test Data:**
- Existing `DogHealth` object ID and updated data.

**Test Environment:**
- Django development environment with a `DogHealth` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogHealth` object was successfully updated, and all expected data updates were confirmed.

---

### Test Case 5: Delete DogHealth

**Test Case Description:**
This test case verifies the deletion of an existing `DogHealth` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogHealth` object exists in the database.
- The logged-in user is the owner of the `DogHealth` object.

**Test Steps:**
1. Send a DELETE request to the `DogHealth` detail endpoint (`DELETE /api/doghealth/{doghealth_id}/`) with the ID of the existing `DogHealth` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `DogHealth` object from the database and verify that it no longer exists.

**Expected Results:**
- The `DogHealth` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `DogHealth` object should no longer exist in the database.

**Test Data:**
- Existing `DogHealth` object ID.

**Test Environment:**
- Django development environment with a `DogHealth` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogHealth` object was successfully deleted, and it no longer exists in the database.


## DogProfile Model CRUD Test Cases

### Test Case 1: Create DogProfile

**Test Case Description:**
This test case verifies the creation of a new `DogProfile` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `DogProfile` objects.

**Test Steps:**
1. Send a POST request to the `DogProfile` creation endpoint (`POST /api/dogprofile/`) with valid data.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `DogProfile` object exists in the database.
4. Verify that the `DogProfile` object is associated with the logged-in user.

**Expected Results:**
- A new `DogProfile` object should be created successfully.
- The response should include the created `DogProfile` object's data.
- The `DogProfile` object should be associated with the logged-in user.
- The `DogProfile` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `DogProfile` object (e.g., values for `dog_name`, `dog_age`, `dog_color`, `dog_bio`, and `dog_profile_image`).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogProfile` object was successfully created, and all expected results were met.

---

### Test Case 2: Read DogProfile

**Test Case Description:**
This test case verifies the retrieval of an existing `DogProfile` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `DogProfile` object exists in the database.

**Test Steps:**
1. Send a GET request to the `DogProfile` detail endpoint (`GET /api/dogprofile/{dogprofile_id}/`) with the ID of an existing `DogProfile` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `DogProfile` object.

**Expected Results:**
- The requested `DogProfile` object should be retrieved successfully.
- The response should include the `DogProfile` object's details.

**Test Data:**
- Existing `DogProfile` object ID.

**Test Environment:**
- Django development environment with `DogProfile` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogProfile` object was successfully retrieved, and all expected details were included in the response.

---

### Test Case 3: Update DogProfile

**Test Case Description:**
This test case verifies the update of an existing `DogProfile` object by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogProfile` object exists in the database.
- The logged-in user is the owner of the `DogProfile` object.

**Test Steps:**
1. Send a PUT request to the `DogProfile` detail endpoint (`PUT /api/dogprofile/{dogprofile_id}/`) with the ID of the existing `DogProfile` object and updated data.
2. Verify that the response status code is 200 (OK).
3. Retrieve the `DogProfile` object from the database and verify that its data has been updated.

**Expected Results:**
- The `DogProfile` object should be updated successfully.
- The response should include the updated `DogProfile` object's data.
- The `DogProfile` object's data in the database should be updated accordingly.

**Test Data:**
- Existing `DogProfile` object ID and updated data.

**Test Environment:**
- Django development environment with a `DogProfile` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogProfile` object was successfully updated, and all expected data updates were confirmed.

---

### Test Case 4: Delete DogProfile

**Test Case Description:**
This test case verifies the deletion of an existing `DogProfile` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `DogProfile` object exists in the database.
- The logged-in user is the owner of the `DogProfile` object.

**Test Steps:**
1. Send a DELETE request to the `DogProfile` detail endpoint (`DELETE /api/dogprofile/{dogprofile_id}/`) with the ID of the existing `DogProfile` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `DogProfile` object from the database and verify that it no longer exists.

**Expected Results:**
- The `DogProfile` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `DogProfile` object should no longer exist in the database.

**Test Data:**
- Existing `DogProfile` object ID.

**Test Environment:**
- Django development environment with a `DogProfile` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `DogProfile` object was successfully deleted, and it no longer exists in the database.
 

## Follower Model CRUD Test Cases

### Test Case 1: Create Follower

**Test Case Description:**
This test case verifies the creation of a new `Follower` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `Follower` objects.
- There is another user to follow (the 'followed' user).

**Test Steps:**
1. Send a POST request to the `Follower` creation endpoint (`POST /api/followers/`) with valid data, including the ID of the user to follow.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `Follower` object exists in the database.
4. Verify that the `Follower` object is associated with the logged-in user as the 'owner' and the selected user as the 'followed'.

**Expected Results:**
- A new `Follower` object should be created successfully.
- The response should include the created `Follower` object's data.
- The `Follower` object should be associated with the logged-in user as the 'owner' and the selected user as the 'followed'.
- The `Follower` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `Follower` object (e.g., user ID of the user to follow).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Follower` object was successfully created, and all expected results were met.

---

### Test Case 2: Read Follower

**Test Case Description:**
This test case verifies the retrieval of an existing `Follower` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `Follower` object exists in the database.

**Test Steps:**
1. Send a GET request to the `Follower` detail endpoint (`GET /api/followers/{follower_id}/`) with the ID of an existing `Follower` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `Follower` object.

**Expected Results:**
- The requested `Follower` object should be retrieved successfully.
- The response should include the `Follower` object's details.

**Test Data:**
- Existing `Follower` object ID.

**Test Environment:**
- Django development environment with `Follower` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Follower` object was successfully retrieved, and all expected details were included in the response.

---

### Test Case 3: Delete Follower

**Test Case Description:**
This test case verifies the deletion of an existing `Follower` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `Follower` object exists in the database.
- The logged-in user is the owner of the `Follower` object.

**Test Steps:**
1. Send a DELETE request to the `Follower` detail endpoint (`DELETE /api/followers/{follower_id}/`) with the ID of the existing `Follower` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `Follower` object from the database and verify that it no longer exists.

**Expected Results:**
- The `Follower` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `Follower` object should no longer exist in the database.

**Test Data:**
- Existing `Follower` object ID.

**Test Environment:**
- Django development environment with a `Follower` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Follower` object was successfully deleted, and it no longer exists in the database.
---

## Like Model CRUD Test Cases

### Test Case 1: Create Like

**Test Case Description:**
This test case verifies the creation of a new `Like` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `Like` objects.
- There is an existing `Post` to be liked.

**Test Steps:**
1. Send a POST request to the `Like` creation endpoint (`POST /api/likes/`) with valid data, including the ID of the `Post` to be liked.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `Like` object exists in the database.
4. Verify that the `Like` object is associated with the logged-in user as the 'owner' and the selected `Post`.

**Expected Results:**
- A new `Like` object should be created successfully.
- The response should include the created `Like` object's data.
- The `Like` object should be associated with the logged-in user as the 'owner' and the selected `Post`.
- The `Like` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `Like` object (e.g., user ID of the 'owner' and `Post` ID to like).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Like` object was successfully created, and all expected results were met.

---

### Test Case 2: Read Like

**Test Case Description:**
This test case verifies the retrieval of an existing `Like` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `Like` object exists in the database.

**Test Steps:**
1. Send a GET request to the `Like` detail endpoint (`GET /api/likes/{like_id}/`) with the ID of an existing `Like` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `Like` object.

**Expected Results:**
- The requested `Like` object should be retrieved successfully.
- The response should include the `Like` object's details.

**Test Data:**
- Existing `Like` object ID.

**Test Environment:**
- Django development environment with `Like` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Like` object was successfully retrieved, and all expected details were included in the response.

---

### Test Case 3: Delete Like

**Test Case Description:**
This test case verifies the deletion of an existing `Like` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `Like` object exists in the database.
- The logged-in user is the owner of the `Like` object.

**Test Steps:**
1. Send a DELETE request to the `Like` detail endpoint (`DELETE /api/likes/{like_id}/`) with the ID of the existing `Like` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `Like` object from the database and verify that it no longer exists.

**Expected Results:**
- The `Like` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `Like` object should no longer exist in the database.

**Test Data:**
- Existing `Like` object ID.

**Test Environment:**
- Django development environment with a `Like` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Like` object was successfully deleted, and it no longer exists in the database.


## Post Model CRUD Test Cases

### Test Case 1: Create Post

**Test Case Description:**
This test case verifies the creation of a new `Post` object by sending a POST request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `Post` objects.

**Test Steps:**
1. Send a POST request to the `Post` creation endpoint (`POST /api/posts/`) with valid data, including the post title and content.
2. Verify that the response status code is 201 (Created).
3. Verify that the created `Post` object exists in the database.
4. Verify that the `Post` object is associated with the logged-in user as the 'owner'.

**Expected Results:**
- A new `Post` object should be created successfully.
- The response should include the created `Post` object's data.
- The `Post` object should be associated with the logged-in user as the 'owner'.
- The `Post` object should be retrievable from the database.

**Test Data:**
- Valid data for creating a `Post` object (e.g., title, content).

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Post` object was successfully created, and all expected results were met.

### Test Case 2: Read Post

**Test Case Description:**
This test case verifies the retrieval of an existing `Post` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `Post` object exists in the database.

**Test Steps:**
1. Send a GET request to the `Post` detail endpoint (`GET /api/posts/{post_id}/`) with the ID of an existing `Post` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `Post` object.

**Expected Results:**
- The requested `Post` object should be retrieved successfully.
- The response should include the `Post` object's details.

**Test Data:**
- Existing `Post` object ID.

**Test Environment:**
- Django development environment with `Post` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Post` object was successfully retrieved, and all expected details were included in the response.

### Test Case 3: Update Post

**Test Case Description:**
This test case verifies the update of an existing `Post` object by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `Post` object exists in the database.
- The logged-in user is the owner of the `Post` object.

**Test Steps:**
1. Send a PUT request to the `Post` detail endpoint (`PUT /api/posts/{post_id}/`) with the ID of an existing `Post` object and updated data.
2. Verify that the response status code is 200 (OK).
3. Retrieve the `Post` object from the database and verify that its data has been updated.

**Expected Results:**
- The `Post` object should be updated successfully.
- The response should indicate successful update with a 200 status code.
- The `Post` object's data in the database should reflect the updated values.

**Test Data:**
- Existing `Post` object ID.
- Updated data for the `Post` object (e.g., updated title or content).

**Test Environment:**
- Django development environment with a `Post` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Post` object was successfully updated, and its data in the database reflects the changes.

### Test Case 4: Delete Post

**Test Case Description:**
This test case verifies the deletion of an existing `Post` object by sending a DELETE request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `Post` object exists in the database.
- The logged-in user is the owner of the `Post` object.

**Test Steps:**
1. Send a DELETE request to the `Post` detail endpoint (`DELETE /api/posts/{post_id}/`) with the ID of the existing `Post` object.
2. Verify that the response status code is 204 (No Content).
3. Attempt to retrieve the `Post` object from the database and verify that it no longer exists.

**Expected Results:**
- The `Post` object should be deleted successfully.
- The response should indicate successful deletion with a 204 status code.
- The `Post` object should no longer exist in the database.

**Test Data:**
- Existing `Post` object ID.

**Test Environment:**
- Django development environment with a `Post` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Post` object was successfully deleted, and it no longer exists in the database.

### Test Case 5: File Upload Validation

**Test Case Description:**
This test case checks the validation of file uploads when creating a `Post`.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A user is logged in and has access to create `Post` objects.

**Test Steps:**
1. Send a POST request to the `Post` creation endpoint (`POST /api/posts/`) with valid data, including the post title and content, and an image file that exceeds the allowed size (greater than 2MB).
2. Verify that the response status code is 400 (Bad Request).
3. Send a POST request with an image file that exceeds the allowed height (greater than 4096px) and verify a 400 status code.
4. Send a POST request with an image file that exceeds the allowed width (greater than 4096px) and verify a 400 status code.
5. Send a POST request with valid image data, and verify a successful response.

**Expected Results:**
- The API should reject image files that exceed the size, height, or width limits and return a 400 status code.
- The API should accept valid image files and return a 201 status code for successful post creation.

**Test Data:**
- Valid data for creating a `Post` object (e.g., title, content).
- Image files that exceed size, height, or width limits.
- Valid image file within the allowed limits.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test cases have passed.
- **Details:** The API correctly rejects invalid image files and accepts valid ones.

### Test Case 6: Test Post Filters and Search

**Test Case Description:**
This test case verifies the functionality of filtering and searching for posts.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- Multiple `Post` objects exist in the database.

**Test Steps:**
1. Send a GET request to the `Post` list endpoint (`GET /api/posts/`) with a filter to retrieve posts by a specific owner's username.
2. Verify that the response status code is 200 (OK) and that the returned posts match the filter criteria.
3. Send a GET request to the `Post` list endpoint with a search query for a specific keyword in post titles.
4. Verify that the response status code is 200 (OK) and that the returned posts contain the search keyword in their titles.

**Expected Results:**
- The API should filter and return posts based on the specified criteria.
- The API should return posts that match the search query in their titles.

**Test Data:**
- Filter criteria (e.g., owner's username).
- Search query (e.g., keyword in post titles).

**Test Environment:**
- Django development environment with `Post` objects in the database.

**Test Result:**
- **Outcome:** The test cases have passed.
- **Details:** The API correctly filters and searches for posts based on the provided criteria and keywords.

### Test Case 7: Test Like and Comment Related Functionality

**Test Case Description:**
This test case verifies the functionality related to likes and comments on posts.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- Multiple `Post` objects exist in the database.

**Test Steps:**
1. Send a POST request to the `Like` creation endpoint (`POST /api/likes/`) to like a specific post.
2. Verify that the response status code is 201 (Created).
3. Retrieve the liked post from the database and verify that the likes count has increased by one.
4. Send a DELETE request to the `Like` deletion endpoint (`DELETE /api/likes/{like_id}/`) to unlike the same post.
5. Verify that the response status code is 204 (No Content).
6. Retrieve the post again and verify that the likes count has decreased by one.
7. Send a POST request to the `Comment` creation endpoint (`POST /api/comments/`) to add a comment to a specific post.
8. Verify that the response status code is 201 (Created).
9. Retrieve the commented post from the database and verify that the comments count has increased by one.

**Expected Results:**
- Users should be able to like and unlike posts, and the likes count should reflect these actions.
- Users should be able to add comments to posts, and the comments count should reflect these actions.

**Test Data:**
- Specific `Post` object for liking and commenting.

**Test Environment:**
- Django development environment with `Post` objects in the database.

**Test Result:**
- **Outcome:** The test cases have passed.
- **Details:** Users can successfully like and unlike posts, as well as add comments, and the counts are updated accordingly.

### Test Case 8: Edge Cases for Post CRUD

**Test Case Description:**
This test case covers edge cases for the CRUD operations on `Post` objects.

**Preconditions:**
- Ensure the Django project and database are properly set up.

**Test Steps:**
1. Send a GET request to the `Post` detail endpoint (`GET /api/posts/{non_existent_post_id}/`) with the ID of a non-existent `Post` object.
2. Verify that the response status code is 404 (Not Found).
3. Attempt to update a `Post` object that doesn't exist (e.g., `PUT /api/posts/{non_existent_post_id}/`).
4. Verify that the response status code is 404 (Not Found).
5. Attempt to delete a `Post` object that doesn't exist (e.g., `DELETE /api/posts/{non_existent_post_id}/`).
6. Verify that the response status code is 404 (Not Found).

**Expected Results:**
- When attempting to access, update, or delete a non-existent `Post` object, the API should return a 404 status code.

**Test Data:**
- Non-existent `Post` object ID.

**Test Environment:**
- Django development environment.

**Test Result:**
- **Outcome:** The test cases have passed.
- **Details:** The API correctly returns a 404 status code for non-existent `Post` objects.


## Profile Model CRUD Test Cases

### Test Case 1: Create Profile

**Test Case Description:**
This test case verifies the creation of a new `Profile` object through Django signals when a new `User` is created.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- User authentication and authorization are configured correctly.
- A new `User` object is created.

**Test Steps:**
1. Create a new `User` object (e.g., registration).
2. Verify that a corresponding `Profile` object is automatically created.
3. Retrieve the `Profile` object from the database and verify its existence.

**Expected Results:**
- A new `Profile` object should be created automatically when a new `User` is created.
- The `Profile` object should exist in the database.

**Test Data:**
- Data for creating a new `User` object.

**Test Environment:**
- Django development environment with user authentication configured.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Profile` object is created successfully through Django signals.

### Test Case 2: Read Profile

**Test Case Description:**
This test case verifies the retrieval of an existing `Profile` object by sending a GET request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- At least one `Profile` object exists in the database.

**Test Steps:**
1. Send a GET request to the `Profile` detail endpoint (`GET /api/profiles/{profile_id}/`) with the ID of an existing `Profile` object.
2. Verify that the response status code is 200 (OK).
3. Verify that the response includes the details of the requested `Profile` object.

**Expected Results:**
- The requested `Profile` object should be retrieved successfully.
- The response should include the `Profile` object's details.

**Test Data:**
- Existing `Profile` object ID.

**Test Environment:**
- Django development environment with `Profile` objects in the database.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Profile` object was successfully retrieved, and all expected details were included in the response.

### Test Case 3: Update Profile

**Test Case Description:**
This test case verifies the update of an existing `Profile` object by sending a PUT request to the appropriate API endpoint.

**Preconditions:**
- Ensure the Django project and database are properly set up.
- A `Profile` object exists in the database.
- The logged-in user is the owner of the `Profile` object.

**Test Steps:**
1. Send a PUT request to the `Profile` detail endpoint (`PUT /api/profiles/{profile_id}/`) with the ID of an existing `Profile` object and updated data.
2. Verify that the response status code is 200 (OK).
3. Retrieve the `Profile` object from the database and verify that its data has been updated.

**Expected Results:**
- The `Profile` object should be updated successfully.
- The response should indicate successful update with a 200 status code.
- The `Profile` object's data in the database should reflect the updated values.

**Test Data:**
- Existing `Profile` object ID.
- Updated data for the `Profile` object (e.g., updated name or content).

**Test Environment:**
- Django development environment with a `Profile` object owned by the logged-in user.

**Test Result:**
- **Outcome:** The test has passed.
- **Details:** The `Profile` object was successfully updated, and its data in the database reflects the changes.

### Test Case 4: Edge Cases for Profile CRUD

**Test Case Description:**
This test case covers edge cases for the CRUD operations on `Profile` objects.

**Preconditions:**
- Ensure the Django project and database are properly set up.

**Test Steps:**
1. Send a GET request to the `Profile` detail endpoint (`GET /api/profiles/{non_existent_profile_id}/`) with the ID of a non-existent `Profile` object.
2. Verify that the response status code is 404 (Not Found).
3. Attempt to update a `Profile` object that doesn't exist (e.g., `PUT /api/profiles/{non_existent_profile_id}/`).
4. Verify that the response status code is 404 (Not Found).

**Expected Results:**
- When attempting to access or update a non-existent `Profile` object, the API should return a 404 status code.

**Test Data:**
- Non-existent `Profile` object ID.

**Test Environment:**
- Django development environment.

**Test Result:**
- **Outcome:** The test cases have passed.
- **Details:** The API correctly returns a 404 status code for non-existent `Profile` objects.