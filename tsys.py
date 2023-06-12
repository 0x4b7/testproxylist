
def gen_pin (mac_str):
    pin = int(mac_str[6:12], 16) % 10000000

# WPS PIN Checksum - for more information see hostapd/wpa_supplicant source (wps_pin_checksum) or
# http://download.microsoft.com/download/a/f/7/af7777e5-7dcd-4800-8a0a-b18336565f5b/WCN-Netspec.doc
    accum = 0
    t = pin
    while (t):
        accum += 3 * (t % 10)
        t /= 10
        accum += t % 10
        t /= 10
        print(accum,t)
    return '%07i%i' % (pin, (10 - accum % 10) % 10)

print(gen_pin('A8423231DC09'))