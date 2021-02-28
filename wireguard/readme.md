# Setup instructions

0. Edit `SERVERURL` environment variable in `docker-compose-server.yml` file.
1. Build & Run server app stack
```bash
docker-compose -f docker-compose-server.yml build
docker-compose -f docker-compose-server.yml up -d
```
2. copy client wireguard config from server to client `wg-client-config/wg0.conf`
```bash
cat wg-server-config/peer_client1/peer_client1.conf
```

3. On other machine build & run client app stack
```bash
docker-compose -f docker-compose-server.yml build
docker-compose -f docker-compose-server.yml up
```
