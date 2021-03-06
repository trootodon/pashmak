# General Modules
pashmak has some general libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `include` operation.

look at this example:

```bash
mem '@hash'; include ^;
# or using import to have easier syntax
import '@hash';
import '@module_name';

# ...
```

you have to give name of module with a `@` before that to the include operation.

### hash module
with hash module, you can calculate hash sum of values:

```bash
import '@hash';

hash.sha256 "hello"; # also you can use hash.md5 and...
out ^; # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

###### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this function calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

#### another hash algos
- hash.blake2b (string)
- hash.blake2s (string)
- hash.md5 (string)
- hash.sha1 (string)
- hash.sha224 (string)
- hash.sha256 (string)
- hash.sha384 (string)
- hash.sha3_224 (string)
- hash.sha3_256 (string)
- hash.sha3_384 (string)
- hash.sha3_512 (string)
- hash.sha512 (string)
- hash.shake_128 (string, length)
- hash.shake_256 (string, length)


### time module
with this module, you can work with time.

###### time.time
this function gives you current UNIX timestamp:

```bash
import '@time';

time.time;
out ^; # output is some thing like this: `1600416438.687201`
```

when you call this function, this function puts the unix timestamp into mem and you can access and use that.

###### time.sleep
this function sleeps for secounds:

```bash
import '@time';

time.sleep 2; # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this function, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` function, then program will sleep for value of `mem` as secounds

#### Another time functions
- time.ctime
- time.gmtime
- time.localtime

### random module
this module makes random numbers

###### random.randint
```bash
import '@random';

random.randint 1, 10; # generates a random int between 1 and 10

out ^; # and puts generated random number in mem and you can access that
```

###### random.random
```bash
import '@random';

random.random; # generates a random float less that 1

out ^; # and puts generated random number in mem and you can access that
```

## file module
with this module, you can work with files smarter.

###### file.open
with this function, you can open a file:

```bash
import '@file';

file.open '/path/to/file.txt', 'r'; # first argument is file path, and second argument is open type. here is `r` means `read`

# now, opened file is in the mem. we can copy it in a variable

$f = ^;

# or

$f = ^ file.open '/path/to/file.txt', 'r';
```

###### file.read
wtih this function, you can read opened file:

```bash
import '@file';

$f = ^ file.open '/path/to/file.txt', 'r';

file.read $f; # now, content of file is in the mem
out ^; # output is content of file
```

###### file.write
with this function, you can write on opened file:

```bash
import '@file';

$f = ^ file.open '/path/to/file.txt', 'w'; # open type is `w` (write)

file.write $f, 'new content'; # first arg is opened file and second arg is content.
```

now file is changed

###### file.close
with this function you can close file after your work:

```bash
import '@file';

$f = ^ file.open '/path/to/file.txt', 'r';

# work with file

file.close $f; # close file after work
```

##### example:

```bash
import '@file';

$file = ^ file.open '/path/to/file.txt', 'r';

$content = ^ file.read $file;

print 'content of file is: ' + $content;
```

###### more modules comming soon...
