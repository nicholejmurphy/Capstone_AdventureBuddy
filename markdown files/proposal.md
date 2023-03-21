# Capstone1 Proposal
![OutThere Logo](OutThere%20(2).png)

>Map? Check. Water? Check. Weather? Check. Misadventure... check??
> 
> There are many ways to plan ahead and prepare before you set off on you next grand adventure, but what about "*expecting the unexpected?*" Misadventure doesn't always come with warning signs.

### What is OutThere?
 OutThere is an interactive app that aims to increase the safety of the adventurer while sharing the stoke with fellow enthusiasts. 

 With OutThere, you can generate a map of your itinerary and add and other significant details, then share them with friends and loved ones through a saved address book. This includes when you plan to leave and when you should be back. There is no worse feeling that being stuck in the wilderness and knowing no one knows where you are or when to start looking for you.

 You can save your trips for future use and can easily update and share them with friends. A simple notification will alert those you wish to contact, along with a time/date to start to worry if they haven't heard from you. 

### Target Demographic:
Adventure comes in many forms. This could look like a walk in the park, a kayak run on a local river, or canyoneering in some of the deepest canyons in the West. If you enjoy recreating in spaces with limited phone service, OutThere is for you!

### Data Usage:
![OutThere Logo](OutThere%20(1).png)
Here is a basic outline of the different types of data OutThere will be accesssing:
1. User Data - this model will store basic user information that will be saved to a user's account for authentication and authorization.
2. Address Data - this model will act as an address book that users can access to more efficiently notify friends of their trips. [This will either be in the form of SMS or Email depending on the selected API I will go with]
3. Adventure Data - this model will store trip information that can be duplicated, updated, or deleted by the user. These trips can be reused when creating an itinerary to share with friends.

![OutThere Logo](OutThere%20(4).png)

### The Creative Approach
This app will create a user friendly interface where a user can login or register an account to save their data. The user can view their profile that includes all of their past trips and their own address book. There will be CRUD functionality with the user, their trips, and their addresses.

![OutThere Logo](OutThere%20(3).png)

### Anticipated Challenges
- I forsee challenges with the SMS API, therfore I may go with a Gmail API or some other email platform. 
- I have struggled with finding proper versioning on my local server. I expect there to be a lot of troubleshooting that wil come with Heroku.
- Breaking down error handling and making sure it is an inclusive application to handle "the unexpected."

### Stretch Goals... the "Further Study"

If time allows, I have additional features I would like to add to the application:
- Creating a search query to find and add friends on the app - creating more of a social media interface where users could just post their trips on the newsfeed and these friends could recieve notifications with their posts as well. Friends could also "give kudos" and add comments to their friends' adventures.
- Incorporate another API for generating waypoints on a map to inlucde in their itinerary. This would include another model for waypoints that a user could have access to. This would be through the Mapquest API.
- A check-in feature allowing users to alert friends that they have safetly returned home.
- A gaurdian feature that will notify a user that they have not checked back in from their trip. If this alert is not addressed, the user's friends will be remindedthat their friend has not yet checked in from their trip and they should follow up with them.