## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file convertSlopeInterceptStandard.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_89 = Integer(89); _sage_const_113 = Integer(113); _sage_const_83 = Integer(83); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_30 = Integer(30); _sage_const_120 = Integer(120); _sage_const_98 = Integer(98); _sage_const_126 = Integer(126); _sage_const_100 = Integer(100); _sage_const_91 = Integer(91); _sage_const_107 = Integer(107)## This file (convertSlopeInterceptStandard.sagetex.sage) was *autogenerated* from convertSlopeInterceptStandard.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('convertSlopeInterceptStandard', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_30 
_st_.blockbegin()
try:
 x = var('x')
 y = var('y')
 
 #################
 def maybeMakeNegative(rational):
     maybeNegative = (-_sage_const_1 )**ZZ.random_element(_sage_const_2 )
     rational = maybeNegative * rational
     return rational
 
 def standardToSlopeInt():
     A = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     B = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     C = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     while gcd(A, B) > _sage_const_1  or gcd(A, C) > _sage_const_1 :
         A = ZZ.random_element(_sage_const_2 , _sage_const_9 )
         B = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         C = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     slope = float(-A/B)
     yInt = float(C/B)
     return [A, B, C, slope, yInt]
 
 def sloptIntToStandard():
     mNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     mDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     yIntNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
     yIntDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     while gcd(mNum, mDenom) > _sage_const_1  or gcd(yIntNum, yIntDenom) > _sage_const_1  or mDenom == yIntDenom:
         mNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         mDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
         yIntNum = maybeMakeNegative(ZZ.random_element(_sage_const_2 , _sage_const_9 ))
         yIntDenom = ZZ.random_element(_sage_const_2 , _sage_const_9 )
     slope = mNum/mDenom
     yInt = yIntNum/yIntDenom
     lcmConstant = (mDenom*yIntDenom/gcd(mDenom, yIntDenom))
     if mNum < _sage_const_0 :
         A = -mNum*lcmConstant/mDenom
         B = lcmConstant
         C = yIntNum*lcmConstant/yIntDenom
     else:
         A = mNum*lcmConstant/mDenom
         B = -lcmConstant
         C = -yIntNum*lcmConstant/yIntDenom
     return [A, B, C, slope, yInt]
 ###############
 A1, B1, C1, slope1, yInt1 = standardToSlopeInt()
 equationXY1 = A1*x + B1*y
 A2, B2, C2, slope2, yInt2 = standardToSlopeInt()
 equationXY2 = A2*x + B2*y
 A3, B3, C3, slope3, yInt3 = sloptIntToStandard()
 equationSlopeInt3 = slope3*x + yInt3
 A4, B4, C4, slope4, yInt4 = sloptIntToStandard()
 equationSlopeInt4 = slope4*x + yInt4
except:
 _st_.goboom(_sage_const_83 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_0 , latex(equationXY1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_1 , latex(C1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_2 , latex(slope1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_3 , latex(yInt1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_98 
 _st_.inline(_sage_const_4 , latex(equationXY2))
except:
 _st_.goboom(_sage_const_98 )
try:
 _st_.current_tex_line = _sage_const_98 
 _st_.inline(_sage_const_5 , latex(C2))
except:
 _st_.goboom(_sage_const_98 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_6 , latex(slope2))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_7 , latex(yInt2))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_107 
 _st_.inline(_sage_const_8 , latex(equationSlopeInt3))
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_9 , latex(A3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_10 , latex(B3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_11 , latex(C3))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_12 , latex(equationSlopeInt4))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_13 , latex(A4))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_14 , latex(B4))
except:
 _st_.goboom(_sage_const_126 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.inline(_sage_const_15 , latex(C4))
except:
 _st_.goboom(_sage_const_126 )
_st_.endofdoc()

