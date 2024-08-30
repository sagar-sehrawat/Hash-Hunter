#!/usr/bin/env python3

import hashlib
import argparse
import sys
import threading
import time 
from colorama import Fore, Style, init


init()

def print_author_info():
    author_info = """
    Author: Sagar Sehrawat
    GitHub: https://github.com/sagar-sehrawat/Hash-Hunter
    """
    print(Fore.YELLOW + author_info + Style.RESET_ALL)

def hash_identifier(length):
    if length == 32:
        return hashlib.md5
    elif length == 40:
        return hashlib.sha1
    elif length == 56:
        return hashlib.sha224
    elif length == 64:
        return hashlib.sha256
    elif length == 96:
        return hashlib.sha384
    elif length == 128:
        return hashlib.sha512
    elif length == 64:  
        return hashlib.blake2s
    elif length == 128:  
        return hashlib.blake2b
    elif length == 56:  
        return hashlib.sha3_224
    elif length == 64:  
        return hashlib.sha3_256
    elif length == 96:  
        return hashlib.sha3_384
    elif length == 128:  
        return hashlib.sha3_512
    else:
        return None

def rotating_animation():
    spinner = ['|', '/', '-', '\\']
    while not exit_event.is_set():
        for symbol in spinner:
            sys.stdout.write(f'\r{Fore.YELLOW}Processing {symbol}{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(0.1)

def file_passwords(hash_file, wordlist_file, verbose):
    with open(hash_file, 'r') as file:
        hashes = [line.strip() for line in file]

    with open(wordlist_file, 'r') as pas:
        passwords = [line.strip() for line in pas]

    for idx, target_hash in enumerate(hashes):
        hash_length = len(target_hash)
        hash_func = hash_identifier(hash_length)

        if hash_func is None:
            print(Fore.RED + "Unsupported hash length: " + str(hash_length) + Style.RESET_ALL)
            continue

        print(Fore.YELLOW + f"Cracking hash: {target_hash}" + Style.RESET_ALL)
        
        global exit_event
        exit_event = threading.Event()
        animation_thread = threading.Thread(target=rotating_animation)
        animation_thread.start()

        found = False
        for password in passwords:
            pass_byte = password.encode('utf-8')
            hash_object = hash_func()
            hash_object.update(pass_byte)
            hash_pass = hash_object.hexdigest()

            if verbose:
                print(Fore.CYAN + f"Trying password: {password}" + Style.RESET_ALL)

            if hash_pass == target_hash:
                print(Fore.GREEN + f"Password found: {password}" + Style.RESET_ALL)
                found = True
                break
        
        exit_event.set()
        sys.stdout.write('\r')
        sys.stdout.flush()
        animation_thread.join()  

        if not found:
            print(Fore.RED + "Password not found for hash: " + target_hash + Style.RESET_ALL)
        
        if idx < len(hashes) - 1:
            sys.stdout.write('\n')  

def main():
    parser = argparse.ArgumentParser(description='Crack hashed Using a passwords wordlist.')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file.')
    parser.add_argument('-f', '--hashfile', required=True, help='Path to the file containing the target hashes.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    
    args = parser.parse_args()

    print_author_info()
    file_passwords(args.hashfile, args.wordlist, args.verbose)

if __name__ == '__main__':
    main()
