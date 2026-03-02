from sys import stdin, stdout, stderr

if stdin.isatty():

    stderr.write("Вводите IP-адресы или доменты построчно или через пробел\n<CTRL+D> для завершения ввода\n")
    ips = stdin.read().split()

    stderr.write("\nВведите hostname\n")
    hostname = stdin.read().repalce("\n", "")
else:
    
    hostname = stdin.readline().replace("\n", "")

    ips = stdin.read().split()


stdout.write("[\n")

for i in range(len(ips)):
    stdout.write("  {\n")
    stdout.write(f"     \"hostname\":\"{hostname}-{i}.com\",\n")
    stdout.write(f"     \"ip\":\"{ips[i]}\"\n")
    stdout.write("  },\n" if i != len(ips)-1 else " }\n")

stdout.write("]")