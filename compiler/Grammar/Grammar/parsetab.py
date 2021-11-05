
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQUALSEQUALSDISTINTleftGREATEREQUALLESSEQUALGREATERLESSleftPLUSMINUSleftTIMESDIVrightNOTrightUMINUSAND BOOL BREAK COLON COMMA CONTINUE DISTINT DIV ELSE ELSEIF END EQUALS EQUALSEQUALS FALSE FLOATLITERAL FUNCTION GREATER GREATEREQUAL ID IF INT64 INTLITERAL LEPAR LESS LESSEQUAL MINUS NOT OR PLUS POINT POT PRINT PRINTLN RETURN RIPAR SEMICOLON STRING STRINGLITERAL STRUCT TIMES TRUE WHILEstart : instructionsinstructions : instructions instruction\n                    | instructioninstruction  : printST SEMICOLON\n                    | ifST SEMICOLON\n                    | declarationST SEMICOLON\n                    | whileST SEMICOLON\n                    | callFunc SEMICOLON\n                    | declareFunc SEMICOLON\n                    | returnST SEMICOLON\n                    | breakST SEMICOLON\n                    | continueST SEMICOLON\n                    | createStruct SEMICOLON\n                    | declareStructST SEMICOLON\n                    | assignAccessST SEMICOLONtypes : INT64\n            |  STRING\n            |  BOOLstatement : instructionsdeclareFunc :  FUNCTION ID LEPAR RIPAR COLON COLON types statement END\n                    | FUNCTION ID LEPAR decParams RIPAR COLON COLON types statement ENDdecParams :    decParams COMMA ID COLON COLON types\n                    | ID COLON COLON typesreturnST : RETURN\n                | RETURN expressiondeclarationST : ID EQUALS expressionprintST  : PRINTLN LEPAR expression RIPARprintST  : PRINT LEPAR expression RIPARifST : IF expression statement END\n            | IF expression statement ELSE statement END\n            | IF expression statement elseIfList ENDelseIfList   : ELSEIF expression statement\n                    | ELSEIF expression statement ELSE statement\n                    | ELSEIF expression statement elseIfListcreateStruct : STRUCT ID attList ENDattList :  attList SEMICOLON ID COLON COLON types SEMICOLON\n                | ID COLON COLON typesdeclareStructST : ID COLON COLON IDassignAccessST : ID POINT ID EQUALS expressionwhileST : WHILE expression statement ENDbreakST : BREAKcontinueST : CONTINUEcallFunc : ID LEPAR RIPAR\n                | ID LEPAR expList RIPARexpList :  expList COMMA expression\n                | expressionexpression   : MINUS expression %prec UMINUS\n                    | NOT expression %prec UMINUS\n                    \n                    | expression PLUS expression\n                    | expression MINUS expression\n                    | expression TIMES expression\n                    | expression DIV expression\n                    | expression POT expression\n\n                    | expression GREATER expression\n                    | expression LESS expression\n                    | expression GREATEREQUAL expression\n                    | expression LESSEQUAL expression\n                    | expression EQUALSEQUALS expression\n                    | expression DISTINT expression\n                    \n                    | expression OR expression\n                    | expression AND expression\n                    | finalExpfinalExp : LEPAR expression RIPAR\n                | INTLITERAL\n                | FLOATLITERAL\n                | STRINGLITERAL\n                | TRUE\n                | FALSE\n                | ID\n                | callFunc\n                | accessSTaccessST : ID POINT ID'
    
