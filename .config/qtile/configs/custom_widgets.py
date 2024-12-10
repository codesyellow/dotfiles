import psutil
import shutil
# from .variables import home

CPU_ICON = ""
CPU_TEMP_ICON = ""
MEM_ICON = ""
ROOT_ICON = ""
HOME_ICON = ""
HDD_ICON = ""


def is_process_running(process_name):
    return process_name in (p.name() for p in psutil.process_iter())


def get_pango(icon_args, info_args):
    bar = "<span size='x-large' foreground='#4c566a'>|</span>"
    icon = f"<span size='{icon_args[0]}' foreground='#EF5A6F' rise='{
        icon_args[1]}'>{icon_args[2]}</span>"
    output = f"{bar} {icon} <span rise='{
        info_args[0]}' foreground='#EF5A6F'>{info_args[1]}</span>"
    return output


def cpu_temp():
    temperature = int(psutil.sensors_temperatures()["coretemp"][0][1])
    if temperature >= 80:
        return get_pango([13000, 5550, CPU_TEMP_ICON],
                         [3800, f"{temperature}°"])


def cpu_usage():
    cpu_usage = int(psutil.cpu_percent(2))
    if cpu_usage > 80:
        return get_pango(icon_args=[13500, 5400, CPU_ICON],
                         info_args=[3800, f"{cpu_usage}%"])


def mem_usage():
    mem_usage = int(psutil.virtual_memory()[2])
    if mem_usage > 80:
        return get_pango([12500, 4200, MEM_ICON], [3800, f"{mem_usage}%"])


def root_space():
    total, used, free = shutil.disk_usage("/")
    total_free = free // (2**30)
    if total_free <= 10:
        return get_pango([12500, 5900, ROOT_ICON], [3800, f"{total_free}G"])


def home_space():
    total, used, free = shutil.disk_usage("/home")
    total_free = free // (2**30)
    if total_free <= 10:
        return get_pango([12500, 2800, HOME_ICON], [2500, f"{total_free}G"])


def hdd_space():
    total, used, free = shutil.disk_usage("/home/digo/.HDD")
    total_free = free // (2**30)
    if total_free <= 30:
        return get_pango([22500, 220, HDD_ICON], [3800, f"{total_free}G"])


def easyeffects_is_on():
    pass
