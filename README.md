# PHOTO GALLERY

## Description
Photo gallery is a personal gallery application that you display your photos for others to see.

### Author: Maureen Wairimu

## User Story

<ul>
<li>Users can view the different photos that interest them.</li>
<li>Users can click on a single photo to expand it and also view the details of the photo.</li>
<li>Users can search for different categories of photos. </li>
<li>Users can copy a link to the photo to share with my friends.</li>
<li>Users can view photos based on the location they were taken.</li>
</ul>

## Technology & Dependency

<ol>
<li>DJANGO web framework.</li>
<li>HTML & CSS(Bootstrap, FontAwesome) </li>
<li>PostgreSQL</li>
</ol>

### Brief Webpage Overview.

<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/landing.jpg" alt="Photo Gallery Home page" width="1000"/>
</ul>

### Live link :

## Setup Instructions

<ol>
<li>Clone or download the repository <code> </code> </li>
<li>Create a virtual environment aand activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li>Install all the requirements <code> pip install -r requirements.txt</code></li>
<li>Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL database client.
</li>
<li>Create a file in your root directory and store a generated SECRET key <code>export SECRET_KEY="<your-key>"</code></li>
<li>Run <code>python3 manage.py server</code></li>
<li>Run test at <code>python3 manage.py test</code></li>
</ol>


## Running the tests
Use the command given below to run automated tests.
<code> python manage.py test news </code>


## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>