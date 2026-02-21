from graph import *
from wordgraphs import *

def test_task1_is_word_1() -> None:
    g = PrecompGraph("web2", 4)
    assert g.is_actual_word("real")

def test_task1_is_word_2() -> None:
    g = PrecompGraph("web2", 4)
    assert g.is_actual_word("yes")

def test_task1_is_word_3() -> None:
    g = PrecompGraph("web2", 4)
    assert g.is_actual_word("leaf")

def test_task1_is_not_word_1() -> None:
    g = PrecompGraph("web2", 4)
    assert not g.is_actual_word("wxyz")

def test_task1_is_not_word_2() -> None:
    g = PrecompGraph("web2", 4)
    assert not g.is_actual_word("Don")

def test_task1_is_not_word_3() -> None:
    g = PrecompGraph("web2", 4)
    assert not g.is_actual_word("length")

def test_task1_adjacent_1() -> None:
    g = PrecompGraph("web2", 4)
    actual = g.adjacent("mane")
    expected = {'mage', 'mans', 'gane', 'mace',
                'mine', 'cane', 'mant', 'manx',
                'tane', 'mana', 'mani', 'made',
                'mang', 'dane', 'sane', 'mank',
                'mand', 'mano', 'maze', 'mare',
                'jane', 'wane', 'mone', 'mate',
                'male', 'nane', 'make', 'mann',
                'many', 'pane', 'rane', 'bane',
                'lane', 'vane'}
    assert actual == expected

def test_task1_adjacent_2() -> None:
    g = PrecompGraph("web2", 4)
    actual = g.adjacent("wxyz")
    expected: set[str] = set()
    assert actual == expected

def test_task1_adjacent_3() -> None:
    g = PrecompGraph("web2", 4)
    actual = g.adjacent("greg")
    expected = {'grey', 'gree', 'grog', 'grig',
                'gleg', 'grew', 'gheg', 'dreg'}
    assert actual == expected

def test_task1_degree_1() -> None:
    g = PrecompGraph("web2", 4)
    assert g.degree("mane") == 34

def test_task1_degree_2() -> None:
    g = PrecompGraph("web2", 4)
    assert g.degree("wxyz") == 0

def test_task1_degree_3() -> None:
    g = PrecompGraph("web2", 4)
    assert g.degree("greg") == 8

def test_task2a_1() -> None:
    g = PrecompGraph("web2", 3)
    actual = variations(g, "wxy", 4)
    
    assert len(actual) == 0

def test_task2a_2() -> None:
    g = PrecompGraph("web2", 3)
    actual = variations(g, "out", 0)
    expected = {"out"}
    
    assert actual == expected

def test_task2a_3() -> None:
    g = PrecompGraph("web2", 3)
    actual = variations(g, "hat", 1)
    expected = {'nat', 'yat', 'hal', 'hot',
                'het', 'fat', 'kat', 'hay',
                'hao', 'hag', 'gat', 'hap',
                'lat', 'sat', 'wat', 'ham',
                'jat', 'zat', 'tat', 'rat',
                'oat', 'had', 'mat', 'hit',
                'eat', 'vat', 'haw', 'hah',
                'han', 'bat', 'hak', 'pat',
                'hut', 'cat', 'hau'}
    
    assert actual == expected

def test_task2a_4() -> None:
    g = PrecompGraph("web2", 3)
    actual = variations(g, "be", 2)
    expected = {'at', 'fi', 'yr', 'ti', 'ro', 'of', 'in', 'zo',
                'ni', 'ha', 'tu', 'am', 'ox', 'mi', 'fu', 'nu',
                'as', 'ah', 'ak', 'or', 'mr', 'ay', 'za', 'if',
                'ma', 'ra', 'my', 'jo', 'so', 'th', 'wi', 'ko',
                'ao', 'vu', 'eu', 'og', 'st', 'oh', 'yn', 'fa',
                'sa', 'to', 'di', 'yo', 'sh', 'pa', 'ab', 'la',
                'hu', 'wu', 'mu', 'td', 'it', 'si', 'hi', 'on',
                'lo', 'aa', 'wo', 'fo', 'wa', 'da', 'aw', 'an',
                'ym', 'ju', 'ow', 'do', 'po', 'od', 'lu', 'go',
                'hy', 'no', 'ea', 'id', 'mo', 'ad', 'ar', 'pu',
                'om', 'io', 'ho', 'ey', 'is', 'ka', 'os', 'ya',
                'al', 'ok', 'gi', 'na', 'ax', 'ga', 'wy', 'ta',
                'ai', 'ca', 'ly'}

    assert actual == expected

