# API surface

`pub` is a contract. Keep it small. Document it.

## Rules

RA-01  Every public item is documented in the Rust rustdoc style.

RA-02  Keep the public surface small. `pub` is a promise, not a default.

RA-03  A breaking change to a `pub` item is a major version.

## How

If a helper is only used inside the crate, it is not `pub`. If a type is `pub`, its documented invariants are the API.

rustdoc on every public item is the minimum. Examples belong on the functions callers will actually invoke.

Semver is mechanical once the surface is honest. Hidden `pub` leakage is how minors become majors.
