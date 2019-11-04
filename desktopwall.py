import subprocess
subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/day_clould.jpg"), shell=True)
