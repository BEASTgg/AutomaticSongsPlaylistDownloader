## Download Any Playlist automatically by just running this script with a custom csv input

Requirements -
(Run in vscode terminal)
~~~
pip install pytube youtube-search-python pandas yt-dlp
~~~

Also install (ffmpeg) - [Click here](https://github.com/BtbN/FFmpeg-Builds/releases)

~~~
Extract it in C:\ffpmeg\(here)

keep both the files there bin and doc
~~~

Now to run this -

~~~
Python downloadfromcsv.py
~~~

after you run this it will ask for a csv file which u need to provide the name for and make sure its in the same folder as where u have downloaded and extracted my repo in .......

To get the csv file you need to go [here](https://www.tunemymusic.com/transfer) and select the source for example spotify and then login via it in the popup then click on load via (whatever u selected) in my case spotify then select the playlist u wanna copy for me it was likedmusic then click start and in choose destination select export as file and select csv then click export then click start transfer and voila u got the csv now input it in my program and it will start downloading.
