#!/bin/python3

__INFO__ = {
    'Encode': 'TVH',
    'Encoder Admin': 'Trần Văn Hoàng',
    'Background': 'Vip Pro Prime',
    'Contact Zalo': '0974698128',
    'Youtuber': 'https://www.youtube.com/@TranVanHoang2005'
}

import ast, random, marshal, base64, bz2, zlib, lzma, time
from ast import *
from time import sleep
import os
import sys
from pystyle import Colors, Colorate

sys.setrecursionlimit(99999999)

ver = str(sys.version_info.major)+'.'+str(sys.version_info.minor)

try:
    from pystyle import *
except ModuleNotFoundError:
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Cài Đặt...')
    __import__('os').system(f'pip{ver} install pystyle')
    from pystyle import *

try:
    System.Clear()
except Exception:
    pass

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
cust = '🐉🐲⭐✦✧✨💫🌠⚡🔥💥☄️🌪❄️🌀🥋🥊⚔️👊🙌👐🟠🔴🟡🟢🔵🟣⚫⚪👽🤖👺🐢🐒🦍👑💎🔮🍑🍗🍚🍶🏯⛩⛰🛡👑🧙\u200d♂️🤜🤛😡😤🥵🤯🌌🌍🌑☀️🌠'

e = dict(zip(string, cust))
decode_map = {v: k for k, v in e.items()}

def banner():
    banner = Colorate.Diagonal(Colors.rainbow, """
████████╗██╗   ██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██║   ██║██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║   ██║███████║   ██║   ██║   ██║██║   ██║██║     
   ██║   ╚██╗ ██╔╝██╔══██║   ██║   ██║   ██║██║   ██║██║     
   ██║    ╚████╔╝ ██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝     ╚═══╝  ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
""")
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def info():
    info = Colorate.Diagonal(Colors.rainbow, """
\nAdmin Tool : Trần Văn Hoàng            Phiên Bản : 1.0
════════════════════════════════════════════════  
Youtuber : Trần Văn Hoàng
Zalo : 0974698128
════════════════════════════════════════════════  
""")
    for X in info:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def enc(s: str) -> str:
    noisy = s.encode().hex()
    mapped = ''.join(e.get(c, c) for c in noisy)
    return f'bien5("{mapped}")'

buitlins = ['__import__', 'abs', 'all', 'any', 'ascii', 'bin', 'breakpoint', 'callable', 'chr', 'compile', 'delattr', 'dir', 'divmod', 'eval', 'exec', 'format', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'aiter', 'len', 'locals', 'max', 'min', 'next', 'anext', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 'vars', 'None', 'Ellipsis', 'NotImplemented', 'False', 'True', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip']

anti = """
import sys

print(' ' * len('[♤] > Đang Chạy...'), end='\\r')

if str(bien12_add('sys').exit) != '<built-in function exit>':
    print('\033[1;39mPhát Hiện Hook Request')
    imp('sys').exit()

if str(print) != '<built-in function print>':
    print('\033[1;39mPhát Hiện Hook Request')
    bien12_add('sys').exit()

if str(exec) != '<built-in function exec>':
    print('\033[1;39mPhát Hiện Hook Request')
    bien12_add('sys').exit()

if str(input) != '<built-in function input>':
    print('\033[1;39mPhát Hiện Hook Request')
    bien12_add('sys').exit()

if str(len) != '<built-in function len>':
    print('\033[1;39mPhát Hiện Hook Request')
    bien12_add('sys').exit()

if str(bien12_add('marshal').loads) != '<built-in function loads>':
    print('\033[1;39mPhát Hiện Hook Request')
    bien12_add('sys').exit()

if "pydevd" in sys.modules or "trace" in sys.argv:
	print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mPhát Hiện Bebug, Thoát !")
	bien12_add('sys').exit()

if sys.argv[0].endswith(".pyc"):
	print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mKhông Hỗ Trợ Chạy File .pyc, Thoát !")
	bien12_add('os')._exit(137)

if len(open(__file__, 'rb').read().splitlines()) != 76:
    print("\033[1;39m[♤] > Không Được Chỉnh Sửa Tập Tin Này !")
    bien12_add('sys').exit()

if __INFO__ != {
    'Encode': 'TVH',
    'Encoder Admin': 'Trần Văn Hoàng',
    'Background': 'Vip Pro Prime',
    'Contact Zalo': '0974698128',
    'Youtuber': 'https://www.youtube.com/@TranVanHoang2005'
}:
    print("\033[1;39m[♤] > Không Được Chỉnh Sửa Tập Tin Này !")
    bien12_add('sys').exit()



"""

def antidec():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))