def test_task2a_5() -> None:
    g = PrecompGraph("web2", 3)
    actual = variations(g, "don", 3)
    expected = {'vug', 'ray', 'tai', 'hup', 'fum',
                'sey', 'gaj', 'gim', 'kea', 'cee',
                'hex', 'yam', 'naw', 'hep', 'cue',
                'mal', 'tho', 'gur', 'bea', 'pal',
                'gum', 'fut', 'lar', 'baw', 'yas',
                'pah', 'tji', 'saw', 'mah', 'tip',
                'keg', 'six', 'yak', 'sec', 'paw',
                'aal', 'saa', 'rum', 'cit', 'cay',
                'jug', 'sud', 'biz', 'kip', 'bab',
                'gut', 'ply', 'kai', 'mix', 'ley',
                'sal', 'ped', 'yat', 'sui', 'say',
                'lid', 'vum', 'bam', 'eye', 'kru',
                'gam', 'big', 'las', 'fay', 'sap',
                'pip', 'sir', 'wat', 'wry', 'teg',
                'gie', 'tap', 'taj', 'rid', 'sip',
                'cel', 'hid', 'sur', 'raw', 'bel',
                'suu', 'pup', 'far', 'ree', 'pig',
                'jay', 'oar', 'syd', 'ker', 'pau',
                'pir', 'hui', 'tao', 'mux', 'jaw',
                'per', 'lac', 'map', 'jab', 'lad',
                'wit', 'git', 'tic', 'wer', 'tay',
                'cad', 'sty', 'shu', 'yad', 'hic',
                'fie', 'ino', 'kat', 'car', 'pew',
                'yuh', 'fir', 'lab', 'yip', 'rat',
                'lea', 'cur', 'lai', 'nae', 'rut',
                'hip', 'tax', 'ing', 'geo', 'nar',
                'sac', 'lie', 'yez', 'nag', 'rah',
                'jam', 'rex', 'fud', 'zoa', 'mac',
                'nig', 'but', 'kex', 'wad', 'fly',
                'sye', 'hal', 'wag', 'mib', 'sia',
                'ras', 'lip', 'tux', 'pac', 'ric',
                'iao', 'cum', 'lew', 'lax', 'wiz',
                'kit', 'loa', 'liv', 'twa', 'sky',
                'led', 'saj', 'hah', 'lak', 'zag',
                'the', 'fid', 'rel', 'sis', 'bye',
                'wet', 'tum', 'mer', 'bus', 'par',
                'hue', 'bid', 'sak', 'hsi', 'stu',
                'guz', 'bet', 'luo', 'gat', 'seg',
                'gad', 'tav', 'sue', 'rik', 'zea',
                'tui', 'rim', 'tup', 'kra', 'yao',
                'tib', 'bac', 'sup', 'yeo', 'gul',
                'rua', 'kua', 'pya', 'sub', 'sax',
                'rag', 'let', 'lim', 'vip', 'nay',
                'ssu', 'vim', 'max', 'guy', 'ned',
                'gud', 'bes', 'hao', 'wed', 'tyg',
                'bim', 'was', 'mil', 'sag', 'tur',
                'wey', 'ged', 'quo', 'oam', 'rip',
                'kaf', 'law', 'gey', 'zac', 'wes',
                'jib', 'nit', 'nap', 'tid', 'gig',
                'zad', 'hyp', 'mao', 'pam', 'haw',
                'mew', 'zed', 'tea', 'twi', 'rix',
                'tad', 'fae', 'dry', 'ges', 'taa',
                'fug', 'jig', 'pap', 'fad', 'bar',
                'wea', 'hum', 'pit', 'nut', 'tag',
                'mir', 'kyu', 'bag', 'sat', 'wye',
                'cud', 'tig', 'pua', 'bae', 'web',
                'mim', 'tau', 'nea', 'mar', 'flo',
                'wro', 'jet', 'pyx', 'ink', 'vee',
                'aum', 'wax', 'bit', 'leu', 'pul',
                'gra', 'nib', 'tut', 'maw', 'hew',
                'vie', 'yed', 'wae', 'tue', 'fed',
                'fry', 'gau', 'rev', 'cly', 'jap',
                'aam', 'wur', 'mus', 'het', 'pik',
                'gel', 'mau', 'sam', 'rhe', 'mem',
                'aid', 'ger', 'zat', 'sit', 'tim',
                'jew', 'tat', 'nip', 'gal', 'bas',
                'pst', 'spy', 'sig', 'vas', 'wap',
                'sum', 'fei', 'pes', 'fit', 'gym',
                'sea', 'cap', 'rap', 'che', 'see',
                'til', 'phi', 'wac', 'zee', 'jur',
                'cub', 'pur', 'wig', 'tec', 'neb',
                'yex', 'hap', 'naa', 'fig', 'hat',
                'tub', 'way', 'zig', 'wir', 'lug',
                'pea', 'lao', 'wut', 'kep', 'pep',
                'vis', 'had', 'mat', 'tra', 'sab',
                'key', 'fam', 'rib', 'shy', 'yee',
                'zax', 'ait', 'wab', 'caw', 'meo',
                'lux', 'leg', 'pim', 'red', 'yet',
                'yew', 'yer', 'lou', 'waf', 'mab',
                'zak', 'fat', 'lap', 'bay', 'gus',
                'ham', 'new', 'kaw', 'gag', 'pry',
                'why', 'wup', 'mel', 'pay', 'gup',
                'feu', 'sie', 'sah', 'pug', 'meg',
                'bad', 'tyt', 'cut', 'zep', 'cup',
                'sad', 'mho', 'bat', 'aim', 'tee',
                'kil', 'pad', 'her', 'ler', 'hak',
                'fub', 'flu', 'bal', 'loy', 'tie',
                'sny', 'pia', 'fro', 'bed', 'khu',
                'gue', 'nat', 'lee', 'kha', 'sar',
                'gio', 'nim', 'kim', 'hey', 'pee',
                'vau', 'fez', 'gas', 'lue', 'jat',
                'bah', 'kaj', 'tua', 'jar', 'lye',
                'reg', 'wid', 'waw', 'fib', 'few',
                'nid', 'nul', 'cid', 'ram', 'lay',
                'val', 'pax', 'met', 'tae', 'tam',
                'blo', 'zoo', 'hie', 'rye', 'kee',
                'hau', 'tri', 'nab', 'sly', 'huk',
                'wis', 'bub', 'nye', 'bud', 'net',
                'lei', 'beg', 'yus', 'pet', 'ear',
                'rit', 'lis', 'cyp', 'fet', 'tst',
                'fey', 'suk', 'mig', 'gay', 'yea',
                'yes', 'ret', 'vat', 'gid', 'lev',
                'rus', 'tit', 'hub', 'wud', 'pat',
                'bra', 'rig', 'lif', 'hut', 'mam',
                'vai', 'sus', 'gee', 'him', 'fix',
                'she', 'hay', 'hia', 'suz', 'pix',
                'cry', 'rax', 'rab', 'tha', 'mes',
                'bug', 'yah', 'who', 'kyl', 'gar',
                'mad', 'cag', 'lut', 'wem', 'put',
                'tal', 'baa', 'rug', 'rue', 'grr',
                'reb', 'cho', 'bib', 'bur', 'gil',
                'yaw', 'jim', 'mev', 'lag', 'hug',
                'keb', 'rud', 'fag', 'ser', 'cab',
                'nee', 'gem', 'wee', 'sai', 'gib',
                'sic', 'taw', 'cal', 'tab', 'hem',
                'pud', 'mae', 'rux', 'his', 'wei',
                'rad', 'war', 'oak', 'tye', 'kef',
                'zar', 'mag', 'lit', 'zel', 'may',
                'mid', 'set', 'lex', 'mas', 'nam',
                'gip', 'sex', 'les', 'sim', 'sew',
                'yid', 'wim', 'laz', 'lox', 'ket',
                'tez', 'fur', 'lum', 'jut', 'gif',
                'mug', 'gap', 'kui', 'fee', 'bee',
                'yap', 'hag', 'huh', 'ann', 'tug',
                'pus', 'mum', 'yis', 'mud', 'lek',
                'sid', 'lam', 'sao', 'try', 'buy',
                'cig', 'cam', 'ind', 'tew', 'hud',
                'zer', 'gyp', 'bap', 'lof', 'cat',
                'ber', 'gab', 'bum', 'kid', 'peg',
                'eel', 'ked', 'aye', 'fip', 'hei',
                'lat', 'wah', 'ted', 'tar', 'leo',
                'vag', 'psi', 'mru', 'nub', 'jud',
                'cep', 'loo', 'rie', 'yar', 'hit',
                'sil', 'yep', 'eat', 'gaz', 'bis',
                'pic', 'get', 'kay', 'pie', 'cro',
                'jag', 'gaw', 'nak', 'liz', 'two',
                'raj', 'bey', 'sib', 'rub', 'thy',
                'pub', 'gez', 'zip'}

    assert actual == expected

