def _get_3_bytes_of_lan_ip_addr() -> str:  # get ip4 of lan network
    """ возвращает локальный айпи тачки, типа: '192.168.0.'
    >>> _get_3_bytes_of_lan_ip_addr()
    '192.168.0.'
    """
    from socket import socket, AF_INET, SOCK_DGRAM
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(('255.255.255.255', 0))  # connect('any.random.ip.addr', anyRandomPort) for UDP doesn't send packets
    local_ip_address_str: str = sock.getsockname()[0]  # получаем локальный айпи адрес источника
    sock.close()
    three_bytes_of_ip: str = local_ip_address_str[0:local_ip_address_str.rfind('.')+1]  # удаляем из строки локального адреса последний октет
    return three_bytes_of_ip


def _scan_lan_for_get_full_ip(three_bytes_of_ip: str) -> str:  # scan all_lan_for_get_ip
    """ перебирает все хосты сети ip, если найден рп-возвращает его адрес(либо 3_bytes_of_lan_ip_addr, если не найдет)"""
    from os import popen  # ищем в арп-таблице по маку (это быстро)
    with popen('arp -a') as f:
        raw_arp_data: str = f.read()

    from re import findall
    mac_pattern: str = "70-f1-1c-"
    search_mask: str = r'\s+(' + three_bytes_of_ip + r'\d+)\s+' + mac_pattern + r'[-0-9a-f]{8}'
    for arp_data_ip in findall(search_mask, raw_arp_data):
        if _these_host_is_a_robot(arp_data_ip):
            return arp_data_ip

    for last_octet_ip in range(1, 255):  # а если не нашли,брутим локалку по айпи от х.х.х.1 до х.х.х.255  (это долго)
        host = three_bytes_of_ip + str(last_octet_ip)
        if _these_host_is_a_robot(host):
            return host

    return three_bytes_of_ip  # а если не нашли , -> 192.168.0.


def _these_host_is_a_robot(normal_ip4: str) -> bool:
    """ проверяет, ip4 - это рп или нет. возвращает True или False """
    from socket import socket, AF_INET, SOCK_STREAM
    shure_these_robot_ip: int = 0
    robot_ports: tuple = (5556, 30001, 30002, 30003)
    for trying_port in robot_ports:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect((normal_ip4, trying_port))
        except:
            sock.close()
            # return False => host is NOT robot
        else:
            sock.close()
            shure_these_robot_ip += 1
            # return True => host is robot
    if shure_these_robot_ip >= len(robot_ports)-1:
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
