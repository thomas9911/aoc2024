use starlark::{environment::Module, values::Heap};
use starlark::eval::Evaluator;
use starlark::syntax::AstModule;
use starlark::syntax::Dialect;
use starlark::values::Value;
use starlark::{environment::GlobalsBuilder, starlark_module};
use std::path::PathBuf;

#[starlark_module]
fn aoc_module(builder: &mut GlobalsBuilder) {
    fn print<'v>(data: Value<'v>) -> anyhow::Result<u32> {
        println!("{}", data);
        Ok(0)
    }

    fn load_data(mut day: String) -> anyhow::Result<String> {
        if !day.ends_with(".txt") {
            day.push_str(".txt");
        }
        let mut pathbuf = PathBuf::from("data");
        pathbuf.push(day);
        let contents = std::fs::read_to_string(pathbuf)?;
        Ok(contents)
    }

    fn sum<'v>(data: Value<'v>, heap: &'v Heap) -> anyhow::Result<Value<'v>> {
        let iter = data.iterate(heap).map_err(|e| e.into_anyhow())?;
        let mut result = heap.alloc(0);
        for item in iter {
            result = result.add(item, heap).map_err(|e| e.into_anyhow())?;
        }
        Ok(result)
    }

    fn check<'v>(left: Value<'v>, right: Value<'v>) -> anyhow::Result<u32> {
        if left != right {
            anyhow::bail!(format!(
                "left is not equal to right
Left:
    {left}
Right:
    {right}"
            ))
        }

        Ok(0)
    }
}

fn run_starlark(filename: &str, content: &str) -> anyhow::Result<serde_json::Value> {
    let mut dialect = Dialect::Extended;
    dialect.enable_f_strings = true;

    let ast: AstModule =
        AstModule::parse(filename, content.to_owned(), &dialect).map_err(|e| e.into_anyhow())?;

    // let globals: Globals = Globals::standard();
    let globals = GlobalsBuilder::standard().with(aoc_module).build();

    // We create a `Module`, which stores the global variables for our calculation.
    let module: Module = Module::new();

    // We create an evaluator, which controls how evaluation occurs.
    let mut eval: Evaluator = Evaluator::new(&module);

    // And finally we evaluate the code using the evaluator.
    let res: Value = eval
        .eval_module(ast, &globals)
        .map_err(|e| e.into_anyhow())?;

    res.to_json_value()
}

fn main() -> anyhow::Result<()> {
    let mut args = std::env::args();
    args.next();

    let mut day_file = args
        .next()
        .ok_or_else(|| anyhow::anyhow!("Missing file argument"))?;
    if !day_file.ends_with(".py") || !day_file.ends_with(".star") {
        day_file.push_str(".py");
    }

    let mut pathbuf = PathBuf::from("days");
    pathbuf.push(day_file);
    let contents = std::fs::read_to_string(pathbuf)?;

    run_starlark("test.star", &contents)?;

    Ok(())
}

#[test]
fn run_starlark_works() {
    let content = r#"
def hello():
    return "hello"

print({})

hello() + " world!"

    "#;

    let out = run_starlark("test.star", &content).unwrap();

    assert_eq!(out, serde_json::Value::String("hello world!".into()));
}
