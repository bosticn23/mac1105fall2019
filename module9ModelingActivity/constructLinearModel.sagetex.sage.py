## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file constructLinearModel.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_187 = Integer(187); _sage_const_89 = Integer(89); _sage_const_85 = Integer(85); _sage_const_116 = Integer(116); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_108 = Integer(108); _sage_const_98 = Integer(98); _sage_const_100 = Integer(100); _sage_const_105 = Integer(105); _sage_const_93 = Integer(93); _sage_const_229 = Integer(229); _sage_const_225 = Integer(225); _sage_const_227 = Integer(227); _sage_const_243 = Integer(243); _sage_const_241 = Integer(241); _sage_const_213 = Integer(213); _sage_const_0p01 = RealNumber('0.01'); _sage_const_0p05 = RealNumber('0.05'); _sage_const_135 = Integer(135); _sage_const_65 = Integer(65); _sage_const_60 = Integer(60); _sage_const_61 = Integer(61); _sage_const_69 = Integer(69); _sage_const_239 = Integer(239); _sage_const_233 = Integer(233); _sage_const_231 = Integer(231); _sage_const_237 = Integer(237); _sage_const_235 = Integer(235); _sage_const_1000 = Integer(1000); _sage_const_120 = Integer(120); _sage_const_70 = Integer(70); _sage_const_128 = Integer(128); _sage_const_78 = Integer(78); _sage_const_112 = Integer(112); _sage_const_202 = Integer(202); _sage_const_81 = Integer(81); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_154 = Integer(154); _sage_const_152 = Integer(152); _sage_const_150 = Integer(150); _sage_const_158 = Integer(158); _sage_const_59 = Integer(59); _sage_const_58 = Integer(58); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_142 = Integer(142); _sage_const_300 = Integer(300); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_170 = Integer(170); _sage_const_176 = Integer(176); _sage_const_190 = Integer(190); _sage_const_194 = Integer(194); _sage_const_198 = Integer(198); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_166 = Integer(166); _sage_const_162 = Integer(162); _sage_const_160 = Integer(160)## This file (constructLinearModel.sagetex.sage) was *autogenerated* from constructLinearModel.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('constructLinearModel', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_42 
_st_.blockbegin()
try:
 x = var("x")
 fixedCost1 = ZZ.random_element(_sage_const_10 , _sage_const_26 )*_sage_const_1000 
 productionCost1 = round(ZZ.random_element(_sage_const_1 , _sage_const_4 )*_sage_const_0p05 , _sage_const_2 )
 sellingPoint1 = round(productionCost1*ZZ.random_element(_sage_const_1 , _sage_const_4 ), _sage_const_2 )
 costs1 = productionCost1*x + fixedCost1
 profits1 = sellingPoint1*x
 revenue1 = profits1 - costs1
except:
 _st_.goboom(_sage_const_50 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_53 
 _st_.inline(_sage_const_0 , latex(fixedCost1))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.current_tex_line = _sage_const_53 
 _st_.inline(_sage_const_1 , latex(productionCost1))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.current_tex_line = _sage_const_53 
 _st_.inline(_sage_const_2 , latex(sellingPoint1))
except:
 _st_.goboom(_sage_const_53 )
try:
 _st_.current_tex_line = _sage_const_57 
 _st_.inline(_sage_const_3 , latex(costs1))
except:
 _st_.goboom(_sage_const_57 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_4 , latex(profits1))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_65 
 _st_.inline(_sage_const_5 , latex(revenue1))
except:
 _st_.goboom(_sage_const_65 )
_st_.current_tex_line = _sage_const_69 
_st_.blockbegin()
try:
 x = var('x')
 savings2 = ZZ.random_element(_sage_const_5 , _sage_const_11 )*_sage_const_1000 
 rent2 = ZZ.random_element(_sage_const_7 , _sage_const_12 )*_sage_const_100 
 food2 = ZZ.random_element(_sage_const_4 , _sage_const_8 )*_sage_const_10 
 misc2 = ZZ.random_element(_sage_const_4 , _sage_const_8 )*_sage_const_8 
 costs2 = (rent2 + _sage_const_4 *food2 + _sage_const_4 *misc2)*x
 profits2 = _sage_const_300  + savings2
 revenue2 = profits2 - costs2
except:
 _st_.goboom(_sage_const_78 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_6 , latex(savings2))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_7 , latex(rent2))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_8 , latex(food2))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_9 , latex(misc2))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_85 
 _st_.inline(_sage_const_10 , latex(costs2))
