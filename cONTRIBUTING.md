# Contribute to Google Fonts

## Feedback

If you have any feedback on Google Fonts API, directory, or the fonts themselves, please create an issue at [github.com/google/fonts/issues](http://github.com/google/fonts/issues)

## New Families

If you would like to include a new font family in the Google Fonts collection, we'll be happy to include it if it meets the following criteria:

* The typeface design is original, or a legitimate revival of a design in the public domain, and of good quality. The Google Design team curates the overall Google Fonts collection and decides if fonts are of good quality. You can get general reviews of your project from the wider international type community during development by posting review requests in the [googlefonts-discuss](https://groups.google.com/forum/#!forum/googlefonts-discuss) group, and the [typedrawers](http://typedrawers.com/categories/critiques%E2%80%94type-design) review forum.  
* The project is **wholly** licensed under the [SIL Open Font License v1.1](http://scripts.sil.org/OFL), and there are no proprietary/restricted-license versions available elsewhere
* The Open Font License does not have any Reserved Font Names ([why](https://github.com/simoncozens/silson/issues/1))
* The copyright holders have all signed the [Google Contributor's License Agreement](https://cla.developers.google.com)
* The font family name does not include any copyright holder names or registered trademarks, and no initials or abbreviations, and no references to languages or writing systems; it should be a simple and unique name, and a limited but easy way to test for uniqueness is [namecheck.fontdata.com](https://namecheck.fontdata.com)  
* The project is developed on Github or similar, with complete corresponding sources, [open to public participation](http://producingoss.com), and actively maintained. Complete corresponding sources means that the fonts are available in your preferred form of modification, the files you actually use to develop the project, along with all the build instructions or scripts needed to  reproduce the process of turning those source files into your released font binaries.  
* All binary font files are available in TTF format, with hinting (such as with [ttfautohint](http://www.freetype.org/ttfautohint/)) and built with a scripted build process, using [fontmake](https://github.com/googlefonts/fontmake)
* All font files have at a minimum the 215 glyphs listed in our [`latin_unique-glyphs.nam`](https://github.com/googlefonts/gftools/blob/master/Lib/gftools/encodings/latin_unique-glyphs.nam) file  
* All font files within the family have the same Unicode character set (unencoded glyphs can differ)  
* All font files pass the [Font Bakery](https://github.com/googlefonts/fontbakery) google-fonts profile checks.
* A `README.md` file is included in the root of the source repository, and inside of that file we can read about [FONTLOG](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl-faq_web#43cecb44) information, and your github usernames, so that we can prepare a description ([example](https://github.com/google/fonts/blob/master/ofl/poppins/DESCRIPTION.en_us.html)) and link your name to your profile.  
* Optionally, a direct `DESCRIPTION.en_us.html` file, a `profile.txt` and a `your-name.jpg` avatar image, to be copied into this repo.
* More detailed design and production details are listed in [github.com/googlefonts/gf-docs/ProjectChecklist](https://github.com/googlefonts/gf-docs/tree/master/ProjectChecklist)  

When you are ready to meet these requirements, please [create a new issue](https://github.com/google/fonts/issues) with a link to the project's source repository.

From time to time, Google Fonts provides financial and design assistance for projects. 
If you would like to discuss this, please mention that you would like someone to contact you privately when filing an issue (and have contact details on your Github profile page.)

### Updates

If your font is already on-boarded and you'd like us to update our copy, please file an issue (instead of making a pull request directly.)

We carefully check the technical aspects of updated fonts to prevent unintended changes, so we prefer to collaborate with you on your upstream project to make a release which we update from. 

## Contributor License Agreement

We love to accept all good patches and contributions to this project. 
There is just one thing contributors need to do first...

Contributions to Google projects must be accompanied by a Contributor License Agreement. 
This is not a copyright assignment, it simply gives Google permission to use and redistribute your contributions as part of the project.

<https://cla.developers.google.com>

You generally only need to submit the Google CLA once, so if you've already submitted one for a different project, you probably don't need to do it again.

After your contribution is included, you will be listed in [CONTRIBUTORS](CONTRIBUTORS) and/or [AUTHORS](AUTHORS) files; 
CONTRIBUTORS is the official list of people who can contribute (and typically have contributed) code to this repository, while the AUTHORS file lists the copyright holders.
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def prepend(value, iterator):
    "Prepend a single value in front of an iterator"
    # prepend(1, [2, 3, 4]) -> 1 2 3 4
    return chain([value], iterator)

def tabulate(function, start=0):
    "Return function(0), function(1), ..."
    return map(function, count(start))

def tail(n, iterable):
    "Return an iterator over the last n items"
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(map(pred, iterable))

def padnone(iterable):
    """Returns the sequence elements and then returns None indefinitely.

    Useful for emulating the behavior of the built-in map() function.
    """
    return chain(iterable, repeat(None))

def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))

def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))

def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)

def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))

def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return map(next, map(operator.itemgetter(1), groupby(iterable, key)))

def iter_except(func, exception, first=None):
    """ Call a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an iterator interface.
    Like builtins.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.

    Examples:
        iter_except(functools.partial(heappop, h), IndexError)   # priority queue iterator
        iter_except(d.popitem, KeyError)                         # non-blocking dict iterator
        iter_except(d.popleft, IndexError)                       # non-blocking deque iterator
        iter_except(q.get_nowait, Queue.Empty)                   # loop over a producer Queue
        iter_except(s.pop, KeyError)                             # non-blocking set iterator

    """
    try:
        if first is not None:
            yield first()            # For database APIs needing an initial cast to db.first()
        while True:
            yield func()
    except exception:
        pass

def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.

    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    return next(filter(pred, iterable), default)

def random_product(*args, repeat=1):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def random_combination_with_replacement(iterable, r):
    "Random selection from itertools.combinations_with_replacement(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)

def nth_combination(iterable, r, index):
    'Equivalent to list(combinations(iterable, r))[index]'
    pool = tuple(iterable)
    n = len(pool)
    if r < 0 or r > n:
        raise ValueError
    c = 1
    k = min(r, n-r)
    for i in range(1, k+1):
        c = c * (n - k + i) // i
    if index < 0:
        index += c
    if index < 0 or index >= c:
        raise IndexError
    result = []
    while r:
        c, n, r = c*r//n, n-1, r-1
        while index >= c:
            index -= c
            c, n = c*(n-r)//n, n-1
        result.append(pool[-1-n])
    return tuple(result)
