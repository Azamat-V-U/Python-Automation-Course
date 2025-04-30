import os
import platform
from subprocess import run
from collections import defaultdict
from datetime import datetime


def report_parser():
    result = run("ps aux", shell=True, capture_output=True, text=True)
    assert result.returncode == 0, f"Actual code: {result.stderr}"
    lines = result.stdout.strip().split("\n")

    headers = lines[0].split()
    data_lines = lines[1:]

    users = set()
    user_processes = defaultdict(int)
    total_memory = 0.0
    total_cpu = 0.0

    max_mem = {'value': 0.0, 'command': ''}
    max_cpu = {'value': 0.0, 'command': ''}

    for line in data_lines:
        columns = line.split(None, len(headers) -1)
        if len(columns) < len(headers):
            continue
        user, cpu, mem, command = columns[0], float(columns[2]), float(columns[3]), columns[10]

        users.add(user)
        user_processes[user] += 1
        total_memory += mem
        total_cpu += cpu

        if mem > max_mem["value"]:
            max_mem = {"value": mem, "command": command[:20]}
        if cpu > max_cpu["value"]:
            max_cpu = {"value": cpu, "command": command[:20]}

    hw_details = (
        f"Node: {platform.node()}\n"
        f"Processor: {platform.processor()}\n"
        f"System: {platform.system()}\n"
        f"CPU: {os.cpu_count()}\n"
        f"Release: {platform.release()}\n"
        f"Version: {platform.version()}\n"
    )

    report_lines = [
        "Отчет о состоянии системы: ",
        f"{hw_details}",
        "Пользователи системы: ",
        f"{', '.join(sorted(users))}",
        "",
        f"Процессов запущено:  {len(data_lines)}",
        "",
        "Пользовательских процессов: ",
        ""
    ] + [
        f"{user} : {count}" for user, count in sorted(user_processes.items())
    ] + [
        "",
        f"Всего памяти используется : {total_memory:.1f}%",
        "",
        f"Всего CPU используется : {total_cpu:.1f}%",
        "",
        f"Больше всего памяти использует : ({max_mem['command']})",
        "",
        f"Больше всего CPU использует : ({max_cpu['command']})",
        ""
    ]

    report = "\n".join(report_lines)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"system_report_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(report)


report_parser()
