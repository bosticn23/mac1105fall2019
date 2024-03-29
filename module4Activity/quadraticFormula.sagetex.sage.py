## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file quadraticFormula.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_101 = Integer(101); _sage_const_121 = Integer(121); _sage_const_103 = Integer(103); _sage_const_8 = Integer(8); _sage_const_99 = Integer(99); _sage_const_123 = Integer(123); _sage_const_94 = Integer(94); _sage_const_110 = Integer(110); _sage_const_125 = Integer(125); _sage_const_10 = Integer(10); _sage_const_112 = Integer(112); _sage_const_33 = Integer(33); _sage_const_114 = Integer(114)## This file (quadraticFormula.sagetex.sage) was *autogenerated* from quadraticFormula.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('quadraticFormula', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_33 
_st_.blockbegin()
try:
 x = var("x")
 
 ################################
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateCoefficients():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     coefficients = [a, b, c]
     discrim = findDiscriminant(coefficients)
     while (discrim < _sage_const_0  or discrim == _sage_const_0  or isSquare(discrim)==true):
         a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         c = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
         coefficients = [a, b, c]
         discrim = findDiscriminant(coefficients)
     return [a, b, c]
 
 def generateSolution(coefficients):
     a, b, c = coefficients
     solveThisQuadratic = a*x**_sage_const_2 +b*x+c
     solution = solve(solveThisQuadratic, x)
     if (solution[_sage_const_0 ].rhs() < solution[_sage_const_1 ].rhs()):
         x0 = round(float(solution[_sage_const_0 ].rhs()), _sage_const_3 )
         x1 = round(float(solution[_sage_const_1 ].rhs()), _sage_const_3 )
         answer = [x0, x1]
         return answer
     else:
         x0 = round(float(solution[_sage_const_1 ].rhs()), _sage_const_3 )
         x1 = round(float(solution[_sage_const_0 ].rhs()), _sage_const_3 )
         answer = [x0, x1]
         return answer
 
 def findDiscriminant(coefficients):
     a, b, c = coefficients
     return b**_sage_const_2  - _sage_const_4 *a*c
 
 def isSquare(integer):
     root = sqrt(integer)
     typeInteger = type(_sage_const_3 )
     if type(root) == typeInteger:
         return True
     else:
         return False
 
 ################################
 coefficients11 = generateCoefficients()
 solution11 = generateSolution(coefficients11)
 problemDisplay11 = coefficients11[_sage_const_0 ]*x**_sage_const_2  + coefficients11[_sage_const_1 ]*x + coefficients11[_sage_const_2 ]
 
 coefficients12 = generateCoefficients()
 solution12 = generateSolution(coefficients12)
 problemDisplay12 = coefficients12[_sage_const_0 ]*x**_sage_const_2  + coefficients12[_sage_const_1 ]*x + coefficients12[_sage_const_2 ]
 
 coefficients13 = generateCoefficients()
 solution13 = generateSolution(coefficients13)
 problemDisplay13 = coefficients13[_sage_const_0 ]*x**_sage_const_2  + coefficients13[_sage_const_1 ]*x + coefficients13[_sage_const_2 ]
except:
 _st_.goboom(_sage_const_94 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_0 , latex(problemDisplay11))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_1 , latex(solution11[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_2 , latex(solution11[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_3 , latex(problemDisplay12))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_4 , latex(solution12[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_5 , latex(solution12[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_6 , latex(problemDisplay13))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_7 , latex(solution13[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_8 , latex(solution13[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_125 )
_st_.endofdoc()

