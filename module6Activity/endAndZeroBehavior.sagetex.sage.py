## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file endAndZeroBehavior.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_200 = Integer(200); _sage_const_299 = Integer(299); _sage_const_297 = Integer(297); _sage_const_238 = Integer(238); _sage_const_0p5 = RealNumber('0.5'); _sage_const_318 = Integer(318); _sage_const_316 = Integer(316); _sage_const_276 = Integer(276); _sage_const_274 = Integer(274); _sage_const_337 = Integer(337); _sage_const_335 = Integer(335); _sage_const_194 = Integer(194); _sage_const_219 = Integer(219); _sage_const_257 = Integer(257); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_30 = Integer(30)## This file (endAndZeroBehavior.sagetex.sage) was *autogenerated* from endAndZeroBehavior.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('endAndZeroBehavior', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_30 
_st_.blockbegin()
try:
 x = var("x")
 def maybeMakeNegative(natural):
     integer = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def listZeros(factor1, factor2):
     z0 = factor1
     z1 = -factor1
     z2 = factor2
     z3 = -factor2
     return [z0, z1, z2, z3]
 
 def generateCoefficientsAndZeros():
     leadingCoefficient = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_10 ))
     factor1 = ZZ.random_element(_sage_const_2 , _sage_const_10 )
     factor2 = ZZ.random_element(_sage_const_2 , _sage_const_10 )
     while factor1 == factor2:
         factor1 = ZZ.random_element(_sage_const_2 , _sage_const_10 )
         factor2 = ZZ.random_element(_sage_const_2 , _sage_const_10 )
     chooseZero = ZZ.random_element(_sage_const_2 )
     if chooseZero == _sage_const_0 :
         zeroOnDisplay = -factor1
         e0 = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         e1 = e0 + _sage_const_2  * ZZ.random_element(_sage_const_1 , _sage_const_4 ) - _sage_const_1 
         e2 = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         e3 = e2 + ZZ.random_element(_sage_const_0 , _sage_const_3 )
     else:
         zeroOnDisplay = -factor2
         e0 = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         e1 = e0 + ZZ.random_element(_sage_const_0 , _sage_const_3 )
         e2 = ZZ.random_element(_sage_const_1 , _sage_const_4 )
         e3 = e2 + _sage_const_2  * ZZ.random_element(_sage_const_1 , _sage_const_4 ) - _sage_const_1 
     zeros = listZeros(factor1, factor2)
     exponents = e0, e1, e2, e3
     return [leadingCoefficient, zeros, exponents, zeroOnDisplay]
 
 def displayPolynomial(leadingCoefficient, zeros, exponents):
     z0, z1, z2, z3 = zeros
     e0, e1, e2, e3 = exponents
     polynomial = leadingCoefficient * (x - z0)**e0 * (x - z1)**e1 * (x - z2)**e2 * (x - z3)**e3
     return polynomial
 
 def endBehaviorAnswer(leadingCoefficient, exponents):
     e0, e1, e2, e3 = exponents
     evenOrOdd = (e0 + e1 + e2 + e3) % _sage_const_2 
     if leadingCoefficient < _sage_const_0  and evenOrOdd == _sage_const_1 :
         answer = "A"
     elif leadingCoefficient < _sage_const_0  and evenOrOdd == _sage_const_0 :
         answer = "B"
     elif leadingCoefficient > _sage_const_0  and evenOrOdd == _sage_const_1 :
         answer = "C"
     elif leadingCoefficient > _sage_const_0  and evenOrOdd == _sage_const_0 :
         answer = "D"
     else:
         answer = "Broken"
     return answer
 
 def zeroBehaviorAnswer(polynomial, zeroOnDisplay, exponentOnDisplay):
     nearZero = zeroOnDisplay - _sage_const_0p5 
     yValue = polynomial(x = nearZero)
     evenOrOdd = exponentOnDisplay % _sage_const_2 
     if yValue > _sage_const_0  and evenOrOdd == _sage_const_0 :
         answer = "EvenPositive"
     elif yValue > _sage_const_0  and evenOrOdd == _sage_const_1 :
         answer = "OddNegative"
     elif yValue < _sage_const_0  and evenOrOdd == _sage_const_0 :
         answer = "EvenNegative"
     else:
         answer = "OddPositive"
     return answer
 
 def findDisplayExponent(zeroOnDisplay, zeros, exponents):
     z0, z1, z2, z3 = zeros
     e0, e1, e2, e3 = exponents
     if zeroOnDisplay == z0:
         return e0
     elif zeroOnDisplay == z1:
         return e1
     elif zeroOnDisplay == z2:
         return e2
     else:
         return e3
 
 ### Question 2 - Answer B ###
 leadingCoefficient2, zeros2, exponents2, zeroOnDisplay2 = generateCoefficientsAndZeros()
 polynomial2 = displayPolynomial(leadingCoefficient2, zeros2, exponents2)
 answer2 = endBehaviorAnswer(leadingCoefficient2, exponents2)
 while answer2 == "A" or answer2 == "C" or answer2 == "D":
     leadingCoefficient2, zeros2, exponents2, zeroOnDisplay2 = generateCoefficientsAndZeros()
     polynomial2 = displayPolynomial(leadingCoefficient2, zeros2, exponents2)
     answer2 = endBehaviorAnswer(leadingCoefficient2, exponents2)
 
 ### Question 3 - Answer D ###
 leadingCoefficient3, zeros3, exponents3, zeroOnDisplay3 = generateCoefficientsAndZeros()
 polynomial3 = displayPolynomial(leadingCoefficient3, zeros3, exponents3)
 answer3 = endBehaviorAnswer(leadingCoefficient3, exponents3)
 while answer3 == "A" or answer3 == "B" or answer3 == "C":
     leadingCoefficient3, zeros3, exponents3, zeroOnDisplay3 = generateCoefficientsAndZeros()
     polynomial3 = displayPolynomial(leadingCoefficient3, zeros3, exponents3)
     answer3 = endBehaviorAnswer(leadingCoefficient3, exponents3)
 
 ### Question 4 - Answer A ###
 leadingCoefficient4, zeros4, exponents4, zeroOnDisplay4 = generateCoefficientsAndZeros()
 polynomial4 = displayPolynomial(leadingCoefficient4, zeros4, exponents4)
 answer4 = endBehaviorAnswer(leadingCoefficient4, exponents4)
 while answer4 == "B" or answer4 == "C" or answer4 == "D":
     leadingCoefficient4, zeros4, exponents4, zeroOnDisplay4 = generateCoefficientsAndZeros()
     polynomial4 = displayPolynomial(leadingCoefficient4, zeros4, exponents4)
     answer4 = endBehaviorAnswer(leadingCoefficient4, exponents4)
 
 ### Question 5 - Answer C ###
 leadingCoefficient5, zeros5, exponents5, zeroOnDisplay5 = generateCoefficientsAndZeros()
 polynomial5 = displayPolynomial(leadingCoefficient5, zeros5, exponents5)
 answer5 = endBehaviorAnswer(leadingCoefficient5, exponents5)
 while answer5 == "A" or answer5 == "B" or answer5 == "D":
     leadingCoefficient5, zeros5, exponents5, zeroOnDisplay5 = generateCoefficientsAndZeros()
     polynomial5 = displayPolynomial(leadingCoefficient5, zeros5, exponents5)
     answer5 = endBehaviorAnswer(leadingCoefficient5, exponents5)
 
 ##### Question 6 - Odd Negative #####
 leadingCoefficient6, zeros6, exponents6, zeroOnDisplay6 = generateCoefficientsAndZeros()
 polynomial6 = displayPolynomial(leadingCoefficient6, zeros6, exponents6)
 exponentOnDisplay6 = findDisplayExponent(zeroOnDisplay6, zeros6, exponents6)
 answer6 = zeroBehaviorAnswer(polynomial6, zeroOnDisplay6, exponentOnDisplay6)
 print answer6
 while answer6 == "EvenPositive" or answer6 == "EvenNegative" or answer6 == "OddPositive":
     leadingCoefficient6, zeros6, exponents6, zeroOnDisplay6 = generateCoefficientsAndZeros()
     polynomial6 = displayPolynomial(leadingCoefficient6, zeros6, exponents6)
     exponentOnDisplay6 = findDisplayExponent(zeroOnDisplay6, zeros6, exponents6)
     answer6 =  zeroBehaviorAnswer(polynomial6, zeroOnDisplay6, exponentOnDisplay6)
 
 ##### Question 7 - Even Negative #####
 leadingCoefficient7, zeros7, exponents7, zeroOnDisplay7 = generateCoefficientsAndZeros()
 polynomial7 = displayPolynomial(leadingCoefficient7, zeros7, exponents7)
 exponentOnDisplay7 = findDisplayExponent(zeroOnDisplay7, zeros7, exponents7)
 answer7 = zeroBehaviorAnswer(polynomial7, zeroOnDisplay7, exponentOnDisplay7)
 while answer7 == "EvenPositive" or answer7 == "OddNegative" or answer7 == "OddPositive":
     leadingCoefficient7, zeros7, exponents7, zeroOnDisplay7 = generateCoefficientsAndZeros()
     polynomial7 = displayPolynomial(leadingCoefficient7, zeros7, exponents7)
     exponentOnDisplay7 = findDisplayExponent(zeroOnDisplay7, zeros7, exponents7)
     answer7 =  zeroBehaviorAnswer(polynomial7, zeroOnDisplay7, exponentOnDisplay7)
 
 ##### Question 8 - Even Positive #####
 leadingCoefficient8, zeros8, exponents8, zeroOnDisplay8 = generateCoefficientsAndZeros()
 polynomial8 = displayPolynomial(leadingCoefficient8, zeros8, exponents8)
 exponentOnDisplay8 = findDisplayExponent(zeroOnDisplay8, zeros8, exponents8)
 answer8 = zeroBehaviorAnswer(polynomial8, zeroOnDisplay8, exponentOnDisplay8)
 while answer8 == "EvenNegative" or answer8 == "OddNegative" or answer8 == "OddPositive":
     leadingCoefficient8, zeros8, exponents8, zeroOnDisplay8 = generateCoefficientsAndZeros()
     polynomial8 = displayPolynomial(leadingCoefficient8, zeros8, exponents8)
     exponentOnDisplay8 = findDisplayExponent(zeroOnDisplay8, zeros8, exponents8)
     answer8 =  zeroBehaviorAnswer(polynomial8, zeroOnDisplay8, exponentOnDisplay8)
 
 ##### Question 9 - Odd Positive #####
 leadingCoefficient9, zeros9, exponents9, zeroOnDisplay9 = generateCoefficientsAndZeros()
 polynomial9 = displayPolynomial(leadingCoefficient9, zeros9, exponents9)
 exponentOnDisplay9 = findDisplayExponent(zeroOnDisplay9, zeros9, exponents9)
 answer9 = zeroBehaviorAnswer(polynomial9, zeroOnDisplay9, exponentOnDisplay9)
 while answer9 == "EvenPositive" or answer9 == "OddNegative" or answer9 == "EvenNegative":
     leadingCoefficient9, zeros9, exponents9, zeroOnDisplay9 = generateCoefficientsAndZeros()
     polynomial9 = displayPolynomial(leadingCoefficient9, zeros9, exponents9)
     exponentOnDisplay9 = findDisplayExponent(zeroOnDisplay9, zeros9, exponents9)
     answer9 =  zeroBehaviorAnswer(polynomial9, zeroOnDisplay9, exponentOnDisplay9)
