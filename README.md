# SpoodleSpace - Backend

![dog danger example](Media/README.md-images/README.md-drf-backend.jpg)

## **[drf-spoodle-space](spoodlespace.herokuapp.com)** was developed using Django and Django Rest Framework to serve as the API for **[SpoodleSpace](spoodle-space-pp5.herokuapp.com)**. 

# ![**SpoodleSPACE**](Media/README.md-images/README.md-paulpuppy.jpg)
**SpoodleSpace** was developed and submitted as my fifth Profile Portfolio Project as part of specializing in Advanced Front-end Development for the Code Institute's Diploma in full-stack software development course. Being the Django Rest Framework API, three custom models and forms were designed to interface with its frontend React JavaScript library. 

This project evolved out of a previous Portfolio Project, which centred around a fictional online community of dog owners using a website called '**[Cockapoo Club](https://home-cockapoo-club-pp4.herokuapp.com)**'.

This iteration of the original concept introduces an entirely new range of features and functionalities. A main site goal for this project was to provide Users with a very different and more engaging interactive experience. 
This expansion on that original concept has allowed me to combine my understanding of **HTML**, **CSS**, **JavaScript**, **Python**, **React**, **Bootstrap**, and **Django REST Framework**. 

- **[Click Here](https://spoodlespace.herokuapp.com/)** to see the deployed website. 

- To view the frontend repository on Github **[Click Here](https://github.com/SamOBrienOlinger/spoodle-space-pp5)**. 

## **Summary**
  This social platform provides Users with an opportunity to connect and share photographs, and even information about owning, training and taking care of a breed of dog called Cockapoos, one of Ireland's newest, most popular and much-loved dog breeds. 
  
  Unlike many other social media platforms that provide a similar experience, this project offers Users a unique way to create and participate in their own community of likeminded pet owners.    

The site is designed to engage millions of potential Users around the world who:

* May already have a Cockapoo dog and need to learn about how to best take care of their dog. 

* May be thinking about getting a new Cockapoo dog and require more information to make their decision. 

 * May already be Cockapoo owners and are interested in connecting with and learning from other Cockapoo owners. 

* Will enjoy sharing photographs and videos of their pets.  

In order to achieve the project's most important goals of enhancing both the UI and UX, how data is manipulated via the front-end application was of fundamental importance.

## Contents

- [User Stories](#user-stories)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

### [User Stories](#user-stories)

  **Navigation and authentication**

  - Navigation: As a user, I can view a navbar from every page so that I can navigate easily between pages.
  - Routing: As a user, I can navigate through pages quickly so that I can view content seamlessly without page refresh.
  - Authentication - Sign up: As a user, I can create a new account so that I can access all the features for signed-up users.
  - Authentication - Sign in: As a user, I can sign in to the app so that I can access functionality for logged-in users.
  - Authentication - Logged in Status: As a user, I can tell if I am logged in or not so that I can log in if I need to.
  - Authentication - Refreshing access tokens: As a user, I can maintain my logged-in status until I choose to log out so that my user experience is not compromised.
  - Navigation: Conditional rendering - As a logged-out user, I can see sign-in and sign-up options so that I can sign in/sign up.
  - Avatar: As a user, I can view users' avatars so that I can easily identify users of the application.

  **Profile**

  - Profile page: As a user, I can view other users' profiles so that I can see their posts and learn more about them.
  - Most followed profiles: As a user, I can see a list of the most followed profiles so that I can see which profiles are popular.
  - As a user, I can view data about other users, such as the number of posts, follows, and users followed so that I can learn more about them.
  - Follow/Unfollow a user: As a logged-in user, I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed.
  - View all posts by a specific user: As a user, I can view all the posts by a specific user so that I can catch up on their latest posts or decide I want to follow them.
  - Update username and password: As a logged-in user, I can update my username and password so that I can change my display name and keep my profile secure.

  **Posting, liking, and commenting on images**

  - Create posts: As a logged-in user, I can create posts with images.
  - View a post: As a user, I can view the details of a single post so that I can learn more about it.
  - Like a post: As a logged-in user, I can like a post so that I can show my support for the posts that interest me.
  - Post page: As a user, I can view the posts page so that I can read the comments about the post.
  - Edit post: As a post owner, I can edit my post title and description so that I can make corrections or update my post after it was created.
  - Create a comment: As a logged-in user, I can add comments to a post so that I can share my thoughts about the post.
  - Comment date: As a user, I can see how long ago a comment was made so that I know how old a comment is.
  - View comments: As a user, I can read comments on posts so that I can read what other users think about the posts.
  - Delete comments: As an owner of a comment, I can delete my comment so that I can control the removal of my comment from the application.
  - Edit a comment: As an owner of a comment, I can edit my comment so that I can fix or update my existing comment.

  **Dog profile**

  - As a logged-in user, I can create and edit my dog profile, including being able to add and change a picture of my dog and information about my dog.
  - As a logged-in user, I can view other users' dog profiles if I am following them.
  - As a user, I can view the most recent dog profiles posted, ordered by most recently created first so that I am up to date with the newest content.
  - As a user, I can search for dog profiles with keywords so that I can find the dog profiles and user profiles I am most interested in.
  - Infinite scroll: As a user, I can keep scrolling through the images on the site that are loaded for me automatically so that I don't have to click on "next page".

  **Dog health details**

  - As a logged-in user, I can create and edit health details about my dog.
  - As a logged-in user, I can view the health details of other users' dogs if I am following them.
  - As a user, I can view the most recent details about the health of users' dogs, ordered by most recently created first so that I am up to date with the newest content.
  - As a user, I can search for dog health details with keywords so that I can find the dog health details and user profiles I am most interested in.
  - Infinite scroll: As a user, I can keep scrolling through the images on the site that are loaded for me automatically so that I don't have to click on "next page".

  **Dog danger details**

  - As a logged-in user, I can create and edit details about how dangerous my dog is.
  - As a logged-in user, I can view the details of how dangerous other users' dogs are if I am following them.
  - As a user, I can view the most recent details posted about how dangerous other users' dogs are, ordered by most recently created first so that I am up to date with the newest content.
  - As a user, I can search for these details with keywords so that I can find the details and user profiles I am most interested in.
  - Infinite scroll: As a user, I can keep scrolling through the images on the site that are loaded for me automatically so that I don't have to click on "next page".

### [Entity Relationship Diagram](#entity-relationship-diagram)

- Built-in Django models were used for this project. 
  
- The three custom models created were:
  - DogProfile
  - DogHealth 
  - DogDanger
  
![Entity Relationship Diagram](Media/README.md-images/README.md-ERD.jpg)

### [Technologies](#technologies)

- #### Languages

  -  [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- #### Frameworks, Libraries, Programs and Services Used
  - [Django:](https://www.djangoproject.com/)

  - [Django Rest Frameworks](https://www.django-rest-framework.org/).

  - [Git:](https://git-scm.com/)

  - [GitHub:](https://github.com/)

  - [PostgreSQL:](https://www.postgresql.org/)

  - [ElephantSQL:](https://www.elephantsql.com/)

  - [Heroku:](https://heroku.com/)
  
 ### [Testing](#testing)
- Create, Read, Update and Delete functionality across this API was tested manually to ensure that the database was being updated as expected when creating, reading, updating or deleting data in concert with Users' interactions on the frontend React app. for further details of testing the frontend which are relevant to backend functionality, Please see the **[frontend repository README.md file](https://github.com/SamOBrienOlinger/spoodle-space-pp5/blob/main/README.md)** 

- Code Institute's CI Python Linter was used to validate all Python code. Every app passed without errors, except for E501 'line too long' warnings. For example:

![Python validator](Media/README.md-images/README.md-ci-linter.jpg)



- Manual testing was used throughout each stage of development to ensure that the acceptance criteria set out in each of the thirteen User Stories was achieved. These can be found in the Github Pages Project [here](https://github.com/users/SamOBrienOlinger/projects/3). 

  The tests conducted for verifying the backend functionality of all apps passed. 
  The following test cases provide a representative sample demonstrating the achievement of all criteria for each User Story.

    **Dog Profiles**

    Comprehensive manual testing was carried out to guarantee that Users without the necessary permissions would not have Write Access. 
    It was a fundamental priority to restrict Users from having the ability to create, update, or delete data; or perform actions that could jeopardize sensitive data; or modify the system's state through adding new records, editing existing content, or making changes to configuration settings. 

    Regarding Authentication and Authorization, test cases conducted on the Dog Profile functionaility demonstrated this.


  1. **List Dog Profiles (Authenticated User)**

    - **Test Steps:**
      - Create an authenticated user account.
      - Create one or more dog profiles.
      - Send a GET request to `/dogprofiles/` endpoint.
  
    - **Expected Result:** 
      - Successful listing of dog profiles with a status code of 200.
  
    - **Actual Result:** 
      - Successful listing of dog profiles with a status code of 200.

  
  2. **List Dog Profiles (Guest User)**
  
    - **Test Steps:**
      - Send a GET request to `/dogprofiles/` endpoint.
  
    - **Expected Result:** 
      - Successful listing of dog profiles with a status code of 200.
  
    - **Actual Result:** 
      - Successful listing of dog profiles with a status code of 200.

  
  3. **Create Dog Profile (Authenticated User)**
  
    - **Test Steps:**
      - Log in with an authenticated user account.
      - Send a POST request to `/dogprofiles/` endpoint with dog profile data.
  
  
    - **Expected Result:** 
      - Dog profile creation with a status code of 201.
  
    - **Actual Result:** 
      - Dog profile creation with a status code of 201.

  
  4. **Create Dog Profile (Guest User)**
  
    - **Test Steps:**
      - Send a POST request to `/dogprofiles/` endpoint with dog profile data.
  
    - **Expected Result:** 
      - Forbidden access with a status code of 403.
  
    - **Actual Result:** 
      - Forbidden access with a status code of 403.

  
  5. **Retrieve Dog Profile by ID (Valid ID)**
  
    - **Test Steps:**
      - Send a GET request to `/dogprofiles/<valid_dog_profile_id>/` endpoint.
  
    - **Expected Result:** 
      - Successful retrieval of the dog profile with a status code of 200.
  
    - **Actual Result:** 
      - Successful retrieval of the dog profile with a status code of 200.

  
  6. **Retrieve Dog Profile by ID (Invalid ID)**
  
    - **Test Steps:**
      - Send a GET request to `/dogprofiles/<invalid_dog_profile_id>/` endpoint.
  
    - **Expected Result:** 
      - Dog profile not found with a status code of 404.
  
    - **Actual Result:** 
      - Dog profile not found with a status code of 404.

  
  7. **Update Own Dog Profile (Authenticated User)**
  
    - **Test Steps:**
      - Log in with an authenticated user account that owns the dog profile.
      - Send a PUT request to `/dogprofiles/<valid_dog_profile_id>/` endpoint with updated dog profile data.
  
    - **Expected Result:** 
      - Dog profile updated with a status code of 200.
  
    - **Actual Result:** 
      - Dog profile updated with a status code of 200.

  
  8. **Update Own Dog Profile (Guest User)**
  
    - **Test Steps:**
      - Send a PUT request to `/dogprofiles/<valid_dog_profile_id>/` endpoint with updated dog profile data.
  
    - **Expected Result:** 
      - Forbidden access with a status code of 403.
  
    - **Actual Result:** 
      - Forbidden access with a status code of 403.

  
  9. **Delete Own Dog Profile (Authenticated User)**
  
    - **Test Steps:**
      - Log in with an authenticated user account that owns the dog profile.
      - Send a DELETE request to `/dogprofiles/<valid_dog_profile_id>/` endpoint.
  
    - **Expected Result:** 
      - Dog profile deleted with a status code of 204.
  
    - **Actual Result:** 
      - Dog profile deleted with a status code of 204.

  
  10. **Delete Own Dog Profile (Guest User)**
  
      - **Test Steps:**
        - Send a DELETE request to `/dogprofiles/<valid_dog_profile_id>/` endpoint.
  
      - **Expected Result:** 
        - Forbidden access with a status code of 403.
  
      - **Actual Result:** 
        - Forbidden access with a status code of 403.

    
    To verify the functionality of API endpoints, the following test cases demonstrated this.

      Test cases


   Tests cases to validate database operations are as follows:

      Test cases

  Error Handling Test cases included:

      Test cases

  Test cases for validating user input:

      Test cases

  
  Pagination Tests:

      Test cases

  Performance Tests

      Test cases

   Integration Tests

      Test cases

  Third-party Service Integration Tests:

      Test cases 
  





- Fixed Bugs

  Migrated changes to models.py files caused the most problems overall. Although the data did exist in [Elephant SQL](https://www.elephantsql.com/), the database was corrupted and had to be delete entirely. A new instances needed to be created and connect to the API. The env.py file and Heroku Config Vars had to be updated accordingly. This issue was caused by a migration that altered a model from having an owner = ForeignKey when a OneToOneField was required. 

### [Deployment](#deployment) 

Creating a database using ElephantSQL was first required. The following steps were taken to do this: 

- login to ElephantSQL.

- click 'Create new instance' on the dashboard.

- name the 'plan' and select the 'Tiny Turtle' option.

- select 'select region' and choose the nearest data centre to your location.

- click 'Review'.

- then go to the ElephantSQL dashboard and click on the 'database instance name' for this project.

- copy the ElephantSQL database URL to your clipboard.

- Return to the Heroku dashboard.


This project was deployed through Heroku using the following steps:

- Log into Heroku
- Select 'Create New App' from your dashboard
- Choose an app name
- Select the appropriate region based on your location
- Click 'Create App'

- On your dashboard, click the 'Deploy' tab
- Locate 'Deployment Method' and choose 'GitHub'
- locate your repository then click 'Connect'

- Click the 'Settings' tab
- Open the 'Config Vars' and click 'Reveal Config Vars'

- The following environment variables need to be added and match the same values in your env.py file:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY

- install psycopg2 and dj-database-urlth libraries to handle database connection.
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
  - set allowed_origins

- gitignore the env.py file
- generate a requirements.txt file

once all the variables are in place, choose the main branch and click 'Deploy Branch'.
Once the build is finished, click 'Open App' located at the top of the page. 

### [Credits](#credits)

  - [W3Schools](https://www.w3schools.com/) 
  - [Stack Overflow](https://stackoverflow.com/)
  - Code Institute's [Moments](https://github.com/Code-Institute-Solutions/moments) module.

  - Code Institute Alumnus [Tom Ainsworth](https://github.com/Tom-Ainsworth) was of great support at strategically important stages to tease out certain bugs.   

  - The [README template](https://github.com/Code-Institute-Solutions/readme-template) provided by Code Institute was very helpful as a model for developing this README file.  

  - My mentors, [Naoise Gaffney](https://github.com/NaoiseGaffney) and [Antonio Rodriguez](AntonioRodriguez_mentor), provided invaluable support and I learned a lot from them throughout the development of this project. 
  
  Last but certainly not least, are the Code Institute's [Student Care Team](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentadvancedfrontend/studentcare) and all the Tutors on the [Student Support Team](https://learn.codeinstitute.net/ci_support/specializationsamplecontent/troubleshooting). Regardless of the challenge faced, they have provided invaluable support to me in developing my skills, knowledge and experience. Thank you very much.
