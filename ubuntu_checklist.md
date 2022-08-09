# Ubuntu Hardening Checklist

- Is the system up-to-date?

- Is the firewall enabled? (ufw)

- Are the password policies set? (pam) & pamcracklib installed? (libpam-cracklib)
  - Password max (PASS_MAX_DAYS = 90)
  - Password min days (PASS_MIN_DAYS = 10)
  - Password warn age (PASS_WARN_AGE = 7)
  - Password attempt limit (auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800)

- Are there any unauthorised files on the system?

- Are there any unauthorised users on the system?

- Are there any unauthorised groups on the system?

- Do users need to be added?

- Are all the passwords of sufficient strength?

- Are there any hacking tools?
