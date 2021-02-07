### Glue

I often need to perform some test on huge files (> 1GB size) and I don't want to keep them on my disk or a cloud service to save space.
So, unless I need otherwise, I just take a small sample file,  I copy/paste it N times on a new file and use it for testing.
But I'm lazy, so in the end I wrote a bunch of python loc to do it.

This is a python utility that takes an input file's absolute path, reads it and copies its content on another file N times.

Usage sample:

```python
python glue.py <input_file> <output_file> <num_of_times>
```
where `num_of_times` is the number of times the source file content must be pasted on the destination file.