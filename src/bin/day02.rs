use anyhow::Result;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn calculate(data: &[i64]) -> bool {
    let mut increasing = true;
    let mut decreasing = true;
    let mut not_too_large = true;

    for (a, b) in data.iter().zip(data.iter().skip(1)) {
        let diff = b - a;
        if increasing && diff <= 0 {
            increasing = false;
        }

        if decreasing && diff >= 0 {
            decreasing = false;
        }

        if not_too_large && diff.abs() > 3 {
            not_too_large = false;
        }
    }

    (increasing && not_too_large) || (decreasing && not_too_large)
}

struct Permutations<'a> {
    data: &'a [i64],
    skip: usize,
}

impl<'a> Iterator for Permutations<'a> {
    type Item = Vec<i64>;

    fn next(&mut self) -> Option<Self::Item> {
        if self.skip >= self.data.len() {
            return None;
        }

        let mut data = Vec::with_capacity(self.data.len() - 1);

        for (index, item) in self.data.iter().enumerate() {
            if index == self.skip {
                continue;
            }
            data.push(*item);
        }

        self.skip += 1;

        Some(data)
    }
}

fn main() -> Result<()> {
    let buffer = BufReader::new(File::open("data/day02.txt")?);

    let mut part1 = 0;
    let mut part2 = 0;
    for line in buffer.lines() {
        let line = line?;
        let data: Vec<i64> = line.split(' ').map(|x| x.parse().unwrap()).collect();
        if calculate(&data) {
            part1 += 1;
        }
        let mut iter = Permutations {
            data: &data,
            skip: 0,
        };
        while let Some(data) = iter.next() {
            if calculate(&data) {
                part2 += 1;
                break;
            }
        }
    }

    assert_eq!(part1, 591);
    assert_eq!(part2, 621);

    Ok(())
}
