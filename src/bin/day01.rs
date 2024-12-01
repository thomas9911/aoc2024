use anyhow::Result;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> Result<()> {
    let buffer = BufReader::new(File::open("data/day01.txt")?);

    let mut lefts = Vec::new();
    let mut rights = Vec::new();

    for line in buffer.lines() {
        let line = line?;
        if let Some((a, b)) = line.split_once("   ") {
            let left: u32 = a.parse()?;
            let right: u32 = b.parse()?;
            lefts.push(left);
            rights.push(right);
        } else {
            anyhow::bail!("invalid input: {}", line);
        }
    }

    lefts.sort_unstable();
    rights.sort_unstable();

    let mut part1 = 0;
    for (left, right) in lefts.iter().zip(&rights) {
        part1 += (*left).abs_diff(*right);
    }

    assert_eq!(part1, 3508942);

    let mut counter_left = HashMap::new();
    for item in lefts.iter() {
        *counter_left.entry(item).or_insert(0) += 1;
    }

    let mut counter_right = HashMap::new();
    for item in rights.iter() {
        *counter_right.entry(item).or_insert(0) += 1;
    }

    let mut part2 = 0;
    for (key, value) in counter_left.iter() {
        if let Some(value2) = counter_right.get(key) {
            part2 += *key * *value * value2;
        }
    }
    assert_eq!(part2, 26593248);

    Ok(())
}
