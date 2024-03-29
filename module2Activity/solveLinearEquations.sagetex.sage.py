## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file solveLinearEquations.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_97 = Integer(97); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_118 = Integer(118); _sage_const_112 = Integer(112); _sage_const_110 = Integer(110); _sage_const_33 = Integer(33); _sage_const_210 = Integer(210); _sage_const_216 = Integer(216); _sage_const_218 = Integer(218); _sage_const_199 = Integer(199); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_120 = Integer(120); _sage_const_204 = Integer(204); _sage_const_125 = Integer(125); _sage_const_102 = Integer(102); _sage_const_104 = Integer(104); _sage_const_18 = Integer(18); _sage_const_224 = Integer(224); _sage_const_226 = Integer(226)## This file (solveLinearEquations.sagetex.sage) was *autogenerated* from solveLinearEquations.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solveLinearEquations', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_32 
_st_.blockbegin()
try:
 # SOLVES BASIC LINEAR EQUATIONS OF THE FORM
     # b0 * (b1 + b2 * x) = b3 ( x * b4 - b5)
 
 x = var('x')
 
 ###################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def generateBlocks():
     listNaturals = range(_sage_const_2 , _sage_const_16 )
     n0, n1, n2, n3, n4, n5 = sample(listNaturals, _sage_const_6 )
     b0 = Integer(-n0)
     b1 = Integer(maybeMakeNegative(n1))
     b2 = Integer(maybeMakeNegative(n2))
     b3 = Integer(-n3)
     b4 = Integer(maybeMakeNegative(n4))
     b5 = Integer(maybeMakeNegative(n5))
     # Begin checking for one solution
     OneSolutionCheck = b0*b2 - b3*b4
     # Makes sure there is exactly one solution
     while (OneSolutionCheck == _sage_const_0 ):
         listNaturals = range(_sage_const_2 , _sage_const_16 )
         n0, n1, n2, n3, n4, n5 = sample(listNaturals, _sage_const_6 )
         b0 = Integer(-n0)
         b1 = Integer(maybeMakeNegative(n1))
         b2 = Integer(maybeMakeNegative(n2))
         b3 = Integer(-n3)
         b4 = Integer(maybeMakeNegative(n4))
         b5 = Integer(maybeMakeNegative(n5))
         # Begin checking for one solution
         OneSolutionCheck = b0*b2 - b3*b4
     blocks = [b0, b1, b2, b3, b4, b5]
     return blocks
 
 #b0 * (b1 + b2 * x) =  b3 ( x * b4 - b5)
 def generateSolution(blocks):
     a, b, c, d, e, f = blocks
     basicLinearEquation = a * (b + c * x) - d * ( x * e - f)
     solution = float(solve(basicLinearEquation, x)[_sage_const_0 ].rhs())
     return solution
 
 ######### END OF DEFINITIONS ##########
 
 ##### QUESTION 10 #####
 blocks10 = generateBlocks()
 answer10 = generateSolution(blocks10)
 displayEquationLeft10 = blocks10[_sage_const_1 ]+blocks10[_sage_const_2 ]*x
 displayEquationRight10 = blocks10[_sage_const_4 ]*x-blocks10[_sage_const_5 ]
 
 ##### QUESTION 11 #####
 blocks11 = generateBlocks()
 answer11 = generateSolution(blocks11)
 displayEquationLeft11 = blocks11[_sage_const_1 ]+blocks11[_sage_const_2 ]*x
 displayEquationRight11 = blocks11[_sage_const_4 ]*x-blocks11[_sage_const_5 ]
 
 ##### QUESTION 12 #####
 blocks12 = generateBlocks()
 answer12 = generateSolution(blocks12)
 displayEquationLeft12 = blocks12[_sage_const_1 ]+blocks12[_sage_const_2 ]*x
 displayEquationRight12 = blocks12[_sage_const_4 ]*x-blocks12[_sage_const_5 ]
 
