
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMENTAR ESCREVER VAR numero string S : com  S : S com  com : ESCREVER escreverops\n                | VAR variavel \n                | COMENTAR string  escreverops : string\n                        | contas\n                        | string ',' escreverops \n                        | contas ',' escreverops contas : numero '*' contas\n                   | numero '+' contas\n                   | numero '-' contas \n                   | numero '/' contas \n                   | numero  variavel : string '=' string\n                     | string '=' numero \n                     | string "
    
_lr_action_items = {'ESCREVER':([0,1,2,6,7,8,9,10,11,12,13,21,22,23,24,25,26,27,28,],[3,3,-1,-2,-3,-6,-7,-14,-4,-17,-5,-8,-9,-10,-11,-12,-13,-15,-16,]),'VAR':([0,1,2,6,7,8,9,10,11,12,13,21,22,23,24,25,26,27,28,],[4,4,-1,-2,-3,-6,-7,-14,-4,-17,-5,-8,-9,-10,-11,-12,-13,-15,-16,]),'COMENTAR':([0,1,2,6,7,8,9,10,11,12,13,21,22,23,24,25,26,27,28,],[5,5,-1,-2,-3,-6,-7,-14,-4,-17,-5,-8,-9,-10,-11,-12,-13,-15,-16,]),'$end':([1,2,6,7,8,9,10,11,12,13,21,22,23,24,25,26,27,28,],[0,-1,-2,-3,-6,-7,-14,-4,-17,-5,-8,-9,-10,-11,-12,-13,-15,-16,]),'string':([3,4,5,14,15,20,],[8,12,13,8,8,27,]),'numero':([3,14,15,16,17,18,19,20,],[10,10,10,10,10,10,10,28,]),',':([8,9,10,23,24,25,26,],[14,15,-14,-10,-11,-12,-13,]),'*':([10,],[16,]),'+':([10,],[17,]),'-':([10,],[18,]),'/':([10,],[19,]),'=':([12,],[20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'com':([0,1,],[2,6,]),'escreverops':([3,14,15,],[7,21,22,]),'contas':([3,14,15,16,17,18,19,],[9,9,9,23,24,25,26,]),'variavel':([4,],[11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> com','S',1,'p_S','gramatica.py',21),
  ('S -> S com','S',2,'p_S1','gramatica.py',25),
  ('com -> ESCREVER escreverops','com',2,'p_com','gramatica.py',30),
  ('com -> VAR variavel','com',2,'p_com','gramatica.py',31),
  ('com -> COMENTAR string','com',2,'p_com','gramatica.py',32),
  ('escreverops -> string','escreverops',1,'p_escreverops','gramatica.py',40),
  ('escreverops -> contas','escreverops',1,'p_escreverops','gramatica.py',41),
  ('escreverops -> string , escreverops','escreverops',3,'p_escreverops','gramatica.py',42),
  ('escreverops -> contas , escreverops','escreverops',3,'p_escreverops','gramatica.py',43),
  ('contas -> numero * contas','contas',3,'p_contas','gramatica.py',50),
  ('contas -> numero + contas','contas',3,'p_contas','gramatica.py',51),
  ('contas -> numero - contas','contas',3,'p_contas','gramatica.py',52),
  ('contas -> numero / contas','contas',3,'p_contas','gramatica.py',53),
  ('contas -> numero','contas',1,'p_contas','gramatica.py',54),
  ('variavel -> string = string','variavel',3,'p_variavel','gramatica.py',61),
  ('variavel -> string = numero','variavel',3,'p_variavel','gramatica.py',62),
  ('variavel -> string','variavel',1,'p_variavel','gramatica.py',63),
]
