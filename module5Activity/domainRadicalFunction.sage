## This file (domainRadicalFunction.sage) was *autogenerated* from the file domainRadicalFunction.tex.
import sagetex
_st_ = sagetex.SageTeXProcessor('domainRadicalFunction')
_st_.blockbegin()
try:
 a1 = ZZ.random_element(2, 10)
except:
 _st_.goboom(32)
_st_.blockend()
try:
 _st_.inline(0, a1)
except:
 _st_.goboom(35)
try:
 _st_.inline(1, a1)
except:
 _st_.goboom(37)
try:
 _st_.inline(2, Infinity)
except:
 _st_.goboom(37)
_st_.blockbegin()
try:
 a2 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 b2 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 factor2 = a2*x + b2
 answer2 = round(float(solve(factor2==0, x)[0].rhs()),3)
except:
 _st_.goboom(50)
_st_.blockend()
try:
 _st_.inline(3, factor2)
except:
 _st_.goboom(53)
try:
 _st_.inline(4, factor2)
except:
 _st_.goboom(53)
try:
 _st_.inline(5, factor2)
except:
 _st_.goboom(53)
try:
 _st_.inline(6, factor2)
except:
 _st_.goboom(53)
try:
 _st_.inline(7, -Infinity)
except:
 _st_.goboom(55)
try:
 _st_.inline(8, Infinity)
except:
 _st_.goboom(55)
_st_.blockbegin()
try:
 a3 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 b3 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 factor3 = a3*x + b3
 answer3 = round(float(solve(factor3==0, x)[0].rhs()),3)
 nearbyCheckGreater3 = answer3 + 1
 while nearbyCheckGreater3 > 0:
     a3 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     b3 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     factor3 = a3*x + b3
     answer3 = round(float(solve(factor3==0, x)[0].rhs()),3)
     nearbyCheckGreater3 = answer3+1
except:
 _st_.goboom(71)
_st_.blockend()
try:
 _st_.inline(9, factor3)
except:
 _st_.goboom(74)
try:
 _st_.inline(10, factor3)
except:
 _st_.goboom(74)
try:
 _st_.inline(11, factor3)
except:
 _st_.goboom(74)
try:
 _st_.inline(12, factor3)
except:
 _st_.goboom(74)
try:
 _st_.inline(13, -Infinity)
except:
 _st_.goboom(76)
try:
 _st_.inline(14, answer3)
except:
 _st_.goboom(76)
_st_.blockbegin()
try:
 a4 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 b4 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
 factor4 = a4*x + b4
 answer4 = round(float(solve(factor4==0, x)[0].rhs()),3)
 nearbyCheckGreater4 = answer4+1
 while nearbyCheckGreater4 > 0:
     a4 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     b4 = (-1)**(ZZ.random_element(2))*(ZZ.random_element(2, 10))
     factor4 = a4*x + b4
     answer4 = round(float(solve(factor4==0, x)[0].rhs()),3)
     nearbyCheckGreater4 = answer4+1
except:
 _st_.goboom(92)
_st_.blockend()
try:
 _st_.inline(15, factor4)
except:
 _st_.goboom(95)
try:
 _st_.inline(16, factor4)
except:
 _st_.goboom(95)
try:
 _st_.inline(17, factor4)
except:
 _st_.goboom(95)
try:
 _st_.inline(18, factor4)
except:
 _st_.goboom(95)
try:
 _st_.inline(19, -Infinity)
except:
 _st_.goboom(97)
try:
 _st_.inline(20, Infinity)
except:
 _st_.goboom(97)
_st_.endofdoc()
