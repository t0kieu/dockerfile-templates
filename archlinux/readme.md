
# Docker templates for archlinux

## archlinux:pacaur

```bash
# Build
docker build -f pacaur.Dockerfile . -t archlinux/pacaur:latest
# Run bash
docker run --tty --interactive archlinux/pacaur:latest /bin/bash
# Example of pacuar command
sudo -u aur pacaur -Syu
```