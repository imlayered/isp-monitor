# ISP Monitor
Monitor if your homelab's public connection dies

This will ping a site of your choice every few seconds as a keep-alive. If connection fails it will start a stopwatch until connection resumes and send outage times to a Discord webhook.


## Install steps
(Debian & Ubuntu | **You must be logged in as root**)
1. Make sure Python is installed using ``python -V``. If this doesn't return something similar to "Python x.x.x" Please run ``sudo apt update && sudo apt upgrade -y && sudo apt install python3 -y``, then rerun ``python -V``
2.  Run ```mkdir /isp-monitor && curl -o /isp-monitor/main.py https://raw.githubusercontent.com/imlayered/isp-monitor/main/main.py && curl -o /isp-monitor/config.json https://raw.githubusercontent.com/imlayered/isp-monitor/main/config.json```
3. Configure your ``config.json`` file. Make sure you modify the Discord webhook URL.
4. Grab [isp-monitor.service](https://github.com/imlayered/isp-monitor/blob/main/isp-monitor.service) and run ``nano /etc/systemd/system/isp-monitor.service``, then paste the code into that file. Hit control+O to save, then control+X to return to console.
5. Run ``systemctl enable isp-monitor && systemctl start isp-monitor && systemctl status isp-monitor``
6. (Optional, but greatly appreaciated) Star the repo. You are now done 🎊
