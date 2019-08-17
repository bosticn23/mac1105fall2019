## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file propertiesOfRealNumbers.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_134 = Integer(134); _sage_const_132 = Integer(132); _sage_const_138 = Integer(138); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_59 = Integer(59); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_15 = Integer(15); _sage_const_123 = Integer(123); _sage_const_126 = Integer(126); _sage_const_100 = Integer(100); _sage_const_128 = Integer(128); _sage_const_140 = Integer(140)## This file (propertiesOfRealNumbers.sagetex.sage) was *autogenerated* from propertiesOfRealNumbers.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('propertiesOfRealNumbers', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_59 
_st_.blockbegin()
try:
 # Order of Operations Question
 # Structure:
     # $\sage{constants[0]} - \sage{constants[1]} \div \sage{constants[2]} * \sage{constants[3]} - (\sage{constants[4]} * \sage{constants[5]})$
 
 def convertToSage(constants):
     p0, p1, p2, p3, p4, p5 = constants
     c0 = Integer(p0)
     c1 = Integer(p1)
     c2 = Integer(p2)
     c3 = Integer(p3)
     c4 = Integer(p4)
     c5 = Integer(p5)
     return [c0, c1, c2, c3, c4, c5]
 
 def generateSolution(constants):
     c0, c1, c2, c3, c4, c5 = convertToSage(constants)
     solution = float((c0 - ((c1/c2) * c3)) - (c4 * c5 ))
     print "Solution: %f" %solution
     return solution
 
 def generateDistractor(constants):
     c0, c1, c2, c3, c4, c5 = convertToSage(constants)
     solution = float(c0 - (c1/(c2 * c3)) - (c4 * c5 ))
     print "Distractor: %f" %solution
     return solution
 
 def createConstants():
     listNaturals=list(range(_sage_const_2 , _sage_const_21 ))
     # Array of 6 distinct integers
     c0, c1, c2, c3, c4, c5 = convertToSage(sample(listNaturals, _sage_const_6 ))
     constants = [c0, c1, c2, c3, c4, c5]
     solution = generateSolution(constants)
     distractor = generateDistractor(constants)
     # CHECKS if doing the question wrong will still give the correct solution.
     index = _sage_const_0 
     while solution == distractor:
         listNaturals = list(range(_sage_const_2 , _sage_const_21 ))
         c0, c1, c2, c3, c4, c5 = convertToSage(sample(listNaturals, _sage_const_6 ))
         constants = [c0, c1, c2, c3, c4, c5]
         solution = generateSolution(constants)
         distractor = generateDistractor(constants)
         # Makes sure we don't get stuck in an infinite loop
         index += _sage_const_1 
         if (index > _sage_const_100 ):
             break
         print index
     print solution, distractor
     return constants
 
 ########## END OF DEFINITIONS ###########
 
 ######### QUESTION 7 ##########
 constants7 = createConstants()
 answer7 = generateSolution(constants7)
 
 ######### QUESTION 8 ##########
 constants8 = createConstants()
 answer8 = generateSolution(constants8)
 
 ######### QUESTION 9 ##########
 constants9 = createConstants()
 answer9 = generateSolution(constants9)
 
except:
 _st_.goboom(_sage_const_123 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_0 , latex(constants7[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_1 , latex(constants7[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_2 , latex(constants7[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_3 , latex(constants7[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_4 , latex(constants7[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_5 , latex(constants7[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.inline(_sage_const_6 , latex(answer7))
except:
 _st_.goboom(_sage_const_128 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_7 , latex(constants8[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_8 , latex(constants8[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_9 , latex(constants8[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_10 , latex(constants8[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_11 , latex(constants8[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_12 , latex(constants8[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_134 
 _st_.inline(_sage_const_13 , latex(answer8))
except:
 _st_.goboom(_sage_const_134 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_14 , latex(constants9[_sage_const_0 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_15 , latex(constants9[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_16 , latex(constants9[_sage_const_2 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_17 , latex(constants9[_sage_const_3 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_18 , latex(constants9[_sage_const_4 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_19 , latex(constants9[_sage_const_5 ]))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_20 , latex(answer9))
except:
 _st_.goboom(_sage_const_140 )
_st_.endofdoc()

