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
