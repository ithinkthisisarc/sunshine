# sunshine
A low level, compiled language built to be small and fast that will probably never be finished.

### Contributing
Please help me! To contribute, download the source and the dependancies listed [here](#compile) and add whatever you want. Some main focuses of mine are
1. Speed (fast)
2. Size (small)
3. Ease of use (very easy)
4. Ease of writing (fairly easy)

Some features that are needed are
1. Variables
2. Functions
3. More types (such as strings/chars)

Any help is greatly appreciated!!!

### Syntax?
What can it do right now?
Basically, nothing. At the moment it can do two things.

The first thing it can do is print math. You can do this with
```rust
fn main() {
println( {{ equation }} );
}
```

The second thing it can do is print `==` comparisons and `!=` comparisons. This looks like
```go
println( 1 == 1 ); {{ results in 1 }}
```
```go
println( 1 != 1 ); {{ results in 0 }}
```

### Compile
**COMPILING HAS BEEN TESTED ON LINUX MINT TESSA. ANY OTHER OPERATING SYSTEMS MIGHT HAVE FAULTY RESULTS**

You also need the following dependancies installed to compile:
1. llvm (for llc)
2. rply
3. gcc
4. llvmlite

Run `python3 main.py test.sun test` to compile. This creates the dotfiles `.output.ll` and `.output.o`, which are then compiled into machine code with gcc.
