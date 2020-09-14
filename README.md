Tweak AF*
===========================
(* means also buggy and WIP AF!!!) 

Python "library" for live coding and tweaking long (already) running scripts (ML training, crawlers).
--

* Have you ever wanted to tweak some constants in your code, WHICH IS ALREADY RUNNING?
    * use `tweak_af.tv()` !!!
        * as a bonus, `tv()` can be easily broken by adding new lines to your script!!!
* Have you ever wanted to rewrite some function in your code, WHICH ALREADY STARTED?
    * use `tweak_af.tf()` !!!
    
**Lets see examples:** or you can check `example.py`

*Tweakable values:*
(inspired by https://github.com/joeld42/ld48jovoc/blob/master/util/tweakval/tweakval.cpp and friends)

TODO: fancy GIF here

* code it (`test_tv.py`):
```
    from tweak_af import tv

    while True:
        print(tv(0))
```
        
* run it: `python test_tv.py &` (in the background, not necessary, but you can use same terminal for editing)
    * you will see that it prints all zeroes
    
* while it is running, edit the code and rewrite it from `tv(0)` to `tv(42)` (or whatever) and save it as usual
    * see that the script, which is still running, now prints your new value!!!
    * Note: if you add new lines before any `tv()` call (while script is running), its logic will be broken
    * Note 2: value is evaluated by `eval()` call, so if there is some exception thrown, it will crash your running script
    
*Tweakable functions:*

TODO: fancy GIF here

* code it (`test_tf.py`):
```
    from tweak_af import tf
    
    def test_func(a, b):
        return a + b
        
    while True:
        print(tf(lambda: test_func(1, 2)) # yeah, lambda is actually needed, because reasons
```        
        
* run it: `python test_tf.py &` (in the background, not necessary, but you can use same terminal for editing)
    * it will print, you guessed right, `3`s
    
* while it is still running, edit the code
    * so, rewrite the `test_func()` to be like `return a + b + 1`
    * save it from wherever you want
    
* now, you get `4`s instead of `3`s
    * Note: you can add more lines to the functions in runtime
    * Note 2: you can add new functions and call them from existing `tf()` functions, which you edit
    * Note 3: you can use `tv()` inside of `tf()` functions, but maybe it will break :-)
    
Tests:
==
* `chmod u+x test.sh`
* run `test.sh` (or only `test_tf.sh`, `test_tv.sh`), if they exit, it probably means that this library works
    
Notes:
==
* methods not supported (yet)
* tested only for Python 3.8 on WSL 2 and macOS 10.14.6 (Mojave)
* you can disable dynamic behavior by `set_tweakables_enabled(False)`, in this case, it will use defaults (or act as passthrough)
* very buggy, poorly written
* this will break debugger (expected)
* not CPU efficient and memory friendly
    * use only for simpler use cases (few functions/values as `tf()`/`tv()`) or not in production code
* use at your own risk, there are no guarantees
* C# version in the works

TODOs:
==
* use fs_notify/inotify and reload dictionaries only when backing file changes
* better tests without bash usage
* method support
* startup and tweak as a service business /sarcasm
* provide licence (probably MIT or BSD one, NOT gpl)
* use GIFs for README!
* fix all the `FIXME`s and `TODO`s! (which basically means rewriting everything in more `pythonic` and efficient way)
* pip package
* make README.md more fancy and readable

    
    





