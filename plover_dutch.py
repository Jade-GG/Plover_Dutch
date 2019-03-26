
KEYS = (
    '#',
    'G-', 'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '5-', '0-', '-E', '-U', '*')

SUFFIX_KEYS = ('G-', '-Z', '-T', '-S')

NUMBER_KEY = '#'

NUMBERS = {
    'G-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '0-',
    '-F': '-6',
    '-P': '-7',
    '-L': '-8',
    '-T': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
    #template
    #(r'^(.*) \^$', r'\1'),

    #!generalized prefix strokes!
    (r'^(.*) \^ (.*)==$', r'\2\1'),


    #list of suffixes:
    #-t     (maakt)
    #-d     (bedoeld)
    #-s     (auto's)
    #-te    (breedte, gemaakte)
    #-de    (rondde)
    #-ste   (grootste)
    #-e     (grote)
    #-en    (worden)
    #-er    (maker)
    #-end   (verwarrend)
    #-in    (gravin)
    #-ing   (verbazing)
    #-ingen?(aanpassingen)
    #-ig    (kattig)
    #-erij  (bakkerij)
    #-erig  (bezitterig)
    #-etje  (mannetje)
    #-tje   (maantje)
    #-kje   (bankje)
    #-ie    (bakkie)
    #-lijk  (walgelijk)
    #-rijk  (vindingrijk)
    #-ij    (ambtenarij)


    #auto + s = auto's
    (r'^(.*[iouy]) \^ s$', r"\1's"),


    #bel + en = bellen (inclusief -etje en -ie)
    (r'^(.*[bcdfghjklmnpqrstvwxyz][aeiou])([bcdfghjklmnpqrstz]) \^ (e|en|er|erij|end|in|ing|ingen|ig|erig|etje|ie)$', r'\1\2\2\3'),

    #groente + en = groenten
    (r'^(.*)([bcdfghjklmnpqrstvwxyz])(e) \^ (e|en|er|erij|end|erig)$', r'\1\2\4'),

    #baal + en = balen (inclusief -ij)
    (r'^(.*)([aeiou])\2([bcdghjklmnpqrtvwxyz]) \^ (e|en|er|erij|end|in|ing|ingen|ig|erig|ij)$', r'\1\2\3\4'),
    #baas + en = bazen
    (r'^(.*)([aeiou])\2s \^ (e|en|er|erij|end|in|ing|ingen|ig|erig)$', r'\1\2z\3'),
    #muis + en = muizen
    (r'^(.*)(ai|au|ei|eu|ie|oe|oi|ou|ui)s \^ (e|en|er|erij|end|in|ing|ingen|ig|erig)$', r'\1\2z\3'),
    #beef + en = beven
    (r'^(.*)([aeiou])\2f \^ (e|en|er|erij|end|in|ing|ingen|ig|erig)$', r'\1\2v\3'),
    #precies + e = precieze
    (r'^(.*ie)s \^ (e|en|er|erij|end|in|ing|ingen|ig|erig)$', r'\1z\2'),


    #koning + -kje = koninkje
    (r'^(.*in)(g) \^ tje$', r'\1kje'),
    #baby + -tje = baby'tje
    (r'^(.*y) \^ tje$', r"\1'tje"),
    #opa + -tje = opaatje
    (r'^(.*[bcdfhdjklmnpqrstvwxyz])([aeou]) \^ tje$', r'\1\2\2tje'),
    #ski + -tje = skietje
    (r'^(.*[bcdfhdjklmnpqrstvwxyz]i) \^ tje$', r'\1etje'),
    #plaat + -tje = plaatje
    (r'^(.*[bdfgklpstxz]) \^ tje$', r'\1je'),

    #boom + -kje = boompje
    (r'^(.*m) \^ tje$', r'\1pje'),
]

ORTHOGRAPHY_RULES_ALIASES = {
}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'G-'        : 'S2-',
        'S-'        : 'S1-',
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'W-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-F'        : '-F',
        '-R'        : '-R',
        '-P'        : '-P',
        '-B'        : '-B',
        '-L'        : '-L',
        '-G'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-Z'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'G-'        : 'q',
        'S-'        : 'a',
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-F'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-L'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'G-'   : 'C',
        'S-'   : 'S',
        'T-'   : 'T',
        'K-'   : 'K',
        'P-'   : 'P',
        'W-'   : 'W',
        'H-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-U'   : 'U',
        '-F'   : 'F',
        '-R'   : 'Q',
        '-P'   : 'N',
        '-B'   : 'B',
        '-L'   : 'L',
        '-G'   : 'G',
        '-T'   : 'Y',
        '-S'   : 'X',
        '-D'   : 'D',
        '-Z'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'G-'   : 'S2-',
        'S-'   : 'S1-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'W-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-U'   : '-U',
        '-F'   : '-F',
        '-R'   : '-R',
        '-P'   : '-P',
        '-B'   : '-B',
        '-L'   : '-L',
        '-G'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ('d_user.json', 'd_commands.json', 'd_main.json')
