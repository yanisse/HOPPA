#Sprint Meeting Report: Sprint 5

##What Worked Well? 
The connection between the html and Flask worked very well, as did the queries. Passing information between the html and Flask was far more painless than expected.
Working the queries through Flask was also very easy and straightforward.

##What Didn’t work well?
Bcrypt caused a bit more trouble. The deployment was made difficult because Bcrypt could not be properly installed to Azure.
Certain entities could not be erased because the of the relationships and foreign keys. This took some time to work out.
While not something within our control, Microsoft had technical difficulties on their end which caused our database to crash. Afterward, the schema was completely lost and had to be redone from scratch.

##What we learned?
Flask makes communication between the front end and back end a far more simple process than we had anticipated. The process is very simple and straightforward.
Relationships and entities involving foreign keys can be somewhat tricky to work with.


#Sprint Meeting Report: Sprint 4

##What Worked Well? 
The registration and login validation came about more easily than expected, though still not exactly easy.
Bcrypt was used for password encryption and was fairly easy to use.
Image serving gave some trouble, but was actually fairly simple. Using file directories instead of data blobs was easier for this.

##What Didn’t work well?
For one member of the group, Bcrypt failed to install, making it far more difficult for him to work with the project.
Initially, the uploading of images was troublesome, but was just a matter of fixing the working directories.
Images being stored as data in blobs within the database proved more difficult to work with than just saving the picture in a file in the server and serving the image from there.

##What we learned?
Serving images by calling them from a file directory stored in the database is easier than storing its data as a blob in the database. Image serving with Flask was a little trickier than expected.


#Sprint Meeting Report: Sprint 3

##What Worked Well? 
In this sprint we were able to deploy our application on Microsoft Azure. 
The front end of the application was updated and new pages were added.

##What Didn’t work well?
We were trying to deploy our application using Heroku, but were unable to do it. Instead of using Heroku we decided to use Microsoft Azure as our cloud service.

##What we learned?
We have learned more about AngularJS and Microsoft Azure, how these developer tools can improve the web application.


#Sprint Meeting Report: Sprint 2

##What Worked Well? 
We were able to use the ideas for design and implementation we created last sprint. Using the mockups created at the last sprint we implemented the front-end of the web application HOPPA. The mockups help us to create our page more easily.

##What Didn’t work well?
As we are progressing in our learning of web application development, we found AngularJS a rich framework with a lot of features we can use in our application. Since we are learning about it and how to use it, we think for next sprint we will be able to improve our MVC enviroment of the application using our selected frameworks, such as AngularJS, Flask and PostgreSQL.

##What we learned?
We have learned more about AngularJS and how this framework can improve development of an application.


#Sprint Meeting Report: Sprint 1

##What Worked Well? 
As we progressed in the design and specifications of the social network to be implemented, our ideas for design and implementation were used in the wireframes and database created. Having these designs done ahead of time sped up the process greatly. Because of this, the mockups were done fairly quickly.

##What Didn’t work well?
The team did not come together quickly enough to create the database in the cloud and thus, the database's implementation did not go over as smoothly as it could have gone.

##What we learned?
We learned that having clear ideas from the start helps implementations go more smoothly and that we should try to have these clearer ideas for every aspect of the project.


#Sprint Meeting Report: Sprint 0

##What Worked Well? 
We think our brainstorming worked well for us, it helped us to decide the final idea and concept of the application to be implement.

##What Didn’t work well?
At first we did not know what our final Development frameworks were going to be, that was the most difficult decision in this sprint. At the end we resolved it by what we thought will help us develop the application more effectively.

##What we learned?
As a group we have learn to unite the ideas of all members and convert it to one, also to work more as a group not individual.

Domain in Microsoft Azure: http://hoppa.azurewebsites.net/
