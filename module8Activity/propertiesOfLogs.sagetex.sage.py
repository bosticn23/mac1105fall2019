## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file propertiesOfLogs.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_42 = Integer(42); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_5 = Integer(5); _sage_const_60 = Integer(60); _sage_const_4 = Integer(4); _sage_const_104 = Integer(104); _sage_const_9 = Integer(9); _sage_const_66 = Integer(66); _sage_const_80 = Integer(80); _sage_const_1 = Integer(1); _sage_const_68 = Integer(68); _sage_const_78 = Integer(78); _sage_const_10 = Integer(10); _sage_const_8 = Integer(8); _sage_const_94 = Integer(94); _sage_const_102 = Integer(102); _sage_const_86 = Integer(86); _sage_const_6 = Integer(6)## This file (propertiesOfLogs.sagetex.sage) was *autogenerated* from propertiesOfLogs.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('propertiesOfLogs', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_42 
_st_.blockbegin()
try:
 x, y, z, = var("x, y, z")
 
 def generateDisplayAndAnswer():
     a = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     expX = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     expY = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     expZ = ZZ.random_element(_sage_const_3 , _sage_const_9 )
     function = (_sage_const_1 /_sage_const_2 )*log(a) + (expX/_sage_const_2 )*log(x) + (expY/_sage_const_2 )*log(y) - expZ*log(z)
     numerator = a*x**expX*y**expY
     denominator = z**expZ
     return [numerator, denominator, function]
 
 ### QUESTION 7 ###
 numerator7, denominator7, answer7 = generateDisplayAndAnswer()
 
 ### Question 8 ###
 numerator8, denominator8, answer8 = generateDisplayAndAnswer()
except:
 _st_.goboom(_sage_const_60 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_0 , latex(numerator7))
except:
 _st_.goboom(_sage_const_66 )
try:
 _st_.current_tex_line = _sage_const_66 
 _st_.inline(_sage_const_1 , latex(denominator7))
except:
 _st_.goboom(_sage_const_66 )
try:
 _st_.current_tex_line = _sage_const_68 
 _st_.inline(_sage_const_2 , latex(answer7))
except:
 _st_.goboom(_sage_const_68 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_3 , latex(numerator8))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_4 , latex(denominator8))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_5 , latex(answer8))
except:
 _st_.goboom(_sage_const_80 )
_st_.current_tex_line = _sage_const_86 
_st_.blockbegin()
try:
 def generateCoefficientsAndAnswer():
     a = ZZ.random_element(_sage_const_3 , _sage_const_10 )
     b = ZZ.random_element(_sage_const_3 , _sage_const_10 )
     answer = round(float(ln(b)- _sage_const_2 *a), _sage_const_3 )
     return [a, b, answer]
 
 constant9, numerator9, answer9 = generateCoefficientsAndAnswer()
except:
 _st_.goboom(_sage_const_94 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_6 , latex(constant9))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_7 , latex(numerator9))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_8 , latex(answer9))
except:
 _st_.goboom(_sage_const_104 )
_st_.endofdoc()