except:
 _st_.goboom(_sage_const_85 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_11 , latex(profits2))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_93 
 _st_.inline(_sage_const_12 , latex(revenue2))
except:
 _st_.goboom(_sage_const_93 )
_st_.current_tex_line = _sage_const_98 
_st_.blockbegin()
try:
 m = var('m')
 officerAspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_5 )
 officerBspeed3 = ZZ.random_element(_sage_const_2 , _sage_const_5 )
 partA3 = officerAspeed3/_sage_const_60  * m
 partB3 = officerAspeed3/_sage_const_60  * m + officerBspeed3/_sage_const_60  * m
 partC3 = sqrt((officerAspeed3/_sage_const_60 )**_sage_const_2  + (officerBspeed3/_sage_const_60 )**_sage_const_2 )*m
except:
 _st_.goboom(_sage_const_105 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_13 , latex(officerAspeed3))
except:
 _st_.goboom(_sage_const_108 )
try:
 _st_.current_tex_line = _sage_const_108 
 _st_.inline(_sage_const_14 , latex(officerBspeed3))
except:
 _st_.goboom(_sage_const_108 )
try:
 _st_.current_tex_line = _sage_const_112 
 _st_.inline(_sage_const_15 , latex(partA3))
except:
 _st_.goboom(_sage_const_112 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_16 , latex(partB3))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_17 , latex(partC3))
except:
 _st_.goboom(_sage_const_120 )
_st_.current_tex_line = _sage_const_128 
_st_.blockbegin()
try:
 t, D = var('t', 'D')
 speedFlat4 = ZZ.random_element(_sage_const_3 , _sage_const_6 )
 speedUp4 = speedFlat4 - ZZ.random_element(_sage_const_1 , _sage_const_3 )
 speedDown4 = speedFlat4 + ZZ.random_element(_sage_const_2 , _sage_const_4 )
 partC4 = (speedFlat4 + speedUp4 + speedDown4)*t
 partD4 = D*(_sage_const_1 /speedUp4 + _sage_const_1 /speedDown4 + _sage_const_1 /speedFlat4)
except:
 _st_.goboom(_sage_const_135 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_18 , latex(speedUp4))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_19 , latex(speedDown4))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_20 , latex(speedFlat4))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_21 , latex(speedUp4*t))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_152 
 _st_.inline(_sage_const_22 , latex(speedDown4*t))
except:
 _st_.goboom(_sage_const_152 )
try:
 _st_.current_tex_line = _sage_const_154 
 _st_.inline(_sage_const_23 , latex(speedFlat4*t))
except:
 _st_.goboom(_sage_const_154 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_24 , latex(D/speedUp4))
except:
 _st_.goboom(_sage_const_158 )
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.inline(_sage_const_25 , latex(D/speedDown4))
except:
 _st_.goboom(_sage_const_160 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_26 , latex(D/speedFlat4))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_166 
 _st_.inline(_sage_const_27 , latex(partC4))
except:
 _st_.goboom(_sage_const_166 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_28 , latex(partD4))
except:
 _st_.goboom(_sage_const_170 )
_st_.current_tex_line = _sage_const_176 
_st_.blockbegin()
try:
 x = var('x')
 teenTicketPrice = ZZ.random_element(_sage_const_3 , _sage_const_7 )
 adultTicketPrice = teenTicketPrice + ZZ.random_element(_sage_const_3 , _sage_const_7 )
 teenTicketCount = ZZ.random_element(_sage_const_30 , _sage_const_70 )
 adultTicketCount = ZZ.random_element(_sage_const_30 , _sage_const_70 )
 totalTickets = teenTicketCount + adultTicketCount
 totalRevenue = teenTicketCount*teenTicketPrice + adultTicketCount*adultTicketPrice
 eqPartA5 = totalTickets - x
 eqPartB5 = eqPartA5 * adultTicketPrice
 eqPartC5 = eqPartB5 + teenTicketPrice * x
except:
 _st_.goboom(_sage_const_187 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_29 , latex(adultTicketPrice))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_30 , latex(teenTicketPrice))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_31 , latex(totalTickets))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_32 , latex(totalRevenue))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_194 
 _st_.inline(_sage_const_33 , latex(eqPartA5))
except:
 _st_.goboom(_sage_const_194 )
