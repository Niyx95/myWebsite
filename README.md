# nyx2k.sh
creation of my website

## Progress Log

### Phase1 -- Initial Setup and purchase of domain
- bought a domain trough Namecheap
- set DNS with Cloudflare
- changed nameserver 

### Phase2 -- main page creation
- Write HTML/CSS of main page
- logo by freelancer
- tested many design

### Phase3 -- curl/https, tunneling and dns records
- installed and reconfigured unattened pachages
- installed Flask via pip3
- creation of  app.py with ANSI escape code
- testing curl on locahost
- installed cloudflared tunnel and setup of DNS records
- set up CNAME record

### Phase4 -- final settings
- redesign of file structure
- set up systemd service to run from boot

## Issues
**At the first i thought to go with apache2 and i did install it and run the http request via apache.
Later on when started to write the curl 
i figured out i could have done all by using Flask, so i redesigned everything. Using Cloudflares was 
also a challange, i learned a lot about networking and DNS record especially.**