def test_task2c_1() -> None:
    g = LazyGraph("web2")
    actual = variations(g, "lanius", 3, False)
    
    assert len(actual) == 0

def test_task2c_2() -> None:
    g = LazyGraph("web2")
    actual_t = variations(g, "cortical", 4, True)
    actual_f = variations(g, "cortical", 4, False)

    expected_t = {'cortices', 'vertices'}
    expected_f = {'vertices'}
    
    assert actual_t == expected_t
    assert actual_f == expected_f

def test_task2c_3() -> None:
    g = LazyGraph("web2")
    actual_t = variations(g, "ionism", 4, True)
    actual_f = variations(g, "ionism", 4, False)

    expected_t = {'malist', 'modest', 'podium', 'modish',
                  'danish', 'codist', 'sodium', 'curium',
                  'datism', 'nosism', 'nazism', 'vanist',
                  'mulism', 'tanist', 'cerium', 'marist'}
    expected_f = {'malist', 'modest', 'curium', 'cerium',
                  'marist'}
    
    assert actual_t == expected_t
    assert actual_f == expected_f

def test_task3_1() -> None:
    g = PrecompGraph("web2", 4)
    actual = shortest_word_path(g, "cite", "molt")
    allowable = [['cite', 'mite', 'mitt', 'mott', 'molt'],
                 ['cite', 'mite', 'mitt', 'milt', 'molt'],
                 ['cite', 'mite', 'mile', 'mole', 'molt'],
                 ['cite', 'mite', 'mile', 'milt', 'molt'],
                 ['cite', 'mite', 'mote', 'mole', 'molt'],
                 ['cite', 'mite', 'mote', 'mott', 'molt'],
                 ['cite', 'cote', 'cole', 'mole', 'molt'],
                 ['cite', 'cote', 'cole', 'colt', 'molt'],
                 ['cite', 'cote', 'mote', 'mole', 'molt'],
                 ['cite', 'cote', 'mote', 'mott', 'molt']
]
                
    assert actual in allowable

