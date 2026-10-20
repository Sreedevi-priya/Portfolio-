# build.py  (simple version)
# Step 1: change the words in quotes below
# Step 2: run  python build.py
# Step 3: open index.html in your browser

# ---------- 1. YOUR INFO (edit the words inside the quotes) ----------
name = "Sreedevi priya"
tagline = "Computer science student. AI, robotics and building things."
intro = "First-year computer science student at BMS College of Engineering, Bengaluru. I love AI and robotics, and I learn by building."
about = "I tried a few paths before computer science. Robotics pulled me in because it is where code meets the real world. I am building my skills one project at a time."
discord = "itz_wizzy_."

# ---------- 2. YOUR PAGE ----------
# This is the web page. The @@WORDS@@ get replaced by your info above.
# Your projects are written right here. To add one, copy a whole project box.
page = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>@@NAME@@ | Portfolio</title>

  <style>
    body {
      background: #1B1F1E;      /* page color */
      color: #EFE6D8;           /* text color */
      font-family: Georgia, serif;
      line-height: 1.7;
      max-width: 640px;
      margin: 0 auto;
      padding: 40px 20px;
    }
    h2 { color: #E6C58C; margin-top: 50px; }        /* gold headings */
    p { color: #B5B0A3; }
    a { color: #E6C58C; }

    .avatar { width: 140px; height: 140px; border-radius: 50%; }

    .project {
      background: #262B29;      /* box color */
      border-radius: 16px;
      padding: 16px 22px;
      margin-bottom: 16px;
    }
    .project img { width: 100%; border-radius: 10px; }
    .label { color: #C58B84; font-size: 14px; }     /* "Still building" */
  </style>
</head>

<body>
  <img class="avatar" src="@@PROFILE@@">
  <h1>@@NAME@@</h1>
  <p>@@TAGLINE@@</p>
  <p>@@INTRO@@</p>

  <h2>Projects</h2>

  <!-- PROJECT 1 -->
  <div class="project">
    <h3>Notes-to-Quiz <span class="label">Still building</span></h3>
    <p>Paste your notes and an AI turns them into a quiz.</p>
  </div>

  <!-- PROJECT 2 -->
  <div class="project">
    <img src="@@ROBOT@@">
    <h3>Desk robot</h3>
    <p>A small desk companion built on an ESP32 board. This is its first face, shown on an OLED screen.</p>
    <a href="https://github.com/your-username/desk-robot">View on GitHub</a>
  </div>

  <h2>About</h2>
  <p>@@ABOUT@@</p>

  <h2>Contact</h2>
  <p>Message me on Discord: @@DISCORD@@</p>
</body>
</html>
"""

# ---------- 3. FILL IN THE BLANKS AND SAVE (you don't need to touch this) ----------
page = page.replace("@@NAME@@", name)
page = page.replace("@@TAGLINE@@", tagline)
page = page.replace("@@INTRO@@", intro)
page = page.replace("@@ABOUT@@", about)
page = page.replace("@@DISCORD@@", discord)

# Put the pictures INSIDE index.html, so they always show.
# (The picture files must be in the same folder as build.py when you run it.)
import base64
profile_data = base64.b64encode(open("profile.jpg", "rb").read()).decode()
robot_data = base64.b64encode(open("desk-robot.jpg", "rb").read()).decode()
page = page.replace("@@PROFILE@@", "data:image/jpeg;base64," + profile_data)
page = page.replace("@@ROBOT@@", "data:image/jpeg;base64," + robot_data)

open("index.html", "w", encoding="utf-8").write(page)
print("Done! Open index.html")
