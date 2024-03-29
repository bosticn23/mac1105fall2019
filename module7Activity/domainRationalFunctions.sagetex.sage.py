## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file domainRationalFunctions.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_184 = Integer(184); _sage_const_186 = Integer(186); _sage_const_116 = Integer(116); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_228 = Integer(228); _sage_const_226 = Integer(226); _sage_const_249 = Integer(249); _sage_const_211 = Integer(211); _sage_const_247 = Integer(247); _sage_const_213 = Integer(213); _sage_const_130 = Integer(130); _sage_const_132 = Integer(132); _sage_const_238 = Integer(238); _sage_const_232 = Integer(232); _sage_const_236 = Integer(236); _sage_const_234 = Integer(234); _sage_const_258 = Integer(258); _sage_const_256 = Integer(256); _sage_const_126 = Integer(126); _sage_const_124 = Integer(124); _sage_const_207 = Integer(207); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_150 = Integer(150); _sage_const_205 = Integer(205); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_144 = Integer(144); _sage_const_142 = Integer(142); _sage_const_148 = Integer(148); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_170 = Integer(170); _sage_const_172 = Integer(172); _sage_const_192 = Integer(192); _sage_const_190 = Integer(190); _sage_const_215 = Integer(215); _sage_const_194 = Integer(194); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_168 = Integer(168); _sage_const_164 = Integer(164); _sage_const_162 = Integer(162)## This file (domainRationalFunctions.sagetex.sage) was *autogenerated* from domainRationalFunctions.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('domainRationalFunctions', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_30 
_st_.blockbegin()
try:
 R, x = QQ['x'].objgen()
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def makeIntegerFactor():
     zero = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     integerFactor = x - zero
     return [integerFactor, zero]
 
 def makeRationalFactor():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     while gcd(abs(a), abs(b)) > _sage_const_1 :
         a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     rationalFactor = a*x + b
     return [rationalFactor, -b/a]
 
 def makeIrrationalQuadratic():
     a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     discrim = b**_sage_const_2  - _sage_const_4 *a*c
     integerType = type(_sage_const_2 )
     while type(sqrt(discrim)) == integerType:
         a = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         b = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         c = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
         discrim = b**_sage_const_2  - _sage_const_4 *a*c
     solution0 = (-b + sqrt(discrim))/_sage_const_2 *a
     solution1 = (-b - sqrt(discrim))/_sage_const_2 *a
     smallerSolution, largerSolution = sorted([solution0, solution1])
     quadratic = a*x**_sage_const_2  + b*x + c
     return [quadratic, smallerSolution, largerSolution]
 
 def makeComplexQuadratic():
     a0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_4 ))
     b0 = maybeMakeNegative(ZZ.random_element(_sage_const_1 , _sage_const_6 ))
     complex0 = a0 + b0*i
     complex1 = a0 - b0*i
     quadratic = x**_sage_const_2  - (a0**_sage_const_2  + b0**_sage_const_2 )
     return [quadratic, complex0, complex1]
 ##########
 function1, answer1 = makeIntegerFactor()
 ###
 function2, answer2 = makeRationalFactor()
 ###
 factor3a, answer3aTEMP = makeRationalFactor()
 factor3b, answer3bTEMP = makeRationalFactor()
 while answer3aTEMP == answer3bTEMP:
     factor3a, answer3aTEMP = makeRationalFactor()
     factor3b, answer3bTEMP = makeRationalFactor()
 answer3a, answer3b = sorted([answer3aTEMP, answer3bTEMP])
 ###
 factor4a, answer4aTEMP = makeIntegerFactor()
 factor4b, answer4bTEMP = makeIntegerFactor()
 while answer4aTEMP == answer4bTEMP:
     function4a, answer4aTEMP = makeIntegerFactor()
     function4b, answer4bTEMP = makeIntegerFactor()
 function4 = factor4a * factor4b
 answer4a, answer4b = sorted([answer4aTEMP, answer4bTEMP])
 ###
 factor5a, answer5aTEMP = makeRationalFactor()
 factor5b, answer5bTEMP = makeRationalFactor()
 while answer5aTEMP == answer5bTEMP:
     function5a, answer5aTEMP = makeRationalFactor()
     function5b, answer5bTEMP = makeRationalFactor()
 function5 = factor5a * factor5b
 answer5a, answer5b = sorted([answer5aTEMP, answer5bTEMP])
 ###
 factor6a, answer6aTEMP = makeRationalFactor()
 factor6b, answer6bTEMP = makeRationalFactor()
 #factor6c, answer6cTEMP = makeIntegerFactor()
 while answer6aTEMP == answer6bTEMP:
     function6a, answer6aTEMP = makeRationalFactor()
     function6b, answer6bTEMP = makeRationalFactor()
 function6 = factor6a * factor6b * x
 answer6a, answer6b, answer6c = sorted([answer6aTEMP, answer6bTEMP, _sage_const_0 ])
 ###
 #factor7a, answer7 = makeIntegerFactor()
 answer7 = _sage_const_0 
 factor7b, answer7complexA, answer7complexB = makeComplexQuadratic()
 function7 = x * factor7b
except:
 _st_.goboom(_sage_const_116 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_124 
 _st_.inline(_sage_const_0 , latex(function1))
except:
 _st_.goboom(_sage_const_124 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_1 , latex(answer1))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_2 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_130 
 _st_.inline(_sage_const_3 , latex(answer1))
except:
 _st_.goboom(_sage_const_130 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_4 , latex(answer1))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_5 , latex(Infinity))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_6 , latex(function2))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_144 
 _st_.inline(_sage_const_7 , latex(answer2))
