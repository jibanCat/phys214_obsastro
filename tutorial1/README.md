# PyRAF

- To open

```
>> pyraf
```

- Get the header

```
imhead <name>.(fits) l+
```

## ISSUES

- The error of `uparm` : create the `login.cls` in your working folder
(http://maravelias.info/2011/05/login-cl-iraf-pyraf/)

```bash
mkiraf
# choose vt100 for most terminals
```

- Interactive pyraf, open as 

```bash
pyraf --ipython
```

- before starting `display`, run
(http://burro.case.edu/Academics/Astr306/iraftips.html)
```
!ds9 &
```

- `ds9` couldn't open error, 

`error while loading shared libraries: libssl.so.10: cannot open shared object file: No such file or directory`

(https://askubuntu.com/questions/339364/libssl-so-10-cannot-open-shared-object-file-no-such-file-or-directory)

```bash
cd /lib/x86_64-linux-gnu
sudo ln -s libssl.so.1.0.0 libssl.so.10
sudo ln -s libcrypto.so.1.0.0 libcrypto.so.10
```

- downgrade `ds9==7.5`
 conda install ds9==7.5

https://github.com/astroconda/astroconda-contrib/issues/410