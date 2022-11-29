import subprocess, re
from run import runYTS
# ytsCommand = ["yts", "cert", "37", "--test-version=dev", "--user-agent=Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/20221123 (lgBreadB, lgBreadM, Wired)", "--nonprod-api", "--verbose", "--json-output=test.json"] 
# print(ytsCommand[4])
co = "--user-agent=Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/20221123 (lgBreadB, lgBreadM, Wired"
new = re.findall(r"\([a-zA-Z0-9].+?\)", co)
b = subprocess.check_output("curl https://dev.yts.devicecertification.youtube/version", shell=True)
c = (new + [b])
# print(c[2])
ytsCommand =subprocess.run(["yts", "cert", "37", "--test-version=dev", {},"--json-output=test.json".format(co)], shell=True)
subprocess.run([ytsCommand], shell=True)

# def windowsRun(ytscommand):
# ytscommand = f""" yts cert 37 --test-version=dev --user-agent="Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/20221123 (lgBreadB, lgBreadM, Wired)"
#  """, "--nonprod-api --no-colors --retry-failed=2" 
#     subprocess.call(ytscommand, shell=True)
#     return windowsRun

# def winRun():
#     windowsRun()
# subprocess.run(['yts', 'discover'], shell=True)
# subprocess.Popen([ytscommand], shell=True)
# subprocess.call(f"""echo {ytscommand}'\n\n\n\n' """, shell=True)
# subprocess.run(["yts", "cert", "37", "--test-version=dev", "--user-agent=Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/20221123 (lgBreadB, lgBreadM, Wired)", "--nonprod-api", "--verbose"], shell=True)
#  hisense = subprocess.run(["yts", "test", "fb", "' '"], capture_output=True, shell=True)
                #  yts cert 37 --test-version=dev --user-agent="Mozilla/5.0 (webOS.TV-2022) Cobalt/22.lts.2.305573-gold (unlike Gecko) v8/8.8.278.8-jit gles Starboard/13, LG_TV_LM21AN_2022/20221123 (lgBreadB, lgBreadM, Wired)" --nonprod-api