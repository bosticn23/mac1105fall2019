## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file determineObliqueAsymptotes.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_209 = Integer(209); _sage_const_8 = Integer(8); _sage_const_242 = Integer(242); _sage_const_233 = Integer(233); _sage_const_9 = Integer(9); _sage_const_235 = Integer(235); _sage_const_244 = Integer(244); _sage_const_215 = Integer(215); _sage_const_217 = Integer(217); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_54 = Integer(54); _sage_const_224 = Integer(224); _sage_const_226 = Integer(226)## This file (determineObliqueAsymptotes.sagetex.sage) was *autogenerated* from determineObliqueAsymptotes.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('determineObliqueAsymptotes', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_54 
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
     return [rationalFactor, a]
 
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
 
 def createPolyDegree1to4(degree):
     if degree == _sage_const_1 :
         poly, deadZero1 = makeRationalFactor()
         leadingCoefficient = derivative(poly, x)/factorial(degree)
     elif degree == _sage_const_2 :
         factor2a, deadZero2a = makeRationalFactor()
         factor2b, deadZero2b = makeRationalFactor()
         poly = factor2a * factor2b
         leadingCoefficient = derivative(derivative(poly, x), x)/factorial(degree)
     elif degree == _sage_const_3 :
         factor3a, deadZero3a = makeRationalFactor()
         factor3b, deadZero3b = makeRationalFactor()
         factor3c, deadZero3c = makeRationalFactor()
         poly = factor3a * factor3b * factor3c
         leadingCoefficient = derivative(derivative(derivative(poly, x), x), x)/factorial(degree)
     elif degree == _sage_const_4 :
         factor4a, deadZero4a = makeRationalFactor()
         factor4b, deadZero4b = makeRationalFactor()
         factor4c, deadZero4c = makeRationalFactor()
         factor4d, deadZero4d = makeRationalFactor()
         poly = factor4a * factor4b * factor4c * factor4d
         leadingCoefficient = derivative(derivative(derivative(derivative(poly, x), x), x), x)/factorial(degree)
     else:
         print "Input a number between 1 and 4"
 
     return [poly, leadingCoefficient]
 
 def horizontalAsymptote():
     chooseType = ZZ.random_element(_sage_const_2 )
     if chooseType == _sage_const_0 :
         degreeDenom = ZZ.random_element(_sage_const_2 , _sage_const_5 )
         degreeNum = ZZ.random_element(_sage_const_1 , degreeDenom)
         polyNumerator, coeffNumerator = createPolyDegree1to4(degreeNum)
         polyDenominator, coeffDenominator = createPolyDegree1to4(degreeDenom)
         horizontalAsymptote = _sage_const_0 
     elif chooseType == _sage_const_1 :
         degreeNumAndDenom = ZZ.random_element(_sage_const_1 , _sage_const_5 )
         polyNumerator, coeffNumerator = createPolyDegree1to4(degreeNumAndDenom)
         polyDenominator, coeffDenominator = createPolyDegree1to4(degreeNumAndDenom)
         horizontalAsymptote = coeffNumerator/coeffDenominator
     else:
         print "Something went wrong creating the Horizontal Asymptote."
     return [polyNumerator, polyDenominator, horizontalAsymptote]
 
 def obliqueAsymptote(z0, missingOrNot):
     a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
     b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
     b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
     #
     numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
     numCo1 = a0*a1*z0
     numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
     numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1*z0
     numCo4 = -b0*b1*z1 + r
     #
     denominator = z0 * x - z1
     quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
     remainder = r
     #
     if missingOrNot == "notMissing":
         while (numCo1==_sage_const_0  or numCo2==_sage_const_0  or numCo3==_sage_const_0  or numCo4==_sage_const_0 ):
             a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             #
             numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
             numCo1 = a0*a1*z0
             numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
             numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1
             numCo4 = -b0*b1*z1 + r
             denominator = z0*x - z1
             quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
             remainder = r
             #
     else:
         index =  _sage_const_0 
         while (abs(numCo1)>_sage_const_0  and abs(numCo2)>_sage_const_0  and abs(numCo3)>_sage_const_0  and abs(numCo4)>_sage_const_0 ):
             a0 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b0 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             a1 = ZZ.random_element(_sage_const_2 , _sage_const_6 )
             b1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             z1 = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             r = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_6 ))
             #
             numeratorPoly = (a0*a1*z0)*x**_sage_const_3  + (-a0*a1*z1 + a0*b1*z0 + a1*b0*z0)*x**_sage_const_2 + (-a0*b1*z1 - a1*b0*z1 + b0*b1*z0)*x + (-b0*b1*z1 + r)
             numCo1 = a0*a1*z0
             numCo2 = -a0*a1*z1 + a0*b1*z0 + a1*b0*z0
             numCo3 = -a0*b1*z1 - a1*b0*z1 + b0*b1
             numCo4 = -b0*b1*z1 + r
             denominator = z0*x - z1
             quotient = (a0*a1)*x**_sage_const_2  + (a0*b1+a1*b0)*x + b0*b1
             remainder = r
             index =  index + _sage_const_1 
             print "Index increases by 1 to %s" %index
             #
     return [numeratorPoly, denominator, quotient, remainder]
 #####
 polyNum1, polyDenom1, horAsy1 = horizontalAsymptote()
 polyNum2, polyDenom2, horAsy2 = horizontalAsymptote()
 #
 choices = ["missing", "notMissing"]
 polyNum3, polyDenom3, obliqueAsy3, deadRemainder3 = obliqueAsymptote(_sage_const_1 , choices[ZZ.random_element(_sage_const_2 )])
 polyNum4, polyDenom4, obliqueAsy4, deadRemainder4 = obliqueAsymptote(ZZ.random_element(_sage_const_2 , _sage_const_6 ), choices[ZZ.random_element(_sage_const_2 )])
except:
 _st_.goboom(_sage_const_209 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_215 
 _st_.inline(_sage_const_0 , latex(polyNum1))
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_215 
 _st_.inline(_sage_const_1 , latex(polyDenom1))
except:
 _st_.goboom(_sage_const_215 )
try:
 _st_.current_tex_line = _sage_const_217 
 _st_.inline(_sage_const_2 , latex(horAsy1))
except:
 _st_.goboom(_sage_const_217 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_3 , latex(polyNum2))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_4 , latex(polyDenom2))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_226 
 _st_.inline(_sage_const_5 , latex(horAsy2))
except:
 _st_.goboom(_sage_const_226 )
try:
 _st_.current_tex_line = _sage_const_233 
 _st_.inline(_sage_const_6 , latex(polyNum3))
except:
 _st_.goboom(_sage_const_233 )
try:
 _st_.current_tex_line = _sage_const_233 
 _st_.inline(_sage_const_7 , latex(polyDenom3))
except:
 _st_.goboom(_sage_const_233 )
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_8 , latex(obliqueAsy3))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_242 
 _st_.inline(_sage_const_9 , latex(polyNum4))
except:
 _st_.goboom(_sage_const_242 )
try:
 _st_.current_tex_line = _sage_const_242 
 _st_.inline(_sage_const_10 , latex(polyDenom4))
except:
 _st_.goboom(_sage_const_242 )
try:
 _st_.current_tex_line = _sage_const_244 
 _st_.inline(_sage_const_11 , latex(obliqueAsy4))
except:
 _st_.goboom(_sage_const_244 )
_st_.endofdoc()