v = antidec()
args = antidec()
kwds = antidec()
d = antidec()
k = antidec()
c = antidec()
arg_ = antidec()
s = antidec()

SANH = f"""#!/bin/python{ver}
# -*- coding: utf-8 -*-

__INFO__ = {{
    'Encode': 'TVH',
    'Encoder Admin': 'Trần Văn Hoàng',
    'Background': 'Vip Pro Prime',
    'Contact Zalo': '0974698128',
    'Youtuber': 'https://www.youtube.com/@TranVanHoang2005'
}}    

class Version(object):
    def __init__(self):
        if str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor) != "{ver}":
            print(f'\033[1;39m[♤] > Phiên Bản Hiện Tại : {{str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor)}}.\\n[♤] > Vui Lòng Cài Đặt Python {ver} Để Dùng !')
            __import__('sys').exit()
        else:
            print('\033[1;39m[♤] > Đang Chạy...', end='\\r')

    def __call__(self, *{args}, **{kwds}):
        global bien1, bien2, bien, bien4, bien5, bien6, bien7, bien8, bien9, bien10, bien, bien12, bien12_add
        globals()['bien6'] = eval('lave'[::-1])
        globals()['bien7'] = bien6('rts'[::-1])
        globals()['bien8'] = bien6('setyb'[::-1])
        globals()['bien9'] = bien6(('tcid')[::-1])
        globals()['bien2'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        globals()['bien'] = "🐉🐲⭐✦✧✨💫🌠⚡🔥💥☄️🌪❄️🌀🥋🥊⚔️👊🙌👐🟠🔴🟡🟢🔵🟣⚫⚪👽🤖👺🐢🐒🦍👑💎🔮🍑🍗🍚🍶🏯⛩⛰🛡👑🧙‍♂️🤜🤛😡😤🥵🤯🌌🌍🌑☀️🌠"
        globals()['bien10'] = bien6('piz'[::-1])
        globals()['bien4'] = bien9(bien10(bien2, bien))
        {d} = {{{v}: {k} for {k}, {v} in bien4.items()}}
        globals()['bien5'] = lambda {s}: getattr(bien8, "fromhex")(bien7().join(({d}.get({c}, {c}) for {c} in {s}))).decode()
        globals()['bien12_add'] = bien6({enc('__tropmi__')}[::-1])
        globals()['bien12'] = bien6({enc('cexe')}[::-1])
        globals()['bien1'] = bien6({enc('tni')}[::-1])

Version()()

class EncTVH(object):
    def __init__(self, *{args}):
        setattr(self, "EncodeTVH1", {enc('base64')})
        setattr(self, "EncodeTVH2", {enc('bz2')})
        setattr(self, "EncodeTVH3", {enc('zlib')})
        setattr(self, "EncodeTVH4", {enc('lzma')})
        setattr(self, "{arg_}", {args}[0])

    def scan(self):
        return getattr(bien12_add(getattr(self, "EncodeTVH4")), {enc("decompress")})(
            getattr(bien12_add(getattr(self, "EncodeTVH3")), {enc("decompress")})(
                getattr(bien12_add(getattr(self, "EncodeTVH2")), {enc("decompress")})(
                    getattr(bien12_add(getattr(self, "EncodeTVH1")), {enc("a85decode")})(getattr(self, "{arg_}"))
                )
            )
        )

class TVHSummoner(object):
    def __init__(self):
        setattr(self, "EncodeTVH5", {enc('marshal')})
        setattr(self, "EncodeTVH6", bien4)
        setattr(self, "EncodeTVH7", bien12)

    def wish(self, {arg_}):
        getattr(self, "EncodeTVH7")(
            getattr(bien12_add(getattr(self, "EncodeTVH5")), {enc("loads")})({arg_}),
            globals()
        )

    def __call__(self, *{args}, **{kwds}):
        bien5 = EncTVH({args}[0]).scan()
        self.wish(bien5)

try:
    TVHSummoner()(BYTECODE)
except Exception as e:
    print(e)
except KeyboardInterrupt:
    exit('\033[1;39m[♤] > ^C : Thoát')"""