_lr_action_items = {'PRINTLN':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[16,16,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,16,-62,-64,-65,-66,-67,-68,-69,-70,-71,16,16,-47,-48,-43,16,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,16,-16,-17,-18,16,16,16,]),'PRINT':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[17,17,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,17,-62,-64,-65,-66,-67,-68,-69,-70,-71,17,17,-47,-48,-43,17,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,17,-16,-17,-18,17,17,17,]),'IF':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[18,18,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,18,-62,-64,-65,-66,-67,-68,-69,-70,-71,18,18,-47,-48,-43,18,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,18,-16,-17,-18,18,18,18,]),'ID':([0,2,3,18,20,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,87,90,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,124,127,133,143,144,145,147,150,156,],[19,19,-3,51,51,59,51,61,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,51,51,19,51,51,-62,51,-64,-65,-66,-67,-68,-69,-70,-71,51,51,88,19,91,51,51,51,51,51,51,51,51,51,51,51,51,51,19,-47,-48,113,-43,116,119,19,51,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,51,51,135,19,141,-16,-17,-18,19,19,19,]),'WHILE':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[20,20,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,20,-62,-64,-65,-66,-67,-68,-69,-70,-71,20,20,-47,-48,-43,20,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,20,-16,-17,-18,20,20,20,]),'FUNCTION':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[21,21,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,21,-62,-64,-65,-66,-67,-68,-69,-70,-71,21,21,-47,-48,-43,21,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,21,-16,-17,-18,21,21,21,]),'RETURN':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[22,22,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,22,-62,-64,-65,-66,-67,-68,-69,-70,-71,22,22,-47,-48,-43,22,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,22,-16,-17,-18,22,22,22,]),'BREAK':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[23,23,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,23,-62,-64,-65,-66,-67,-68,-69,-70,-71,23,23,-47,-48,-43,23,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,23,-16,-17,-18,23,23,23,]),'CONTINUE':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[24,24,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,24,-62,-64,-65,-66,-67,-68,-69,-70,-71,24,24,-47,-48,-43,24,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,24,-16,-17,-18,24,24,24,]),'STRUCT':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,84,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,143,144,145,147,150,156,],[25,25,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,25,-62,-64,-65,-66,-67,-68,-69,-70,-71,25,25,-47,-48,-43,25,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,25,-16,-17,-18,25,25,25,]),'$end':([1,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,],[0,-1,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'END':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,89,92,97,125,137,142,143,144,145,148,154,155,160,162,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,95,-19,118,123,126,136,-32,-37,-16,-17,-18,-34,-33,159,163,-36,]),'ELSE':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,137,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,96,-19,147,]),'ELSEIF':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,137,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,98,-19,98,]),'SEMICOLON':([4,5,6,7,8,9,10,11,12,13,14,15,22,23,24,44,46,47,48,49,50,51,52,53,60,79,80,83,84,92,93,94,95,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,118,123,126,129,136,142,143,144,145,158,159,162,163,],[27,28,29,30,31,32,33,34,35,36,37,38,-24,-41,-42,-62,-64,-65,-66,-67,-68,-69,-70,-71,-25,-47,-48,-26,-43,124,-27,-28,-29,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,-38,-40,-35,-31,-39,-30,-37,-16,-17,-18,162,-20,-36,-21,]),'LEPAR':([16,17,18,19,20,22,39,40,42,43,45,51,54,55,59,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[39,40,45,55,45,45,45,45,45,45,45,55,45,45,90,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'MINUS':([18,20,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,83,84,86,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,127,128,129,],[42,42,42,42,42,66,42,42,-62,42,-64,-65,-66,-67,-68,-69,-70,-71,42,42,66,66,66,66,42,42,42,42,42,42,42,42,42,42,42,42,42,-47,-48,66,66,-43,66,42,-49,-50,-51,-52,66,66,66,66,66,66,66,66,66,-63,-72,-44,42,42,66,66,66,]),'NOT':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'INTLITERAL':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FLOATLITERAL':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'STRINGLITERAL':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'TRUE':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'FALSE':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'EQUALS':([19,88,],[54,117,]),'COLON':([19,56,91,119,120,122,130,131,132,135,140,141,146,152,],[56,87,122,130,131,134,138,139,140,146,151,152,153,157,]),'POINT':([19,51,],[57,82,]),'PLUS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[65,-62,-64,-65,-66,-67,-68,-69,-70,-71,65,65,65,65,-47,-48,65,65,-43,65,-49,-50,-51,-52,65,65,65,65,65,65,65,65,65,-63,-72,-44,65,65,65,]),'TIMES':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[67,-62,-64,-65,-66,-67,-68,-69,-70,-71,67,67,67,67,-47,-48,67,67,-43,67,67,67,-51,-52,67,67,67,67,67,67,67,67,67,-63,-72,-44,67,67,67,]),'DIV':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[68,-62,-64,-65,-66,-67,-68,-69,-70,-71,68,68,68,68,-47,-48,68,68,-43,68,68,68,-51,-52,68,68,68,68,68,68,68,68,68,-63,-72,-44,68,68,68,]),'POT':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[69,-62,-64,-65,-66,-67,-68,-69,-70,-71,69,69,69,69,-47,-48,69,69,-43,69,-49,-50,-51,-52,69,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,69,69,69,]),'GREATER':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[70,-62,-64,-65,-66,-67,-68,-69,-70,-71,70,70,70,70,-47,-48,70,70,-43,70,-49,-50,-51,-52,70,-54,-55,-56,-57,70,70,70,70,-63,-72,-44,70,70,70,]),'LESS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[71,-62,-64,-65,-66,-67,-68,-69,-70,-71,71,71,71,71,-47,-48,71,71,-43,71,-49,-50,-51,-52,71,-54,-55,-56,-57,71,71,71,71,-63,-72,-44,71,71,71,]),'GREATEREQUAL':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[72,-62,-64,-65,-66,-67,-68,-69,-70,-71,72,72,72,72,-47,-48,72,72,-43,72,-49,-50,-51,-52,72,-54,-55,-56,-57,72,72,72,72,-63,-72,-44,72,72,72,]),'LESSEQUAL':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[73,-62,-64,-65,-66,-67,-68,-69,-70,-71,73,73,73,73,-47,-48,73,73,-43,73,-49,-50,-51,-52,73,-54,-55,-56,-57,73,73,73,73,-63,-72,-44,73,73,73,]),'EQUALSEQUALS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[74,-62,-64,-65,-66,-67,-68,-69,-70,-71,74,74,74,74,-47,-48,74,74,-43,74,-49,-50,-51,-52,74,-54,-55,-56,-57,-58,-59,74,74,-63,-72,-44,74,74,74,]),'DISTINT':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[75,-62,-64,-65,-66,-67,-68,-69,-70,-71,75,75,75,75,-47,-48,75,75,-43,75,-49,-50,-51,-52,75,-54,-55,-56,-57,-58,-59,75,75,-63,-72,-44,75,75,75,]),'OR':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[76,-62,-64,-65,-66,-67,-68,-69,-70,-71,76,76,76,76,-47,-48,76,76,-43,76,-49,-50,-51,-52,76,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,76,76,76,]),'AND':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,84,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,127,128,129,],[77,-62,-64,-65,-66,-67,-68,-69,-70,-71,77,77,77,77,-47,-48,77,77,-43,77,-49,-50,-51,-52,77,-54,-55,-56,-57,-58,-59,77,-61,-63,-72,-44,77,77,77,]),'RIPAR':([44,46,47,48,49,50,51,52,53,55,62,63,79,80,81,84,85,86,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,128,143,144,145,149,161,],[-62,-64,-65,-66,-67,-68,-69,-70,-71,84,93,94,-47,-48,112,-43,114,-46,120,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,132,-45,-16,-17,-18,-23,-22,]),'COMMA':([44,46,47,48,49,50,51,52,53,79,80,84,85,86,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,128,143,144,145,149,161,],[-62,-64,-65,-66,-67,-68,-69,-70,-71,-47,-48,-43,115,-46,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-63,-72,-44,133,-45,-16,-17,-18,-23,-22,]),'INT64':([134,138,139,151,153,157,],[143,143,143,143,143,143,]),'STRING':([134,138,139,151,153,157,],[144,144,144,144,144,144,]),'BOOL':([134,138,139,151,153,157,],[145,145,145,145,145,145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instructions':([0,41,58,96,127,147,150,156,],[2,78,78,78,78,78,78,78,]),'instruction':([0,2,41,58,78,96,127,147,150,156,],[3,26,3,3,26,3,3,3,3,3,]),'printST':([0,2,41,58,78,96,127,147,150,156,],[4,4,4,4,4,4,4,4,4,4,]),'ifST':([0,2,41,58,78,96,127,147,150,156,],[5,5,5,5,5,5,5,5,5,5,]),'declarationST':([0,2,41,58,78,96,127,147,150,156,],[6,6,6,6,6,6,6,6,6,6,]),'whileST':([0,2,41,58,78,96,127,147,150,156,],[7,7,7,7,7,7,7,7,7,7,]),'callFunc':([0,2,18,20,22,39,40,41,42,43,45,54,55,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,96,98,115,117,127,147,150,156,],[8,8,52,52,52,52,52,8,52,52,52,52,52,8,52,52,52,52,52,52,52,52,52,52,52,52,52,8,8,52,52,52,8,8,8,8,]),'declareFunc':([0,2,41,58,78,96,127,147,150,156,],[9,9,9,9,9,9,9,9,9,9,]),'returnST':([0,2,41,58,78,96,127,147,150,156,],[10,10,10,10,10,10,10,10,10,10,]),'breakST':([0,2,41,58,78,96,127,147,150,156,],[11,11,11,11,11,11,11,11,11,11,]),'continueST':([0,2,41,58,78,96,127,147,150,156,],[12,12,12,12,12,12,12,12,12,12,]),'createStruct':([0,2,41,58,78,96,127,147,150,156,],[13,13,13,13,13,13,13,13,13,13,]),'declareStructST':([0,2,41,58,78,96,127,147,150,156,],[14,14,14,14,14,14,14,14,14,14,]),'assignAccessST':([0,2,41,58,78,96,127,147,150,156,],[15,15,15,15,15,15,15,15,15,15,]),'expression':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[41,58,60,62,63,79,80,81,83,86,99,100,101,102,103,104,105,106,107,108,109,110,111,127,128,129,]),'finalExp':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'accessST':([18,20,22,39,40,42,43,45,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,98,115,117,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'statement':([41,58,96,127,147,150,156,],[64,89,125,137,154,155,160,]),'expList':([55,],[85,]),'attList':([61,],[92,]),'elseIfList':([64,137,],[97,148,]),'decParams':([90,],[121,]),'types':([134,138,139,151,153,157,],[142,149,150,156,158,161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> instructions','start',1,'p_start','grammar.py',195),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','grammar.py',200),
  ('instructions -> instruction','instructions',1,'p_instructions','grammar.py',201),
  ('instruction -> printST SEMICOLON','instruction',2,'p_instruction','grammar.py',209),
  ('instruction -> ifST SEMICOLON','instruction',2,'p_instruction','grammar.py',210),
  ('instruction -> declarationST SEMICOLON','instruction',2,'p_instruction','grammar.py',211),
  ('instruction -> whileST SEMICOLON','instruction',2,'p_instruction','grammar.py',212),
  ('instruction -> callFunc SEMICOLON','instruction',2,'p_instruction','grammar.py',213),
  ('instruction -> declareFunc SEMICOLON','instruction',2,'p_instruction','grammar.py',214),
  ('instruction -> returnST SEMICOLON','instruction',2,'p_instruction','grammar.py',215),
  ('instruction -> breakST SEMICOLON','instruction',2,'p_instruction','grammar.py',216),
  ('instruction -> continueST SEMICOLON','instruction',2,'p_instruction','grammar.py',217),
  ('instruction -> createStruct SEMICOLON','instruction',2,'p_instruction','grammar.py',218),
  ('instruction -> declareStructST SEMICOLON','instruction',2,'p_instruction','grammar.py',219),
  ('instruction -> assignAccessST SEMICOLON','instruction',2,'p_instruction','grammar.py',220),
  ('types -> INT64','types',1,'p_type','grammar.py',225),
  ('types -> STRING','types',1,'p_type','grammar.py',226),
  ('types -> BOOL','types',1,'p_type','grammar.py',227),
  ('statement -> instructions','statement',1,'p_statement','grammar.py',237),
  ('declareFunc -> FUNCTION ID LEPAR RIPAR COLON COLON types statement END','declareFunc',9,'p_function','grammar.py',242),
  ('declareFunc -> FUNCTION ID LEPAR decParams RIPAR COLON COLON types statement END','declareFunc',10,'p_function','grammar.py',243),
  ('decParams -> decParams COMMA ID COLON COLON types','decParams',6,'p_decParams','grammar.py',250),
  ('decParams -> ID COLON COLON types','decParams',4,'p_decParams','grammar.py',251),
  ('returnST -> RETURN','returnST',1,'p_return','grammar.py',260),
  ('returnST -> RETURN expression','returnST',2,'p_return','grammar.py',261),
  ('declarationST -> ID EQUALS expression','declarationST',3,'p_declaration','grammar.py',269),
  ('printST -> PRINTLN LEPAR expression RIPAR','printST',4,'p_printlnST','grammar.py',274),
  ('printST -> PRINT LEPAR expression RIPAR','printST',4,'p_printST','grammar.py',278),
  ('ifST -> IF expression statement END','ifST',4,'p_ifST','grammar.py',283),
  ('ifST -> IF expression statement ELSE statement END','ifST',6,'p_ifST','grammar.py',284),
  ('ifST -> IF expression statement elseIfList END','ifST',5,'p_ifST','grammar.py',285),
  ('elseIfList -> ELSEIF expression statement','elseIfList',3,'p_elseIfList','grammar.py',294),
  ('elseIfList -> ELSEIF expression statement ELSE statement','elseIfList',5,'p_elseIfList','grammar.py',295),
  ('elseIfList -> ELSEIF expression statement elseIfList','elseIfList',4,'p_elseIfList','grammar.py',296),
  ('createStruct -> STRUCT ID attList END','createStruct',4,'p_createStruct','grammar.py',307),
  ('attList -> attList SEMICOLON ID COLON COLON types SEMICOLON','attList',7,'p_attList','grammar.py',311),
  ('attList -> ID COLON COLON types','attList',4,'p_attList','grammar.py',312),
  ('declareStructST -> ID COLON COLON ID','declareStructST',4,'p_declareStruct','grammar.py',323),
  ('assignAccessST -> ID POINT ID EQUALS expression','assignAccessST',5,'p_assignAccess','grammar.py',328),
  ('whileST -> WHILE expression statement END','whileST',4,'p_while','grammar.py',333),
  ('breakST -> BREAK','breakST',1,'p_break','grammar.py',338),
  ('continueST -> CONTINUE','continueST',1,'p_continue','grammar.py',343),
  ('callFunc -> ID LEPAR RIPAR','callFunc',3,'p_callfunc','grammar.py',348),
  ('callFunc -> ID LEPAR expList RIPAR','callFunc',4,'p_callfunc','grammar.py',349),
  ('expList -> expList COMMA expression','expList',3,'p_callparams','grammar.py',357),
  ('expList -> expression','expList',1,'p_callparams','grammar.py',358),
  ('expression -> MINUS expression','expression',2,'p_expression','grammar.py',367),
  ('expression -> NOT expression','expression',2,'p_expression','grammar.py',368),
  ('expression -> expression PLUS expression','expression',3,'p_expression','grammar.py',370),
  ('expression -> expression MINUS expression','expression',3,'p_expression','grammar.py',371),
  ('expression -> expression TIMES expression','expression',3,'p_expression','grammar.py',372),
  ('expression -> expression DIV expression','expression',3,'p_expression','grammar.py',373),
  ('expression -> expression POT expression','expression',3,'p_expression','grammar.py',374),
  ('expression -> expression GREATER expression','expression',3,'p_expression','grammar.py',376),
  ('expression -> expression LESS expression','expression',3,'p_expression','grammar.py',377),
  ('expression -> expression GREATEREQUAL expression','expression',3,'p_expression','grammar.py',378),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression','grammar.py',379),
  ('expression -> expression EQUALSEQUALS expression','expression',3,'p_expression','grammar.py',380),
  ('expression -> expression DISTINT expression','expression',3,'p_expression','grammar.py',381),
  ('expression -> expression OR expression','expression',3,'p_expression','grammar.py',383),
  ('expression -> expression AND expression','expression',3,'p_expression','grammar.py',384),
  ('expression -> finalExp','expression',1,'p_expression','grammar.py',385),
  ('finalExp -> LEPAR expression RIPAR','finalExp',3,'p_finalExp','grammar.py',420),
  ('finalExp -> INTLITERAL','finalExp',1,'p_finalExp','grammar.py',421),
  ('finalExp -> FLOATLITERAL','finalExp',1,'p_finalExp','grammar.py',422),
  ('finalExp -> STRINGLITERAL','finalExp',1,'p_finalExp','grammar.py',423),
  ('finalExp -> TRUE','finalExp',1,'p_finalExp','grammar.py',424),
  ('finalExp -> FALSE','finalExp',1,'p_finalExp','grammar.py',425),
  ('finalExp -> ID','finalExp',1,'p_finalExp','grammar.py',426),
  ('finalExp -> callFunc','finalExp',1,'p_finalExp','grammar.py',427),
  ('finalExp -> accessST','finalExp',1,'p_finalExp','grammar.py',428),
  ('accessST -> ID POINT ID','accessST',3,'p_accessST','grammar.py',450),
]