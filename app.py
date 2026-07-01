from flask import Flask, request, send_file


#create Object
app = Flask(__name__)

#ANSI Escape color codes
reset="\033[0m"
bold="\033[1m"
red="\033[38;5;196m"
purple="\033[38;5;93m"
white="\033[38;5;15m"


#curl response in ANSI code
curl_response = f"""
{red}
 ███╗   ██╗██╗   ██╗██╗  ██╗██████╗ ██╗  ██╗
 ████╗  ██║╚██╗ ██╔╝╚██╗██╔╝╚════██╗██║ ██╔╝
 ██╔██╗ ██║ ╚████╔╝  ╚███╔╝  █████╔╝█████╔╝ 
 ██║╚██╗██║  ╚██╔╝   ██╔██╗ ██╔═══╝ ██╔═██╗ 
 ██║ ╚████║   ██║   ██╔╝ ██╗███████╗██║  ██╗
 ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{reset}

{white}Networking // Linux // sysadmin{reset}

{purple}--------------------------------------{reset}

{white}
Hy I'm Nikolas'

I'm 31 years old, from the Dolomites in Italy.

I developed an interest in technology since i was
a little boy, but life redirected me into hospitality.
After a decade in it, i decided to shift my life.

Studying solo in my free time, i developed a strong passion 
for networking, Linux and systems administration.
I've built several IoT devices, few gaming PC, a self-hosted 
Linux server on a Raspberry Pi 5,
learning something new everday.

I will bring strong teamwork ability, flexibility, determination,
and a happy face is always included.

In my free time i like to enjoy nature, i love to swim
and see all the colors in life. But honestly, i'm in front of the screen
testing new things, ideas or whatever is in my mind.

Check out my GitHub account to see what iv`e build so far.
{reset}

{purple}--------------------------------------{reset}

{red}>{reset} github.com/Niy95

"""

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '')
    if 'curl' in user_agent:
        return curl_response, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return send_file('~/Documents/MyDir/github_repos/myWebsite/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