try:
 _st_.current_tex_line = _sage_const_198 
 _st_.inline(_sage_const_34 , latex(eqPartB5))
except:
 _st_.goboom(_sage_const_198 )
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_35 , latex(eqPartC5))
except:
 _st_.goboom(_sage_const_202 )
_st_.current_tex_line = _sage_const_213 
_st_.blockbegin()
try:
 v = var('v')
 concA = ZZ.random_element(_sage_const_1 , _sage_const_4 )*_sage_const_5 
 concB = ZZ.random_element(_sage_const_2 , _sage_const_5 )*_sage_const_10 
 concTotal = ZZ.random_element(_sage_const_10 , _sage_const_31 )
 while concTotal < concA or concTotal > concB:
     concTotal = ZZ.random_element(_sage_const_10 , _sage_const_31 )
 totalVolume = ZZ.random_element(_sage_const_5 , _sage_const_15 )
 eqPartA6 = totalVolume - v
 eqPartB6 = concA * _sage_const_0p01  * v
 eqPartC6 = concB * _sage_const_0p01  * eqPartA6
 eqPartD6 = eqPartB6 + eqPartC6
except:
 _st_.goboom(_sage_const_225 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_227 
 _st_.inline(_sage_const_36 , latex(concA))
except:
 _st_.goboom(_sage_const_227 )
try:
 _st_.current_tex_line = _sage_const_227 
 _st_.inline(_sage_const_37 , latex(concB))
except:
 _st_.goboom(_sage_const_227 )
try:
 _st_.current_tex_line = _sage_const_227 
 _st_.inline(_sage_const_38 , latex(totalVolume))
except:
 _st_.goboom(_sage_const_227 )
try:
 _st_.current_tex_line = _sage_const_227 
 _st_.inline(_sage_const_39 , latex(concTotal))
except:
 _st_.goboom(_sage_const_227 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_40 , latex(concB))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_41 , latex(concB))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.current_tex_line = _sage_const_229 
 _st_.inline(_sage_const_42 , latex(concA))
except:
 _st_.goboom(_sage_const_229 )
try:
 _st_.current_tex_line = _sage_const_231 
 _st_.inline(_sage_const_43 , latex(concB))
except:
 _st_.goboom(_sage_const_231 )
try:
 _st_.current_tex_line = _sage_const_231 
 _st_.inline(_sage_const_44 , latex(eqPartA6))
except:
 _st_.goboom(_sage_const_231 )
try:
 _st_.current_tex_line = _sage_const_233 
 _st_.inline(_sage_const_45 , latex(concA))
except:
 _st_.goboom(_sage_const_233 )
try:
 _st_.current_tex_line = _sage_const_233 
 _st_.inline(_sage_const_46 , latex(concA))
except:
 _st_.goboom(_sage_const_233 )
try:
 _st_.current_tex_line = _sage_const_233 
 _st_.inline(_sage_const_47 , latex(concA))
except:
 _st_.goboom(_sage_const_233 )
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_48 , latex(concA))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_235 
 _st_.inline(_sage_const_49 , latex(eqPartB6))
except:
 _st_.goboom(_sage_const_235 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_50 , latex(concB))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_51 , latex(concB))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_237 
 _st_.inline(_sage_const_52 , latex(concA))
except:
 _st_.goboom(_sage_const_237 )
try:
 _st_.current_tex_line = _sage_const_239 
 _st_.inline(_sage_const_53 , latex(concB))
except:
 _st_.goboom(_sage_const_239 )
try:
 _st_.current_tex_line = _sage_const_239 
 _st_.inline(_sage_const_54 , latex(eqPartC6))
except:
 _st_.goboom(_sage_const_239 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.inline(_sage_const_55 , latex(concTotal))
except:
 _st_.goboom(_sage_const_241 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.inline(_sage_const_56 , latex(concTotal))
except:
 _st_.goboom(_sage_const_241 )
try:
 _st_.current_tex_line = _sage_const_241 
 _st_.inline(_sage_const_57 , latex(concA))
except:
 _st_.goboom(_sage_const_241 )
try:
 _st_.current_tex_line = _sage_const_243 
 _st_.inline(_sage_const_58 , latex(concTotal))
except:
 _st_.goboom(_sage_const_243 )
try:
 _st_.current_tex_line = _sage_const_243 
 _st_.inline(_sage_const_59 , latex(eqPartD6))
except:
 _st_.goboom(_sage_const_243 )
_st_.endofdoc()

