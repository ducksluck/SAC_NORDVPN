# SAC_NordVPN:  An OpenVPN config scraper and random connection tool
This a python solution to help randomize VPN servers users connect to.  
Scrapes all NordVPN's OpenVPN configs and threads downloads. Downloading all 10,000+ servers takes approximately 20 minutes even with threading.  
Users can select a country of preferece as well as double-VPN country pairs. Script launches OpenVPN as subprocess to handle login credentials as usual. 

[![SAC_NordVPN_Menu](https://github.com/ducksluck/SAC_NordVPN/Menu.PNG)](#Menu)

**Requirements**  
 1) Python must be installed and a IDE such as pyCharm
 2) OpenVPN must be installed  
 3) You must have a NordVPN account. (that is if you wish to connect. )  
 4) Install 'Requests' and 'Beautifulsoup' using the following commands using admin cmdline within location of pip3 (likely:  %localappdata%\Programs\Python\Python39\Scripts)
	- pip3 install beautifulsoup4
	- pip3 install requests
 

**First Use**  

 1) Launch your python IDE as admin (or cmommand prompt) and run menu.py
 2) Select an option to download configs.  The reason for purging old configs is to ensure that you are attempting to connect to a valid server that is in fact still in operation by NordVPN.  
 3) Connect either to a randoom, selected country, or double vpn server.
 4) If you don't like the colors change them. Changed color preferences persist after restart.

*Note:  The option 'Download: All Configs' has an option within to increase worker threads. Although it would be nice to have 100 threads downloading these configs at a time nordVPN servers will only allow so many downloads within a given period of time. If that limit is exceeded they will serve a smaller corrupt config file containing a warning that a limit has been reached. ( *shakes head* They could just provide us with an option to download a zip of all the configs. It's only ~28MB UNCOMPRESSED) Recommended number for max threads is 30-40. It could take about 17 mins to download the 10,600+ configs (TCP and UDP).  


**Show Countries and Double VPNS**    
[![SAC_NordVPN_Countries](https://github.com/ducksluck/SAC_NordVPN/Countries.PNG)](#Countries)
  

[![SAC_NordVPN_DoubleVPNs](https://github.com/ducksluck/SAC_NordVPN/DoubleVPNs.PNG)](#DoubleVPNs)
 

Any thoughts or feedback is appreciated.
