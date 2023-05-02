# Capstone1 Proposal
![OutThere Logo](/MD_images/OutThere_Logo.png)

>Log your adventures. Share with friends. Stay found.

### What is OutThere?
 OutThere is an interactive app that aims to increase the safety of the adventurer while sharing the stoke with fellow enthusiasts. 
 
 With OutThere, you can keep track of your adventures and plan for ones to come. Keep track of your favorite campsites, trailheads, or water sources by saving waypoints. With the waypoints you add, you can check them all out on a map and also save the map to you computer or phone! 
 
 Find friends on OutThere and share your adventures with on another! Help keep yourself found by sharing your travel plans... just in case things don't go as planned.  

### Target Demographic:
Adventure comes in many forms. This could look like a walk in the park, a kayak run on a local river, or canyoneering in some of the deepest canyons in the West. If you enjoy recreating in spaces with limited phone service, OutThere is for you!

### Data Usage:
Here is a basic outline of the different types of data OutThere will be accesssing:
1. User Data - this model will store basic user information that will be saved to a user's account for authentication and authorization.
2. Adventure Data - this model will store trip information that can be duplicated, updated, or deleted by the user. These trips can be reused when creating an itinerary to share with friends.
3. Waypoint Data - This data will be for all saved waypoints associated with a given adventure. These pieces are used to concat into a sting including all waypoints that is sent throughthe api request.
![Database Map](/MD_images/database_mapping.png)

### The Creative Approach
OutThere is built with backend Python with Flask, WTForms, and Bcrypt and frontend in JavaScript, JQuery, Jinja, and Bootstrap. The database is held through Postgres. CRUD functionality is applied to both User and Adventure models. To access most of the app, a user must signup or log in. 

Most of the data help on the app is user generated. A user may create a profile and provide their own data. They also may create Adventures and post them to share with other users. Users may follow one another to view others' posts!

On each adventure, a user may add a kudos for a friend to share excitement and praise. If the user is the creator of an adventure, they may update or delete it's content as well as add additional waypoints on it. 

A user may add waypoints and then choose to generate a map to display them. This action is done through an Axios request to the local app.py API to generate a query string including a list of concatenated waypoints. This string is then returned, and through embeding the newly made url request into an img tag's src attribute, it is then displayed as a static map img to the user. 

![Mapquest Logo](/MD_images/apis.png)

### Stretch Goals... the "Further Study"
Additional features I would like to add to the application:
- Including the Twilio API to allow users to send SMS messages to friends off the app when tey head out for their adventure. this would give their friend details about their trip as well as an expected return time for when to check back in to ensure they made it home safely. 
- A check-in feature allowing users to alert friends that they have safetly returned home. This could be seen on the adventure in the news feed. It would be highlited in red if the user has not checked back in yet. If this alert is not addressed, the user's friends will be reminded that their friend has not yet checked in from their trip and they should follow up with them.
- Allow a "save adventure" feature that could save other's adventures to you favorites list - maybe a trip you hope to do in the future!

### How to get started
![Set Up Instructions](/MD_images/app_setup.png)

### Deployed at outthere.herokuapp.com