def test_task3_2() -> None:
    g = PrecompGraph("web2", 4)
    actual = shortest_word_path(g, "done", "here")
    allowable = [['done', 'dene', 'dere', 'here']]
                
    assert actual in allowable

def test_task3_3() -> None:
    g = PrecompGraph("web2", 4)
    actual = shortest_word_path(g, "drop", "kick")
    allowable = [['drop', 'prop', 'poop', 'pook', 'pock', 'pick', 'kick']]
                
    assert actual in allowable

def test_task4a_1() -> None:
    g = LetterSeqGraph("web2")
    actual = g.adjacent("p")
    expected = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    
    assert actual == expected

def test_task4a_2() -> None:
    g = LetterSeqGraph("web2")
    actual = g.adjacent("qq")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            if a + b != "qq" and (a == "q" or b == "q"):
                expected.add(a + b)
    
    assert actual == expected

def test_task4a_3() -> None:
    g = LetterSeqGraph("web2")
    actual = g.adjacent("wxy")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            for c in lc:
                if a + b + c != "wxy" and \
                   ((a == "w" and b == "x") or (a == "w" and c == "y") or
                    (b == "x" and c == "y")):
                    expected.add(a + b + c)
    
    assert actual == expected

def test_task4a_4() -> None:
    g = LetterSeqGraph("web2")
    actual = g.adjacent("oh")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            if a + b != "oh" and (a == "o" or b == "h"):
                expected.add(a + b)
    
    assert actual == expected

