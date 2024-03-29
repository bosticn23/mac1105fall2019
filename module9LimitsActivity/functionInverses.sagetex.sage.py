## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file functionInverses.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_201 = Integer(201); _sage_const_185 = Integer(185); _sage_const_110 = Integer(110); _sage_const_116 = Integer(116); _sage_const_157 = Integer(157); _sage_const_173 = Integer(173); _sage_const_213 = Integer(213); _sage_const_195 = Integer(195); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_36 = Integer(36); _sage_const_100 = Integer(100); _sage_const_167 = Integer(167); _sage_const_129 = Integer(129); _sage_const_94 = Integer(94); _sage_const_229 = Integer(229); _sage_const_223 = Integer(223)## This file (functionInverses.sagetex.sage) was *autogenerated* from functionInverses.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('functionInverses', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_36 
_st_.blockbegin()
try:
 x = var("x")
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateInverseLinear():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     line1 = a * x + b
     line2 = (x - b)/a
     return [line1, line2]
 
 def generateInverseSquareRoot():
     h1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     h2 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     k = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     squareRoot = sqrt(h1*x + h2) + k
     pivot = -h2/h1
     if (h1*(pivot - _sage_const_1 ) + h2) &lt; _sage_const_0 :
         domain = [pivot, Infinity]
     else:
         domain = [-Infinity, pivot]
     squareRootInverse = ((x-k)**_sage_const_2  - h2)/h1
     return [squareRoot, squareRootInverse, domain]
 
 def generateSquared():
     h1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     h2 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     k = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     squared = (h1*x + h2)**_sage_const_2  + k
     return squared
 
 def generateInverseCube():
     h1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     h2 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     k = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     cube = (h1*x + h2)**_sage_const_3  + k
     cubeInverse = ((x-k)**(_sage_const_1 /_sage_const_3 ) - h2)/h1
     return [cube, cubeInverse]
 
 def generateInverseCubeRoot():
     h1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     h2 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     k = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_8 ))
     cubeRoot = (h1*x + h2)**(_sage_const_1 /_sage_const_3 ) + k
     cubeRootInverse = ((x-k)**_sage_const_3  - h2)/h1
     return [cubeRoot, cubeRootInverse]
 #########
 f1, f1Inverse = generateInverseCube()
 f2 = generateSquared()
 f3, f3Inverse = generateInverseLinear()
 f4, f4Inverse, domain4 = generateInverseSquareRoot()
 while domain4[_sage_const_0 ] > -Infinity:
     f4, f4Inverse, domain4 = generateInverseSquareRoot()
 f5, f5Inverse = generateInverseCubeRoot()
 
except:
 _st_.goboom(_sage_const_94 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_0 , latex(f1))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.inline(_sage_const_1 , latex(f1Inverse))
except:
 _st_.goboom(_sage_const_110 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_2 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_3 , latex(Infinity))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_129 
 _st_.inline(_sage_const_4 , latex(f2))
except:
 _st_.goboom(_sage_const_129 )
try:
 _st_.current_tex_line = _sage_const_157 
 _st_.inline(_sage_const_5 , latex(f3))
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_6 , latex(f3Inverse))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_7 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_8 , latex(Infinity))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_185 
 _st_.inline(_sage_const_9 , latex(f4))
except:
 _st_.goboom(_sage_const_185 )
try:
 _st_.current_tex_line = _sage_const_195 
 _st_.inline(_sage_const_10 , latex(f4Inverse))
except:
 _st_.goboom(_sage_const_195 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_11 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_12 , latex(domain4[_sage_const_1 ]))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_213 
 _st_.inline(_sage_const_13 , latex(f5))
except:
 _st_.goboom(_sage_const_213 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_14 , latex(f5Inverse))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_15 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_16 , latex(Infinity))
except:
 _st_.goboom(_sage_const_229 )
_st_.endofdoc()

