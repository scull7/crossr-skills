# Input parsing

Parse at the edge. The core never sees wire types.

## Rules

RP-01  Parse wire values into domain types at the adapter edge. Do not validate later.

RP-02  Newtypes that wrap wire input are constructed at the edge, not deep in the core.

RP-03  Invalid input dies at the parse boundary. The core receives a domain value or nothing.

## How

A string from HTTP, a CLI flag, or a JSON field is not a `UserId`. Parse it in the adapter:

```rust
impl UserId {
    pub fn parse(raw: &str) -> Result<Self, ParseError> { /* … */ }
}

fn handle(req: Request) -> Result<Response, GatewayError> {
    let id = UserId::parse(&req.path_id)?;
    Ok(service.get(id)?.into())
}
```

Stringly types that leak past the edge become boolean flags and sentinel checks in the core. Kill them at the door.
