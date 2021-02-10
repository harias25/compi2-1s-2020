
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDORESTOrightUMENOSDECIMAL DIVIDIDO ENTERO IMPRIMIR MAS MENOS PARDER PARIZQ POR PTCOMA RESTOinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : imprimir_instr \n                        | error imprimir_instr     : IMPRIMIR PARIZQ expresion PARDER PTCOMAexpresion : primitiva \n                 | expresion_unaria\n                 | expresion_numerica expresion : PARIZQ expresion PARDER expresion_numerica   :   expresion MAS expresion \n                            |   expresion MENOS expresion \n                            |   expresion POR expresion\n                            |   expresion DIVIDIDO expresion\n                            |   expresion RESTO expresionexpresion_unaria   :   MENOS expresion %prec UMENOSprimitiva : ENTERO\n                 | DECIMAL '
    
_lr_action_items = {'error':([0,2,3,4,5,7,26,],[5,5,-3,-4,-5,-2,-6,]),'IMPRIMIR':([0,2,3,4,5,7,26,],[6,6,-3,-4,-5,-2,-6,]),'$end':([1,2,3,4,5,7,26,],[0,-1,-3,-4,-5,-2,-6,]),'PARIZQ':([6,8,9,16,19,20,21,22,23,],[8,9,9,9,9,9,9,9,9,]),'ENTERO':([8,9,16,19,20,21,22,23,],[14,14,14,14,14,14,14,14,]),'DECIMAL':([8,9,16,19,20,21,22,23,],[15,15,15,15,15,15,15,15,]),'MENOS':([8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,27,28,29,30,31,],[16,16,20,-7,-8,-9,-17,-18,16,20,16,16,16,16,16,-16,-10,-11,-12,-13,-14,-15,]),'PARDER':([10,11,12,13,14,15,17,24,25,27,28,29,30,31,],[18,-7,-8,-9,-17,-18,25,-16,-10,-11,-12,-13,-14,-15,]),'MAS':([10,11,12,13,14,15,17,24,25,27,28,29,30,31,],[19,-7,-8,-9,-17,-18,19,-16,-10,-11,-12,-13,-14,-15,]),'POR':([10,11,12,13,14,15,17,24,25,27,28,29,30,31,],[21,-7,-8,-9,-17,-18,21,-16,-10,21,21,-13,-14,-15,]),'DIVIDIDO':([10,11,12,13,14,15,17,24,25,27,28,29,30,31,],[22,-7,-8,-9,-17,-18,22,-16,-10,22,22,-13,-14,-15,]),'RESTO':([10,11,12,13,14,15,17,24,25,27,28,29,30,31,],[23,-7,-8,-9,-17,-18,23,-16,-10,23,23,-13,-14,-15,]),'PTCOMA':([18,],[26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,7,]),'imprimir_instr':([0,2,],[4,4,]),'expresion':([8,9,16,19,20,21,22,23,],[10,17,24,27,28,29,30,31,]),'primitiva':([8,9,16,19,20,21,22,23,],[11,11,11,11,11,11,11,11,]),'expresion_unaria':([8,9,16,19,20,21,22,23,],[12,12,12,12,12,12,12,12,]),'expresion_numerica':([8,9,16,19,20,21,22,23,],[13,13,13,13,13,13,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',81),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',87),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',92),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',96),
  ('instruccion -> error','instruccion',1,'p_instruccion','gramatica.py',97),
  ('imprimir_instr -> IMPRIMIR PARIZQ expresion PARDER PTCOMA','imprimir_instr',5,'p_instruccion_imprimir','gramatica.py',101),
  ('expresion -> primitiva','expresion',1,'p_expresion','gramatica.py',109),
  ('expresion -> expresion_unaria','expresion',1,'p_expresion','gramatica.py',110),
  ('expresion -> expresion_numerica','expresion',1,'p_expresion','gramatica.py',111),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_par','gramatica.py',116),
  ('expresion_numerica -> expresion MAS expresion','expresion_numerica',3,'p_expresion_numerica','gramatica.py',121),
  ('expresion_numerica -> expresion MENOS expresion','expresion_numerica',3,'p_expresion_numerica','gramatica.py',122),
  ('expresion_numerica -> expresion POR expresion','expresion_numerica',3,'p_expresion_numerica','gramatica.py',123),
  ('expresion_numerica -> expresion DIVIDIDO expresion','expresion_numerica',3,'p_expresion_numerica','gramatica.py',124),
  ('expresion_numerica -> expresion RESTO expresion','expresion_numerica',3,'p_expresion_numerica','gramatica.py',125),
  ('expresion_unaria -> MENOS expresion','expresion_unaria',2,'p_expresion_unaria','gramatica.py',142),
  ('primitiva -> ENTERO','primitiva',1,'p_expresion_primitiva','gramatica.py',149),
  ('primitiva -> DECIMAL','primitiva',1,'p_expresion_primitiva','gramatica.py',150),
]