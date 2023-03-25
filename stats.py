
options = {
    "measure_temp": ["temp", "'C"],
    "get_mem gpu": ["gpu", "M"],
    "get_mem arm": ["arm", "M"],
    "measure_clock core": ["frequency(1)", ""],
    "measure_clock arm": ["frequency(48)", ""],
    "measure_clock v3d": ["frequency(46)", ""],
    "measure_volts core": ["volt", "V"],
    "measure_volts sdram_c": ["volt", "V"],
    "measure_volts sdram_i": ["volt", "V"],
    "measure_volts sdram_p": ["volt", "V"],
    "get_throttled": ["throttled", "x0"],
}


def vcgencmd(option):
    """
        https://elinux.org/RPI_vcgencmd_usage
        https://github.com/nezticle/RaspberryPi-BuildRoot/wiki/VideoCore-Tools
    """
    if option in options:
        cmd = "/opt/vc/bin/vcgencmd {}".format(option)
        Domoticz.Debug("cmd: {}".format(cmd))
        try:
            res = os.popen(cmd).readline()
            Domoticz.Debug("res: {}".format(res))
            res = res.replace("{}=".format(options[option][0]), "")
            res = res.replace("{}\n".format(options[option][1]), "")
            Domoticz.Debug("res (replaced): {}".format(res))
        except:
            res = "0"
    else:
        res = "0"
    return float(res)


# --------------------------------------------------------------------------------

global _last_idle, _last_total
_last_idle = _last_total = 0


def getBits(value, start, length):
    return (value >> start) & 2 ** length - 1


def getClock(p):
    Domoticz.Debug("getClock p: {}".format(p))
    if p in [
        "arm",
        "core",
        "dpi",
        "emmc",
        "h264",
        "hdmi",
        "isp",
        "pixel",
        "pwm",
        "uart",
        "v3d",
        "vec",
    ]:
        res = vcgencmd("measure_clock {}".format(p))
        Domoticz.Debug("getClock measure_clock: {}".format(res))
    else:
        Domoticz.Debug("getClock: Invalid parameter")
        res = "0"
    return int(res)


def getCPUcount():
    return os.cpu_count()


def getCPUcurrentSpeed():
    # Return CPU speed in Mhz
    try:
        res = os.popen(
            "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"
        ).readline()
    except:
        res = "0"
    return round(int(res) / 1000)


def getCPUtemperature():
    # Return CPU temperature
    try:
        res = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    except:
        res = "0"
    return round(float(res) / 1000, 1)


def getCPUuptime():
    try:
        with open("/proc/uptime") as f:
            fields = [float(column) for column in f.readline().strip().split()]
        res = round(fields[0])
    except:
        res = 0.0
    return res


def getCPUuse():
    """
        Return % of CPU used by user
        Based on: https://rosettacode.org/wiki/Linux_CPU_utilization#Python
    """
    global _last_idle, _last_total
    try:
        with open("/proc/stat") as f:
            fields = [float(column) for column in f.readline().strip().split()[1:]]
        idle, total = fields[3], sum(fields)
        idle_delta, total_delta = idle - _last_idle, total - _last_total
        _last_idle, _last_total = idle, total
        res = round(100.0 * (1.0 - idle_delta / total_delta), 2)
    except:
        res = 0.0
    return res


def getDomoticzMemory():
    # ps aux | grep domoticz | awk '{sum=sum+$6}; END {print sum}'
    try:
        res = (
            os.popen("ps aux | grep domoticz | awk '{sum=sum+$6}; END {print sum}'")
            .readline()
            .replace("\n", "")
        )
    except:
        res = "0"
    return float(res)


def getGatewayLatency():
    try:
        gateway = (
            os.popen("route -n | awk '$1 == \"0.0.0.0\" { print $2 }'")
            .readline()
            .strip()
        )
        rtt = (
            os.popen("ping -c1 {} | grep rtt".format(gateway))
            .readline()
            .split()[3]
            .split("/")[0]
        )
    except:
        rtt = "0"
    return float(rtt)


def getGPUtemperature():
    # Return GPU temperature
    return float(vcgencmd("measure_temp"))


def getHostname():
    return socket.gethostname()


def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 1))
    except socket.error:
        return None
    return s.getsockname()[0]


def getIP6():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    try:
        s.connect(("2001:4860:4860::8888", 1))
    except socket.error:
        return None
    return s.getsockname()[0]


def getMemory(p):
    if p in ["arm", "gpu"]:
        res = vcgencmd("get_mem {}".format(p))
    else:
        res = "0"
    return float(res)


def getNetworkConnections(state):
    # Return number of network connections
    res = 0
    try:
        for line in os.popen("netstat -tun").readlines():
            if line.find(state) >= 0:
                res += 1
    except:
        res = 0
    return res


def getPiRevision():
    try:
        res = (
            os.popen("cat /proc/cpuinfo | grep Revision\t")
            .readline()
            .replace("\n", "")
            .split(":")[1]
            .strip()
        )
        # Convert hex to int
        res = int(res, 16)
    except:
        res = None
    return res


def getRAMinfo():
    # Return RAM information in a list
    # Based on: https://gist.github.com/funvill/5252169
    p = os.popen("free -b")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            res = line.split()[1:4]
            # Index 0: total RAM
            # Index 1: used RAM
            # Index 2: free RAM
            return round(100 * int(res[1]) / int(res[0]), 2)


# http://www.microcasts.tv/episodes/2014/03/15/memory-usage-on-the-raspberry-pi/
# https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=164787
# https://stackoverflow.com/questions/22102999/get-total-physical-memory-in-python/28161352
# https://stackoverflow.com/questions/17718449/determine-free-ram-in-python
# https://www.reddit.com/r/raspberry_pi/comments/60h5qv/trying_to_make_a_system_info_monitor_with_an_lcd/


def getThrottled():
    return int(vcgencmd("throttled"))


def getUpStats():
    # Get uptime of RPi
    # Based on: http://cagewebdev.com/raspberry-pi-showing-some-system-info-with-a-python-script/
    # Returns a tuple (uptime, 5 min load average)
    try:
        s = os.popen("uptime").readline()
        load_split = s.split("load average: ")
        up = load_split[0]
        up_pos = up.rfind(",", 0, len(up) - 4)
        up = up[:up_pos].split("up ")[1]
        return up
    except:
        return ""


def getVoltage(p):
    # Get voltage
    # Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=30697
    if p in ["core", "sdram_c", "sdram_i", "sdram_p"]:
        res = vcgencmd("measure_volts {}".format(p))
    else:
        res = "0"
    return float(res)