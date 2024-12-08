# AOC 2024 in starlark


- days folder contain the starlark solutions
- src folder is the rust code to run the starlark code
- src/bin is some solutions in Rust (run with cargo run --bin day01)

For commands see the Justfile:

new day:

- `just generate <day number>` (for instance just generate 9)
- file the data/<day number>.txt with the example input
- write code in days/<day number>.py
- run the code with: `just run <day number>` (for instance just run 1)
- download the real input with `just download-day <day number>`

format starlark/python code: `just format`
formatting is done with ruff, you can download this with `just download-ruff`

