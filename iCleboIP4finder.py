def _get_3_bytes_of_lan_ip_addr() -> str:  # get ip4 of lan network
    """ возвращает локальный айпи тачки, типа: '192.168.0.'
    >>> _get_3_bytes_of_lan_ip_addr()
    '192.168.0.'
    """
    from socket import socket, AF_INET, SOCK_DGRAM
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(('255.255.255.255', 0))  # connect('any.random.ip.addr', anyRandomPort) for UDP doesn't send packets
    local_ip_address_str = sock.getsockname()[0]  # получаем локальный айпи адрес источника
    sock.close()
    ip4 = local_ip_address_str[0:local_ip_address_str.rfind('.')+1]  # удаляем из строки локального адреса последний октет
    return ip4


def _scan_lan_for_get_full_ip(ip: str) -> str:  # scan all_lan_for_get_ip
    """ перебирает все хосты сети ip, если найден рп-возвращает его адрес(либо 3_bytes_of_lan_ip_addr, если не найдет)"""
    from os import popen  # ищем в арп-таблице по маку (это быстро)
    with popen('arp -a') as f:
        raw_arp_data = f.read()
    list_of_ips: list = []
    from re import findall, search
    mac_pattern = "70-f1-1c-"

    for (arp_data_ip, arp_data_mac) in findall('('+ip+r'[0-9])+\s+('+mac_pattern+r'[-0-9a-f]{8})', raw_arp_data):
        list_of_ips.append(arp_data_ip)  # ...а если не нашли...

    if not list_of_ips:  # брутим локалку по айпи от х.х.х.1 до х.х.х.255  (это долго)
        for last_octet_ip in range(1, 255):
            host = ip + str(last_octet_ip)
            if _these_host_is_a_robot(host):
                ip = host
                break
            else:
                continue
        return ip
    else:
        ip = list_of_ips[0]
        return ip


def _these_host_is_a_robot(ip4: str) -> bool:
    """ проверяет, ip4 - это рп или нет. возвращает True или False """
    from socket import socket, AF_INET, SOCK_STREAM
    shure_these_robot_ip: int = 0

    for trying_port in (5556, 30001, 30002, 30003):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect((ip4, trying_port))
        except:
            sock.close()
            # return False
        else:
            sock.close()
            shure_these_robot_ip += 1
            # return True
    if shure_these_robot_ip >= 3:
        return True
    else:
        return False


def get_ip() -> str:
    """Return iClebo_O5 LAN IP4 address
    >>> get_ip()
    '192.168.0.4'
    """
    return _scan_lan_for_get_full_ip(_get_3_bytes_of_lan_ip_addr())


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    exit(0)
