from Вбудовані import built_math, built_random, built_datetime, built_os, built_sys
from Зовнішні import (
    ext_requests,
    ext_numpy,
    ext_colorama,
    ext_pillow,
    ext_pyfiglet,
    ext_art,
    ext_cowsay,
    ext_schedule,
    ext_cpuinfo,
    ext_speedtest,
)


def main():
    print("=== ВБУДОВАНІ БІБЛІОТЕКИ (5) ===")
    built_math.run_math()
    built_random.run_random()
    built_datetime.run_datetime()
    built_os.run_os()
    built_sys.run_sys()

    print("\n=== ЗОВНІШНІ БІБЛІОТЕКИ (10) ===")
    ext_requests.run_requests()
    ext_numpy.run_numpy()
    ext_colorama.run_colorama()
    ext_pillow.run_pillow()
    ext_pyfiglet.run_pyfiglet()
    ext_art.run_art()
    ext_cowsay.run_cowsay()
    ext_schedule.run_schedule()
    ext_cpuinfo.run_cpuinfo()
    ext_speedtest.run_speedtest()


if __name__ == "__main__":
    main()