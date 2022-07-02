<div align="center">
<h1> ᴠ-ᴛᴏʀʀᴇɴᴛ ʙᴏᴛ <h1>
</div>

> So basically Tortoolkit is aimed to be the most versatile torrent leecher and youtube-dl bot for telegram. 
> This bot is highly customizable and to customize this bot you don't need to restart the bot every time. 
> The bot gets started with minimum variables and others can be set as and when needed using the /settings.

<br/> <div align="center">
[![Fork](https://telegra.ph/file/0cf5e3964afe499d19a2b.png)](https://github.com/hey-adithya/Bharat-Leech-Bot/fork) • [![Telegram Group](https://telegra.ph/file/6ebc3fca0426110f74aa8.png)](https://t.me/BharatTorrentPro)
</div>

<br/> <div align="center">
## <b>ᴡʜᴀᴛꜱ ɴᴇᴡ?</b>
</div>

- MegaDL added
- Overall download and upload progress.
- Pixeldrain DL support.
- Alert on when the bot boots up.
	
<details>

   <summary><h3>Features:<h3></summary>
	
Following are some awesome features offered by this bot:-
- Using the best torrent client to deal with torrent : [qBittorrent](https://github.com/qbittorrent/qBittorrent)
- Customised QBT engine with Custom Trackers
- You can choose which files you want to download from the torrent.
- A glorious settings menu from you can control the bot.
- If the bot is in the group, the users have their own settings like:
  - Permanent thumbnail support.
  - Users can choose if they want a file or video.
  - Load in their own rclone config so that the torrent/direct link is uploaded to their drive. (Work in Progress)
- Extraction of ZIP, TAR, ISO, RAR wih and without password. If you chose to extarct the archive and you enter the password wrong it will prompt you to enter the password upto 3 times after that zip will be uploaded as it is.
- G Drive Index support.
- Admins can put hard limits on the max torrent size and max youtube playlist size.
- Aria2 for direct links download.
- Upload to gdrive by using RCLONE.
  - You can load multiple drives in the conf and can switch on fly using the settings.
- Sorted YTDL download menu.
- Zip and upload also available.
- Get the server status.
- InstaDL support
- Browse the settings menu and try stuff. ;)

</details>
<details>

  <summary><h3>Deployment:<h3></summary>

## ***Heroku***
	
 For Heroku users New repo will come after Yash Khadse Is Free and Available .. (But This repo will work on heroku) 

<div align="center"> 
	
[![Deploy](https://telegra.ph/file/8b6445eaa73f3adaeb031.png)](heroku-deployment.md) </div>

## ***Zeet***
According to me, this platform provides resources that are enough for a genuine user and by default prevents Abuse:
Click the logo to see the video guide to see how to deploy. The web is not yet available but soon will be available on Zeet.

<div align="center"> 
	
[![Deploy](https://telegra.ph/file/bbe0d718668b24192e4fc.png)](https://youtu.be/WWi9JWDzXSw) </div>

## ***VPS Deployment Docker***
ExecVarsSample.py location:- `tortoolkit/consts/ExecVarsSample.py`

<div align="center">
	
[![Dockr](https://telegra.ph/file/ad341fecc21a631af2847.png)](https://youtu.be/c8_TU1sPK08) </div>


Steps:-
1. You should install docker first :- [How to Install Docker](https://docs.docker.com/engine/install/)

2. Clone the repo and edit ExecVarsSample.py 
   1. While editing Change 
      1. `API_HASH`
      2. `API_ID`
      3. `BOT_TOKEN`
      4. `ALD_USR`
      5. `BASE_URL_OF_BOT`
      6. `Uncomment the below DATABASE_URL and comment out the above DATABASE_URL`
      7. Also if the given procedure dosent work then set  `IS_VPS` to True and if you want to change the port when IS_VPS is true then change `SERVPORT` to your desired port number. (Note this should be used as backup)

3. After that execute these commands in root of the repo where tortoolkit folder is located.
    1. `apt install docker-compose`
    2. `docker-compose up`

4. If you edit a file like ExecVarsSample.py in future just run below commands
    1. `docker-compose build`
    2. `docker-compose up`

 ## ***VPS Deployment Without Docker***
 
 <div align="center"> 
	 
[![digitalOcean](https://telegra.ph/file/9bde4bc83653a202ef2da.png)](https://youtu.be/HYjG4-VfxXs) </div>

1. Run the following commands. (Following commands can be used to setup the vps from scratch)
   
    1. `git clone https://github.com/yash-dk/TorToolkit-Telegram.git`
    2. `sudo apt update`
    3. `sudo apt install -y python3.8`
    4. `sudo apt install -y python3-venv`
    5. `python3 -m venv venv`
    6. `source venv/bin/activate`
    7. `cd TorToolkit-Telegram`
    8. `pip install -r requirements.txt`
	9. `sudo apt install -y postgresql postgresql-contrib`
	10. `apt -qq install -y curl git wget python3 python3-pip aria2 ffmpeg mediainfo unzip p7zip-full p7zip-rar`
	11. `curl https://rclone.org/install.sh | bash`
	12. `apt-get install -y software-properties-common`
	13. `apt-get -y update`
	14. `add-apt-repository -y ppa:qbittorrent-team/qbittorrent-stable`
	15. `apt install -y qbittorrent-nox`
2. After that setup the database:- Remember the 'your-pass' that you enter below
    1. `sudo -u postgres bash`
    2. `createdb tortk`
    3. `psql`
    4. `ALTER USER postgres with password 'your-pass';`
    5. `exit`
    6. `exit`

3. After that setup the Variables.

	Assuming that you are in the directory where you clonned the repo
	   
    1. `cd TorToolkit-Telegram/tortoolkit/consts`
	2. `nano ExecVarsSample.py`
    3. Change the following:-
       1.  `API_HASH`
       2.  `API_ID`
       3.  `BOT_TOKEN`
       4.  `ALD_USR`
       5.  `BASE_URL_OF_BOT`
       6.  Change `DATABASE_URL = "dbname=tortk user=postgres password=your-pass host=127.0.0.1 port=5432"`

           Enter the password in the above string.
       7.  After that run (You can use any port for the web interface here i am using 80).
           Each time before starting the bot export the port Number

           `export PORT=80`

4. And finally run this in clonned folder.
    1. `chmod 777 start.sh`
    2. `./start.sh`

## Variables
- `IS_VPS`
    - Values :- `False`/`True`
    - Default Value :- `False`
    - Use :- Only set to True if you get errors regarding web server in VPS deployment. Only use as backup.

</details>

<br/> <div align="center">
<b>𝙲𝚘𝚖𝚙𝚞𝚕𝚜𝚘𝚛𝚢 𝚅𝚊𝚛𝚜:</b>
</div>
	  
- `API_HASH`
  - Values :- Valid API HASH obtained from Telegram.
  - Default Value :- `""`
  - Use :- To connect to Telegram.

- `API_ID`
  - Values :- Valid API ID obtained from Telegram.
  - Default Value :- `0`
  - Use :- To connect to Telegram.

- `BOT_TOKEN`
  - Values :- Valid BOT TOKEN Obtained from Botfather.
  - Default Value :- `""`
  - Use :- To connect to Telegram as BOT.

- `BASE_URL_OF_BOT`
  - Values :- Valid BASE URL of where the bot is deploy. Ip/domain of your bot like "http://myip" or if oy have chosen other port then 80 then "http://myip:port". No slash at the end.
  - Default Value :- `""`
  - Use :- This is used for file selection of the torrent.

- `ALD_USR`
  - Values :- It is a list of IDs of all the allowed groups and useres who can use this bot in private. 
    - To supply multiple IDs in ExecVarsSample.py seperate by comma ','. 
    - To supply multiple IDs from Environemnt variable seperate by spaces.
  - Default Value :- `[]` 
  - Use :- Users and groups with ids here can use the bot.

- `DATABASE_URL` = 
  - Values :- Postgres database URL. Just replace your credentials from below. OR directly Paste the URI you obtained from a database hosting or somewhere else.
  - Default Value :- `dbname=tortk user=postgres password=your-pass host=127.0.0.1 port=5432`
  - Use :- Used to connect to DB. DB is used for many stuff in this bot. 

- `OWNER_ID` = 
  - Values :- Owner's ID
  - Default Value :- `0`
  - Use :- Used to restrict use of certain stuff to owner only. 
	 
<br/> <div align="center">
<b>𝙾𝚙𝚝𝚒𝚘𝚗𝚊𝚕 𝚅𝚊𝚛𝚜:</b>
</div>  

- `GD_INDEX_URL`
  - Values :- Base URL of the index that you are using. (Now that you should include the directory also in URL if you have set `RCLONE_BASE_DIR`). (Dosen't matter if a slash is at the end or not)
  - Default Value :- `False`
  - Use :- Provides an addition Index link for Google Drive Upload.

- `EDIT_SLEEP_SECS`
  - Values :- Seconds to Sleep before edits. Recommended is 40. (If you are using the bot for your own you can try 10 if you get FloodWait Error in LOGS then increase the value) [Can be set from settings menu]
  - Default Value :- `40`
  - Use :- The bot will update the progress regulary after these number of seconds.

- `TG_UP_LIMIT`
  - Values :- Telegram Upload limit in bytes. (you can set max `2147483648` which is ~2GB) [Can be set from settings menu]
  - Default Value :- `1700000000`
  - Use :- The bot will use this value to automatically slice the file bigger that this size into small parts to upload to Telegram.

- `FORCE_DOCUMENTS`
  - Values :- `True`/`False` [Can be set from settings menu]
  - Default Value :- `False`
  - Use :- Should all the upload to telegram be forced as documents or not.

- `COMPLETED_STR`
  - Values :- Any character [Only 1 character] [Can be set from settings menu]
  - Default Value :- `Ⓑ`
  - Use :- Character used to denote completed progress in the progress bar. 


- `REMAINING_STR`
  - Values :- Any character [Only 1 character] [Can be set from settings menu]
  - Default Value :- `○`
  - Use :- Character used to denote remaining progress in the progress bar. 

- `RCLONE_BASE_DIR`
  - Values :- Rclone Base Directory to where stuff should be clonned inside your drive. [Cannot be configured from settings]
  - Default Value :- `"/"`
  - Use :- The bot will upload all the files to that folder in the drive.

- `LEECH_ENABLED`
  - Values :- `True`/`False` [Can be set from settings under control action]
  - Default Value :- `True`
  - Use :- Upload to telegram should be enabled or not.

- `RCLONE_ENABLED`
  - Values :- `True`/`False` [Can be set from settings under control action]
  - Default Value :- `False`
  - Use :- Upload to rclone should be enabled or not.


- `DEFAULT_TIMEOUT`
  - Values :- `"leech"`/`"rclone"`
  - Default Value :- `"leech"`
  - Use :- Default destination (rclone or leech) to choose if the user fails to choose upload destination in 60 seconds.

- `RCLONE_CONFIG`
  - Values :- Path to the RCLONE.conf file [IT IS RECOMMENDED TO SET THIS FROM SETTINGS MENU]
  - Default Value :- `False`
  - Use :- Rclone file path.

- `DEF_RCLONE_DRIVE`
  - Values :- Default Rclone drive from the config file. This is the heading of a config from the file. [IT IS RECOMMENDED TO SET THIS FROM SETTINGS MENU]
  - Default Value :- `""`
  - Use :- Name of the config in the conf file to refer to.

- `MAX_YTPLAYLIST_SIZE`
  - Values :- Max size of a playlist that is allowed (Number of videos) [Can be set from settings menu]
  - Default Value :- `20` 
  - Use :- Stops the user from downloading big playlists.

- `MAX_TORRENT_SIZE`
  - Values :- Max torrent size in GBs that is allowed. [Can be set from settings menu]
  - Default Value :- `10`
  - Use :- Stops the user from downloading big torrents.

- `USER_CAP_ENABLE` : Work in progress
- `USER_CAP_LIMIT` : Work in progress

- `QBitTorrent Configurations`
  - To modify QBT engine Preferences ... Please check `qBittorrent.conf` in root of the repo..
  - To modify Trackers for QBT ... Please check `start.sh` file in root of the repo.. or [click](https://github.com/hey-adithya/BharatTorrentPro-/blob/master/start.sh#L2) to see.

### **Rest Variables are not to be changed**

<details>

  <summary><h3>Bot Commands:<h3></summary>

<br/>

    leech - To Leech a torrent or download a direct link
    ytdl - Donwload YouTube Video
    pytdl - Download YouTube Playlist
    about - About the bot
    ustatus -  To See Your Active Tasks
    status - Status of all the downloads
    server - Get server status
    usettings - User Settings (private also)
    setthumb - Set the thumbnail
    clearthumb - Clear the thumbnail
    speedtest - Testing internet speed host
    settings - Bot Settings For Owner Only🧑🏻‍💻
    pauseall - Pause all torrents For Owner Only🧑🏻‍💻
    resumeall - Resume all torrents For Owner Only🧑🏻‍💻
    purge - Delete all torrents For Owner Only🧑🏻‍💻
    getlogs - Get the robot logs For Owner Only🧑🏻‍💻
  
</details>

<details>
	
  <summary><h3>Credits:<h3></summary>
	
<br/> <div align="center">
	
[Hey-Adithya](https://github.com/hey-adithya) for coordinator

[Yash-DK](https://github.com/yash-dk) Owner of TorToolkit Repository

[AmirulAndalib](https://github.com/AmirulAndalib) for modding

[Lonami](https://github.com/LonamiWebs/Telethon/) for awesome Telethon 

[All the Libraries owner](https://github.com/yash-dk/TorToolkit-Telegram/blob/master/requirements.txt) 
	
</div>
</details>
