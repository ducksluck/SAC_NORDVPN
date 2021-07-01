# SAC_NordVPN:  An OpenVPN config scraper and random connection tool
This is a Python solution to help randomize VPN servers which users connect to and automate the downloading process from NordVPN's endless wall of text. 

Features:
   -SAC_NordVPN can scrape all configs, specified countries, and double-VPN country pairs. 
   -Script can manage connections by launching OpenVPN and killing existing OVPN processes. 
   -Color scheme can be changed.
   -Users can download TCP, UPD or both.
   -Downloads are threaded and max workers can be adjusted as needed. Downloading all 10,000+ servers takes approximately 20 minutes even with threading. NordVPN has a limit for downloads in a given minute. (approx 30 workers hits the max allotment)  If the limit is reached the config will be corrupt (contains a warning message only). These corrupted files will automatically be purged and downloaded agian. 

**CREDENTIALS ARE NOT MANAGED FOR SECURITY REASONS & PEACE OF MIND**
Yes, you still need to manually type in your creds as such.

[![SAC_NordVPN_Menu](https://github.com/ducksluck/SAC_NordVPN/blob/main/Menu.PNG)](#Menu)

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
[![SAC_NordVPN_Countries](https://github.com/ducksluck/SAC_NordVPN/blob/main/Countries.PNG)](#Countries)
  

[![SAC_NordVPN_DoubleVPNs](https://github.com/ducksluck/SAC_NordVPN/blob/main/DoubleVPNs.PNG)](#DoubleVPNs)
 

Any thoughts or feedback is appreciated.