def test_task4a_5() -> None:
    g = LetterSeqGraph("web2")
    actual = g.degree("p")
    expected = 25
    
    assert actual == expected

def test_task4a_6() -> None:
    g = LetterSeqGraph("web2")
    actual = g.degree("wx")
    expected = 25 + 25
    
    assert actual == expected

def test_task4a_7() -> None:
    g = LetterSeqGraph("web2")
    actual = g.degree("wxy")
    expected = 25 + 25 + 25
    
    assert actual == expected

def test_task4a_8() -> None:
    g = LetterSeqGraph("web2")
    actual = g.degree("oh")
    expected = 25 + 25
    
    assert actual == expected

def test_task4a_9() -> None:
    g = LetterSeqGraph("web2")
    actual = g.is_actual_word("oh")
    expected = True
    
    assert actual == expected

def test_task4a_10() -> None:
    g = LetterSeqGraph("web2")
    actual = g.is_actual_word("wx")
    expected = False
    
    assert actual == expected

def test_task4c_is_word_1() -> None:
    g = LazyGraph("web2")
    assert g.is_actual_word("extraordinary")

def test_task4c_is_word_2() -> None:
    g = LazyGraph("web2")
    assert g.is_actual_word("toledo")

def test_task4c_is_word_3() -> None:
    g = LazyGraph("web2")
    assert g.is_actual_word("lengthy")

def test_task4c_is_not_word_1() -> None:
    g = LazyGraph("web2")
    assert not g.is_actual_word("qwert")

def test_task4c_is_not_word_2() -> None:
    g = LazyGraph("web2")
    assert not g.is_actual_word("Toledo")

def test_task4c_is_not_word_3() -> None:
    g = LazyGraph("web2")
    assert not g.is_actual_word("misspalled")

def test_task4c_adjacent_1() -> None:
    g = LazyGraph("web2")
    actual = g.adjacent("mane")
    expected = {'mage', 'mans', 'gane', 'mace',
                'mine', 'cane', 'mant', 'manx',
                'tane', 'mana', 'mani', 'made',
                'mang', 'dane', 'sane', 'mank',
                'mand', 'mano', 'maze', 'mare',
                'jane', 'wane', 'mone', 'mate',
                'male', 'nane', 'make', 'mann',
                'many', 'pane', 'rane', 'bane',
                'lane', 'vane'}
    assert actual == expected

def test_task4c_adjacent_2() -> None:
    g = LazyGraph("web2")
    actual = g.adjacent("qwertyu")
    expected: set[str] = set()
    assert actual == expected

def test_task4c_adjacent_3() -> None:
    g = LazyGraph("web2")
    actual = g.adjacent("lavish")
    expected = {'lamish', 'livish', 'lawish', 'cavish', 'luvish',
                'lakish', 'ravish', 'latish'}
                
    assert actual == expected

def test_task4c_degree_1() -> None:
    g = LazyGraph("web2")
    assert g.degree("mane") == 34

def test_task4c_degree_2() -> None:
    g = LazyGraph("web2")
    assert g.degree("qwertyu") == 0

def test_task4c_degree_3() -> None:
    g = LazyGraph("web2")
    assert g.degree("lavish") == 8
