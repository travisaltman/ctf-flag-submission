First shout out to Will Campbell (https://www.linkedin.com/in/willcampbell0352/) for creating this script on the fly during a CTF at RVAsec 12.  This was the attack / defend style CTF that https://metactf.com/ hosted.  Was fun and challenging and in my opinion better than those jeopardy style CTFs.

The request.py is the only file meant to run locally that grabs flags, throws them into json format, determines if the flag is expired, parses response into a beautiful soup object, parses the flag out of that response, then submits it to the CTF server.

Nothing fancy just wanted to throw it into a repo for reference.