except:
 _st_.goboom(_sage_const_97 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_0 , latex(blocks10[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_1 , latex(displayEquationLeft10))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_2 , latex(blocks10[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_3 , latex(displayEquationRight10))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_4 , latex(answer10))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_5 , latex(blocks11[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_6 , latex(displayEquationLeft11))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_7 , latex(blocks11[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_8 , latex(displayEquationRight11))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_9 , latex(answer11))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_10 , latex(blocks12[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_11 , latex(displayEquationLeft12))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_12 , latex(blocks12[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_13 , latex(displayEquationRight12))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_14 , latex(answer12))
except:
 _st_.goboom(_sage_const_120 )
_st_.current_tex_line = _sage_const_125 
_st_.blockbegin()
try:
 # Type 2 - Solve Advanced linear equations (fractions)
 #(coefficients[0]*x + numerators[0])/denominators[0]
     # - (coefficients[1]*x+numerators[1])/denominators[1]
     # = (coefficients[2]*x+numerators[2])/denominators[2]
 
 x = var('x')
 ###################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 #No restrictions on coefficients or numerators
 def createThreeRandomIntegers():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_3 , _sage_const_9 ))
     return [a, b, c]
 
 def createThreeDistinctRandomNaturals():
     possibleNaturals= range(_sage_const_2 ,_sage_const_7 )
     n1, n2, n3 = sample(possibleNaturals, _sage_const_3 )
     naturals = [Integer(n1), Integer(n2), Integer(n3)]
     return naturals
 
 def createThreeDistinctRandomIntegers():
     a, b, c = sample(range(_sage_const_3 , _sage_const_8 ), _sage_const_3 )
     return [Integer(maybeMakeNegative(a)), Integer(maybeMakeNegative(b)), Integer(maybeMakeNegative(c))]
 
 def createViableConstants():
     a, b, c = createThreeRandomIntegers()
     d, e, f = createThreeRandomIntegers()
     g, h, i = createThreeDistinctRandomNaturals()
     # Check that there is exactly one solution to the linear equation
     OneSolutionCheck = (a/g) - (b/h) - (c/i)
     while (OneSolutionCheck == _sage_const_0 ):
         a, b, c = createThreeRandomIntegers()
         d, e, f = createThreeRandomIntegers()
         g, h, i = createThreeDistinctRandomNaturals()
         OneSolutionCheck = (a/g) - (b/h) - (c/i)
     return [a, b, c, d, e, f, g, h, i]
 
 def createSolution(constants):
     a, b, c, d, e, f, g, h, i = constants
     equationBlockOne = (a*x+d)/g
     equationBlockTwo = (b*x+e)/h
     equationBlockThree = (c*x+f)/i
     toSolve = equationBlockOne - equationBlockTwo - equationBlockThree
     solution = round(float(solve(toSolve, x)[_sage_const_0 ].rhs()), _sage_const_3 )
     return solution
 
 ######## END OF DEFINITIONS ###########
 
 ##### QUESTION 13 #####
 constants13 = createViableConstants()
 displayNumeratorA13 = constants13[_sage_const_0 ] * x + constants13[_sage_const_3 ]
 displayNumeratorB13 = constants13[_sage_const_1 ] * x + constants13[_sage_const_4 ]
 displayNumeratorC13 = constants13[_sage_const_2 ] * x + constants13[_sage_const_5 ]
 answer13 = createSolution(constants13)
 
 ##### QUESTION 14 #####
 constants14 = createViableConstants()
 displayNumeratorA14 = constants14[_sage_const_0 ] * x + constants14[_sage_const_3 ]
 displayNumeratorB14 = constants14[_sage_const_1 ] * x + constants14[_sage_const_4 ]
 displayNumeratorC14 = constants14[_sage_const_2 ] * x + constants14[_sage_const_5 ]
 answer14 = createSolution(constants14)
 
 ##### QUESTION 15 #####
 constants15 = createViableConstants()
 displayNumeratorA15 = constants15[_sage_const_0 ] * x + constants15[_sage_const_3 ]
 displayNumeratorB15 = constants15[_sage_const_1 ] * x + constants15[_sage_const_4 ]
 displayNumeratorC15 = constants15[_sage_const_2 ] * x + constants15[_sage_const_5 ]
 answer15 = createSolution(constants15)
except:
 _st_.goboom(_sage_const_199 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_15 , latex(displayNumeratorA13))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_16 , latex(constants13[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_17 , latex(displayNumeratorB13))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_18 , latex(constants13[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_19 , latex(displayNumeratorC13))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_20 , latex(constants13[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_204 )
try:
 _st_.current_tex_line = _sage_const_210 
 _st_.inline(_sage_const_21 , latex(answer13))
except:
 _st_.goboom(_sage_const_210 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_22 , latex(displayNumeratorA14))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_23 , latex(constants14[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_24 , latex(displayNumeratorB14))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_25 , latex(constants14[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_26 , latex(displayNumeratorC14))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_216 
 _st_.inline(_sage_const_27 , latex(constants14[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_216 )
try:
 _st_.current_tex_line = _sage_const_218 
 _st_.inline(_sage_const_28 , latex(answer14))
except:
 _st_.goboom(_sage_const_218 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_29 , latex(displayNumeratorA15))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_30 , latex(constants15[_sage_const_6 ]))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_31 , latex(displayNumeratorB15))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_32 , latex(constants15[_sage_const_7 ]))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_33 , latex(displayNumeratorC15))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_34 , latex(constants15[_sage_const_8 ]))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_226 
 _st_.inline(_sage_const_35 , latex(answer15))
except:
 _st_.goboom(_sage_const_226 )
_st_.endofdoc()