def _args(name):
    return ast.arguments(
        posonlyargs=[],
        args=[ast.arg(arg=name)],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )

def obfstr(s):
    lst=[ord(i) for i in s]; v=antidec()
    lam3=ast.Lambda(
        args=_args(antidec()),
        body=ast.Call(
            func=ast.Attribute(
                value=ast.Call(ast.Name('bien7',ast.Load()),[],[]),
                attr="join", ctx=ast.Load()
            ),
            args=[ast.GeneratorExp(
                elt=ast.Call(ast.Name("chr",ast.Load()),[ast.Name(v,ast.Load())],[]),
                generators=[ast.comprehension(
                    target=ast.Name(v,ast.Store()),
                    iter=ast.List([ast.Constant(x) for x in lst],ast.Load()),
                    ifs=[], is_async=0
                )]
            )],
            keywords=[]
        )
    )
    lam2=ast.Lambda(_args(antidec()),
        ast.Call(lam3,[ast.Constant("Tran Van Hoang (TVH)")],[]))
    lam1=ast.Lambda(_args(antidec()),
        ast.Call(lam2,[ast.Constant("Tran Van Hoang (TVH)")],[]))
    return ast.Call(lam1,[ast.Constant("Tran Van Hoang (TVH)")],[])

def obfint(i):
    haha=2010-i
    lam3=ast.Lambda(_args(antidec()),
        ast.Call(ast.Name("bien1",ast.Load()),
            [ast.BinOp(ast.Constant(2010),ast.Sub(),ast.Constant(haha))],[]))
    lam2=ast.Lambda(_args(antidec()),
        ast.Call(lam3,[ast.Constant("Tran Van Hoang (TVH)")],[]))
    lam1=ast.Lambda(_args(antidec()),
        ast.Call(lam2,[ast.Constant("Tran Van Hoang (TVH)")],[]))
    return ast.Call(lam1,[ast.Constant("Tran Van Hoang (TVH)")],[])

def joinstr(f):
    if not isinstance(f, ast.JoinedStr):
        return f
    vl = []
    for i in f.values:
        if isinstance(i, ast.Constant):
            vl.append(i)
        elif isinstance(i, ast.FormattedValue):
            value_expr = i.value
            if i.conversion == 115:
                value_expr = Call(func=Name(id='bien7', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 114:
                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 97:
                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])
            if i.format_spec:
                if isinstance(i.format_spec, ast.JoinedStr):
                    spec_expr = joinstr(i.format_spec)
                elif isinstance(i.format_spec, ast.Constant):
                    spec_expr = i.format_spec
                elif isinstance(i.format_spec, ast.FormattedValue):
                    spec_parts = []
                    spec_value = i.format_spec.value
                    if i.format_spec.conversion == 115:
                        spec_value = Call(func=Name(id='bien7', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 114:
                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 97:
                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])
                    spec_expr = spec_value
                else:
                    spec_expr = i.format_spec
                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])
            elif i.conversion == -1:
                value_expr = Call(func=Name(id='bien7', ctx=Load()), args=[value_expr], keywords=[])
            vl.append(value_expr)
        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):
            vl.append(joinstr(i))
        else:
            vl.append(Call(func=Name(id='bien7', ctx=Load()), args=[i], keywords=[]))
    if not vl:
        return Constant(value='')
    if len(vl) == 1 and isinstance(vl[0], ast.Constant):
        return vl[0]
    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])

