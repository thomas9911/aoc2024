set dotenv-load

generate day:
    mkdir -p days
    mkdir -p data
    echo "data = load_data(\"day$(printf "%02d" {{day}})\")" > days/day$(printf "%02d" {{day}}).py
    touch data/day$(printf "%02d" {{day}}).txt

run day:
    cargo run --release -- day$(printf "%02d" {{day}})


download-ruff:
    curl -LsSf https://astral.sh/ruff/install.sh | sh

format:
    ruff format days/*.py

download-day day:
    curl -b session=$session https://adventofcode.com/2024/day/{{day}}/input > data/day$(printf "%02d" {{day}}).txt
    
    
# curl 'https://adventofcode.com/2024/day/8/input' --compressed -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: nl,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: https://adventofcode.com/2024/day/8' -H 'Connection: keep-alive' -H 'Cookie: session=53616c7465645f5f0f8f98ff0334e10b0181ca410f6aa8a7fda4dab68ea52f2005fab5e9c335e61b381a2aaaaaaa8d526b851f66e1dff6b0c7ec63e719f7469e' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Priority: u=0, i'
