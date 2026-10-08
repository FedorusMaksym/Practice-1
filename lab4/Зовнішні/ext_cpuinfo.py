import cpuinfo

def run_cpuinfo():
    info = cpuinfo.get_cpu_info()
    print("Модель процесора:", info.get("brand_raw", "Не визначено"))