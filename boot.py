import sys
import os

import random
import time

from game import game_welcome


def boot_sequence():
  os.system("cls")
  time.sleep(1)
  # Set terminal text color to green (ANSI escape code)
  print("\033[32m", end="")

  print("[    0.000000] Initializing Hyper-Kernel v6.9.0-meme-generic...")
  print("[    0.000014] CPU 0: Vendor Intel / AMD / Powered by Potato Engine")
  print("[    0.000042] [ OK ] Allocated 8192 MB of virtual ram.exe from Cloud Drive")
  print(
      "[    0.000105] [ OK ] Mounted root filesystem: /dev/sda1 (Format:"
      " FAT32_BUT_FAST)"
  )
  print("[    0.000199] [ OK ] ACPI: Power management initialized (Status: Panic)")
  time.sleep(0.2)

  # First batch of kernel modules
  for i in range(1, 67):
    rand_num = random.randint(1000, 9999)
    print(
        f"[    0.00{rand_num}] Loading kernel driver: sys_module_{i}.sys..."
        " [ OK ]"
    )
    time.sleep(0.01)

  print(
      "[    0.089102] [!!] WARNING: Cat paws detected on keyboard during"
      " pre-boot..."
  )
  print("[    0.091244] [ OK ] Ignored cat typing successfully.")
  print(
      "[    0.104921] [!!] WARNING: High CPU temperature detected (Cooking an"
      " egg on heatsink...)"
  )
  print(
      "[    0.105112] [ OK ] Initialized liquid nitrogen cooling fan:"
      " RGB_LIGHTS=MAX"
  )
  time.sleep(0.2)

  # Network and hardware stack
  print("[    0.150221] [ OK ] Scanning for vintage floppy disk drives...")
  print(
      "[    0.155810] [ OK ] Floppy drive found: 3.5 inch (Contains unread"
      " 1998 meme)"
  )
  print("[    0.180492] [ OK ] Starting service: TaskManagerTaskKiller.exe")
  print(
      "[    0.211902] [ OK ] Starting service: WindowsUpdateWatcher (Paused"
      " until 2099)"
  )
  print("[    0.250119] [ OK ] Starting service: Auto-Downloading More RAM v2.1...")
  print("[    0.290331] [!!] ERROR: 404 Solitaire.exe not found! Attempting hotfix...")
  print("[    0.312001] [ OK ] Solitaire driver recovered successfully.")
  print(
      "[    0.350123] [ OK ] Mounting nostalgic nostalgia drive (C:\\RetroDrive)..."
  )
  time.sleep(0.2)

  # Expanded Quantum & Weird Hardware Batch
  for i in range(201, 267):
    rand_num = random.randint(1000, 9999)
    print(
        f"[    0.38{rand_num}] [ OK ] Calibrating quantum flux capacitor"
        f" node_{i}..."
    )
    time.sleep(0.01)

  print("[    0.412001] [ OK ] Loading audio drivers: DialUpScreech.wav")
  print("[    0.435122] [!!] WARNING: Internet Explorer attempted to start itself.")
  print("[    0.440011] [ OK ] Blocked Internet Explorer with extreme prejudice.")
  print("[    0.460912] [ OK ] Initializing Microsoft Bob sentiment analyzer...")
  print("[    0.491023] [ OK ] Clippy assistant standing by to offer unwanted help.")

  # Mid-boot simulation loop (Extra chunk of chaotic logs)
  for i in range(300, 383):
    rand_num = random.randint(1000, 9999)
    print(
        f"[    0.5{rand_num}] [ OK ] Synthesizing retro shader pipeline"
        f" patch_{i}..."
    )
    time.sleep(0.01)

  print("[    0.589012] [ OK ] Bypassing firewall with sheer positive attitude...")
  print("[    0.612041] [ OK ] Loading Minecraft server wrapper plugin (Paper 1.20)...")
  print("[    0.645102] [ OK ] Injecting infinite coffee supply into developer stream...")

  # Second stream of system integrity blocks
  for i in range(100, 236):
    rand_num = random.randint(100, 999)
    print(
        f"[    0.6{rand_num}] [ OK ] Verifying system integrity:"
        f" block_{i}/1000 passed."
    )
    time.sleep(0.01)

  # Windows 7 specific and weird app hooks
  print("[    0.801233] [ OK ] Bypassing Windows Genuine Advantage check...")
  print("[    0.825100] [ OK ] Loading Aero Glass Transparency Shaders...")
  print("[    0.850912] [ OK ] Initializing Microsoft Pinball physics engine...")
  print("[    0.890411] [ OK ] Generating fake error logs to confuse IT department...")
  print(
      '[    0.910223] [ OK ] Connecting to local Wi-Fi: "FBIOpenUp_5G"... ['
      " CONNECTED ]"
  )
  print("[    0.940192] [ OK ] Reticulating splines and summoning desktop gadgets...")
  print(
      "[    0.970112] [ OK ] Defragmenting imagination sector in brain..."
  )
  print("[    1.012901] [ OK ] Checking for half-life 3 release status... [ NONE ]")
  print("[    1.050421] [ OK ] Downloading additional patience...")

  # Final batch of weird modules before completion
  for i in range(400, 431):
    rand_num = random.randint(1000, 9999)
    print(
        f"[    1.1{rand_num}] [ OK ] Finalizing kernel subsystem component"
        f" omega_{i}..."
    )
    time.sleep(0.01)

  print("[    1.684546] [ OK ] Googleing... (How to delete system files)...")
  print("[    1.120941] [ OK ] Unpacking System32... (Just kidding, don't delete it)")
  print("[    1.189021] [ OK ] Finalizing desktop environment and loading wallpaper...")
  print("[    1.250102] [ OK ] Summoning taskbar clock and volume slider...")
  print("[    1.310492] [ OK ] System ready for maximum productivity (or gaming)...")
  print()
  print("======================================================================")
  print("                      BOOT SEQUENCE COMPLETE                          ")
  print("======================================================================")
  print()
  print("      /\\_/\\  ")
  print('     ( o.o )   ^< "Task failed successfully! System ready."')
  print("      ^> ^<")
  print()

  # Reset terminal color back to default
  print("\033[0m", end="")
  input("Press ENTER to continue...")
  game_welcome()