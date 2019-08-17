## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file dividingPolynomials.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_135 = Integer(135); _sage_const_32 = Integer(32); _sage_const_138 = Integer(138); _sage_const_171 = Integer(171); _sage_const_155 = Integer(155); _sage_const_152 = Integer(152); _sage_const_33 = Integer(33); _sage_const_174 = Integer(174); _sage_const_193 = Integer(193); _sage_const_190 = Integer(190); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_51 = Integer(51); _sage_const_127 = Integer(127)## This file (dividingPolynomials.sagetex.sage) was *autogenerated* from dividingPolynomials.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('dividingPolynomials', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_51 
_st_.blockbegin()
try:
 x = var("x")
 
 def maybeMakeNegative(natural):
     integer = natural*(-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     return integer
 
 def generateSyntheticDivisionTerms(z0, missingOrNot):
     #Goal: (a0*x+b0)*(a1*x+b1)*(z0*x-z1)+r
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
 #####
 #####
 dividend2, divisor2, quotient2, remainder2 = generateSyntheticDivisionTerms(_sage_const_1 , "notMissing")
 
 dividend3, divisor3, quotient3, remainder3 = generateSyntheticDivisionTerms(ZZ.random_element(_sage_const_2 , _sage_const_6 ), "notMissing")
 
 dividend4, divisor4, quotient4, remainder4 = generateSyntheticDivisionTerms(_sage_const_1 , "missing")
 
 dividend5, divisor5, quotient5, remainder5 = generateSyntheticDivisionTerms(ZZ.random_element(_sage_const_2 , _sage_const_6 ), "missing")
except:
 _st_.goboom(_sage_const_127 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_0 , latex(dividend2))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_1 , latex(divisor2))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_2 , latex(quotient2))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_3 , latex(remainder2))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_135 
 _st_.inline(_sage_const_4 , latex(divisor2))
except:
 _st_.goboom(_sage_const_135 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_5 , latex(dividend2))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_6 , latex(quotient2))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_7 , latex(divisor2))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_8 , latex(remainder2))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_9 , latex(dividend3))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_10 , latex(divisor3))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_11 , latex(quotient3))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_12 , latex(remainder3))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_13 , latex(divisor3))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_14 , latex(dividend3))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_15 , latex(quotient3))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_16 , latex(divisor3))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_17 , latex(remainder3))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_18 , latex(dividend4))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_19 , latex(divisor4))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_20 , latex(quotient4))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_21 , latex(remainder4))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_171 
 _st_.inline(_sage_const_22 , latex(divisor4))
except:
 _st_.goboom(_sage_const_171 )
try:
 _st_.current_tex_line = _sage_const_174 
 _st_.inline(_sage_const_23 , latex(dividend4))
except:
 _st_.goboom(_sage_const_174 )
try:
 _st_.current_tex_line = _sage_const_174 
 _st_.inline(_sage_const_24 , latex(quotient4))
except:
 _st_.goboom(_sage_const_174 )
try:
 _st_.current_tex_line = _sage_const_174 
 _st_.inline(_sage_const_25 , latex(divisor4))
except:
 _st_.goboom(_sage_const_174 )
try:
 _st_.current_tex_line = _sage_const_174 
 _st_.inline(_sage_const_26 , latex(remainder4))
except:
 _st_.goboom(_sage_const_174 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_27 , latex(dividend5))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_28 , latex(divisor5))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_29 , latex(quotient5))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_30 , latex(remainder5))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_31 , latex(divisor5))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_193 
 _st_.inline(_sage_const_32 , latex(dividend5))
except:
 _st_.goboom(_sage_const_193 )
try:
 _st_.current_tex_line = _sage_const_193 
 _st_.inline(_sage_const_33 , latex(quotient5))
except:
 _st_.goboom(_sage_const_193 )
try:
 _st_.current_tex_line = _sage_const_193 
 _st_.inline(_sage_const_34 , latex(divisor5))
except:
 _st_.goboom(_sage_const_193 )
try:
 _st_.current_tex_line = _sage_const_193 
 _st_.inline(_sage_const_35 , latex(remainder5))
except:
 _st_.goboom(_sage_const_193 )
_st_.endofdoc()
