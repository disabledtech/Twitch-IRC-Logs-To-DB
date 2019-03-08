<div align="center"><a href="http://g.recordit.co/tjl5YvR0xI.gif"><img src="http://g.recordit.co/tjl5YvR0xI.gif"></a></div>
<h1 align="center">Twitch IRC Logs-to-Database</h1>

<div align="center">
    <p>This script is intended to turn the logs from my <a href="https://github.com/disabledtech/Twitch-IRC-Logger" target="_blank">Twitch IRC Logger</a> into a SQLite database with columns for the timestamp, user, their message, and the channel it was sent in. It can easily be changed to any database supported by <a href="https://www.sqlalchemy.org/" target="_blank">SQLAlchemy</a>.</p>
    <p>3.17 million messages logged over a period of 24 hours monitoring the top 10 channels created a 290mb database file. </p>
</div>

<br/>

<div align="center">
  <a href="http://badges.mit-license.org">
    <img src="http://img.shields.io/:license-mit-blue.svg?style=flat-square)"
      alt="MIT Licence" />
  </a>
</div>

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Support](#support)



---

## Prerequisites

<br/>

- Python <b>3.6</b> or newer.

- <a href="https://www.sqlalchemy.org/" target="_blank">SQLAlchemy</a> is used to store our data in a database.
```
pip install SQLAlchemy
```

---
## Usage

<br/>

Optionally configure the settings in ```config.ini``` however the default settings will work just fine and a config file will be created if it is missing.

1. Run ```log_parse.py``` and the needed subdirectories and a database file will be created in the same directory as the script. 
2. Place the log file(s) you want added to the database in <i>logs_new</i>
3. Run ```logs_parse.py``` again, it will add the data to the database.

### Config.ini Settings

<table>
    <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td><strong>database_name</strong></td>
        <td>The name of the database file.</td>
    </tr>
    <tr>
        <td><strong>new_logs</strong></td>
        <td>The name of the folder where the script will look for log files to process.</td>
    </tr>
    <tr>
        <td><strong>old_logs</strong></td>
        <td>The name of the folder where the script will put log files it has processed.</td>
    </tr> 
</table>
<br/>

---

## Support

Reach out to me at one of the following places if you need help!

- Reddit at <a href="https://www.reddit.com/user/AntiHydrogen" target="_blank">`/u/AntiHydrogen`</a>
- Github at <a href="https://github.com/disabledtech" target="_blank">`disabledtech`</a>


---

## License

MIT License

Copyright (c) 2019 disabledtech

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

