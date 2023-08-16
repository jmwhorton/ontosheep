## Usage

Requires: Docker Compose

1. Run `docker compose run app > results.txt`.  Results will be saved to `results.txt`
2. Once complete, you will also need to stop the triplestore container: `docker ps` to get the name, then `docker stop <container name>`.
