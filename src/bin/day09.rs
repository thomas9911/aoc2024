use anyhow::Result;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

pub type Layout = Vec<Option<u32>>;

pub fn print_layout(layout: &Layout) {
  let mut buffer = String::new();

  for item in layout {
    if let Some(x) = item {
      buffer.push_str(&format!("{}", x));
    } else {
      buffer.push('.');
    }
  }

  println!("{}", buffer);
}

fn compact_layout(layout: &mut Layout) -> Result<()> {
  loop {
    if let Some(i) = layout.iter().position(|x| x == &None){
      if let Some(Some(x)) = layout.pop() {
        layout.get_mut(i).map(|y| *y = Some(x));
      }
    } else {
      break;
    }
  }

  Ok(())
}

fn checksum(layout: &Layout) -> usize {
  let mut score = 0;
  for (i, item) in layout.iter().enumerate() {
    if let Some(x) = item {
      score += i * (*x as usize);
    }
  }
  return score
}


fn main() -> Result<()> {
  let data = std::fs::read_to_string("data/day09.txt")?;
  let data = data.trim().to_string();

  let mut on_spacing = false;
  let mut current_id = 0;
  let mut layout = Vec::with_capacity(data.len());

  for ch in data.chars() {
    let item: u32 = ch.to_digit(10).ok_or_else(|| anyhow::anyhow!("invalid char"))?;
    for _ in 0..item {
      if on_spacing {
        layout.push(None)
      } else {
        layout.push(Some(current_id))
      }
    }
    if on_spacing {
      current_id += 1;
      on_spacing = false;
    } else {
      on_spacing = true;
    }
  }

  // print_layout(&layout);
  compact_layout(&mut layout)?;
  // print_layout(&layout);
  let checksum = checksum(&layout);

  println!("{}", checksum);

  Ok(())
}