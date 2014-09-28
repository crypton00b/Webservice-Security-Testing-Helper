Webservice-Security-Testing-Helper
==================================

Security Testing Webservices helper for scanners/soap ui from fiddler(http request interceptor) dumps

How to Use:

First crawl through the website with fiddler(interceptor) storing all the requests and responses in it.Now just save all 

the entries in fiddler containing the POST webservice request to different services invoking different methods.Save all 

such entries as .saz file.Now change the extension to '.zip' file and extract it.save this into some path in your 

drive.Now run the script with this path as the input path.Give another path where u want the output folders to be saved 

when asked.


Once the script is run,you get different different folder named after the services containing text files named on the 

methods invoked.These text files would contain the concerned xml request that for that method.


Now you can use these xml requests in soap Ui or Appscan for scanning the webservices...

Please note-I wrote this code for one of my project and it worked perfectly for my need.I didnt consider the exception 

cases in this.So you are free to change the code according to ur need.And do note that this works only for those POST 

requests which contains a 'soapAction' in its request..
