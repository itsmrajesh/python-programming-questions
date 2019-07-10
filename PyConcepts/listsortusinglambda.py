cricket=[ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]

cricket.sort(key=lambda name: name[::][-1].lower() )
print(cricket)