except:
 _st_.goboom(_sage_const_194 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_200 
 _st_.inline(_sage_const_0 , latex(polynomial2))
except:
 _st_.goboom(_sage_const_200 )
try:
 _st_.current_tex_line = _sage_const_219 
 _st_.inline(_sage_const_1 , latex(polynomial3))
except:
 _st_.goboom(_sage_const_219 )
try:
 _st_.current_tex_line = _sage_const_238 
 _st_.inline(_sage_const_2 , latex(polynomial4))
except:
 _st_.goboom(_sage_const_238 )
try:
 _st_.current_tex_line = _sage_const_257 
 _st_.inline(_sage_const_3 , latex(polynomial5))
except:
 _st_.goboom(_sage_const_257 )
try:
 _st_.current_tex_line = _sage_const_274 
 _st_.inline(_sage_const_4 , latex(zeroOnDisplay6))
except:
 _st_.goboom(_sage_const_274 )
try:
 _st_.current_tex_line = _sage_const_276 
 _st_.inline(_sage_const_5 , latex(polynomial6))
except:
 _st_.goboom(_sage_const_276 )
try:
 _st_.current_tex_line = _sage_const_297 
 _st_.inline(_sage_const_6 , latex(zeroOnDisplay7))
except:
 _st_.goboom(_sage_const_297 )
try:
 _st_.current_tex_line = _sage_const_299 
 _st_.inline(_sage_const_7 , latex(polynomial7))
except:
 _st_.goboom(_sage_const_299 )
try:
 _st_.current_tex_line = _sage_const_316 
 _st_.inline(_sage_const_8 , latex(zeroOnDisplay8))
except:
 _st_.goboom(_sage_const_316 )
try:
 _st_.current_tex_line = _sage_const_318 
 _st_.inline(_sage_const_9 , latex(polynomial8))
except:
 _st_.goboom(_sage_const_318 )
try:
 _st_.current_tex_line = _sage_const_335 
 _st_.inline(_sage_const_10 , latex(zeroOnDisplay9))
except:
 _st_.goboom(_sage_const_335 )
try:
 _st_.current_tex_line = _sage_const_337 
 _st_.inline(_sage_const_11 , latex(polynomial9))
except:
 _st_.goboom(_sage_const_337 )
_st_.endofdoc()

