import pwd
for p in pwd.getpwall():
    print(p[0])