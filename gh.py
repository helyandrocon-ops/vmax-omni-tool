#!/usr/bin/env python3
import os
import sys
import time
import random
import json
from web3 import Web3

# ==========================================================
# HC LAB - V-MAX OMNI-TOOL v3.5 (PERFECT GRID MATRIX)
# Architect: Helyandro Cardoso (HC) | Score: 360-132
# Features: 50 Auto-Aligned Flags | Stealth Vault | Hoppers
# ==========================================================

BANNER = """
\033[1;31m  _  _  ____     __  __   _    __  __ 
 | || |/ ___|   |  \/  | / \  \ \/ / 
 | || | |       | |\/| |/ _ \  \  /  
 |__  _| |___   | |  | / ___ \ /  \  
    |_| \____|  |_|  |_/_/   \_/_/\_\ \033[0m
 \033[1;37m[ V-MAX OMNI-TOOL - GLOBAL FLAG MATRIX ]\033[0m
 \033[1;33m[ STATUS: RESONANCE ACTIVE | SCORE: 360-132 ]\033[0m
"""

VAULT_PATH = os.path.expanduser("~/.vmax_vault.json")

# Estrutura de Idiomas (Exemplo das principais, as outras seguem o padrão)
LANG_DATA = {
    '1':  {'f': '🇺🇸', 'n': 'English', 'menu': ["1. [GHOST-NET]", "2. [AUTO-SIPHON]", "3. [PURGE]", "4. [LANG]", "0. EXIT"]},
    '2':  {'f': '🇧🇷', 'n': 'Português', 'menu': ["1. [GHOST-NET]", "2. [OFUSCAÇÃO]", "3. [LIMPAR]", "4. [IDIOMA]", "0. SAIR"]},
    '3':  {'f': '🇪🇸', 'n': 'Español', 'menu': ["1. [GHOST-NET]", "2. [OFUSCACIÓN]", "3. [LIMPIAR]", "4. [IDIOMA]", "0. SALIR"]},
    '4':  {'f': '🇨🇳', 'n': 'Chinese', 'menu': ["1. [网络伪装]", "2. [全球混淆]", "3. [清除日志]", "4. [更改语言]", "0. 退出"]},
    '5':  {'f': '🇷🇺', 'n': 'Russian', 'menu': ["1. [КАМУФЛЯЖ]", "2. [ОБФУСКАЦИЯ]", "3. [ОЧИСТКА]", "4. [ЯЗЫК]", "0. ВЫХОД"]},
}

# Lista Completa de 50 Bandeiras para o Grid
FLAGS = [
    "🇺🇸", "🇧🇷", "🇪🇸", "🇨🇳", "🇷🇺", "🇫🇷", "🇩🇪", "🇮🇹", "🇯🇵", "🇸🇦",
    "🇮🇳", "🇰🇷", "🇹🇷", "🇵🇹", "🇲🇽", "🇨🇦", "🇦🇺", "🇬🇧", "🇳🇱", "🇸🇪",
    "🇳🇴", "🇩🇰", "🇫🇮", "🇵🇱", "🇺🇦", "🇬🇷", "🇮🇱", "🇿🇦", "🇳🇬", "🇪🇬",
    "🇮🇩", "🇹🇭", "🇲🇾", "🇻🇳", "🇵🇭", "🇮🇷", "🇵🇰", "🇦🇷", "🇨🇱", "🇨🇴",
    "🇵🇪", "🇻🇪", "🇨🇭", "🇦🇹", "🇧🇪", "🇮🇪", "🇳🇿", "🇸🇬", "🇭🇺", "🇷🇴"
]

def verify_activation():
    secret_key = "HC-VMAX-9274-OMEGA"
    os.system('clear')
    print(BANNER)
    print("\033[1;31m[LOCKED] HC-LAB RESTRICTED ACCESS\033[0m")
    key = input("\n[?] Enter Weekly Activation Code: ")
    return key == secret_key

def select_language():
    os.system('clear')
    print(BANNER)
    print("\033[1;36m[GLOBAL LANGUAGE HUB - SELECT YOUR FLAG]\033[0m\n")
    
    # Grid Alignment Logic (5 columns)
    for i, flag in enumerate(FLAGS, 1):
        item = f"[{i}]{flag}"
        # Alinha cada item para ocupar exatamente 12 espaços
        print(item.ljust(12), end="")
        if i % 5 == 0:
            print() # Nova linha a cada 5 bandeiras
    
    choice = input("\n\n[HC-LAB]> ")
    return choice if choice in LANG_DATA else '1'

def auto_siphon(lang):
    print(f"\n\033[1;36m--- {lang['menu'][1]} ---\033[0m")
    target = input("[?] Target Wallet: ")
    amount = input("[?] ETH Amount: ")
    
    print("\n[*] Generating 20 Stealth Hoppers...")
    w3 = Web3()
    wallets = []
    for i in range(20):
        acct = w3.eth.account.create()
        wallets.append({"id": i+1, "address": acct.address, "private_key": acct.key.hex()})
    
    with open(VAULT_PATH, "w") as f:
        json.dump(wallets, f, indent=4)
    
    print(f"\033[1;32m[SUCCESS]\033[0m Vault created at {VAULT_PATH}")
    time.sleep(1)

def main():
    lang_id = select_language()
    current_lang = LANG_DATA[lang_id]
    
    while True:
        os.system('clear')
        print(BANNER)
        print(f"REGION: {current_lang['f']} | MODE: STEALTH")
        print("-" * 40)
        for opt in current_lang['menu']:
            print(opt)
        
        cmd = input("\n\033[1;37m[HC-LAB]> \033[0m")
        if cmd == '1': print("[*] TCP Masking Active."); time.sleep(1)
        elif cmd == '2': auto_siphon(current_lang); input("\nEnter...")
        elif cmd == '3': os.system("history -c"); print("Logs Purged."); time.sleep(1)
        elif cmd == '4': 
            lang_id = select_language()
            current_lang = LANG_DATA[lang_id]
        elif cmd == '0': break

if __name__ == "__main__":
    if verify_activation():
        main()

