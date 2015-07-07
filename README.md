this is a test project for getcleanly.com
to get things running you can run
pip install -r requirements.txt
or create virtualenv and run the above command

comments
--------
1. in settings.py you should change the path for MEDIA_ROOT
2. the admin ui start acting strange, i guess its because i played with static and media settings
    edit: its indeed the media_url setting, i gave it the same name as the static_url

what left
---------
1. add tests
2. upload the proj to heroku
3. use bootstrap
