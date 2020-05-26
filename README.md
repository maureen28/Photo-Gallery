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


## BDD
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>Display image details</td>
<td><strong>Hover over the desired image</strong></td>
<td>Information about the the image will be displayed, i.e, the location, category and a brief descrption of the image.</td>
</tr>
<tr>
<td>Search for images by category/location</td>
<td><strong>Category/Location name</strong></td>
<td>The images that fit search description will be displayed</td>
</tr>
<tr>
<td>Copy image link</td>
<td><strong>Click on the copy button</strong></td>
<td>Image link will be copied to clipboard.</td>
</tr>
</table>


## Technology & Dependency

<ol>
<li>Owl Carousel</li>
<li>DJANGO web framework.</li>
<li>HTML & CSS(Bootstrap, FontAwesome) </li>
<li>PostgreSQL</li>
</ol>

### Brief Webpage Overview.

<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/landing.jpg" alt="Photo Gallery Home page" width="1000"/>
<li>Below is an expanded image Once you hover over the image</li>
<img src="/expand.jpg" alt="Expanded image " width="800"/>
<li>Below is the image with its description once you search the image</li>
<img src="/find.jpg" alt="Found image" width="800"/>
</ul>

### Live link : https://nimophotogall.herokuapp.com/

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
<li>Run <code>python3 manage.py runserver</code></li>
<li>Make your first app at <code>python3 manage.py startapp [name of folder]</code></li>
</ol>


## Running the tests
Use the command given below to run automated tests.
<code> python manage.py test mygallery </code>


## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>