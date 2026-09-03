# Input parsing

Parse at the edge. The core never sees wire types.

## Rules

RP-01  Parse wire values into domain newtypes at the adapter edge. Do not validate later. Naked `String` / `&str` must not cross into the core.

RP-02  Newtypes that wrap wire input are constructed at the edge, not deep in the core.

RP-03  Invalid input dies at the parse boundary. The core receives a domain value or nothing.

## How

A string from HTTP, a CLI flag, or a JSON field is not a `UserId`. Parse it into a newtype in the adapter (New Type pattern: wrap the primitive so the core cannot be handed a raw string):

```rust
impl UserId {
    pub fn parse(raw: &str) -> Result<Self, ParseError> { /* … */ }
}

fn handle(req: Request) -> Result<Response, GatewayError> {
    let id = UserId::parse(&req.path_id)?;
    Ok(service.get(id)?.into())
}
```

Core signatures take `UserId`, `Email`, `TenantId` — not `String`. Stringly types that leak past the edge become boolean flags and sentinel checks in the core. Kill them at the door.
