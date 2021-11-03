# httpfs
A simple file server and my first python app

# Project Usage
1. Clone the repo
2. Install the application with $ pip install -e.
3. For now, use test command httpfs -p 8080 -d anything or httpfs -p 5050 -d anything

# Uninstallation
1. The project can be removed with $ pip uninstall -e.

# Test Commands
1. curl localhost:8080
2. telnet localhost 5050
3. http://localhost:8080/foo
4. curl --header "Content-Type: application/json" -d "{\"value\":\"node JS\"}" localhost:8080
