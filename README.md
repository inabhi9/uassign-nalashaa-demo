Python Coding Exercise (1 Hour)
====================================================
This was assigne by [http://www.nalashaa.com/][1] for the Python opening. They want to examin the approach one had taken to solve the problem.

Create a solution using OO Python, capable of connecting to a REST service to obtain a collection of JSON objects containing links to News Stories about a certain topic, saving any images from the news stories to a folder.  

Your code should achieve the following objectives:  
 
  1. Call the Guardian REST endpoint and retrieve the data
  2. Iterate the objects
  3. For each object call the contained url;
      a. Parse the contents of the returned object and attempt to extract the image hrefs
      b. Request the images directly and save to a folder
  4. If time permits, complete the same task for the BBC REST endpoint  

You should implement the solution using a base class that contains generic code for connecting to an API, capable of iterating through objects and storing the image files to the disk. The 'Guardian' class will then extend this class to process content specifically for that API - this approach should afford you the best opportunity at achieving objective 4.

Information you will need  

  * Guardian REST endpoint to fetch stories about Obama:
  [http://content.guardianapis.com/search?q=obama&format=json][2]
  * Guardian API Key (if needed):
    `2ugtcs5mf3s39cgdc2c6b8pp`
  * Guardian API Documentation:
    [http://explorer.content.guardianapis.com/#/?format=json&order-by=newest][3]
  * BBC News REST endpoint to fetch technology stories:
  [http://api.bbcnews.appengine.co.uk/stories/technology][4]
  * BBC News API Documentation
  [http://api.bbcnews.appengine.co.uk/][5]  


  [1]: http://www.nalashaa.com/
  [2]: http://content.guardianapis.com/search?q=obama&format=json
  [3]: http://explorer.content.guardianapis.com/#/?format=json&order-by=newest
  [4]: http://api.bbcnews.appengine.co.uk/stories/technology
  [5]: http://api.bbcnews.appengine.co.uk/