class cv(ast.NodeTransformer):
    def visit_JoinedStr(self, node):
        node = joinstr(node)
        return node

class hide(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id in buitlins:
            node = Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='bien12_add', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Constant(value=node.id)], keywords=[])
        return node
    
class obf(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node = obfstr(node.value)
        elif isinstance(node.value, int):
            node = obfint(node.value)
        return node

def gen_jcode(code):
    men = antidec()
    tranvanhoang = antidec()
    tvh = antidec()
    return [Assign(targets=[Name(id=tranvanhoang, ctx=Store())], value=Constant(value=men), lineno=0), Assign(targets=[Name(id=tvh, ctx=Store())], value=Constant(value=True), lineno=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id=tranvanhoang, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=tvh, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=True)])]), body=[Expr(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Constant(value='dit me may')))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id=tranvanhoang, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=tvh, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=False)])]), body=[Try(body=[Expr(value=Tuple(elts=[BinOp(left=Constant(value=1), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=123), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=12312321312), op=Div(), right=Constant(value=0))], ctx=Load()))], handlers=[ExceptHandler(body=[code])], orelse=[], finalbody=[])], orelse=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id=tranvanhoang, ctx=Load()), ops=[Eq()], comparators=[Constant(value='gay')]), Compare(left=Name(id=tvh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=False)])]), body=[Expr(value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai lon cha nha may')], keywords=[])), args=[], keywords=[]))], orelse=[While(test=Constant(value=True), body=[Pass()], orelse=[]), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai dit thang cha may')], keywords=[]))])])])]

class junk(ast.NodeTransformer):
    def visit_Module(self, node):
        for i, j in enumerate(node.body):
            if isinstance(j, (ast.FunctionDef, ast.ClassDef)):
                self.visit(j)
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_FunctionDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_ClassDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node
        
banner()
info()

while True:
    file_name = input(
        "\n\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mNhập Tên File \033[1;31m: \033[1;36m"
    )
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            code = ast.parse(anti + f.read())
        break
    except FileNotFoundError:
        print("\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;31mFile Không Tồn Tại")
        
hide_builtins = True if input(
    "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Ẩn Nội Dung Tích Hợp Không ? \033[1;39m(\033[1;32my\033[1;39m/\033[1;31mn\033[1;39m) \033[1;31m: \033[1;36m"
) != 'n' else False

junk_code = True if input(
    "\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mBạn Có Muốn Thêm Mã Rác Không (Nên Chọn Yes) \033[1;39m(\033[1;32my\033[1;39m/\033[1;31mn\033[1;39m) \033[1;31m: \033[1;36m"
) != 'n' else False

print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Encode...')
st = time.time()
print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Chuyển Đổi F-String Thành Chuỗi Nối...')
code = cv().visit(code)

if hide_builtins:
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐang Ẩn Nội Dung File...')
    code = hide().visit(code)

print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mEncode Nội Dung...')
code = obf().visit(code)

if junk_code:
    print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mThêm Kí Tự Ngẫu Nhiên...')
    code = junk().visit(code)

print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐọc...')
code = marshal.dumps(compile(ast.unparse(code), '<Bien5>', 'exec'))

print('\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mEncoded...')
code = base64.a85encode(bz2.compress(zlib.compress(lzma.compress(code))))

open("obf-"+file_name,'wb').write(SANH.replace("BYTECODE", str(code)).encode())

print(f'\033[1;32m[\033[1;31m♤\033[1;32m]\033[1;33m ➩ \033[1;32mĐã Lưu Thành {"obf-"+file_name}')