except:
 _st_.goboom(_sage_const_144 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_8 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_148 
 _st_.inline(_sage_const_9 , latex(answer2))
except:
 _st_.goboom(_sage_const_148 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_10 , latex(answer2))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_11 , latex(Infinity))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_12 , latex(factor3a))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_13 , latex(factor3b))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_164 
 _st_.inline(_sage_const_14 , latex(answer3a))
except:
 _st_.goboom(_sage_const_164 )
try:
 _st_.current_tex_line = _sage_const_164 
 _st_.inline(_sage_const_15 , latex(answer3b))
except:
 _st_.goboom(_sage_const_164 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_16 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.inline(_sage_const_17 , latex(answer3a))
except:
 _st_.goboom(_sage_const_168 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_18 , latex(answer3a))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_19 , latex(answer3b))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_20 , latex(answer3b))
except:
 _st_.goboom(_sage_const_172 )
try:
 _st_.current_tex_line = _sage_const_172 
 _st_.inline(_sage_const_21 , latex(Infinity))
except:
 _st_.goboom(_sage_const_172 )
try:
 _st_.current_tex_line = _sage_const_184 
 _st_.inline(_sage_const_22 , latex(function4))
except:
 _st_.goboom(_sage_const_184 )
try:
 _st_.current_tex_line = _sage_const_186 
 _st_.inline(_sage_const_23 , latex(answer4a))
except:
 _st_.goboom(_sage_const_186 )
try:
 _st_.current_tex_line = _sage_const_186 
 _st_.inline(_sage_const_24 , latex(answer4b))
except:
 _st_.goboom(_sage_const_186 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_25 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_26 , latex(answer4a))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_192 
 _st_.inline(_sage_const_27 , latex(answer4a))
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.current_tex_line = _sage_const_192 
 _st_.inline(_sage_const_28 , latex(answer4b))
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.current_tex_line = _sage_const_194 
 _st_.inline(_sage_const_29 , latex(answer4b))
except:
 _st_.goboom(_sage_const_194 )
try:
 _st_.current_tex_line = _sage_const_194 
 _st_.inline(_sage_const_30 , latex(Infinity))
except:
 _st_.goboom(_sage_const_194 )
try:
 _st_.current_tex_line = _sage_const_205 
 _st_.inline(_sage_const_31 , latex(function5))
except:
 _st_.goboom(_sage_const_205 )
try:
 _st_.current_tex_line = _sage_const_207 
 _st_.inline(_sage_const_32 , latex(answer5a))
except:
 _st_.goboom(_sage_const_207 )
try:
 _st_.current_tex_line = _sage_const_207 
 _st_.inline(_sage_const_33 , latex(answer5b))
except:
 _st_.goboom(_sage_const_207 )
try:
 _st_.current_tex_line = _sage_const_211 
 _st_.inline(_sage_const_34 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_211 )
try:
 _st_.current_tex_line = _sage_const_211 
 _st_.inline(_sage_const_35 , latex(answer5a))
except:
 _st_.goboom(_sage_const_211 )
try:
 _st_.current_tex_line = _sage_const_213 
 _st_.inline(_sage_const_36 , latex(answer5a))
except:
 _st_.goboom(_sage_const_213 )
try:
 _st_.current_tex_line = _sage_const_213 
 _st_.inline(_sage_const_37 , latex(answer5b))
except:
 _st_.goboom(_sage_const_213 )
try:
 _st_.current_tex_line = _sage_const_215 
 _st_.inline(_sage_const_38 , latex(answer5b))
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_215 
 _st_.inline(_sage_const_39 , latex(Infinity))
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_226 
 _st_.inline(_sage_const_40 , latex(function6))
except:
 _st_.goboom(_sage_const_226 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_41 , latex(answer6a))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_42 , latex(answer6b))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_43 , latex(answer6c))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_232 
 _st_.inline(_sage_const_44 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_232 )
try:
 _st_.current_tex_line = _sage_const_232 
 _st_.inline(_sage_const_45 , latex(answer6a))
except:
 _st_.goboom(_sage_const_232 )
try:
 _st_.current_tex_line = _sage_const_234 
 _st_.inline(_sage_const_46 , latex(answer6a))
except:
 _st_.goboom(_sage_const_234 )
try:
 _st_.current_tex_line = _sage_const_234 
 _st_.inline(_sage_const_47 , latex(answer6b))
except:
 _st_.goboom(_sage_const_234 )
try:
 _st_.current_tex_line = _sage_const_236 
 _st_.inline(_sage_const_48 , latex(answer6b))
except:
 _st_.goboom(_sage_const_236 )
try:
 _st_.current_tex_line = _sage_const_236 
 _st_.inline(_sage_const_49 , latex(answer6c))
except:
 _st_.goboom(_sage_const_236 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_50 , latex(answer6c))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_51 , latex(Infinity))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_247 
 _st_.inline(_sage_const_52 , latex(function7))
except:
 _st_.goboom(_sage_const_247 )
try:
 _st_.current_tex_line = _sage_const_249 
 _st_.inline(_sage_const_53 , latex(answer7))
except:
 _st_.goboom(_sage_const_249 )
try:
 _st_.current_tex_line = _sage_const_256 
 _st_.inline(_sage_const_54 , latex(-Infinity))
except:
 _st_.goboom(_sage_const_256 )
try:
 _st_.current_tex_line = _sage_const_256 
 _st_.inline(_sage_const_55 , latex(answer7))
except:
 _st_.goboom(_sage_const_256 )
try:
 _st_.current_tex_line = _sage_const_258 
 _st_.inline(_sage_const_56 , latex(answer7))
except:
 _st_.goboom(_sage_const_258 )
try:
 _st_.current_tex_line = _sage_const_258 
 _st_.inline(_sage_const_57 , latex(Infinity))
except:
 _st_.goboom(_sage_const_258 )
_st_.endofdoc()

