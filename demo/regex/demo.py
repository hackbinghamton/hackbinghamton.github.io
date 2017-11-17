import re



# The `match` method matches a pattern at the beginning of a string
def example_1():
    '''
    >>> example_1()
    <_sre.SRE_Match object; span=(0, 11), match='hello world'>
    '''
    hello_regex = re.compile(r'hello world')
    result = hello_regex.match('hello world blah blah')
    print(result)


def example_2():
    '''
    >>> example_2()
    None
    '''
    hello_regex = re.compile(r'hello world')
    result = hello_regex.match('blah blah hello world')
    print(result)


# We can use the `search` method to find a pattern in the middle of string
def example_3():
    '''
    >>> example_3()
    <_sre.SRE_Match object; span=(10, 21), match='hello world'>
    '''
    hello_regex = re.compile(r'hello world')
    result = hello_regex.search('blah blah hello world')
    print(result)


# Special Characters
# ╭─────────────────┬──────────────────────────────────────╮
# │    Character    │           Meaning                    │
# ├─────────────────┼──────────────────────────────────────┤
# │       .         │ any character except \n (newline)    │
# ├─────────────────┼──────────────────────────────────────┤
# │       \d        │ any digit                            │
# ├─────────────────┼──────────────────────────────────────┤
# │       \D        │ any non-digit                        │
# ├─────────────────┼──────────────────────────────────────┤
# │       \s        │ any whitespace character             │
# ├─────────────────┼──────────────────────────────────────┤
# │       \S        │ any non-whitespace character         │
# ├─────────────────┼──────────────────────────────────────┤
# │       \w        │ any word character [A-Za-z0-9_]      │
# ├─────────────────┼──────────────────────────────────────┤
# │       \W        │ any non-word character               │
# ╰─────────────────┴──────────────────────────────────────╯


def example_4():
    '''
    >>> example_4()
    <_sre.SRE_Match object; span=(0, 1), match='7'>
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('7')
    print(result)


def example_5():
    '''
    >>> example_5()
    <_sre.SRE_Match object; span=(0, 1), match='7'>
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('78baxter')
    print(result)


def example_6():
    '''
    >>> example_6()
    None
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('baxter78')
    print(result)


def example_7():
    '''
    >>> example_7()
    <_sre.SRE_Match object; span=(0, 1), match='b'>
    '''
    digit_regex = re.compile(r'\w')
    result = digit_regex.match('baxter78')
    print(result)


# Quantifiers
# ╭─────────────────┬───────────────────────────────────────────╮
# │    Character    │           Meaning                         │
# ├─────────────────┼───────────────────────────────────────────┤
# │        *        │ 0 or more copies of previous regex        │
# ├─────────────────┼───────────────────────────────────────────┤
# │        +        │ 1 or more copies of previous regex        │
# ├─────────────────┼───────────────────────────────────────────┤
# │        ?        │ 0 or 1 of copies of previous regex        │
# ├─────────────────┼───────────────────────────────────────────┤
# │       {m}       │ m copies of previous regex                │
# ├─────────────────┼───────────────────────────────────────────┤
# │      {m,n}      │ m to n copies of previous regex           │
# ├─────────────────┼───────────────────────────────────────────┤
# │                 │                                           │
# ╰─────────────────┴───────────────────────────────────────────╯


def example_7():
    '''
    >>> example_7()
    <_sre.SRE_Match object; span=(0, 6), match='aaaaaa'>
    '''
    regex = re.compile(r'a*')
    result = regex.search('aaaaaabcd')
    print(result)


def example_7():
    '''
    >>> example_7()
    <_sre.SRE_Match object; span=(0, 0), match=''>

    This matches empty string because r'a*' means match 0 or more
    '''
    regex = re.compile(r'a*')
    result = regex.search('bbbbaaaaaabcd')
    print(result)


def example_8():
    '''
    >>> example_8()
    <_sre.SRE_Match object; span=(4, 10), match='aaaaaa'>
    '''
    regex = re.compile(r'a+')
    result = regex.search('bbbbaaaaaabcd')
    print(result)


def example_9():
    '''
    >>> example_9()
    <_sre.SRE_Match object; span=(4, 7), match='abc'>
    <_sre.SRE_Match object; span=(4, 6), match='ac'>
    '''
    regex = re.compile(r'abb?c')
    result1 = regex.search('____abc____')
    result3 = regex.search('____abbc____')
    result2 = regex.search('____ac_____')
    print(result1)
    print(result3)
    print(result2)


# Options
# We can use r'abc|def' to match 'abc' or 'def'
# And we can use r'ab(c|d)ef' to match 'abcef' or 'abdef'


def example_10():
    '''
    >>> example_10()
    <_sre.SRE_Match object; span=(0, 6), match='baxter'>
    <_sre.SRE_Match object; span=(0, 6), match='harvey'>
    '''
    regex = re.compile(r'baxter|harvey')
    result1 = regex.search('baxter')
    result2 = regex.search('harvey')
    print(result1)
    print(result2)


# Anchors
# ╭─────────────────┬───────────────────────────────────────────╮
# │    Character    │           Meaning                         │
# ├─────────────────┼───────────────────────────────────────────┤
# │       ^         │ Matches the start of a string             │
# ├─────────────────┼───────────────────────────────────────────┤
# │       $         │ Matches the end of a string               │
# ├─────────────────┼───────────────────────────────────────────┤
# │     (?=...)     │ Matches if ... matches next               │
# ├─────────────────┼───────────────────────────────────────────┤
# │     (?!...)     │ Matches if ... does not match next        │
# ├─────────────────┼───────────────────────────────────────────┤
# │     (?<=...)    │ Matches if ... matches before             │
# ├─────────────────┼───────────────────────────────────────────┤
# │     (?<!...)    │ Matches if ... does not match before      │
# ╰─────────────────┴───────────────────────────────────────────╯


def example_11():
    '''
    >>> example_11()
    None
    <_sre.SRE_Match object; span=(0, 5), match='hello'>
    '''
    regex = re.compile(r'^hello')
    result1 = regex.search('blah hello')
    result2 = regex.search('hello')
    print(result1)
    print(result2)


def example_12():
    '''
    >>> example_12()
    <_sre.SRE_Match object; span=(5, 10), match='hello'>
    None
    '''
    regex = re.compile(r'hello$')
    result1 = regex.search('blah hello')
    result2 = regex.search('hello blah')
    print(result1)
    print(result2)


def example_13():
    '''
    >>> example_13()
    <_sre.SRE_Match object; span=(0, 15), match='The quick brown'>
    '''
    regex = re.compile(r'[\w ]+(?=\sfox)')
    result = regex.search('The quick brown fox')
    print(result)


def example_14():
    '''
    >>> example_14()
    <_sre.SRE_Match object; span=(7, 15), match='Workshop'>
    '''
    regex = re.compile(r'(?<=HackBU )\w+')
    result = regex.search('HackBU Workshop')
    print(result)
